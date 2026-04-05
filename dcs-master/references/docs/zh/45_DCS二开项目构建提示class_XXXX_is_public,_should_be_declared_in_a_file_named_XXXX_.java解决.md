# DCS二开项目构建提示"class XXXX is public, should be declared in a file named XXXX .java"解决方案

> 分类: 常见问题与解决方案/构建类问题
> 来源: https://vip.kingdee.com/knowledge/628244553509914624?productLineId=40&isKnowledge=2&lang=zh-CN

---

**

## 1 问题描述

DCS二开项目构建提示class XXXX is public, should be declared in a file named XXXX .java"，如下图所示：

![image](https://vip.kingdee.com/download/0109eb6668e5f06e4de4a4037677986e621b.png)

## 2 解决方法

- 如上图所示提示“error: class Purchase is public, should be declared in a file named Purchase.java”错误的主要原因是：Java 规定，每个公共类都必须在一个与其同名且具有`.java`扩展名的文件中声明，而该项目中的SaleDeliveryBillPlugin.java文件中定义的公共类名却是Purchase，违反了java规定所以构建错误，因此只需要按如下方式修改，然后重新构建即可：

     方法一：将SaleDeliveryBillPlugin.java文件重名为Purchase.java；

     方法二：将SaleDeliveryBillPlugin.java文件内的公共类Purchase改成SaleDeliveryBillPlugin即可；

![image](https://vip.kingdee.com/download/0109e930c11af90b4bf9983ec46aeb88fda8.png)

##