NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
---
INVALID LANGUAGE PAIR SPECIFIED. EXAMPLE: LANGPAIR=EN|IT USING 2 LETTER ISO OR RFC3066 LIKE ZH-CN. ALMOST ALL LANGUAGES SUPPORTED BUT SOME MAY HAVE NO CONTENT
![image](https://vip.kingdee.com/download/010977e455a0ba2748dc8f5153000b0896f6.png)
Option 2 (Direct Authorization): Enter the list of users, select a user, and click "Direct Authorization".
![image](https://vip.kingdee.com/download/010917f7a42264d4419981a0f8791f228e8f.png)
Find the collaborative development cloud, and check the collaborative development cloud to select all functions.Then click “Save” in the top left corner.
![image](https://vip.kingdee.com/download/0109f58bc4c8f86240afb888b1d9d90c1980.png)
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip-admin.kingdee.com/download/01094fff81cab2524f159b759e7ac7ef0d49.png)
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip-admin.kingdee.com/download/0109aa07105cec974e4a974b4fe6fb97f32f.png)
When entering the "Project Management" interface for the first time, a pop-up box will prompt the user to log in with the GitLab account password.
![image](https://vip-admin.kingdee.com/download/0109e84b59439178451bbec157cc8285d6c4.png)
Enter your account password in the GitLab account login box to log in.
![image](https://vip.kingdee.com/download/01093581beef90f245e1b4471b8222385bf1.png)
INVALID LANGUAGE PAIR SPECIFIED. EXAMPLE: LANGPAIR=EN|IT USING 2 LETTER ISO OR RFC3066 LIKE ZH-CN. ALMOST ALL LANGUAGES SUPPORTED BUT SOME MAY HAVE NO CONTENT
![image](https://vip.kingdee.com/download/010916f79321aac24fd79ba0fe4f36e80c36.png)
Items created after April 8, 2024 with the same developer identity as the current data and with a logged-in GitLab account in the project member list will be filtered.

(Tip: If the project you have created does not exist in the project list, please scan the code and contact the administrator of the collaborative development platform. The QR code is at the end of the article.)
![image](https://vip.kingdee.com/download/0109bf61bb1f52d64a9abce1a7dfc0b2cf70.png)
After the user selects an item, click OK to complete the connection application.Status changed to pending confirmation.
![image](https://vip.kingdee.com/download/01090436b47268344b2ea2cf3fe75a96b03a.png)
![image](https://vip-admin.kingdee.com/download/0109eb9ac043dc1349ee9e96622567e68a60.png)
When the association status of the project is "pending confirmation", the user is required to manually confirm it, as follows:

The user needs to log in to dcs.kingdee.com and execute the consent link in the "List of connected data centers" on the project details page.This action can only be confirmed by the project administrator.
![image](https://vip.kingdee.com/download/01099defa4ff10c44d15a10080d101b6a81b.png)
After the connection is successful, return to the Kingdee AI Starry Sky Collaborative Development Platform and refresh the current interface.

(1) Status before refresh is pending confirmation
![image](https://vip.kingdee.com/download/0109e9a2542f58954376b1fc7e49e88277fc.png)
(2) After refreshing, when the status is associated, you can enter operation 5.
![image](https://vip.kingdee.com/download/01091773b5ba4ddf41c5bcdf82f16c29ac27.png)
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip.kingdee.com/download/0109b339a9416eaa42b48c917de73f1339e1.png)
Enter the metadata push function interface and filter out the metadata modified by the current user by default.
![image](https://vip.kingdee.com/download/010975fb55690fc94d5793d936e628e98904.png)
Select metadata such as Cloud, Apps, and Pages expanded today and click Add to add the selected metadata to the list on the right.

Note: Be sure to tick both the app and the page of the extension on, and then push the repository.Otherwise, only the page will be pushed, and no app information (including groups and menus) will be pushed, resulting in the development platform of the target environment can not find the deployed content.
![image](https://vip.kingdee.com/download/0109b4fabb3f97f0431e9aed0bb20bb454b7.png)
Note: Pushing is only possible if the metadata version of the current data center (that is, the last modified time) is higher than the metadata version of the GitLab repository, preventing the metadata of the GitLab repository from being overwritten by the lower version (the last modified earlier) metadata.
![image](https://vip.kingdee.com/download/010923fbd878f1cb4e268d0418fdd158f145.png)
After selecting the metadata that needs to be pushed to the warehouse, click the "Push to Warehouse" button.After a successful push, is the user prompted to build the successful push metadata?Click the "Build" button to build the selected metadata, which is used to operate the push ladder in six for deployment.

(Hint: does it include the plugin code?If the user needs to package the plugin code together with this build, this option can be checked.Please leave unchecked if the plugin code is not included in the repository.)
![image](https://vip.kingdee.com/download/0109541fb9dd5f9b43e4b6ddbd15cf0a89ff.png)
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip.kingdee.com/download/0109d1e56fb3965c4b29b628f5b6efd60e3a.png)
The system will filter out the 5 patches that were recently built successfully, and the user can select any one of the patches to push.
![image](https://vip.kingdee.com/download/01096b518a4375704fd7845ea2722c6dd1fa.png)
After the push is successful, ask the user to log in to the ladder bill of lading and deploy with the latest pushed patch. See [How to deploy on ladder bills of lading] (https://vip.kingdee.com/knowledge/specialDetail/512315349249697024?category=576345986969244160)