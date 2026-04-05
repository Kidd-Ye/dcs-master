#!/usr/bin/env node

const fs = require("fs");
const path = require("path");

const statePath = path.join(__dirname, "..", "state", "ui-element-cache.json");

function usage() {
  process.stderr.write(
    [
      "Usage:",
      "  node scripts/ui-cache.js list",
      "  node scripts/ui-cache.js page --page <pageKey>",
      "  node scripts/ui-cache.js resolve [--page <pageKey>] [--url <url>] [--title <title>] [--body <text>] [--element <elementKey>] [--field <field>]",
      "  node scripts/ui-cache.js upsert --page <pageKey> --element <elementKey> --selector <selector> [--action <action>] [--description <text>] [--host <host>] [--url-include <fragment>] [--title-include <fragment>] [--body-include <fragment>] [--validate-text <text>] [--source <text>]",
      "  node scripts/ui-cache.js invalidate --page <pageKey> --element <elementKey>",
      "",
    ].join("\n"),
  );
}

function readState() {
  return JSON.parse(fs.readFileSync(statePath, "utf8"));
}

function writeState(state) {
  state.updatedAt = new Date().toISOString();
  fs.writeFileSync(statePath, JSON.stringify(state, null, 2) + "\n");
}

function fail(message, code = 1) {
  process.stderr.write(message + "\n");
  process.exit(code);
}

function parseArgs(argv) {
  const args = { _: [] };
  for (let i = 0; i < argv.length; i += 1) {
    const token = argv[i];
    if (!token.startsWith("--")) {
      args._.push(token);
      continue;
    }
    const key = token.slice(2);
    const next = argv[i + 1];
    if (!next || next.startsWith("--")) {
      args[key] = true;
      continue;
    }
    if (Object.prototype.hasOwnProperty.call(args, key)) {
      const current = Array.isArray(args[key]) ? args[key] : [args[key]];
      current.push(next);
      args[key] = current;
    } else {
      args[key] = next;
    }
    i += 1;
  }
  return args;
}

function asArray(value) {
  if (value === undefined) {
    return [];
  }
  return Array.isArray(value) ? value : [value];
}

function includesAll(haystack, needles) {
  if (!needles.length) {
    return true;
  }
  if (!haystack) {
    return false;
  }
  return needles.every((needle) => haystack.includes(needle));
}

function matchPage(page, context) {
  const match = page.match || {};
  const scoreParts = [];

  if (match.hostEquals) {
    if (!context.host || context.host !== match.hostEquals) {
      return null;
    }
    scoreParts.push(5);
  }

  const urlIncludes = asArray(match.urlIncludes);
  if (urlIncludes.length) {
    if (!context.url || !includesAll(context.url, urlIncludes)) {
      return null;
    }
    scoreParts.push(urlIncludes.length);
  }

  const titleIncludes = asArray(match.titleIncludes);
  if (titleIncludes.length) {
    if (!context.title || !includesAll(context.title, titleIncludes)) {
      return null;
    }
    scoreParts.push(titleIncludes.length);
  }

  const bodyIncludes = asArray(match.bodyIncludes);
  if (bodyIncludes.length) {
    if (!context.body || !includesAll(context.body, bodyIncludes)) {
      return null;
    }
    scoreParts.push(bodyIncludes.length);
  }

  return scoreParts.reduce((sum, part) => sum + part, 0);
}

function getHost(url) {
  if (!url) {
    return "";
  }
  try {
    return new URL(url).host;
  } catch (_error) {
    return "";
  }
}

function printJson(value) {
  process.stdout.write(JSON.stringify(value, null, 2) + "\n");
}

function ensurePage(state, pageKey) {
  const page = state.pages.find((item) => item.pageKey === pageKey);
  if (!page) {
    fail(`Unknown pageKey: ${pageKey}`);
  }
  return page;
}

function main() {
  const argv = process.argv.slice(2);
  if (!argv.length) {
    usage();
    process.exit(1);
  }

  const command = argv[0];
  const args = parseArgs(argv.slice(1));
  const state = readState();

  if (command === "list") {
    const summary = {
      version: state.version,
      updatedAt: state.updatedAt,
      pages: state.pages.map((page) => ({
        pageKey: page.pageKey,
        elements: Object.keys(page.elements || {}),
      })),
    };
    printJson(summary);
    return;
  }

  if (command === "page") {
    const pageKey = args.page;
    if (!pageKey) {
      fail("Missing --page");
    }
    printJson(ensurePage(state, pageKey));
    return;
  }

  if (command === "resolve") {
    const pageKey = args.page;
    const elementKey = args.element;
    const field = args.field;

    let page = null;
    if (pageKey) {
      page = ensurePage(state, pageKey);
    } else {
      const context = {
        url: args.url || "",
        title: args.title || "",
        body: args.body || "",
        host: getHost(args.url || ""),
      };
      const matches = state.pages
        .map((item) => ({ page: item, score: matchPage(item, context) }))
        .filter((item) => item.score !== null)
        .sort((left, right) => right.score - left.score);
      page = matches.length ? matches[0].page : null;
    }

    if (!page) {
      process.exit(2);
    }

    if (!elementKey) {
      if (field) {
        const value = page[field];
        if (value === undefined) {
          process.exit(3);
        }
        process.stdout.write(String(value) + "\n");
        return;
      }
      printJson(page);
      return;
    }

    const element = (page.elements || {})[elementKey];
    if (!element) {
      process.exit(4);
    }
    if (field) {
      const value = element[field];
      if (value === undefined) {
        process.exit(5);
      }
      process.stdout.write(String(value) + "\n");
      return;
    }
    printJson({ pageKey: page.pageKey, elementKey, ...element });
    return;
  }

  if (command === "upsert") {
    const pageKey = args.page;
    const elementKey = args.element;
    const selector = args.selector;
    if (!pageKey || !elementKey || !selector) {
      fail("Missing required arguments for upsert");
    }

    let page = state.pages.find((item) => item.pageKey === pageKey);
    if (!page) {
      page = {
        pageKey,
        match: {},
        elements: {},
      };
      state.pages.push(page);
    }

    if (args.host) {
      page.match.hostEquals = args.host;
    }

    const mergeIncludes = (key, values) => {
      const merged = [...new Set([...(page.match[key] || []), ...values])];
      if (merged.length) {
        page.match[key] = merged;
      }
    };

    mergeIncludes("urlIncludes", asArray(args["url-include"]));
    mergeIncludes("titleIncludes", asArray(args["title-include"]));
    mergeIncludes("bodyIncludes", asArray(args["body-include"]));

    page.elements[elementKey] = {
      selector,
      action: args.action || "click",
      description: args.description || "",
      validateText: args["validate-text"] || "",
      source: args.source || "manual upsert",
      updatedAt: new Date().toISOString(),
    };

    writeState(state);
    printJson({ ok: true, pageKey, elementKey, selector });
    return;
  }

  if (command === "invalidate") {
    const pageKey = args.page;
    const elementKey = args.element;
    if (!pageKey || !elementKey) {
      fail("Missing required arguments for invalidate");
    }
    const page = ensurePage(state, pageKey);
    if (!page.elements || !page.elements[elementKey]) {
      process.exit(6);
    }
    delete page.elements[elementKey];
    writeState(state);
    printJson({ ok: true, pageKey, elementKey });
    return;
  }

  usage();
  process.exit(1);
}

main();
