# 在线构建

> 分类: 快速入门/6-构建补丁包并推送天梯
> 来源: https://vip.kingdee.com/knowledge/522131914992685824?productLineId=40&isKnowledge=2&lang=zh-CN

---

1 登录协同开发平台

登录协同开发平台，网址为：[https://dcs.kingdee.com/](https://dcs.kingdee.com/) 

2 发起在线构建

（1）勾选一个项目，点击“在线构建”；

（2）点击“在线构建”按钮；

（3）根据使用场景，如果只需要构建元数据，构建内容请选择“元数据”；若需要构建jar包，则请选择“元数据+插件代码”；

（4）针对星瀚，可通过实施配置平台推送差量元数据到协同开发平台后进行构建，因此如果是星瀚的项目，存在【部分元数据】、【部分元数据+插件代码】的选项，对于实施平台差量元数据的推送使用方式，可查看文章：https://vip.kingdee.com/link/s/lIzTn

（5）点击“开始构建”按钮。

![image](https://vip.kingdee.com/download/01090cae815ae1c14f6b96fc31603aebf354.png)

此时项目列表对应的该项目的“最近一次构建结果”会更新为运行中，待此状态更新为成功时，补丁即构建完成。

![image](https://vip.kingdee.com/download/01094cb59dbfd667472da6959d978d082f15.png)

补丁构建成功后，可以进入制品列表，等待质量扫描完成。等质量扫描结论为通过时，即可进行补丁推送到天梯部署。

![image](https://vip.kingdee.com/download/010939b08c407bec4afc9133f65d2d7bd402.png)

若制品的质量扫描不通过，请点击“查看质量报告”，了解更多详情。如下图：

![image](https://vip.kingdee.com/download/0109cf28dabb55914e01a6009712b65d7290.png)

Fortify扫描中，严重、高危、中危漏洞数量必须清零。用户可以下载PDF了解质量问题以及对应的修复建议。

SonarQube扫描的严重、高危级别漏洞数量必须清零才能通过。具体可以点击“查看详情。根据漏洞名称与所在行数定位问题，查看“修复建议”完成漏洞修复。修复完成后，重新发起在线构建即可再次扫描。

![image](https://vip.kingdee.com/download/0109a55035f1977d4faa8912982e75efcb53.png)

常见的处理方法参考《[SonarQube扫描结果常见处理方式](https://developer.kingdee.com/article/489707796431276032?productLineId=29)》