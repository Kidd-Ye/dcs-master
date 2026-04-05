# 如何推送元数据到项目的GitLab仓库？

> 分类: 快速入门/4-扩展元数据/如何将扩展的元数据上传到项目GitLab仓库
> 来源: https://vip.kingdee.com/knowledge/592005636909247744?productLineId=40&isKnowledge=2&lang=zh-CN

---

*本知识仅适用于金蝶AI星空，星瀚请忽略。

## 1 功能介绍
        用户在公有云沙箱环境或者本地开发环境进行了元数据扩展后，要部署到公有云生产环境前，需要通过协同开发平台将元数据构建成一个补丁，才可以推送天梯进行部署。

       协同开发平台的每个项目都会创建一个仓库，用于存放用户提交的元数据。每次发起构建时，协同开发平台会从项目的仓库拉取需要部署的元数据进行打包，再推送到天梯部署生产环境。

       本功能支持用户在金蝶AI星空环境直接选择元数据，推送项目GitLab仓库。

 

## 2 主要操作

## 操作一：权限配置
请用户登录本地搭建的金蝶AI星空客户端（若本地未搭建环境，可以登录公有云租户沙箱环境），通过以下两种方式授权：

方式一（全功能用户）：在金蝶AI星空客户端使用administrator登录，进入“全功能用户列表”，将用户设置为全功能用户后，即可完成协同开发平台功能配置。

