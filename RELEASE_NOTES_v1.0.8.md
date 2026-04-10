# Release Notes v1.0.8

## 更新内容

### 改进：版本检查功能适配所有 Agent 工具

- **AGENTS.md**: 新增完整的版本检查指南，支持所有工具
- **SKILL.md**: 新增各工具版本检查命令对照表
- **CLAUDE.md**: 新增 Claude 项目级版本检查和升级命令
- **GEMINI.md**: 新增 Gemini 项目级版本检查和升级命令
- **.cursor/rules/dcs-master.mdc**: 新增 Cursor 项目级版本检查和升级命令

### 支持的工具

版本检查功能现已适配以下所有工具：

| 工具 | 安装路径 | 版本检查命令 |
|------|----------|--------------|
| QoderWork | `~/.qoderwork/skills/dcs-master/` | `python3 ~/.qoderwork/skills/dcs-master/scripts/version-check-wrapper.py` |
| Codex | `~/.codex/skills/dcs-master/` | `python3 ~/.codex/skills/dcs-master/scripts/version-check-wrapper.py` |
| OpenCode | `.opencode/skills/dcs-master/` | `python3 .opencode/skills/dcs-master/scripts/version-check-wrapper.py` |
| Claude Code | `.dcs-master/` | `python3 .dcs-master/scripts/version-check-wrapper.py` |
| Cursor | `.dcs-master/` | `python3 .dcs-master/scripts/version-check-wrapper.py` |
| GitHub Copilot | `.dcs-master/` | `python3 .dcs-master/scripts/version-check-wrapper.py` |
| Gemini CLI | `.dcs-master/` | `python3 .dcs-master/scripts/version-check-wrapper.py` |

### 使用方式

1. 每次使用 skill 前，先运行对应工具的版本检查命令
2. 如果检测到新版本，在回复开头提示用户
3. 提供对应工具的升级命令

### 版本更新

- 版本号: `v1.0.8`

## 兼容性

- 完全兼容 v1.0.7 的所有功能
