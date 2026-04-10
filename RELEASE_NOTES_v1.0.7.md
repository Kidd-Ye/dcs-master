# Release Notes v1.0.7

## 更新内容

### 新增：自动版本检查功能

- **SKILL.md**: 新增版本检查说明，每次使用 skill 前会检查是否有新版本
- **AGENTS.md**: 新增版本检查提示和升级命令
- **新增脚本** `scripts/version-check-wrapper.py`: 版本检查包装脚本，格式化输出更新提示

### 功能说明

现在 dcs-master 具备版本检查能力：

1. **手动检查**: 运行 `python3 ~/.qoderwork/skills/dcs-master/scripts/version-check-wrapper.py`
2. **升级命令**: `python3 ~/.qoderwork/skills/dcs-master/scripts/upgrade-from-github.py qoderwork --to ~/.qoderwork/skills`

当检测到新版本时，会显示如下提示：
```
📦 **发现新版本**: dcs-master 1.0.7 → 1.0.8
   升级命令: python3 .../upgrade-from-github.py qoderwork --to ~/.qoderwork/skills
```

### 版本更新

- 版本号: `v1.0.7`

## 兼容性

- 完全兼容 v1.0.6 的所有功能
