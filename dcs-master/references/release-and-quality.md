# DCS Release And Quality

Load this file when the user is working on publish, quality reports, test reports, hot deployment, or DCS integrations such as PCS, translation platform, and app market.

## Publish Chain

1. Build the package.
2. If the package contains code, wait for quality scan and inspect the report.
3. Complete and approve the test report when required.
4. Use `发布` in DCS or product-side `项目管理` to push the artifact to 天梯 or the private-cloud deployment platform.
5. In 天梯, create the deployment order, validate in sandbox first, then apply to production.

## Quality Report Rules

- Quality reports are based on Fortify and SonarQube results.
- Current platform behavior may also include metadata-scan conclusions for metadata-only artifacts.
- DCS web build guidance states:
  - Fortify severe, high, and medium findings must all be zero before pass
  - SonarQube severe and high findings must be zero before pass
- In the report, use the rule name, file path, line number, and repair suggestion to plan the fix.
- Do not assume metadata-only packages have empty quality-conclusion fields.
- Current field rule: metadata-only artifacts may also run metadata scanning and produce a quality conclusion.

## How To Work A Quality Report

1. Identify the failing engine: Fortify or SonarQube.
2. Sort by severity first.
3. Use exact file and line references when the report provides them.
4. If the user wants code changes, inspect the real repo and fix the narrowest root cause.
5. After edits, tell the user to rebuild and rescan in DCS.

## When Quality Conclusion Does Not Appear

- If build is already successful but the quality conclusion still does not appear, first consider two common causes:
  - the build content is large and scan time is still in progress
  - one scan engine is abnormal, so the overall quality conclusion cannot be produced
- For the first case, guide the user to wait and keep checking the scan-related status.
- For the second case, do not guess a repo-side fix first; route the user to DCS operations for handling.

## Test Report Flow

- New build artifacts start with test-report status `待填写`.
- If no PCS project is associated, the user can fill the requirement list manually.
- If the DCS project is already associated with PCS, requirements can be imported into the report through the PCS security-code linkage.
- All installation-check items must pass before submission.
- Reviewer permission is separate. Project admins have it by default and can grant it to other members.
- If the report is rejected, the user should revise it and resubmit until approval.

## PCS Association

- DCS can associate a PCS project by security code.
- The user creates the linkage in DCS `关联PCS项目`, then copies the DCS security code from PCS.
- Once associated, DCS test reports can import PCS development requirements.

## Publish To 天梯

- After `发布`, the artifact appears in 天梯 under the collaborative custom-development artifact area.
- If the risk level is `C` or `D`, the artifact must be reviewed in 天梯 before it can be selected for deployment ordering.
- The deployment order is created in the custom-development patch order area, usually with app type `扩展应用`.
- After sandbox deployment succeeds, validate the business result before applying to production.

## Time-Window Warning

- The bundled documents contain historical deployment-window rules.
- One document shows legacy sandbox windows such as `12:00`, `18:00`, and `21:00`.
- Another document says a hot-deploy rollout planned for `2025-10-30` would reduce sandbox windows to a single `03:30` window.
- Treat these as historical references only. If the user asks about current scheduling rules, re-verify them before answering.

## Hot Deployment

- Only for public-cloud standard tenants.
- Sandbox only.
- Not for single-tenant environments.
- Not for SSO or third-party login plugins.
- The package must pass hot-deploy rule checks before DCS shows the hot-deploy option during publish.
- Even if hot deployment is available, the user can still choose normal deployment.

## App-Market Integration

- DCS can associate a project with an app-market app by security code.
- After association, the user can request signing and choose ecosystem-product build during online build.
- After build, verify that the package contains `amk` prefixed artifacts in the expected locations.

## Translation-Platform Integration

- DCS can associate a translation-platform environment by security code.
- The translation platform can publish multilingual artifacts into the DCS project artifact list.
- After DCS quality scan passes, multilingual artifacts can be pushed to 天梯 like normal custom artifacts.

## Private-Cloud Note

- The bundled docs confirm that DCS `发布` can push artifacts to a private-cloud deployment platform.
- They do not include a full step-by-step guide for the downstream private-cloud screen flow.
- When the user needs exact private-cloud operations after the DCS publish step, say what is confirmed and ask for platform-specific context or screenshots.

## Project Dashboard

Project dashboards are useful for monitoring repeated issues.

- Build dashboard
  - build success rate
  - average build duration
  - push counts
  - deployment success rate
  - error distribution
- Quality dashboard
  - total vulnerabilities
  - severe, high, medium, low counts
  - files with issues
  - ignored findings

Use the dashboard when the user asks for trend analysis, team bottlenecks, or repeated build-failure patterns.
