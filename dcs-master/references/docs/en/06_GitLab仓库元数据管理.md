NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
---
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip.kingdee.com/download/0109e30bc3005b7f4a37b865d81a3c608e24.png)
(3) Functional interface

In the warehouse management function interface, users can use the menu on the left to find the corresponding business cloud and application nodes under the cloud, each application contains SQL scripts and page information.There are currently three functions that users can delete scripts and metadata under the app, roll back the version of the page, and save the page to the data center.
![image](https://vip.kingdee.com/download/010905eaff0eb7be475e9e29de11f95f4290.png)
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip.kingdee.com/download/01094021b3614fbf4593bdc9ed30577f4697.png)
![image](https://vip.kingdee.com/download/0109f9fea1201af64ceea890ea863a2f7aa1.png)
(2) Rollback

    Each time the user uses the Push Metadata function to push the latest metadata to the repository, the repository records a version information.This feature is available when the user wants to fallback to a version of the metadata.

    Premise for using this feature: * * There is a metadata in the current data center that is completely consistent with the warehouse * *.
![image](https://vip.kingdee.com/download/01095ab33c80a5af46d7a4736b0e564e2f5c.png)
Click the "Rollback" button, the "Metadata History" list pops up, and the previous version is selected for metadata comparison.* * The comparison here is between the version of the current repository and the version selected in the list. * *
![image](https://vip.kingdee.com/download/0109c11b3110eced4d5e868cc6bfe094920b.png)
![image](https://vip.kingdee.com/download/01094142c4158a264a349fb4adfc13f5e794.png)
After comparing the metadata and confirming that the selected version is the one you want to roll back, click Roll Back.At this point, the * * platform will roll back all the files corresponding to the "Voucher Posting" page in the repository to the content of the specified version, and generate a latest version to be stored in the repository.In the meantime, save the latest version to your current data center.Use the rollback function with caution.As shown in the following figure, the version (modification time) of the page changes to the latest after rolling back. * *
![image](https://vip.kingdee.com/download/01099b74566eec134ea58f0d125deb7e8d73.png)
(3) Save to data center

    Many users mistakenly deleted the metadata after the development platform extended it.At this point, you can save the metadata directly to the current environment through the "Save to Data Center" function, without the need to deploy the package.
![image](https://vip.kingdee.com/download/0109ed249ca5db4a423ba6912ff246d8550f.png)
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip.kingdee.com/download/0109feed4ddd7c1647cfb9c5f1265e037d1d.png)