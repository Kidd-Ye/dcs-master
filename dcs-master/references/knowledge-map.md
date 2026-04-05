# DCS 知识地图

本文档是增强版 DCS 助理的知识索引，将 46 篇详细文档按主题分类，便于快速检索。

---

## 知识文档结构

```
references/docs/
├── zh/          # 中文文档 (46篇)
└── en/          # 英文文档 (46篇)
```

---

## 按主题分类索引

### 1. 入门与概览

| 编号 | 中文文档 | 英文文档 | 核心内容 |
|------|----------|----------|----------|
| 01 | 金蝶AI星空-协同开发平台-使用指南.md | Kingdee AI Galaxy - Collaborative Dev Platform Guide.md | 端到端完整指南 |
| 02 | 轻扩展概述.md | Light Extension Overview.md | 轻扩展概念与边界 |
| 27 | 金蝶AI星空-协同开发平台使用指南.md | Kingdee AI Galaxy - Collaborative Dev Platform User Guide.md | 完整使用指南（近01） |

### 2. 账号与项目初始化

| 编号 | 中文文档 | 英文文档 | 核心内容 |
|------|----------|----------|----------|
| 12 | 1-创建开发商标识.md | 1-Create Developer Identifier.md | 开发商标识创建与团队管理 |
| 13 | 2-创建项目.md | 2-Create Project.md | 项目创建、仓库生成、成员邀请 |
| 14 | 3-将项目与天梯租户关联.md | 3-Associate Project with Tenant.md | 项目与天梯租户关联 |
| 29 | 如何修改Git密码.md | How to Reset Git Password.md | Git密码重置流程 |
| 38 | 找不到开发商标识如何处理.md | How to Handle Missing Developer Identifier.md | 开发商标识选择失败分析 |

### 3. 元数据管理

| 编号 | 中文文档 | 英文文档 | 核心内容 |
|------|----------|----------|----------|
| 06 | GitLab仓库元数据管理.md | GitLab Repository Metadata Management.md | 仓库查看、删除、回滚、保存到数据中心 |
| 19 | 直接推送元数据到项目的GitLab仓库.md | Push Metadata Directly to GitLab.md | 产品侧推送（推荐） |
| 20 | 如何导出元数据并上传到项目GitLab仓库.md | How to Export and Upload Metadata.md | 导出上传方式（备选） |
| 28 | 如何单独构建元数据.md | How to Build Metadata Only.md | 元数据单独构建 |
| 41 | 数据中心版本低于仓库版本_or_元数据的id不一致如何处理.md | Handle Version Mismatch or ID Inconsistency.md | 版本冲突、ID不一致解决 |
| 43 | 构建失败，提示"仓库中datamodel内容为空"如何处理.md | Handle Empty Datamodel Error.md | 空datamodel处理 |

### 4. 构建与仓库

| 编号 | 中文文档 | 英文文档 | 核心内容 |
|------|----------|----------|----------|
| 04 | 纯插件代码补丁包构建.md | Pure Plugin Code Patch Build.md | Jar-only构建 |
| 05 | 构建时可选构建依赖版本.md | Build Dependency Version Selection.md | 依赖版本选择与风险 |
| 08 | 选择部分元数据和脚本发起构建.md | Build with Partial Metadata.md | 部分包构建 |
| 09 | 如何构建静态资源制品包.md | How to Build Static Resource Package.md | 静态资源打包规则 |
| 24 | 方式一：金蝶AI星空客户端构建补丁包.md | Method 1: Client-side Build.md | 客户端构建（推荐） |
| 25 | 方式二：使用DCS网页端构建并推送补丁包.md | Method 2: Web Build and Push.md | 网页端构建 |
| 42 | DCS二开项目构建提示gradle.properties不存在解决方案.md | Fix Missing gradle.properties.md | Gradle文件缺失解决 |
| 44 | DCS项目构建提示依赖错误解决方案.md | Fix Dependency Errors.md | 依赖错误诊断 |
| 45 | DCS二开项目构建提示class_XXXX_is_public解决.md | Fix Public Class Name Mismatch.md | 类名文件名不匹配 |
| 46 | 元数据构建失败原因与解决方案汇总.md | Metadata Build Failure Solutions.md | 元数据构建失败汇总 |

### 5. 插件开发

