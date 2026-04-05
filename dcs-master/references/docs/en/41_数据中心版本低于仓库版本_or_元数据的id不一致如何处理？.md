NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
---
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip.kingdee.com/download/0109880bfde191464c96aa7ab00a227caf2a.png)
**
**

* * Problem analysis * *: There are two scenarios that users need to judge for themselves.

* * Scenario 1 * *: The user has expanded the application or page in the local development environment or the public cloud sandbox environment, and pushed it to the GitLab repository through the functions of the collaborative development platform. * * It has not been deployed to the production environment * *.Subsequently, the application or page was deleted from the sandbox or local development environment, and the application or page with the same name was re-expanded.Although the name and encoding seen on the card of the app or page are consistent, the value set in the id field of the database is actually inconsistent.At this time, when the user wants to push the last extended application or page to the GitLab repository, the collaborative development platform compares the current metadata with the id in the repository, finds the inconsistency and warns in advance, prohibiting the user from pushing and initiating the patch construction.
INVALID LANGUAGE PAIR SPECIFIED. EXAMPLE: LANGPAIR=EN|IT USING 2 LETTER ISO OR RFC3066 LIKE ZH-CN. ALMOST ALL LANGUAGES SUPPORTED BUT SOME MAY HAVE NO CONTENT
![image](https://vip.kingdee.com/download/01098d7d9a356be941599127b174767cf8df.png)
Enter the warehouse management interface, find the application to which the metadata you want to delete belongs in the tree node on the left, and then expand the node to find the "page information" to find the corresponding page on the right.Click Remove from repository to delete the metadata.After deletion, you can return to the "Metadata Push" interface to push metadata to the repository.
![image](https://vip.kingdee.com/download/01093e536e45bc00425fbb4de4acecae4254.png)
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip-admin.kingdee.com/download/0109439ce94fc7434bb087566bb1b94fc0e8.png)
- Enter the development platform of the sandbox environment to export each page under the travel for everyone app. After one page is exported, it is a separate zip file, which is convenient for subsequent import.

- Export the production environment and import the compressed package of the application in the development platform, at this time, the IDs of the sandbox environment and the production environment with the same name have become consistent.The user can then re-import each page exported in the previous step in the development platform and associate it with this app.

- Use the metadata push function of the collaborative development platform to push the entire travel application of the sandbox environment to the warehouse together, at this time, the metadata versions of the sandbox environment, the GitLab warehouse and the production environment remain the same.

(2) If the check result is inconsistent when a page in the sandbox environment pushes the GitLab warehouse, follow the steps below:

- Taking the conflict of the page (named testorg0805) under the travel for everyone app as an example, the user enters the development platform of the production environment and exports the metadata file of the page, as shown in the following figure.
![image](https://vip-admin.kingdee.com/download/0109c04af57b65ec444c8ce0b3be8db7d997.png)
- Go to the development platform of the sandbox environment to export the metadata file of the page with the same name (named testorg0805) for backup, and then delete it.Then import the zip file of the page exported by the production environment (named testorg0805), so that the page with the same name of the sandbox environment and the production environment is the same, and its id is exactly the same.
![image](https://vip-admin.kingdee.com/download/0109b543ec26fef2487dae38face79bb70bd.png)
INVALID LANGUAGE PAIR SPECIFIED. EXAMPLE: LANGPAIR=EN|IT USING 2 LETTER ISO OR RFC3066 LIKE ZH-CN. ALMOST ALL LANGUAGES SUPPORTED BUT SOME MAY HAVE NO CONTENT
![image](https://vip.kingdee.com/download/010920113df302c94a12a689c185148551de.png)
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT