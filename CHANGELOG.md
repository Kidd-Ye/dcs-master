# DCS Master 更新日志

所有版本的更新记录都集中在此文件中。

---

## [v1.1.0] - 合并 Release Notes

### 改进
- 将所有分散的 `RELEASE_NOTES_v*.md` 文件合并为单一的 `CHANGELOG.md`
- 统一版本历史记录格式，便于查阅
- 删除旧版 RELEASE_NOTES 文件，减少仓库冗余

---

## [v1.0.9] - 维护更新

### 更新内容
- 版本号更新至 v1.0.9

---

## [v1.0.8] - 版本检查功能适配所有 Agent 工具

### 改进
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

---

## [v1.0.7] - 自动版本检查功能

### 新增
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

---

## [v1.0.6] - 海外版 DCS (旗舰国际版) 支持

### 新增
- **海外版 DCS 地址**: `https://dcs.kdsuite.ai/ierp/`
- **重要差异**: 海外版创建项目时需要上传开发商标识文件，而非从下拉列表选择
  - 用户需先向开发商管理员或金蝶对接人获取开发商标识文件
  - 创建项目时上传该文件，DCS 会自动读取其中的标识信息

### 文档更新
- `references/getting-started.md`: 新增 DCS Editions 章节，区分国内版和海外版
- `references/getting-started.md`: 新增 International Edition Project Creation 说明

---

## [v1.0.5] - SKILL.md 元数据优化

### 改动
- 精简 `dcs-master/SKILL.md` 的 front matter `description`
- 去掉不必要的品牌名和旧 skill 偏好描述
- 保留核心触发范围，减少触发文案噪音

---

## [v1.0.4] - 安全与结构优化

### 改进
- 重写 `dcs-master/SKILL.md` 主结构：
  - 明确适用范围
  - 收敛执行总则
  - 统一输出契约
  - 拆分模式选择、证据策略、图文回答、资料路由、边界约束
- 去除主文件中偏人格化、偏口语化的表达，改成更客观的技能定义
- 移除文档中的本机绝对路径引用
- 将具体联系人姓名改为角色化描述，避免公开暴露个人信息
- 收紧浏览器自动化中的敏感信息示例：
  - 不再推荐通过 `export` 长时间暴露账号密码
  - 改为当前 shell 会话临时读取
  - 明确禁止把账号、密码或安全码写入配置、脚本、缓存或版本库
- 收紧自举升级链路：
  - 不再引用 `main` 分支远程脚本
  - 改为固定提交下载
  - 增加 SHA-256 校验后再执行

---

## [v1.0.3] - SKILL.md 结构重构

### 改进
- 重写 `SKILL.md` 主结构：
  - 先说明"什么时候用"
  - 再明确"先做什么"
  - 再统一"首轮回复格式"
  - 再分开说明四种模式和取材顺序
- 把原本平铺的信息改成可执行导航：教练模式、诊断模式、修复模式、浏览器协作模式
- 强化参考资料加载规则：先按问题类型选资料，不再默认把整套 references 一次读完
- 收紧边界表达：明确哪些场景要重新核验，明确哪些问题不要误导到 DCS 元数据发布

---

## [v1.0.2] - 安装健康检查

### 新增
- 新增安装健康检查脚本：`scripts/check-install-health.py`
- 新增自动修复路径：当安装副本缺少关键文件时，可直接调用升级脚本进行覆盖修复
- 扩展升级脚本支持更多安装形态：codex、qoderwork、skilldir、opencode、claude、cursor、copilot、gemini、universal

### 修复的问题
- 已安装副本缺失关键 `references/*.md` 文件时，之前没有统一检测机制
- QoderWork 这类"技能目录型安装"之前没有明确升级入口
- 用户虽然安装了 skill，但因为副本不完整，无法稳定触发图文增强回答

---

## [v1.0.1] - 规则修正与升级能力

### 规则修正
- 修正天梯关联菜单路径为：`协同开发云 -> 关联环境 -> 关联公有云环境`
- 区分：`看不到 ISV标准产品开发` 与 `选不出开发商标识`
- 补充 ISV 项目类型授权规则：
  - 新建项目时，`ISV标准产品开发` 默认不一定展示
  - 需要先联系 DCS 平台运营人员
  - 再按平台要求联系指定的生态授权对接人
- 修正构建结果长期不出时的处理路径：
  - 优先查看构建日志
  - 若日志也无法提示问题，则到 DCS 云之家沟通群联系官方平台支持人员
- 修正"构建成功但质量结论迟迟不出"的处理逻辑
- 修正元数据-only 制品规则：不再默认认为元数据-only 制品没有质量结论
- 增加术语纠正：`开发商表示` -> `开发商标识`

### 升级能力
- 增加版本检查脚本：`scripts/check-skill-update.py`
- 增加覆盖升级脚本：`scripts/upgrade-from-github.py`
- 已为旧用户补充"自举升级命令"，即使本地还没有升级脚本，也可以直接拉取最新版本并升级

---

## 版本兼容性说明

- 所有 v1.0.x 版本之间保持向后兼容
- 建议始终使用最新版本以获得最佳体验

---

## 升级命令参考

### QoderWork
```bash
python3 ~/.qoderwork/skills/dcs-master/scripts/upgrade-from-github.py qoderwork --to ~/.qoderwork/skills
```

### Codex
```bash
python3 ~/.codex/skills/dcs-master/scripts/upgrade-from-github.py codex --to ~/.codex/skills
```

### OpenCode (项目级)
```bash
python3 .opencode/skills/dcs-master/scripts/upgrade-from-github.py opencode --to . --scope project
```

### Claude / Cursor / Copilot / Gemini (项目级)
```bash
python3 .dcs-master/scripts/upgrade-from-github.py universal --to .
```
