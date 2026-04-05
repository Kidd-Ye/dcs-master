# DCS项目构建提示"依赖错误"解决方案

> 分类: 常见问题与解决方案/构建类问题
> 来源: https://vip.kingdee.com/knowledge/626374877439787776?productLineId=40&isKnowledge=2&lang=zh-CN

---

## 一 问题描述
    DCS二开项目代码构建提示"依赖错误"，如下图所示：

![image](https://vip.kingdee.com/download/01008ca80022b5554a8ab9178de2141ed253.png)

## 二 解决方法

### 原因1：没添加基本依赖模块
①：项目创建后使用小助手初始化会code下面的base有common和helper模块，需要一起提交到仓库，

因为common模块以添加了基本依赖jar，使用小助手初始化项目的业务模块（如下图的yza5-cosmic.yza5-pwo19-fcloud-fapp）会引用到common模块会从而自动添加了基础的jar依赖，因为如果出现上诉错误时请检查common和helper模块是否提交到GitLab仓库里面。

![image](https://vip.kingdee.com/download/01006046d22641854e9380361accfa51172d.png)

### 原因2：没添加具体依赖
①：先看"构建错误智能分析"里面的"日志详情行数"，然后展开展开日志详情，下拉到具体行数，查看错误提示，如下图所示：
![image](https://vip-admin.kingdee.com/download/0109e3818630414742d4a3ac15c8e64d9ac0.png)

②：从如上图所示可以看出错误原因是“org.apache.commons.httpclient.HttpClient”依赖没有被引入到项目中，导致找不到HttpClient类的实现。

③：在本地开发环境IDEA里面找到引入的HttpClient类，按Ctrl+鼠标左键点击，会跳转到指定HttpClient.class。

![image](https://vip.kingdee.com/download/010915dc35799c0747e7812d6931aacb5f9c.png)

④：在HttpClient.class界面点击定位，会可以看到HttpClient.class对应的jar。

![image](https://vip-admin.kingdee.com/download/01093d8163864799479b8c702131226677c7.png)
⑤：然后选中对应jar，右击鼠标，选择“Open In”->"Explorer"

![image](https://vip.kingdee.com/download/0109d8dd6c6bb288444e96d1fbc3e48aee86.png)

⑥：可以看到对应的jar在“trd”目录下的commons-httpclient-3.1.jar。

![image](https://vip.kingdee.com/download/01093c32f02168e64bc9803bd112a6406dce.png)

⑦：可以在如下位置添加:

```
api fileTree(dir: trd, include: 'commons-httpclient-*.jar')
```
其中trd对应苍穹trd、bos、cus、biz中的目录，commons-httpclient-*.jar不带版本是为了方便下次升级版本时版本号发生变化不用修改依赖引入，不推荐直接使用api fileTree(dir: trd, include: '*.jar')，因为（*.jar）方式引用所有的jar包，不符合规范，也会严重影响构建性能，项目请按需引用jar包，业务插件引用规范也可参考：

https://developer.kingdee.com/article/241153002391024896

![image](https://vip.kingdee.com/download/0109d97a4022e79b4c70ae5eb0909eec831c.png)