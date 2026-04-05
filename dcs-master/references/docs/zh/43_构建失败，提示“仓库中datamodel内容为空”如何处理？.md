# 构建失败，提示“仓库中datamodel内容为空”如何处理？

> 分类: 常见问题与解决方案/构建类问题
> 来源: https://vip.kingdee.com/knowledge/558741008465501952?productLineId=40&isKnowledge=2&lang=zh-CN

---

**场景：**构建失败，查看日志发现提示信息有：仓库中datamodel内容为空，构建失败。

![image](https://vip.kingdee.com/download/01095622c8ae6bfd403d8532e4912436af5e.png)

**分析：**当仓库中的datamodel文件夹中没有符合规范的元数据文件时，平台无法正常构建元数据压缩包。规范的元数据结构如下图所示。

![image](https://vip.kingdee.com/download/0109e87f6c4943a14367a00714238e95422c.png)

**解决方案：**使用产品中的”协同开发平台“，先关联项目，之后将元数据推送到项目的仓库。具体参考知识《[如何推送元数据到项目的GitLab仓库？](https://vip.kingdee.com/knowledge/specialDetail/512315349249697024?category=592008682863621120&id=592005636909247744&productLineId=40&lang=zh-CN)》。