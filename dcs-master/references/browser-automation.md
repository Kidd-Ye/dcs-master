# DCS 平台浏览器自动化操作指南

本文档详细说明如何使用浏览器自动化完成 DCS 平台的各项操作。

---

## 前置准备

### 1. 安装浏览器自动化工具

```bash
# 安装 agent-browser CLI
npm install -g agent-browser

# 安装 Chromium 浏览器
agent-browser install
```

### 2. 验证安装

```bash
agent-browser --version
```

---

## 触发策略

浏览器自动化必须遵守两层规则：

1. **先给选项，再拿授权**
   - 如果用户当前目标是登录、创建项目、关联数据中心、关联环境、查看构建、发布部署这类浏览器里就能完成的任务，助手在首轮回复里必须显式告知：
     - 可以继续手动带练
     - 也可以由助手直接打开浏览器代操作
2. **拿到明确授权后才能执行**
   - 只有用户明确回复类似下面的话，才进入真正的浏览器自动化模式：
     - `帮我打开浏览器创建 DCS 项目`
     - `你直接帮我操作`
     - `帮我登录 DCS`

这条规则的目的，是避免出现两种问题：

- 用户本来想让助手代操作，但助手没有把这个入口说出来
- 助手在没有授权的情况下直接操作浏览器

### 推荐开场句

当用户说：

- `带我一步步创建 DCS 项目`
- `从零开始带我建项目`

助手首轮应在正常教练输出后补一句：

```text
如果你想我直接打开浏览器代操作，直接回：帮我打开浏览器创建 DCS 项目
```

---

## 基础操作命令

### 会话管理

```bash
# 设置会话名称（保持登录状态）
export AGENT_BROWSER_SESSION=dcs_session

# 关闭已有会话（避免冲突）
agent-browser --session dcs_session close 2>/dev/null

# 查看所有会话
agent-browser session list
```

---

## 页面元素缓存

为了减少用户等待，浏览器自动化默认优先复用本地缓存，而不是每次都先抓整页。

标准流程：

1. 读取当前页 `url` 和 `title`
2. 先查询 `state/ui-element-cache.json`
3. 命中稳定选择器时直接定位
4. 只有缓存失效或没有记录时，才回退到 `snapshot` / `eval` / 截图
5. 一旦确认了新的稳定元素，立即写回缓存

### 缓存文件与脚本

- `scripts/ui-cache.js`：查询、写入、失效化缓存
- `state/ui-element-cache.json`：页面指纹与关键元素选择器

### 常用命令

```bash
# 查看当前缓存摘要
node scripts/ui-cache.js list

# 通过 URL + Title 解析元素选择器
node scripts/ui-cache.js resolve \
  --url "https://dcs.kdgalaxy.com/ierp/?formId=home_page&code=1773973754faaff7aaa640a8bce77bc9" \
  --title "协同开发云" \
  --element create_project_button \
  --field selector

# 直接按 pageKey 获取缓存
node scripts/ui-cache.js resolve \
  --page dcs_dashboard_home \
  --element create_project_button

# 写入或刷新缓存
node scripts/ui-cache.js upsert \
  --page dcs_dashboard_home \
  --element create_project_button \
  --selector "#tblnew" \
  --action click \
  --description "项目列表工具栏新增按钮" \
  --host dcs.kdgalaxy.com \
  --url-include "/ierp/?formId=home_page" \
  --title-include "协同开发云" \
  --validate-text "新增" \
  --source "live session"

# 选择器失效时删除
node scripts/ui-cache.js invalidate \
  --page dcs_dashboard_home \
  --element create_project_button
```

### 缓存规则

1. 不缓存 `@e10` 这类临时引用，只缓存稳定 CSS 选择器、DOM id 或稳定属性。
2. 优先级：`id` > `data-*` / `name` > 稳定 class 组合 > 文本+结构推导。
3. 缓存命中后先直接执行，不要默认再跑一次 `snapshot`。
4. 如果直接执行失败，再抓页面，并在重新定位成功后更新缓存。
5. 写缓存时尽量带上页面指纹：
   - host
   - url 关键片段
   - title 关键片段
   - 必要时 body 关键文本

### 导航操作

```bash
# 打开 DCS 平台（有头模式，推荐）
agent-browser --session dcs_session --headed open https://dcs.kingdee.com

# 等待页面加载完成
agent-browser --session dcs_session wait --load networkidle

# 获取当前 URL
agent-browser --session dcs_session get url

# 刷新页面
agent-browser --session dcs_session open https://dcs.kingdee.com
```

### 元素交互

```bash
# 获取页面快照（带元素引用）
agent-browser --session dcs_session snapshot -i

# 填写输入框
agent-browser --session dcs_session fill @e1 "<当前会话中的用户名输入>"
agent-browser --session dcs_session fill @e2 "<当前会话中的敏感输入>"

# 点击按钮
agent-browser --session dcs_session click @e3

# 选择下拉框
agent-browser --session dcs_session select @e4 "选项文本"

# 勾选复选框
agent-browser --session dcs_session check @e5
```

