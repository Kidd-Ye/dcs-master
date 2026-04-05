# SQL上传与部署

> 分类: 最新功能
> 来源: https://vip.kingdee.com/knowledge/700651662389374208?productLineId=40&isKnowledge=2&lang=zh-CN

---

## 1 功能介绍
当需要调整数据库表结构长度，或为表创建索引、删除索引时，使用协同开发平台的SQL上传与部署功能，将SQL快速部署到天梯。

1）在项目管理界面点击推送元数据，进入元数据推送界面。

![image](https://vip.kingdee.com/download/010949c584d69a314161973ee6a3cf84325e.png)

2）点击右上角上传脚本，选择脚本需要执行的应用，并上传脚本文件，点击确定。

![image](https://vip.kingdee.com/download/010937ae9b31b6fd4a57a2f2bba86d913f33.png)

3）此时该应用的应用信息与刚上传的脚本都出现在待推送列表，点击右上角推送仓库，将应用信息与脚本信息一同推送到仓库。

![image](https://vip.kingdee.com/download/0109b9be94b2fb1c4b2485e8e94303a62b69.png)

![image](https://vip.kingdee.com/download/0109b8e7793bd84b42adbf42a15992f3e7e0.png)

推送成功后，系统提示用户是否将推送成功的元数据进行构建？点击“构建”按钮即可将选择的脚本进行补丁包构建。

（提示：是否包含插件代码？若用户本次构建需要将插件代码也一起打包，可以勾选此选项。如果仓库中没有包含插件代码，请不要勾选。）

![image](https://vip.kingdee.com/download/0109550a9afe1dde434395aabe3a35dfc016.png)

5）构建了补丁包成功后，界面中的推送天梯按钮会置为”构建中“，等待按钮上的文字显示”发布“时即可点击按钮。

![image](https://vip.kingdee.com/download/01094f27f8ab46524cd4bd14be12a711063d.png)

![image](https://vip.kingdee.com/download/0109d211b5f2e06d4f498d5299f20e23d207.png)

6）发布完成后参考[天梯提单部署补丁包](https://vip.kingdee.com/knowledge/specialDetail/512315349249697024?category=521996232781303296&id=576103829129523456&type=Knowledge&productLineId=1&lang=zh-CN)。