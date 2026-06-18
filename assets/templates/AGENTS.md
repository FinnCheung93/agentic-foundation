# AGENTS.md

本文档是 `{{PROJECT_NAME}}` 的 agent 工作入口。它只保留最低启动动作、关键触发和硬底线；文件职责、信息路由和扩展文档登记以 `.foundation/README.md` 为准。

## Minimum Start

重要工作开始前，先读取：

- 本文件
- `.foundation/README.md`
- `.foundation/STATE.md`

是否需要读取 `.foundation/PRINCIPLES.md`、`.foundation/LOG.md` 或 `.foundation/SUGGESTIONS.md`，按 `.foundation/README.md` 的信息性质和缺失风险判断。

## Governance Triggers

- **Before Work**：先明确本轮目标、边界、影响范围和可验证完成标准；不确定就问，别猜。
- **Before Mutation**：触碰主交付物、稳定结构、发布路径、已有用户改动或同名文件前，先判断风险、冲突和回退方式。
- **After Work**：收尾前判断是否需要更新当前状态、记录重要历史、提出未裁决治理提案或推进治理复盘触发计数。

用户指出错误、遗漏、误解、重复问题或规则冲突时，先修复当前问题，再按 `.foundation/README.md` 判断是否需要记录或提出治理改进。

## Hard Rules

- 不静默覆盖已有文件。发现冲突、旧结构或同名文件时，先说明影响并请求用户裁决。
- 没要求的不写；只做与本轮目标直接相关的增量修改，不顺手重构或扩展。
- 没有明确收益时，不强行改写、吸收或提出建议；可以说明已检查，无需处理。
- 高风险改动先用低风险方式验证；不可行时保留备份或回退点，再请求用户许可。
- 记录前先按 `.foundation/README.md` 判断信息性质；不要把长期原则、当前状态、历史事件和未裁决提案混写。
- 未裁决的治理建议不进入正式治理文件；影响不清时进入 `.foundation/SUGGESTIONS.md` 或请求用户裁决。
- 不把 PRD、Specs、项目计划、测试矩阵或实现任务写入治理地基；这些内容应由对应流程或项目文档承接。
- `STATE.md` 只放当前接续快照，通过修订保持当下状态；不要写成历史流水。
- 不能伪造能力或证据。工具、权限或环境不可用时，说明不可用；只报告真实完成的检查和验收。