### 信息获取

```bash
# 获取元素文本
agent-browser --session dcs_session get text @e1

# 获取页面标题
agent-browser --session dcs_session get title

# 截图保存
agent-browser --session dcs_session screenshot --full dcs_status.png
```

---

## DCS 专用操作流程

### 流程 1：DCS 登录

```bash
#!/bin/bash
# dcs_login.sh

SESSION="dcs_login"
DCS_URL="https://dcs.kingdee.com"

# 关闭可能存在的旧会话
agent-browser --session $SESSION close 2>/dev/null
sleep 1

# 打开 DCS 首页
echo "正在打开 DCS 首页..."
agent-browser --session $SESSION --headed open $DCS_URL
agent-browser --session $SESSION wait --load networkidle

# 获取首页元素并点击“登录”
echo "获取首页元素并点击登录入口..."
agent-browser --session $SESSION snapshot -i

# 注意：实际使用时需要替换为真实的元素引用 @eX
# agent-browser --session $SESSION click @e1
# agent-browser --session $SESSION wait --load networkidle

# 获取登录方式元素
echo "识别当前可用的登录方式..."
agent-browser --session $SESSION snapshot -i

# 先把页面上的登录方式反馈给用户，再按用户选择继续
# 例如：
# - 账号密码登录
# - 手机验证码登录
# - 企业 SSO
# - 扫码登录

# 如果用户选择账号密码登录，再继续填写表单
# agent-browser --session $SESSION click @e2
# agent-browser --session $SESSION fill @e3 "your_username"
# agent-browser --session $SESSION fill @e4 "<按当前会话输入的敏感信息>"
# agent-browser --session $SESSION click @e5

# 等待登录完成
# agent-browser --session $SESSION wait --url "**/dashboard"

echo "登录流程完成"
```

### 流程 2：创建 DCS 项目

```bash
#!/bin/bash
# dcs_create_project.sh

SESSION="dcs_project"

# 先尝试命中缓存中的创建入口
URL=$(agent-browser --session $SESSION get url)
TITLE=$(agent-browser --session $SESSION get title)
CREATE_BTN=$(node scripts/ui-cache.js resolve \
  --url "$URL" \
  --title "$TITLE" \
  --element create_project_button \
  --field selector 2>/dev/null || true)

if [ -n "$CREATE_BTN" ]; then
  agent-browser --session $SESSION click "$CREATE_BTN" || true
  agent-browser --session $SESSION wait 1500
else
  # 缓存缺失时再走页面导航或人工探测
  agent-browser --session $SESSION --headed open "https://dcs.kingdee.com/project/create"
  agent-browser --session $SESSION wait --load networkidle
fi

# 获取表单元素
echo "获取项目创建表单..."
agent-browser --session $SESSION snapshot -i

# 填写项目信息（根据实际元素引用调整）
# agent-browser --session $SESSION fill @e1 "项目名称"
# agent-browser --session $SESSION fill @e2 "项目描述"
# agent-browser --session $SESSION select @e3 "项目类型"
# agent-browser --session $SESSION select @e4 "依赖产品"
# agent-browser --session $SESSION select @e5 "开发商标识"

# 提交创建
# agent-browser --session $SESSION click @e6

# 等待创建完成
# agent-browser --session $SESSION wait --load networkidle

# 截图确认
echo "项目创建结果："
agent-browser --session $SESSION screenshot --full project_created.png
```

### 流程 3：查看构建状态

```bash
#!/bin/bash
# dcs_check_build.sh

SESSION="dcs_build"
PROJECT_ID="your_project_id"

# 打开构建看板
agent-browser --session $SESSION --headed open "https://dcs.kingdee.com/project/$PROJECT_ID/builds"
agent-browser --session $SESSION wait --load networkidle

# 获取构建列表
echo "当前构建状态："
agent-browser --session $SESSION snapshot -i

# 截图保存
agent-browser --session $SESSION screenshot --full build_status.png
```

### 流程 4：关联数据中心

```bash
#!/bin/bash
# dcs_link_datacenter.sh

SESSION="dcs_datacenter"
PROJECT_ID="your_project_id"

# 打开数据中心管理页
agent-browser --session $SESSION --headed open "https://dcs.kingdee.com/project/$PROJECT_ID/datacenters"
agent-browser --session $SESSION wait --load networkidle

# 点击关联数据中心按钮
echo "获取页面元素..."
agent-browser --session $SESSION snapshot -i

# agent-browser --session $SESSION click @e1
# agent-browser --session $SESSION wait --load networkidle

# 选择数据中心
# agent-browser --session $SESSION select @e2 "数据中心名称"
# agent-browser --session $SESSION click @e3

# 确认关联
# agent-browser --session $SESSION wait --load networkidle
agent-browser --session $SESSION screenshot --full datacenter_linked.png
```

---

## 与对话交互的集成模式

### 模式 1：用户请求 -> 助手执行 -> 反馈结果