![image](https://vip.kingdee.com/download/010977e455a0ba2748dc8f5153000b0896f6.png)

方式二（直接授权）：进入用户列表，选中一个用户，点击”直接授权“。

![image](https://vip.kingdee.com/download/010917f7a42264d4419981a0f8791f228e8f.png)

查找到协同开发云，并且勾选协同开发云即可选中全部功能。再点击左上角”保存“。

![image](https://vip.kingdee.com/download/0109f58bc4c8f86240afb888b1d9d90c1980.png)

## 操作二： 导入开发商标识
用户首次进入协同开发平台这个应用，检测到当前数据中心没有导入开发商标识时，会提示用户需先登录管理员账号（administrator）设置开发商标识。请用户先登录开发者门户创建开发商标识，具体操作可点击 [如何创建开发商标识](https://vip.kingdee.com/knowledge/specialDetail/512315349249697024?category=576345986969244160&id=527779748768929280&productLineId=40&lang=zh-CN) 查看。已经导入开发商标识的用户可以跳过此操作。

注意：若是客户定制化项目，必须使用客户创建的开发商标识，即组织类型为金蝶客户。

![image](https://vip-admin.kingdee.com/download/01094fff81cab2524f159b759e7ac7ef0d49.png)

## 操作三： 登录GitLab
点击协同开发平台工作台的“项目管理”功能进入项目管理功能界面。

![image](https://vip-admin.kingdee.com/download/0109aa07105cec974e4a974b4fe6fb97f32f.png)

首次进入“项目管理”功能界面时，会弹框提示需用户使用GitLab账号密码进行登录。

![image](https://vip-admin.kingdee.com/download/0109e84b59439178451bbec157cc8285d6c4.png)

在GitLab账号登录框中输入账号密码进行登录。

![image](https://vip.kingdee.com/download/01093581beef90f245e1b4471b8222385bf1.png)

【常见问题】

（1）[如何激活GitLab账号](https://vip.kingdee.com/knowledge/specialDetail/512315349249697024?category=542028759550149120&id=536206600902817792&productLineId=40&lang=zh-CN)

（2）[如何修改GitLab密码](https://vip.kingdee.com/knowledge/specialDetail/512315349249697024?category=542028759550149120&id=536215396576301568&productLineId=40&lang=zh-CN)

## 操作四： 关联项目
用户登录GitLab账号后，点击“关联项目”。

![image](https://vip.kingdee.com/download/010916f79321aac24fd79ba0fe4f36e80c36.png)

系统将过滤出与当前数据的开发商标识一致、2024年4月8日后创建且项目成员列表中包含登录的GitLab账号的项目。

（提示：如果已经创建的项目在项目列表不存在时，请云之家扫码进群联系协同开发平台管理员处理，二维码在文章末尾处。）

![image](https://vip.kingdee.com/download/0109bf61bb1f52d64a9abce1a7dfc0b2cf70.png)

用户选择一个项目后，点击确定即可完成关联申请。状态变为待确认。

![image](https://vip.kingdee.com/download/01090436b47268344b2ea2cf3fe75a96b03a.png)

![image](https://vip-admin.kingdee.com/download/0109eb9ac043dc1349ee9e96622567e68a60.png)

当项目的关联状态为“待确认”时，需要用户手动确认，具体方式如下：

用户需登录dcs.kingdee.com，在项目详情页的“关联数据中心列表”中执行同意关联。该操作只能由项目管理员进行确认。

![image](https://vip.kingdee.com/download/01099defa4ff10c44d15a10080d101b6a81b.png)

关联成功后，回到金蝶AI星空协同开发平台，刷新当前界面。

（1）刷新前状态为待确认

![image](https://vip.kingdee.com/download/0109e9a2542f58954376b1fc7e49e88277fc.png)
（2）刷新后状态为已关联时，即可进入操作五

![image](https://vip.kingdee.com/download/01091773b5ba4ddf41c5bcdf82f16c29ac27.png)

## 操作五： 推送元数据
用户关联项目完成后，可以进入“元数据推送”功能界面。可点击已关联项目列表中操作列的“推送元数据”跳转进入。

![image](https://vip.kingdee.com/download/0109b339a9416eaa42b48c917de73f1339e1.png)

进入元数据推送功能界面，默认过滤出当前用户今天修改的元数据。

![image](https://vip.kingdee.com/download/010975fb55690fc94d5793d936e628e98904.png)

选择今天扩展的云、应用和页面等元数据，点击“添加”，即可将选中的元数据加入到右侧列表中。

注意：请务必将扩展的应用和页面都勾选上，然后推送仓库。否则会出现只推送了页面，没有推送应用信息（包含分组和菜单），而导致目标环境的开发平台找不到部署的内容。

![image](https://vip.kingdee.com/download/0109b4fabb3f97f0431e9aed0bb20bb454b7.png)

注意：只有当前数据中心的元数据版本（即最后修改时间）高于GitLab仓库的元数据版本，才可以进行推送，防止低版本（最后修改时间较早）元数据覆盖GitLab仓库的元数据。

![image](https://vip.kingdee.com/download/010923fbd878f1cb4e268d0418fdd158f145.png)

选择好需要推送到仓库的元数据后，点击“推送到仓库”按钮。推送成功后，系统提示用户是否将推送成功的元数据进行构建？点击“构建”按钮即可将选择的元数据进行构建，用于操作六中的推送天梯进行部署。

（提示：是否包含插件代码？若用户本次构建需要将插件代码也一起打包，可以勾选此选项。如果仓库中没有包含插件代码，请不要勾选。）

![image](https://vip.kingdee.com/download/0109541fb9dd5f9b43e4b6ddbd15cf0a89ff.png)

## 操作六： 推送天梯
用户在操作五中构建了补丁包成功后，可以回到“项目管理”界面，点击“推送天梯”按钮。

![image](https://vip.kingdee.com/download/0109d1e56fb3965c4b29b628f5b6efd60e3a.png)

系统将过滤出最近构建成功的5个补丁，用户可以选择任意一个补丁进行推送。

![image](https://vip.kingdee.com/download/01096b518a4375704fd7845ea2722c6dd1fa.png)

推送成功后，请用户登录天梯提单，使用最新推送的补丁进行部署。具体操作请查看  [如何在天梯提单部署](https://vip.kingdee.com/knowledge/specialDetail/512315349249697024?category=576345986969244160&id=576103829129523456&productLineId=40&lang=zh-CN) 。