NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
---
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
Idea does not resolve all projects; DCS resolves all projects (for example, if you add or remove modules, you need to modify all projects, because it only works in DCS, so you only need to modify KingCode).

Inside idea, the setting.gradle configuration is as follows
![image](https://vip.kingdee.com/download/0100a49a36d756c044dea071361aa296e843.png)
DCS will parse the all project, the bulid.gradle configuration of the project is as follows
![image](https://vip.kingdee.com/download/0100b2ac69df24474b9f83d5a79e9dddeb37.png)
Idea has simplified the build.gradle, so the idea native build.gradle has only 3 lines by default and should not be submitted to KingCode

dependencies {
api project (': xxx')
}

The local build.gradle configuration for idea is shown below (using the xx-xx-xx-business project as an example)
![image](https://vip.kingdee.com/download/010001c4770499b647dfa1502dfae098b463.png)
From the following figure in the DCS initialization code
![image](https://vip.kingdee.com/download/0100f103a0bf19b8417b9a4219084d38e4c9.png)
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip.kingdee.com/download/0100bc73caf4440342408ec884f09a6bbe5b.png)
If there is an inter-app dependency, delete the module reference in the relying party's build.gradle
implementation (project (': xxx')).　For example, to remove the yza5-imsc-app-business module, since the yza5-imsc-app-mservice module references yza5-imsc-app-business, you need to modify the following
![image](https://vip.kingdee.com/download/010079866006e58f4168aff12feee0090fc8.png)
* * (II) The build.gradle of the * * DCS in Scenario 2 is modified as follows

Modify build.gradle in the all project in KingCode To remove the yza5-imsc-iptm-business module, modify the following figure
![image](https://vip.kingdee.com/download/0100b74e19d86d394df59c52f5c53a579814.png)
If there is an inter-app dependency, delete the module reference in the relying party's build.gradle in KingCode.　If you delete the yza5-imsc-iptm-business module, since the module is referenced by yza5-imsc-iptm-webapi, you need to modify it as follows
![image](https://vip.kingdee.com/download/010049caf57a0f9d4eca923a221a75da6762.png)
* * 2, * * Add the modules you need

* * (a) * * How to modify idea's build.gradle

Copy the existing module in idea. If you want to add the module yza5-imsc-iptm-webapi, copy yza5-imsc-iptm-business and modify it to the corresponding name.

Modify the outermost settings.gradle to add the corresponding module.For example, to add the yza5-imsc-iptm-webapi module, modify the following figure
![image](https://vip.kingdee.com/download/010010a18533bf3b4206ad9af26d8bfa1769.png)
Modify the build.gradle of yza5-imsc-iptm-webapi, you can refer to the build.gradle of other modules to modify it, for example
![image](https://vip.kingdee.com/download/0100fafdc07f57d74f1480ecf718434483bb.png)
* * (II) * * How to modify build.gradle in DCS

If you add the yza5-imsc-iptm-webapi module, you need to modify the build.gradle in the all project as shown in the following figure
![image](https://vip.kingdee.com/download/01000cb0b3b68d4b4d589ce925c34666ace0.png)
Submit new modules and modifications from idea to KingCode

Copy the build.gradle of the other module in KingCode and modify the build.gradle of the current module in KingCode as shown below
![image](https://vip.kingdee.com/download/01007c17bd954e5745ea8dd1c08673c7a2fb.png)
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip.kingdee.com/download/0100391bcb5362154f0fa25f9113416f3acc.png)
* * 2, * * * * How to modify build.gradle in DCS * *

For specific implementation methods, please use Cloud Home to scan the code into the group and contact Wu Gang for processing.
![image](https://vip.kingdee.com/download/0100f53432446172435b8d807a27684a743a.jpg)
NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
![image](https://vip.kingdee.com/download/010073e251d3700949ac97bf8173000853a2.png)
* * 2, * * How to modify build.gradle in DCS

There is no need to modify the configuration, it will be automatically relied upon when built.But to focus on the application order in the DCS build task entry, the default trailing depends on the front