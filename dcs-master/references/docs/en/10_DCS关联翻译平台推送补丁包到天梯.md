NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
---
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip.kingdee.com/download/01005ed4bcdb14d34690b4ed7a5beb6b9b68.png)
Click the Add Association button.
![image](https://vip.kingdee.com/download/010031372ee3475747dcb5d6c7cb9760ecd6.png)
Enter the “Environment Configuration” interface of the translation platform.The access link to the translation platform is: [https://translate.kdcloud.com] (/tolink? target = https %3A % 2F % 2Ftranslate.kdcloud.com)
![image](https://vip.kingdee.com/download/0100e5b78f1792ea4659bcedb4b10f48589b.png)
Click the "Encoding" in the blue font in the environment configuration list, as shown in agilepre, and copy the "Environment Security Code" in the pop-up environment configuration interface.
![image](https://vip.kingdee.com/download/010070e3363042e447cf9e8558b9182c227a.png)
Return to the DCS interface, select the item, fill in the security code and save.If the security code is verified, the environment code, environment name, environment domain name and other information will be displayed, and the user can confirm whether it is the target environment according to the information.
![image](https://vip.kingdee.com/download/01003bd664f5b7b041709d1d725dfabbc6fe.png)
* * (2) Push patches to DCS project artifact list * *

After the user builds the patch on the translation platform, he can select a patch in the build record list and push the patch to the corresponding project artifact list of the DCS by clicking the "Publish DCS" button.
![image](https://vip.kingdee.com/download/010075bdec6164c240f78506aa9f16750c78.png)
After the push is successful, you need to wait for the DCS to initiate the artifact construction (estimated 1-2 minutes) process. After refreshing the artifact list, you can see the artifacts pushed from the translation platform.The user can determine whether the artifact is from the translation platform based on the "artifact source".
![image](https://vip.kingdee.com/download/0100e5d7509493ad4f42a027b193018df3ab.png)
* * (3) Push multilingual products to the ladder * *

When the quality scanning conclusion of the product is "passed", the user can select the multilingual product to push to the ladder in the same way as pushing the customized development patch package.