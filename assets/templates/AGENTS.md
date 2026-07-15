# AGENTS.md

本文档是 `{{PROJECT_NAME}}` 的 agent 工作入口。完整文档地图见 `docs/README.md`；治理路由见 `docs/foundation/README.md`。

## Start Here

重要工作开始前，最少读取：

- `README.md`
- `docs/README.md`
- `docs/foundation/STATE.md`

是否继续读取 `docs/foundation/PRINCIPLES.md`、`docs/foundation/LOG.md`、ADR、归档索引、review 或其它项目文档，由本轮风险和 `docs/foundation/README.md` 判断。

## Working Rules

- 先对齐目标、边界和完成标准；不确定就问，能可靠确认的先自己确认。
- 只做与本轮目标直接相关的事；不顺手重构、扩写、改名或引入新流程。
- 不静默覆盖已有文件、用户改动或稳定结构；有冲突和高风险时先说明影响与回退方式。
- 完成前做与风险匹配的验证；不能验证时明确说明，不伪造结果。
- 验证失败先当作事实信号；不要为了绿灯而放宽、跳过、删除或改写测试 / 检查 / 验收标准；确需修改标准时按 `docs/foundation/PRINCIPLES.md` 判断和记录依据。
- 记录前先判断信息性质；长期规则、当前状态、历史记录、决策理由和具体交付物分开承载。
- 高风险改动优先用低风险方式让用户验证；不可行时先保留备份或回退点，再改主体。

## Foundation Triggers

当用户说“记住、以后、不要再、为什么又、同步、升级、复盘、决策、归档、ADR、hook、subagent”，或当你发现文档与项目事实不一致、验证失败原因不清、同类问题复现、旧文档污染入口、重要决策可能被遗忘时，先做一次轻量判断：

- 无需记录：继续当前任务。
- 已获授权且位置明确：按 `docs/foundation/README.md` 增量更新对应文件。
- 未获授权、影响不清或需要新增结构：先提出候选和理由，等用户裁决。
