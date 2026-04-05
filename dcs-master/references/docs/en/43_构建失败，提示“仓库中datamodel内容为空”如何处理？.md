NO QUERY SPECIFIED. EXAMPLE REQUEST: GET?Q=HELLO&LANGPAIR=EN|IT
---
* * Scenario: * * The build failed, check the logs and find that the prompt information is: The content of the datamodel in the repository is empty, and the build failed.
![image](https://vip.kingdee.com/download/01095622c8ae6bfd403d8532e4912436af5e.png)
* * Analysis: * * The platform fails to build metadata compression packages properly when there are no conforming metadata files in the datamodel folder in the repository.The metadata structure of the specification is shown in the figure below.
![image](https://vip.kingdee.com/download/0109e87f6c4943a14367a00714238e95422c.png)
* * Solution: * * Use the "co-development platform" in the product to first associate the project and then push the metadata to the project's warehouse. [How do I push metadata to the project's GitLab repository?] (https://vip.kingdee.com/knowledge/specialDetail/512315349249697024?category=592008682863621120)