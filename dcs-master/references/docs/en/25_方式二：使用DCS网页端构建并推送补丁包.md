NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
---
1 Log in to the collaborative development platform

Log in to the co-development platform at [https://dcs.kingdee.com/] (https://dcs.kingdee.com/) 

2 Initiating an online build

(1) Check a project and click "Build Online";

(2) Click the "Build Online" button;

(3) According to the usage scenario, if you only need to build metadata, select "Metadata" for the build content; if you need to build a jar package, select "Metadata plug-in code";

(4) For Xinghan, the difference metadata can be pushed to the collaborative development platform through the implementation of the configuration platform. Therefore, if it is a Xinghan project, there are options for [partial metadata] and [partial metadata plug-in code]. For the implementation of the platform's difference metadata, you can see the article: https://vip.kingdee.com/link/s/lIzTn

(5) Click the “Start Build” button.
![image](https://vip.kingdee.com/download/01090cae815ae1c14f6b96fc31603aebf354.png)
The "Last Build Result" of the project corresponding to the project list is updated to running. When this status is updated to successful, the patch is completed.
![image](https://vip.kingdee.com/download/01094cb59dbfd667472da6959d978d082f15.png)
After the patch is successfully built, you can enter the artifact list and wait for the quality scan to complete.When the quality scan conclusion is passed, the patch can be pushed to the ladder for deployment.
![image](https://vip.kingdee.com/download/010939b08c407bec4afc9133f65d2d7bd402.png)
If the product does not pass the quality scan, click "View Quality Report" for more details. As shown below:
![image](https://vip.kingdee.com/download/0109cf28dabb55914e01a6009712b65d7290.png)
During a Fortify scan, the number of critical, high-risk, and medium-risk vulnerabilities must be cleared.Users can download the PDF for quality issues and corresponding fixes.

The number of critical, high-risk vulnerabilities scanned by SonarQube must be cleared to pass.You can do this by clicking on “View details.Review the "Fix Recommendations" to complete the bug fix according to the bug name and the number of rows.Once the fix is complete, re-initiate the online build to scan again.
![image](https://vip.kingdee.com/download/0109a55035f1977d4faa8912982e75efcb53.png)
Common Processing Methods Refer to [Common Processing Methods for SonarQube Scan Results] (https://developer.kingdee.com/article/489707796431276032?productLineId=29)