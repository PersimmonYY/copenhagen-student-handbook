# 落地主题路由

本插件以仓库根目录为基准读取手册源文件。只打开解决当前问题所需的章节。

| 用户问题 | 优先读取 | 官方核验重点 |
|---|---|---|
| 录取后到出发前 | `chapters/before_departure.tex` | SIRI、丹麦驻华机构、海关及航空公司 |
| 学习类居留、生物信息、公共福利 | `chapters/visa_permit.tex` | New to Denmark / SIRI |
| 抵丹后前30天 | `chapters/arrival_30_days.tex` | International House Copenhagen、Borger.dk、MitID、Skat.dk |
| 搬家、续签、离境、毕业身份 | `chapters/residence_lifecycle.tex` | SIRI、所在市政府及学校 |
| 银行、NemKonto、Digital Post | `chapters/life_guide.tex` 中财务与数字生活 | Life in Denmark、MitID、Digital Post、银行自身页面 |

## 必须实时核验的字段

- 申请费、自给金额及公共福利限制；
- 居留申请表、办理入口和生物信息要求；
- CPR 登记资格、所需住址和预约方式；
- 黄卡寄送与查询方式；
- 税务、NemKonto、MitID、Digital Post 的当前办理路径；
- 办公地址、电话、开放时间和预计处理时间。

仓库的 `SOURCE_REGISTER.md` 是核验队列，不是永远正确的事实数据库。先找到对应 Claim ID，再打开其官方来源确认正文和适用身份。

## 依赖表达

每个行动项标记为以下一种：

- `现在可做`：不依赖尚未完成事项；
- `可并行`：可与当前主要流程同时推进；
- `等待前置条件`：写明具体等待什么；
- `需要人工确认`：官方页面不足以判断个案。
