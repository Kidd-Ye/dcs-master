# DCS Knowledge Index

Source folder: bundled Chinese knowledge docs under `references/docs/zh`

Use this index to map user questions to the original source articles. `01` and `27` are near-duplicate overall guides.

## Overall Guides And Onboarding

- `01_金蝶AI星空-协同开发平台-使用指南.md`: Overall end-to-end guide from account binding to 天梯 publish.
- `02_轻扩展概述.md`: What light extension is, where it fits, and why it is different from DCS custom delivery.
- `12_1-创建开发商标识.md`: How to create the developer identifier and manage team members.
- `13_2-创建项目.md`: DCS project creation, auto-created repo, project roles, and invite-member flow.
- `14_3-将项目与天梯租户关联.md`: How to associate a DCS project with a public-cloud tenant.
- `19_直接推送元数据到项目的GitLab仓库（金蝶AI星空推荐使用）.md`: Product-side metadata push, build, and publish flow for 星空.
- `20_如何导出元数据并上传到项目GitLab仓库？.md`: Fallback ways to export metadata and upload it to the repo.
- `21_开发服务器简介.md`: Lightweight versus container development environments.
- `22_CosmicStudio开发者工具下载与安装.md`: Developer tool download, install, and usage notes.
- `23_如何使用协同开发平台与小助手开发插件.md`: IDEA helper workflow for plugin project initialization and team development.
- `24_方式一：金蝶AI星空客户端构建补丁包（推荐使用）.md`: Product-side build path.
- `25_方式二：使用DCS网页端构建并推送补丁包.md`: DCS web build path and quality-scan gate.
- `26_7-在天梯提单部署_.md`: How to create the 天梯 deployment order and move from sandbox to production.
- `27_金蝶AI星空-协同开发平台使用指南.md`: Near-duplicate of the overall guide in `01`.
- `28_如何单独构建元数据.md`: Metadata-only build and its scan behavior.
- `29_如何修改Git密码.md`: Git password reset flow.

## Repo, Build, And Package Variants

- `04_纯插件代码补丁包构建.md`: Jar-only build path.
- `05_构建时可选构建依赖版本.md`: Choosing build dependency versions and version-risk notes.
- `06_GitLab仓库元数据管理.md`: Repo viewer, delete, rollback, and save-to-data-center operations.
- `07_SQL上传与部署.md`: Upload SQL scripts, package them, and publish.
- `08_选择部分元数据和脚本发起构建.md`: Partial-package build from repo content.
- `09_如何构建静态资源制品包.md`: Static-resource packaging rules and folder layout.
- `10_DCS关联翻译平台推送补丁包到天梯.md`: Translation-platform linkage and multilingual artifact flow.

## Quality, Reports, And Operations

- `03_如何填写测试报告并审核.md`: Test-report creation, PCS linkage, checklist, submit, and audit.
- `11_DCS_协同开发云项目看板使用指南.md`: Build dashboard and quality dashboard usage.
- `31_如何查看质量报告.md`: Where to open quality reports and how to inspect findings.
- `32_如何将协同平台的项目与应用市场的应用进行关联.md`: App-market association and signing flow.
- `34_金蝶AI星空之热部署.md`: Hot-deployment scope, rules, and publish preconditions.
- `37_天梯部署规则（金蝶AI星空）.md`: Historical deployment-window and deployment-rule notes.

## Platform Basics

- `15_云管理说明.md`: Cloud concept, cloud operations, and git or SVN sync at cloud level.
- `16_应用管理.md`: App management, original or third-party apps, menus, objects, and extension.
- `17_设计器使用说明.md`: Designer layout, control areas, and page operations.
- `18_单据与列表介绍.md`: Bill and list concepts, typical scenarios, and creation flow.
- `33_数据中心如何与项目关联？.md`: Product-side data-center association with a DCS project.

## Troubleshooting And Exception Knowledge

- `30_构建日志常见问题及解决方案.md`: Missing `bos` or `biz` or `trd` or `cus` dependency patterns.
- `35_苍穹开发助手引用协同code模板-疑难问题解答.md`: IDEA helper versus DCS Gradle differences, module changes, and dependency notes.
- `36_如何通过配置传输快速传输_辅助资料分类.md`: Why some configuration data should use configuration transfer instead of metadata deployment.
- `38_找不到开发商标识如何处理.md`: Developer-identifier selection failure analysis.
- `39_天梯部署常见问题解答.md`: Deployment success but metadata missing, app-code conflict, and page-code conflict.
- `40_协同开发平台中，推送补丁时提示“未查询到关联环境！”，如何处理？.md`: Missing environment association during publish.
- `41_数据中心版本低于仓库版本_or_元数据的id不一致如何处理？.md`: Push-blocking checks for older metadata, ID mismatch, and forbidden light-extension upload.
- `42_DCS二开项目构建提示gradle.properties不存在解决方案.md`: Missing Gradle build files in repo.
- `43_构建失败，提示“仓库中datamodel内容为空”如何处理？.md`: Empty or invalid `datamodel` repo content.
- `44_DCS项目构建提示依赖错误解决方案.md`: Dependency-error diagnosis and jar lookup workflow.
- `45_DCS二开项目构建提示class_XXXX_is_public,_should_be_declared_in_a_file_named_XXXX_.java解决.md`: File-name and public-class-name mismatch.
- `46_元数据构建失败原因与解决方案汇总.md`: Missing cloud `datamodel.xml`, missing app entries, case-mismatch repo folders, and partial-build metadata errors.
