NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
---
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip.kingdee.com/download/01008ca80022b5554a8ab9178de2141ed253.png)
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip.kingdee.com/download/01006046d22641854e9380361accfa51172d.png)
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip-admin.kingdee.com/download/0109e3818630414742d4a3ac15c8e64d9ac0.png)
②: It can be seen from the above figure that the error reason is that the "org.apache.commons.httpclient.HttpClient" dependency has not been introduced into the project, resulting in the implementation of the HttpClient class not being found.

③: Locate the introduced HttpClient class in the local development environment idea, press Ctrl left-click, and it will jump to the specified HttpClient.class.
![image](https://vip.kingdee.com/download/010915dc35799c0747e7812d6931aacb5f9c.png)
④: Click on the positioning in the HttpClient.class interface, you will see the jar corresponding to HttpClient.class.
![image](https://vip-admin.kingdee.com/download/01093d8163864799479b8c702131226677c7.png)
⑤: Then select the corresponding jar, right-click and select "Open In" - > "Explorer"
![image](https://vip.kingdee.com/download/0109d8dd6c6bb288444e96d1fbc3e48aee86.png)
⑥: You can see the corresponding jar in the commons-httpclient-3.1.jar under the "trd" directory.
![image](https://vip.kingdee.com/download/01093c32f02168e64bc9803bd112a6406dce.png)
⑦: can be added in the following locations:

```
api fileTree (dir: trd, include: 'commons-httpclient- * .jar')
```
Among them, trd corresponds to the directory in the sky trd, bos, cus, biz, commons-httpclient- * .jar without version is to facilitate the next upgrade version number changes without modifying the dependency introduction, and it is not recommended to use api fileTree (dir: trd, include: '* .jar') directly, because (* .jar) refers to all jar packages, which does not conform to the specification, and will seriously affect the build performance. Please refer to the jar package on demand for the project, and the business plugin reference specification can also be referred to:
https://developer.kingdee.com/article/241153002391024896
![image](https://vip.kingdee.com/download/0109d97a4022e79b4c70ae5eb0909eec831c.png)