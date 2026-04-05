# DCS Build And Repo

Load this file when the user is pushing metadata, preparing builds, managing the DCS repo, or setting up plugin code.

## Repo Model

- DCS creates one repo per project.
- Important folders:
  - `code/`: plugin code
  - `datamodel/`: metadata files
  - `webapp/`: static resources
  - `docs/`: optional documents
  - `cosmic.json`: project descriptor
- DCS manages metadata and code. Many business-configuration objects are outside this path and should go through configuration transfer instead.

## Recommended Build Paths

- For 金蝶AI星空, prefer product-side `元数据推送` plus `构建/发布` when the user is already working in the product environment.
- DCS web `在线构建` is the universal path and is also the main path for some cross-platform flows.
- For 星瀚, partial metadata may come from the implementation platform before DCS build.

## Metadata Push Rules

1. Associate the product data center to the DCS project first.
2. Open `元数据推送`.
3. Select the changed cloud, app, and page objects.
4. Always include the app itself when pushing its pages. Otherwise menus, groups, or app info can be missing after deployment.
5. DCS blocks pushes when the current data-center version is older than the repo version.
6. After push, choose whether to build immediately.
7. Only select `包含插件代码` if the repo really contains code to package.

## Build Type Chooser

- Metadata only
  - Use when no plugin code or SQL is needed.
  - Do not assume this package skips every scan step.
  - Current platform behavior may still perform metadata scanning and produce a quality conclusion.
- Metadata plus plugin code
  - Default for combined delivery.
- Plugin code only or Jar-only
  - Use when only jar deployment is needed and no metadata or SQL should be included.
- Partial package
  - Use when selecting only part of the repo metadata or SQL to build.
- SQL upload and deploy
  - Upload the script under the target app, push app info plus SQL together, then build and publish.
- Static resource package
  - Requires at least one valid metadata item in `datamodel/`; otherwise build fails.

## Build Dependency Version

- Public-cloud projects that are already associated with a tenant can usually choose sandbox or production dependency version.
- Private-cloud projects can choose from all build dependency versions, so the user must judge compatibility.
- Warn the user when sandbox version is higher than production version. If the code references newer APIs, fields, or components, production deployment can break.

## Repo Management Operations

Use DCS repo viewer when the repo content itself is the problem.

- Delete from repo
  - Remove unwanted metadata or scripts to avoid packaging dirty data.
- Roll back
  - Roll a page or metadata item back to a historical repo version.
  - Only use when the current data center is already consistent enough to accept the rollback result.
- Save to data center
  - Restore repo metadata directly into the current data center when the metadata was deleted by mistake.

## SQL Packaging

1. Enter `元数据推送`.
2. Upload the SQL script under the target app.
3. Push both the app info and the script to the repo.
4. Build the package.
5. Publish it to 天梯 or private cloud from DCS.

## Static Resource Packaging

- Static resources go under `webapp/isv/<developer-identifier>/...`.
- The folder under `isv/` must use the current project's developer identifier. Otherwise the resource files will not be packaged.
- File rules:
  - no Chinese characters in directory or file names
  - lowercase English names are preferred
  - allowed types: `jpg`, `jpeg`, `png`, `gif`, `ico`, `js`, `css`, `html`, `htm`
  - single-file size limit: `1MB` for JS or CSS, `200KB` for others
  - history is cumulative: old deployed files stay in place unless overwritten by the same path
- The docs require at least one metadata item in `datamodel/` before building a static-resource package.

## Plugin Development With IDEA Helper

Use this when the user wants to develop plugin code, not only metadata.

1. Install the IDEA helper from the developer portal.
2. Initialize the Gradle project from the DCS repo URL.
3. Fill cloud or app identifiers and server information so the helper can download dependencies from the dev server.
4. On the first initialization, commit every generated project file that DCS needs for cloud build.
5. Other team members then clone the initialized repo instead of re-creating the whole structure.
6. Run `DebugApplication.java` for local debug after dependencies are ready.

## DCS Gradle Versus IDEA Gradle

- Local IDEA helper projects use a newer Gradle model than DCS cloud build.
- DCS cloud build still expects repo-side Gradle files that match DCS conventions.
- Do not blindly commit IDEA-only simplified Gradle changes into the repo.
- If DCS build breaks, inspect the repo-side Gradle files in KingCode or GitLab, not only the local IDEA view.
- When adding or removing modules, remember that DCS resolves the `all` project and module order differently from local IDEA.

## What Not To Deploy Through Metadata

These should usually go through configuration transfer, not DCS metadata packaging:

- system parameters
- conversion rules
- document types
- print templates
- auxiliary data and auxiliary-data categories
- master data such as materials, customers, suppliers
