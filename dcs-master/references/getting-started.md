# DCS Getting Started

Load this file when the user is setting up DCS access, a new project, or an environment association.

## First-Time Checklist

1. Log in to `https://dcs.kingdee.com`.
2. Bind a frequently used email. DCS uses this email to create the GitLab account.
3. Open the password email and finish the GitLab password setup.
4. In the product environment, grant `协同开发云` permissions or make the user a full-function user.
5. Create or obtain the correct developer identifier in `https://dev.kingdee.com/custom/team`.
6. Create the project once. DCS auto-creates the Git repo.
7. Invite project members.
8. Complete data-center association in the product-side platform if metadata will be pushed from the product.
9. Complete tenant or environment association before publishing to 天梯 or private cloud.

## DCS And GitLab Onboarding

- First login to DCS prompts the user to bind an email.
- DCS creates the GitLab account from that email.
- The user must finish password setup from the email before GitLab login works in product-side `项目管理`.
- If the user forgets the Git password, reset it from the project member list, copy the temporary password, sign in to GitLab, and set a new password there.

## Developer Identifier Rules

- Customer custom-development projects must use a customer-owned developer identifier with org type `金蝶客户`.
- ISV product-development projects must use an `ISV伙伴` identifier.
- The operator must be a member of the developer-identifier team. This is separate from DCS project membership.
- If the identifier cannot be selected during project creation, check:
  - the project type matches the org type
  - the current user has already been invited into the developer-identifier team
- Developer-identifier team invitations are done in the developer portal and confirmed through system messages.

## Project Creation Rules

- A customer usually needs one DCS project first. Do not create a new project for every build.
- Key fields during creation:
  - `项目类型`: controls developer-identifier filtering and downstream usage
  - `依赖产品`: 苍穹 or 金蝶AI星空
  - `依赖产品版本`: should match the customer production environment
  - project role: admin or developer
  - Git user role
  - push permission: only users with this permission can push patches
- Saving the project creates the repo automatically and usually initializes:
  - `code/`
  - `datamodel/`
  - `docs/`
  - `webapp/`
  - `cosmic.json`

### ISV Project-Type Availability

- `ISV标准产品开发` is not always shown by default in the project-type list.
- If the user cannot see the ISV project type at all, do not collapse this into a pure developer-identifier problem.
- Current platform rule from field experience:
  - the user should first contact DCS platform operations
  - operations will direct the user to contact 唐佐平 in the ecology team for authorization
  - after authorization, the user can create `ISV标准产品开发` projects
- Treat this as a gating permission on project-type visibility, not merely a downstream identifier-selection filter.

## Member Invitation

- DCS project members are added after the project is created.
- Admin copies the invitation link and sends it to the member.
- The invited member confirms the email and applies to join.
- Project admin reviews and approves the request.
- Project membership does not replace developer-identifier-team membership. Some flows require both.

## Product-Side Data-Center Association

Use this when the user wants to push metadata directly from 金蝶AI星空 product-side `协同开发平台`.

1. In the product-side platform, choose `关联项目`.
2. The list only shows projects that meet all of these:
   - same developer identifier as the current data center
   - created after `2024-04-08`
   - current Git user is already in the DCS project member list
3. The product-side status becomes `待确认`.
4. A DCS project admin must open the same project in DCS and approve the request in `关联数据中心列表`.
5. Refresh the product-side page until the status becomes `已关联`.

## Public-Cloud Tenant Association

Use this before pushing artifacts to 天梯.

1. In DCS `协同开发云 -> 关联环境 -> 关联公有云环境`, add a new environment.
2. Select the project and enter the public-cloud production tenant domain.
3. Copy the security code.
4. A customer ops account signs in to `https://ops.kdcloud.com` and confirms the association.
5. Wait around 3 minutes or refresh the result in DCS.
6. Publish only after the association status is `已关联`.

## Private-Cloud Association

- Private-cloud projects should associate the private-cloud environment instead of the public-cloud tenant.
- The bundled docs confirm the branch exists, but they do not include a full downstream private-cloud screen guide.

## Common Setup Blockers

- `找不到开发商标识`
  - create the identifier, or get team authorization from the owner
  - make sure org type matches project type
- `新建项目时看不到 ISV标准产品开发`
  - this is not the same as "cannot select developer identifier"
  - check whether the account has been opened for ISV project-type creation
  - if not, ask the user to contact DCS platform operations and follow the authorization path to 唐佐平 for ISV project creation
- product-side project not visible for association
  - check developer identifier, project creation date, and DCS project membership
- `未查询到关联环境`
  - the tenant or private-cloud environment was not associated, or the association is not yet approved

## Success Signals

- GitLab login works in product-side `项目管理`.
- Product-side project association status is `已关联`.
- Environment association status is `已关联`.
- The user can see the project repo and member list in DCS.
