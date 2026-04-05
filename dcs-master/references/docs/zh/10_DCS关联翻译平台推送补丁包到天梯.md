# DCS关联翻译平台推送补丁包到天梯

> 分类: 最新功能
> 来源: https://vip.kingdee.com/knowledge/773577437979952896?productLineId=40&isKnowledge=2&lang=zh-CN

---

## 1 功能介绍

DCS与翻译平台通过安全码实现项目与环境的关联，实现翻译平台的补丁推送到DCS项目的制品列表，最终可以推送多语言补丁到天梯进行提单部署。

本功能基于用户已熟悉翻译平台的操作，了解如何构建多语言补丁。更多[翻译平台](https://developer.kingdee.com/knowledge/specialDetail/390506228612990208?productLineId=29&lang=zh-CN)知识可点击查阅。

## 2 操作步骤

**（1）关联翻译平台**

访问dcs.kingdee.com，在左侧找到菜单“关联翻译平台”。

![image](https://vip.kingdee.com/download/01005ed4bcdb14d34690b4ed7a5beb6b9b68.png)

点击“新增关联”按钮。

![image](https://vip.kingdee.com/download/010031372ee3475747dcb5d6c7cb9760ecd6.png)

进入翻译平台的“环境配置”界面。翻译平台的访问链接为：[https://translate.kdcloud.com](/tolink?target=https%3A%2F%2Ftranslate.kdcloud.com)

![image](https://vip.kingdee.com/download/0100e5b78f1792ea4659bcedb4b10f48589b.png)

点击环境配置列表中蓝色字体的“编码”，如图中的agilepre，在弹出的环境配置界面复制“环境安全码”。

![image](https://vip.kingdee.com/download/010070e3363042e447cf9e8558b9182c227a.png)

回到DCS界面，选择项目，填写安全码后保存。若安全码验证通过，即会显示环境编码、环境名称、环境域名等信息，用户可以根据信息进行确认是否为目标环境。

![image](https://vip.kingdee.com/download/01003bd664f5b7b041709d1d725dfabbc6fe.png)

**（2）推送补丁到DCS项目制品列表**

用户在翻译平台构建补丁后，可在构建记录列表选中一个补丁，通过点击“发布DCS”按钮将补丁推送到DCS对应的项目制品列表。

![image](https://vip.kingdee.com/download/010075bdec6164c240f78506aa9f16750c78.png)

推送成功后，需要等待DCS发起制品构建（预估1-2分钟）流程，刷新制品列表后即可看到从翻译平台推送过来的制品。用户可根据“制品来源”判断制品是否来自翻译平台。

![image](https://vip.kingdee.com/download/0100e5d7509493ad4f42a027b193018df3ab.png)

**（3）推送多语言制品到天梯**

当制品的质量扫描结论为“通过”时，用户可以选中多语言制品推送到天梯，具体操作与推送定制开发补丁包的方式相同。