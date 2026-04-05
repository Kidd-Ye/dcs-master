# DCS二开项目构建提示"gradle.properties不存在"解决方案

> 分类: 常见问题与解决方案/构建类问题
> 来源: https://vip.kingdee.com/knowledge/622821065705577984?productLineId=40&isKnowledge=2&lang=zh-CN

---

## 1 问题描述

DCS二开项目构建提示"gradle.properties不存在"，如下图所示：

![image](https://vip.kingdee.com/download/0109dc5962de6e0b4edbac9024f68e07f582.png)

原因主要构建所需gradle相关的构建文件没有提交到GitLab仓库,导致DCS拉取代码进行构建时没有构建文件，从而无法构建。

## 2 解决方法
在DCS创建二开项目时，在IDEA通过苍穹插件创建的北斗项目会默认创建的基本代码框架，而这些二开的项目是采用gradle进行构建的，但是当插件创建完北斗项目后，gradle���建项目相关配置文件如build.gradle、config.gradle等文件还是没提交到GitLab仓库，因此如下图所示，需要将红色框内的文件提交推送到Gitlab仓库后，重新构建项目即可。

![image](https://vip.kingdee.com/download/01099cb6268d821f4f9a8be42116f0d45f97.png)

##