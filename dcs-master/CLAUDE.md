@AGENTS.md

## Claude Code

- 把上面导入的 `AGENTS.md` 视为权威规则。
- **每次使用前，先按 AGENTS.md 中的说明执行版本检查**。
- 需要细节时，再按 `AGENTS.md` 里的路径懒加载对应引用文件。
- 回复保持短、稳、可验收，不要退化成长篇说明书。

### Claude 项目级版本检查

```bash
python3 .dcs-master/scripts/version-check-wrapper.py
```

### Claude 项目级升级

```bash
python3 .dcs-master/scripts/upgrade-from-github.py universal --to .
```
