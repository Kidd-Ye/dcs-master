# DCS Master v1.0.2

## 更新摘要

这个版本在 `v1.0.1` 的基础上，补齐了安装完整性检查与修复能力，重点解决“用户已安装 skill，但实际副本缺文件、图文增强失效、升级路径不清晰”的问题。

## 本次新增

- 新增安装健康检查脚本：
  - `scripts/check-install-health.py`
- 新增自动修复路径：
  - 当安装副本缺少关键文件时，可直接调用升级脚本进行覆盖修复
- 扩展升级脚本支持更多安装形态：
  - `codex`
  - `qoderwork`
  - `skilldir`
  - `opencode`
  - `claude`
  - `cursor`
  - `copilot`
  - `gemini`
  - `universal`

## 重点修复的问题

- 已安装副本缺失关键 `references/*.md` 文件时，之前没有统一检测机制
- QoderWork 这类“技能目录型安装”之前没有明确升级入口
- 用户虽然安装了 skill，但因为副本不完整，无法稳定触发图文增强回答

## 使用方式

### 检查安装是否完整

```bash
python3 ~/.codex/skills/dcs-master/scripts/check-install-health.py
```

### 自动修复缺失文件

```bash
python3 ~/.codex/skills/dcs-master/scripts/check-install-health.py --repair
```

### QoderWork 用户

```bash
python3 ~/.qoderwork/skills/dcs-master/scripts/check-install-health.py
python3 ~/.qoderwork/skills/dcs-master/scripts/check-install-health.py --repair
```

## 版本说明

- `skill-manifest.json` 已更新到 `1.0.2`
- 建议所有已安装用户升级到 `v1.0.2`

## 升级建议

如果你曾经安装过一个不完整的 `dcs-master` 副本，尤其是：

- 缺少 `intent-routing.md`
- 缺少 `rich-answering.md`
- 缺少 `response-templates.md`
- 缺少 `knowledge-map.md`
- 缺少完整 `references/docs`

那么建议尽快升级到 `v1.0.2`，否则仍可能出现：

- 该给图文时没给图文
- 该走精细分流时只给普通文本回答
- 升级时不知道该怎么覆盖旧副本
