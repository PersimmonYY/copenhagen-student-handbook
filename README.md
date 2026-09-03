# 哥本哈根留学生存手册

本项目由哥本哈根中国学生学者联合会维护，面向从中国赴丹麦、以非欧盟身份申请或持有学生居留许可的留学生。

当前内部审核版本为 **2026.11（2026--2027 学年版）**。内容已经过两轮编译、链接检查和逐页视觉检查，但政策、费用、交通产品及服务入口仍可能变化。审核者在实际办理前仍应再次打开正文所列官方页面核对。

> **内部审核状态：** 当前仓库和 PDF 仅用于 CSSA-Copenhagen 内部协作审核，尚非对外正式发布版本。请勿将 PDF、源文件、截图、仓库或 Release 链接转发至内部审核范围之外。本项目不是开源项目，也未授权开放内容许可。具体边界见 [COPYRIGHT.md](COPYRIGHT.md)。

## 查看内部审核稿

- [下载当前审核版 PDF](output/pdf/哥本哈根留学生存手册_2026.11.pdf)
- [查看更新路线图](UPGRADE_PLAN.md)
- [查看关键事实来源台账](SOURCE_REGISTER.md)
- [查看社交平台内容与版权规范](SOCIAL_CONTENT_POLICY.md)

## 项目结构

```text
main.tex                 LaTeX 主文件、版式和章节顺序
chapters/                各章节正文
figures/                 手册使用的图片和二维码
output/pdf/              已发布的 PDF 版本
SOURCE_REGISTER.md       易变事实与官方来源维护台账
UPGRADE_PLAN.md          版本计划及完成情况
COMMENT_INTEGRATION.md   共建批注处理记录
SOCIAL_CONTENT_POLICY.md 社交平台材料的核验和版权规则
PLUGIN_DESIGN.md          哥哈留学助手插件设计和阶段计划
plugins/                  本地 Codex 插件与五个专项 skills
```

## 哥哈留学助手插件（MVP）

仓库包含 `plugins/copenhagen-chinese-student-guide/`，将手册内容按落地、日常生活、求职和内部维护分为可按需调用的 skills。插件默认服务于来自中国的非欧盟高等教育学生；涉及居留、工作权限、税务、福利、医疗、合同、金额、期限和联系方式时，必须重新打开官方原始页面核验。

当前插件仍处于本地 MVP 和内部审核阶段，尚未建立公开 marketplace，也没有引入 Jobnet、Jobindex 或 Rejseplanen 的第三方实现。结构、边界和后续计划见 [PLUGIN_DESIGN.md](PLUGIN_DESIGN.md)。

从仓库根目录运行离线结构审计：

```powershell
python plugins/copenhagen-chinese-student-guide/scripts/audit_handbook.py .
```

该脚本只检查来源台账、章节引用和核验日期结构，不能代替人工打开官方网页复核。

## 如何参与检查

发现问题时，优先提交 Issue；准备直接修改时，请新建分支并发起 Pull Request。不要直接修改稳定主分支。

适合提交的内容包括：

- 已失效或跳转错误的官方链接；
- 金额、期限、资格、办理流程等事实变化；
- 对中国籍非欧盟学生不适用或容易造成误解的表述；
- 排版、错别字、目录或交叉引用问题；
- 有官方来源支持的新章节建议；
- 明确标注为个人经验、且不冒充官方结论的实用提醒。

详细流程见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 本地生成 PDF

项目使用 XeLaTeX。Windows 环境已提供构建脚本：

```powershell
.\build.ps1
```

如果 MiKTeX 不在脚本默认位置，可传入安装根目录：

```powershell
.\build.ps1 -TeXRoot 'D:\path\to\miktex'
```

构建应连续运行两遍，以更新目录和交叉引用。生成的临时文件及根目录 `main.pdf` 不进入版本库；正式发布文件放在 `output/pdf/`。

## 内容边界

- 官方事实以主管机关、学校或服务机构的原始页面为准。
- 小红书、B站、Reddit、微信群及个人评论只用于发现问题或补充经验，不能单独证明政策事实。
- 未获授权时，不复制社交平台原文、截图、图片或原创表格；正文应独立撰写。
- 本手册不是法律、移民、医疗、税务或个案咨询。

## 版权与许可

当前版本仅供 CSSA-Copenhagen 内部协作审核，尚非对外正式发布版本。仓库因协作需要在技术上公开可访问，但这不表示内容已经正式对外发布或获得传播授权。**本项目不属于开源项目，也未授予开放内容许可。**

内部审核参与者可以在 GitHub 内查看、Fork 和修改内容，并提交 Issue 或 Pull Request。请勿将 PDF、源文件、截图、仓库或 Release 链接转发至内部审核范围之外；未经书面许可，不得转载、镜像、重新上传、改编、汇编或商业使用本手册内容。

完整声明及转载授权联系方式见 [COPYRIGHT.md](COPYRIGHT.md)。