```
用户：帮我登录 DCS

助手：
1. 打开 `https://dcs.kingdee.com`
2. 默认点击页面上的`登录`
3. 读取页面上的登录方式，并询问："我看到这些登录方式：A / B / C。你想用哪一种？"
4. 用户选择后，助手只收集该方式需要的信息
5. 助手执行对应登录动作
6. 助手反馈："已成功登录 DCS，截图如下：[截图]"
7. 助手询问："接下来您想做什么？创建项目、查看构建状态还是其他操作？"
```

执行约束：

- 如果当前任务在缓存中已有稳定选择器，先查 `scripts/ui-cache.js`，不要默认先抓整页。
- 只有缓存命不中或执行失败时，才回退到 `snapshot` / `eval` / 截图。

### 模式 1.5：先给入口，再由用户授权

```
用户：带我一步步创建 DCS 项目

助手：
1. 先按教练模式给当前阶段的最小动作
2. 在回复末尾明确补一句："如果你想我直接打开浏览器代操作，直接回：帮我打开浏览器创建 DCS 项目"
3. 用户回复授权后，再真正打开浏览器执行
```

### 模式 2：多步骤连续操作

```
用户：帮我创建一个完整的项目流程

助手：
1. 确认："我将帮您完成以下步骤：
   - 登录 DCS
   - 创建项目
   - 关联数据中心
   - 关联环境
   请确认是否开始？"

2. 用户确认后开始执行

3. 每完成一步，助手反馈：
   "步骤 X 完成：[截图/描述]
   正在进行下一步..."

4. 全部完成后总结：
   "所有步骤已完成，项目已创建并配置好，您可以开始推送元数据了。"
```

### 模式 3：遇到问题暂停询问

```
用户：帮我创建项目

助手执行中遇到选择开发商标识...

助手暂停并询问：
"检测到您有多个开发商标识，请选择：
1. ISV_xxx（ISV类型）
2. CUSTOM_xxx（定制类型）
请输入编号或标识名称："

用户回复后，助手继续执行...
```

### 模式 4：登录方式选择

```
用户：帮我登录 DCS

助手打开首页并点击“登录”后看到多个方式...

助手暂停并询问：
"我已经打开 DCS 登录入口，当前页面可见这些登录方式：
1. 账号密码登录
2. 手机验证码登录
3. 扫码登录
请告诉我你想用哪一种；我再继续下一步。"
```

---

## 安全与权限

### 敏感信息处理

```bash
# 推荐：在当前 shell 会话中临时读取敏感信息，不写入配置文件或历史命令
read -r "DCS_USERNAME?Username: "
read -rs "DCS_PASSWORD?Password: "
printf '\n'

# 脚本中引用
agent-browser --session $SESSION fill @e1 "$DCS_USERNAME"
agent-browser --session $SESSION fill @e2 "$DCS_PASSWORD"
unset DCS_PASSWORD
```

补充规则：

- 不要在看到真实登录页之前预设用户一定使用账号密码。
- 只有在用户明确选择了对应登录方式后，才收集该方式需要的敏感信息。
- 不要把账号、密码或安全码写入 shell 配置、脚本文件、缓存文件或版本库。
- 成功定位到稳定元素后，优先回写 `state/ui-element-cache.json`，不要只记在当前会话上下文里。

### 高风险操作确认

以下操作需要用户明确二次确认：

- 删除项目
- 删除仓库内容
- 发布到生产环境
- 修改敏感配置

```
助手："即将执行【发布到生产环境】操作，此操作不可撤销。
请确认：是/否"

用户确认后才执行...
```

---

## 常见问题与解决

### 问题 1：元素定位失败

**现象**：`Element not found` 或 `@eX` 引用失效

**解决**：
```bash
# 重新获取快照
agent-browser --session $SESSION snapshot -i

# 使用语义定位替代
agent-browser --session $SESSION find text "登录" click
agent-browser --session $SESSION find placeholder "用户名" fill "xxx"
```

### 问题 2：页面加载超时

**现象**：`Timeout waiting for navigation`

**解决**：
```bash
# 增加等待时间
agent-browser --session $SESSION wait 5000

# 或等待特定元素出现
agent-browser --session $SESSION wait @e1
```

### 问题 3：会话冲突

**现象**：`Browser not launched. Call launch first.`

**解决**：
```bash
# 关闭所有会话
agent-browser session list
agent-browser --session <session_name> close

# 或强制清理
agent-browser close 2>/dev/null
```

---

## 最佳实践

1. **使用有意义的会话名称**
   - `dcs_prod` - 生产环境
   - `dcs_test` - 测试环境
   - `dcs_project_a` - 特定项目

2. **每步操作后验证**
   - 操作后截图确认
   - 检查页面标题或 URL
   - 验证关键元素是否存在

3. **保持会话复用**
   - 登录后保持会话，避免重复登录
   - 长时间未操作后检查会话状态

4. **错误处理**
   - 关键操作前保存状态
   - 失败时截图记录
   - 提供清晰的错误信息

---

## 参考文档

- [agent-browser 完整文档](https://github.com/your-org/agent-browser)
- [DCS 平台操作手册](../docs/zh/)
- [故障排查指南](./troubleshooting.md)