| 编号 | 中文文档 | 英文文档 | 核心内容 |
|------|----------|----------|----------|
| 21 | 开发服务器简介.md | Development Server Overview.md | 轻量与容器环境 |
| 22 | CosmicStudio开发者工具下载与安装.md | CosmicStudio Download and Install.md | 开发者工具安装 |
| 23 | 如何使用协同开发平台与小助手开发插件.md | Use DCS with IDEA Helper.md | IDEA小助手开发流程 |
| 35 | 苍穹开发助手引用协同code模板-疑难问题解答.md | IDEA Helper Troubleshooting.md | IDEA与DCS Gradle差异 |

### 6. 质量与测试

| 编号 | 中文文档 | 英文文档 | 核心内容 |
|------|----------|----------|----------|
| 03 | 如何填写测试报告并审核.md | How to Fill and Audit Test Report.md | 测试报告创建与审核 |
| 11 | DCS_协同开发云项目看板使用指南.md | DCS Project Dashboard Guide.md | 构建与质量看板 |
| 31 | 如何查看质量报告.md | How to View Quality Report.md | 质量报告查看 |
| 30 | 构建日志常见问题及解决方案.md | Build Log Common Issues.md | 构建日志常见问题 |

### 7. 发布与部署

| 编号 | 中文文档 | 英文文档 | 核心内容 |
|------|----------|----------|----------|
| 07 | SQL上传与部署.md | SQL Upload and Deployment.md | SQL脚本上传与部署 |
| 10 | DCS关联翻译平台推送补丁包到天梯.md | Translation Platform Integration.md | 翻译平台关联 |
| 26 | 7-在天梯提单部署.md | Create Deployment Order in Tianti.md | 天梯提单部署 |
| 32 | 如何将协同平台的项目与应用市场的应用进行关联.md | Associate with App Market.md | 应用市场关联 |
| 34 | 金蝶AI星空之热部署.md | Hot Deployment.md | 热部署规则与前提 |
| 37 | 天梯部署规则（金蝶AI星空）.md | Tianti Deployment Rules.md | 部署时间窗与规则 |
| 39 | 天梯部署常见问题解答.md | Tianti Deployment FAQ.md | 部署常见问题 |
| 40 | 协同开发平台中，推送补丁时提示"未查询到关联环境！".md | Handle "Environment Not Found" Error.md | 环境关联问题 |

### 8. 平台基础概念

| 编号 | 中文文档 | 英文文档 | 核心内容 |
|------|----------|----------|----------|
| 15 | 云管理说明.md | Cloud Management.md | 云概念与操作 |
| 16 | 应用管理.md | Application Management.md | 应用管理、菜单、对象 |
| 17 | 设计器使用说明.md | Designer Usage.md | 设计器布局与操作 |
| 18 | 单据与列表介绍.md | Bill and List Introduction.md | 单据列表概念与场景 |
| 33 | 数据中心如何与项目关联.md | How to Associate Data Center.md | 数据中心关联 |

### 9. 配置传输与特殊场景

| 编号 | 中文文档 | 英文文档 | 核心内容 |
|------|----------|----------|----------|
| 36 | 如何通过配置传输快速传输_辅助资料分类.md | Configuration Transfer for Auxiliary Data.md | 配置传输替代元数据部署 |

---

## 快速检索表

### 按问题类型检索

| 问题类型 | 优先查看文档 |
|----------|--------------|
| 新手入门 | 01, 12-14, 19, 22-23 |
| 构建失败 | 30, 42-46, troubleshooting.md |
| 部署失败 | 37, 39-41, troubleshooting.md |
| 元数据问题 | 06, 19-20, 28, 41, 43, 46 |
| 插件开发 | 21-23, 35 |
| 质量报告 | 03, 11, 31 |
| 环境关联 | 14, 33, 38, 40 |

### 按错误关键词检索

| 错误关键词 | 对应文档编号 |
|------------|--------------|
| 未查询到关联环境 | 40 |
| 数据中心版本低于仓库版本 | 41 |
| 元数据的id不一致 | 41 |
| gradle.properties不存在 | 42 |
| 仓库中datamodel内容为空 | 43 |
| 依赖错误 | 44 |
| class XXXX is public | 45 |
| 找不到开发商标识 | 38 |

---

## 使用建议

1. **教练模式**：优先加载 `coach-playbooks.md` + `milestone-checklists.md`
2. **诊断模式**：优先加载 `troubleshooting.md` + 对应错误文档
3. **修复模式**：优先加载具体技术文档（如 42-46）+ `build-and-repo.md`
4. **双语支持**：根据用户语言自动选择 `docs/zh/` 或 `docs/en/`
