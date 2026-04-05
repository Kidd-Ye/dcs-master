# 苍穹开发助手引用协同code模板-疑难问题解答

> 分类: 常见问题与解决方案
> 来源: https://vip.kingdee.com/knowledge/526100305423800832?productLineId=40&isKnowledge=2&lang=zh-CN

---

## 一、gradle配置问题说明
**1.问题原因**

当前IDEA的gradle版本和DCS版本不一致，所以IDEA与DCS中的gradle配置不同。

IDEA的gradle是为了本地管理构建及运行时依赖；DCS的gradle是为了完成云端构建并上天梯。 IDEA的gradle版本为7.3；DCS的gradle版本为5.x，故gradle配置的语法是不同的。

注：当前IDEA的gradle版本和DCS版本不一致问题，计划下个版本解决

**2.注意事项**

注：下文的KingCode表示git仓库。 

IDEA本地的gradle配置，是用于运行本地项目工程，不需要提交到git仓库上， 否则将影响在线构建。

解决DCS构建问题的对应的gradle配置才需要提交到git仓库。

IDEA中的gradle配置不要直接提交到KingCode；如果需要解决DCS构建问题，需要直接修改KingCode中的gradle配置。

IDEA不会解析all工程；DCS会解析all工程（举例：如果增加或删除模块，需要修改all工程，由于只在DCS生效，所以只需要修改KingCode）。

IDEA里面setting.gradle 配置如下图

![image](https://vip.kingdee.com/download/0100a49a36d756c044dea071361aa296e843.png)

DCS会解析all工程，该工程的bulid.gradle配置如下图

![image](https://vip.kingdee.com/download/0100b2ac69df24474b9f83d5a79e9dddeb37.png)

IDEA对build.gradle做了简化，所以，IDEA本地的build.gradle默认只有3行，且不要提交到KingCode

dependencies {
api project(':xxx')
}

IDEA本地的build.gradle配置如下图（使用xx-xx-xx-business工程为例）

![image](https://vip.kingdee.com/download/010001c4770499b647dfa1502dfae098b463.png)

来源于 DCS初始化代码里面的如下图

![image](https://vip.kingdee.com/download/0100f103a0bf19b8417b9a4219084d38e4c9.png)

## 二、模块调整
**1、删除不需要的模块**

删除不需要的模块分为两个场景，一种是本地IDEA如何通过修改build.gradle实现不需要的模块删除；一种是如何修改协同项目代码仓库中的build.gradle实现不需要的模块删除。具体方案如下：

**（一）场景一中IDEA的build.gradle修改如下**

如果不需要某个模块，该模块可以删除也可以不删除。

若想要删除不必要的模块，请修改最外层的settings.gradle，去掉要删除的模块。例如若要删除yza5-imsc-iptm-webapi模块，　如下图需删除代码第33行和第62行。

![image](https://vip.kingdee.com/download/0100bc73caf4440342408ec884f09a6bbe5b.png)

如果存在应用间依赖，要删除依赖方的build.gradle中的模块引用
implementation(project(':xxx'))。　例如若要删除yza5-imsc-app-business模块，由于yza5-imsc-app-mservice模块引用了yza5-imsc-app-business，　则需要修改如下

![image](https://vip.kingdee.com/download/010079866006e58f4168aff12feee0090fc8.png)

**（二）场景二中**DCS的build.gradle修改如下

在KingCode中修改all工程中的build.gradle　若要删除yza5-imsc-iptm-business模块，修改如下图

![image](https://vip.kingdee.com/download/0100b74e19d86d394df59c52f5c53a579814.png)

如果存在应用间依赖，要在KingCode中删除依赖方的build.gradle中的模块引用。　若删除yza5-imsc-iptm-business模块，　由于yza5-imsc-iptm-webapi引用了该模块，需要修改如下

![image](https://vip.kingdee.com/download/010049caf57a0f9d4eca923a221a75da6762.png)

**2、**增加自己需要的模块

**（一）**IDEA的build.gradle如何修改

复制IDEA中的已有模块，若想增加模块yza5-imsc-iptm-webapi，复制yza5-imsc-iptm-business，　并修改为对应的名称。

修改最外层的settings.gradle，新增对应的的模块。例如若要新增yza5-imsc-iptm-webapi模块，　修改如下图

![image](https://vip.kingdee.com/download/010010a18533bf3b4206ad9af26d8bfa1769.png)

修改yza5-imsc-iptm-webapi的build.gradle，　可以参考其他的模块的build.gradle进行修改，例如

![image](https://vip.kingdee.com/download/0100fafdc07f57d74f1480ecf718434483bb.png)

**（二）**DCS中的build.gradle如何修改

如增加了yza5-imsc-iptm-webapi模块，需要修改all工程中的build.gradle 如下图

![image](https://vip.kingdee.com/download/01000cb0b3b68d4b4d589ce925c34666ace0.png)

将IDEA中新建的模块以及修改的内容提交到KingCode

复制其他模块在KingCode的build.gradle，并在KingCode中修改当前模块的build.gradle　例如下图

![image](https://vip.kingdee.com/download/01007c17bd954e5745ea8dd1c08673c7a2fb.png)

### 

## 三、存在三方包依赖
**1、IDEA的build.gradle如何修改**

手工将lib中的包，复制到systemProp.cosmic_home指定的目录中的cus子目录．　例如下图

![image](https://vip.kingdee.com/download/0100391bcb5362154f0fa25f9113416f3acc.png)

**2、****DCS的build.gradle如何修改**

具体实现方式请使用云之家扫码进群联系吴帮处理。

![image](https://vip.kingdee.com/download/0100f53432446172435b8d807a27684a743a.jpg)

## 四、存在应用间依赖
**1、**IDEA的build.gradle如何修改

修改依赖方的build.gradle中，增加implementation(project(':xxx'))

例如，　yza5-imsc-app-mservice依赖了　yza5-imsc-app-business模块，则需要修改如下图

![image](https://vip.kingdee.com/download/010073e251d3700949ac97bf8173000853a2.png)

**2、**DCS的build.gradle如何修改

不用修改配置，构建时会自动依赖。但要关注在DCS构建任务分录中的应用顺序，默认后边依赖前边