# DCS Master

一个面向金蝶 DCS / 协同开发平台的通用 AI 技能包。

它把原本分散的 DCS 教练、排障、浏览器协作、图文增强能力统一进一个可分发的包里，适合 DCS 新手、实施、开发、排障和发布人员使用。

## 支持的工具

- Codex
- OpenCode
- Claude Code
- Cursor
- GitHub Copilot
- Gemini CLI

## 能做什么

- 带你一步步创建 DCS 项目
- 处理 GitLab 绑定、开发商标识、成员邀请
- 处理数据中心、租户、环境关联
- 指导元数据、代码、SQL、静态资源构建
- 解读质量报告、测试报告和漏洞扫描结果
- 处理构建失败、发布失败、部署异常
- 在你明确授权后协助浏览器操作
- 用截图和原文链接解释具体页面操作

## 仓库结构

仓库根目录给人类阅读和安装使用，真正的技能内容在 [`dcs-master/`](./dcs-master) 子目录。

## 安装

### Codex

如果你已经安装了 Codex 自带的 `skill-installer`，可直接从 GitHub 安装：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo Kidd-Ye/dcs-master --path dcs-master
```

### OpenCode

项目级安装：

```bash
python3 dcs-master/scripts/install-portable-skill.py opencode --to /path/to/project --scope project
```

### Claude / Cursor / Copilot / Gemini

给任意项目一次性安装通用规则：

```bash
python3 dcs-master/scripts/install-portable-skill.py universal --to /path/to/project
```

### 直接下载 ZIP

1. 下载本仓库的 Release ZIP
2. 解压后进入仓库目录
3. 按上面的工具类型执行对应安装命令

## 典型提问

- 带我一步步创建 DCS 项目
- 你直接帮我打开浏览器创建项目
- DCS 项目怎么创建，带图告诉我
- 构建报依赖错误怎么修
- 发布时报未查询到关联环境怎么办
- SonarQube 高危怎么修

## 版本

- 当前版本：`v1.0.0`

## 许可证

本项目使用 MIT License，见 [`LICENSE`](./LICENSE)。
