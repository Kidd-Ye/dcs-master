# GitLab仓库元数据管理

> 分类: 最新功能
> 来源: https://vip.kingdee.com/knowledge/631430400245596928?productLineId=40&isKnowledge=2&lang=zh-CN

---

## **1 ****功能介绍**
协同开发平台的GitLab仓库元数据管理功能，无需用户在浏览器访问GitLab仓库网址，即可方便快捷地了解仓库中的元数据和脚本信息。支持快捷删除和回滚元数据的版本。

（1）版本：2024.10.29发布的金蝶AI星空

（2）功能入口

进入“项目管理”功能界面，先选中一个项目，再点击“查看仓库”按钮。

![image](https://vip.kingdee.com/download/0109e30bc3005b7f4a37b865d81a3c608e24.png)

 （3）功能界面

在仓库管理功能界面，用户可以使用左侧菜单找到对应的业务云以及云下的应用节点，每个应用下包含SQL脚本和页面信息。当前提供用户可删除应用下的脚本和元数据、回滚页面的版本、保存页面到数据中心三个功能。

![image](https://vip.kingdee.com/download/010905eaff0eb7be475e9e29de11f95f4290.png)

## **2 ****应用场景**
（1）从仓库删除

    仓库中存储了用户提交的最新元数据信息，协同开发平台每次发起构建时，会从仓库中查找对应的元数据进行补丁包构建。当用户仓库中存放的不是期望的元数据时，可以通过此功能进行删除，防止脏数据部署到目标环境。

    比如用户的仓库中，在“财务会计”云下的“总账”这个应用中存在“凭证过账”这个页面，通过“从仓库删除”这个功能，可以直接删除仓库中的凭证过账”这个页面对应的文件。如下图所示，将会删除yza5_gl_voucherpost_ext.dym 和

yza5_gl_voucherpost_ext.zh_CN.dymx两个文件。

![image](https://vip.kingdee.com/download/01094021b3614fbf4593bdc9ed30577f4697.png)

![image](https://vip.kingdee.com/download/0109f9fea1201af64ceea890ea863a2f7aa1.png)

（2）回滚

    用户每次使用“推送元数据”功能，将最新元数据推送到仓库时，仓库会记录一个版本信息。当用户想要回退到某个版本的元数据时，即可使用此功能。

    使用此功能的前提：**当前数据中心存在一个与仓库完全一致的元数据**。

![image](https://vip.kingdee.com/download/01095ab33c80a5af46d7a4736b0e564e2f5c.png)

    点击“回滚”按钮，弹出“元数据历史”列表，选中上一个版本进行元数据对比。**这里的对比是当前仓库的版本与列表选中的版本进行对比。**

![image](https://vip.kingdee.com/download/0109c11b3110eced4d5e868cc6bfe094920b.png)

![image](https://vip.kingdee.com/download/01094142c4158a264a349fb4adfc13f5e794.png)

     通过元数据对比，确认选中的版本是您期望回滚的版本后，即可点击“回滚”。此时，**平台将把仓库中的“凭证过账”这个页面对应的所有文件都回滚到指定的版本的内容，生成一个最新的版本存储在仓库中。同时，将最新的版本保存到您当前的数据中心。请谨慎使用回滚功能。如下图所示，回滚后，页面的版本（修改时间）都变为最新的。**

![image](https://vip.kingdee.com/download/01099b74566eec134ea58f0d125deb7e8d73.png)

（3）保存到数据中心

    很多用户在开发平台扩展了元数据后，误操作删除了该元数据。此时可以通过“保存到数据中心”功能将元数据直接保存到当前环境，不需要通过部署包。

![image](https://vip.kingdee.com/download/0109ed249ca5db4a423ba6912ff246d8550f.png)

## **3 ****疑难解答**
     功能使用过程中有疑问或者遇到问题，请云之家扫码进群咨询管理员。

![image](https://vip.kingdee.com/download/0109feed4ddd7c1647cfb9c5f1265e037d1d.png)