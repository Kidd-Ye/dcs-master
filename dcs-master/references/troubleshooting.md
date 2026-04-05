# DCS Troubleshooting

Load this file when the user provides an error string, a failed build, a failed deployment, or a repo inconsistency.

## Triage Inputs

Collect only what you need to move forward:

- exact error text
- build type: metadata, metadata plus code, code only, SQL, static resources
- where it failed: product-side push, DCS build, quality scan, 天梯 deployment
- relevant repo files, log lines, screenshots, or quality-report entries

## Push-Validation Errors

### `未查询到关联环境`

- Cause: the project is not associated to the tenant or environment, or the association is not yet approved.
- Fix: complete `关联环境` in DCS and confirm the security code in 天梯 or the target environment.

### `数据中心版本低于仓库版本`

- Cause: the current app or page was last saved earlier than the repo version.
- Fix: if the user really wants to deploy the current version, reopen the metadata in the current environment, make a real change, save it, then push again.

### `元数据的id不一致`

There are two common cases.

- Case 1: same-named app or page was recreated after earlier repo push, but never deployed to production.
  - Fix: delete the conflicting metadata from the repo with DCS repo viewer, then push the current metadata again.
- Case 2: same-named app or page was recreated after the earlier version had already been deployed to production.
  - Fix: sync the production version back into sandbox or local first, then redevelop on top of that version so sandbox, repo, and production all share the same IDs.
  - For app-level conflict: import the production app into sandbox, then re-import the page backups under that app.
  - For page-level conflict: back up the sandbox page, delete it, import the production page, then push the whole app again.

### `轻扩展元数据禁止上传`

- Cause: the user is trying to push light-extension metadata from a sandbox restored from production.
- Fix: stop. Do not push that light-extension metadata through DCS.

## Build Failures

### Build Result Never Changes To Success Or Failure

- Symptom: the build stays in a running or unresolved state for a long time and never clearly becomes `成功` or `失败`.
- Default handling path:
  1. first open the build log
  2. use the log output as the primary troubleshooting evidence
  3. if the build log still does not expose a useful clue, route the user to DCS platform support instead of guessing
- Current field rule:
  - if the log is also not helpful, ask the user to contact 林心梅 or 谭鼎鹏 in the DCS 云之家沟通群
- Do not prioritize dashboard-style interpretation ahead of the build log for this scenario.

## Quality-Scan Problems

### Quality Conclusion Never Appears After Build Success

- Symptom: the build has already succeeded, but the quality conclusion still does not appear.
- First split the case into two common branches:
  - the current build contains a lot of content, so the scan is still taking a long time
  - one scan engine is abnormal, so the overall quality conclusion cannot be produced
- Default handling path:
  1. confirm whether the scan is simply taking longer than usual
  2. if there is reason to suspect scan-engine abnormality, route the user to DCS operations instead of guessing a repo-side fix

### `gradle.properties不存在`

- Cause: required Gradle files were never committed to the repo.
- Fix: commit the build files created by the IDEA helper, including files such as `build.gradle`, `config.gradle`, and `gradle.properties`, then rebuild.

### `仓库中datamodel内容为空`

- Cause: `datamodel/` does not contain valid metadata in the expected structure.
- Fix: associate the product data center, push metadata to the repo through DCS or product-side `协同开发平台`, then rebuild.

### Missing `datamodel.xml` Under A Cloud

- Error pattern: `云XX缺少datamodel.xml，请补充`
- Cause: the cloud folder exists, but its `datamodel.xml` is missing.
- Fix: create `datamodel.xml` for that cloud and list all apps under the cloud.

### Cloud `datamodel.xml` Missing An App Entry

- Error pattern: `云XXX/datamodel.xml缺少应用XXX的信息`
- Cause: the cloud-level `datamodel.xml` is incomplete.
- Fix: add the missing app entry and commit the change.

### Partial-Build Cloud Error Or Mixed Case Cloud Folders

- Error patterns:
  - `cloudName=XXX部分构建元数据错误,请检查GitLab仓库数据`
  - same cloud exists twice with upper and lower case folder names
- Cause: repo folder names were created with inconsistent case.
- Fix:
  - back up the repo content
  - normalize folder names to the code shown by DCS
  - for severe mixed-case corruption, clear the bad `datamodel` content and repush metadata from DCS

### `compileJava FAILED` Or `package kd.bos does not exist`

- Cause: a required platform jar dependency is missing from the repo-side Gradle config.
- Fix: add the smallest matching dependency instead of importing every jar by wildcard.
- Example patterns from the docs:
  - `compile fileTree(dir: bos, include: 'bos-form-core*.jar')`
  - `compile fileTree(dir: bos, include: 'bos-form-metadata*.jar')`
- Emergency wildcard imports exist, but they are discouraged because they slow builds and weaken dependency control.

### `依赖错误`

Two common causes:

- Base modules were not committed.
  - The helper-created `common` and `helper` modules often need to be in the repo.
- A specific jar was never declared.
  - Use the local IDE to trace the missing class to its jar, then add a precise dependency.
  - Example:
    - missing class `org.apache.commons.httpclient.HttpClient`
    - locate its jar under `trd`
    - add `api fileTree(dir: trd, include: 'commons-httpclient-*.jar')`

### `class XXXX is public, should be declared in a file named XXXX.java`

- Cause: the public class name and file name do not match.
- Fix: rename the file to the public class name, or rename the public class to match the file.

## IDEA Helper Versus DCS Build Differences

- Local IDEA helper Gradle config and DCS repo-side Gradle config are not identical.
- Do not blindly commit simplified IDEA-only `build.gradle` files to the repo.
- DCS resolves the `all` project and module graph differently from local IDEA.
- When changing modules, update the repo-side Gradle files that DCS actually reads.

## Deployment Problems

### Deployment Succeeds But Metadata Is Missing In The Target Environment

- Likely cause: the package is missing the app-level XML file named after the app code.
- Fix:
  - re-export the app
  - push metadata again
  - confirm the repo now contains the app-code XML file under the right app folder

### App-Code Or Page-Code Conflict In Production

- Cause: test or sandbox and production contain objects with the same code but different internal IDs.
- Fix: treat production as the source of truth, import the production object into test or sandbox, redevelop on top of that copy, then deploy again.

### Auxiliary Data Category Is Empty After Deployment

- Cause: category IDs differ between sandbox and production.
- Fix: use configuration transfer, not DCS metadata deployment.
- Also align the business-unit code between environments before syncing.

## Repo Recovery Operations

Use DCS repo viewer when repair should happen at repo level.

- Delete unwanted repo metadata.
- Roll back to a previous repo version.
- Save repo metadata back to the current data center.

## Code-Fix Workflow

1. Start from the exact failing file, line, or rule.
2. Fix the narrowest root cause.
3. Preserve repo-side DCS compatibility, especially in Gradle files.
4. Run feasible local verification.
5. Tell the user exactly how to rebuild or rescan in DCS.

## Good Default Diagnostic Order

1. Check prerequisites and associations.
2. Check repo structure.
3. Check build type and dependency version.
4. Check build log or quality report details.
5. Repair the repo or code.
6. Rebuild.
7. Re-verify publish or deployment.
