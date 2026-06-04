# Checks

本文档是重要工作前后的检查表。它只负责检查，不重新定义文件职责或记忆路由；文件职责和路由以 `.foundation/README.md` 为准。

## 执行前检查

- 已读取 `AGENTS.md`、`.foundation/README.md`、`.foundation/PRINCIPLES.md`、`.foundation/STATE.md`。
- 已确认本轮任务类型：治理 / PRD / Specs / 实现 / 其它。
- 已明确本轮目标、边界、影响范围和验收方式。
- 已说明会触碰哪些文件或模块、依赖哪些文件或模块、不触碰哪些文件或模块。
- 已确认是否存在冲突文件、旧结构或用户未裁决事项。

## 执行中验证

- 优先使用脚本、临时目录、最小样例、预览或局部路径验证。
- 不能旁路验证时，说明原因和风险。
- 发现模块边界不清时，先暂停并请求裁决。
- 不为了验证方便扩大改动范围。

## 执行后检查

- 已运行可用检查、预览或最小验证。
- 已根据验证结果修复问题并再次验证。
- 已确认 `STATE.md` 只记录当前接续信息，没有写成历史流水。
- 已确认重要变更、决策、事故、验收或复盘记录在 `LOG.md`。
- 已确认未裁决治理建议进入 `SUGGESTIONS.md`。
- 已确认记录位置符合 `.foundation/README.md` 的唯一记忆路由。

## 生成物职责去重检查

- `AGENTS.md` 只包含入口协议、Mandatory Loop 和 Hard Rules。
- `.foundation/README.md` 是唯一文件职责与记忆路由权威。
- `.foundation/PRINCIPLES.md` 只包含长期原则、禁区和取舍依据。
- `.foundation/STATE.md` 只保留 3-5 条最近接续点，不记录完整历史。
- `.foundation/LOG.md` 承载完整历史账本。
- `.foundation/CHECKS.md` 只做检查表，不重新定义路由。
- `.foundation/SUGGESTIONS.md` 只记录未裁决治理提案。
