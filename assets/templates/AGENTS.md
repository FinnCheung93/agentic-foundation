# AGENTS.md

本文档是 `{{PROJECT_NAME}}` 的 agent 工作入口。它只定义开工前必须遵守的入口协议、Mandatory Loop 和 Hard Rules；详细文件职责、记录路由和检查清单以 `.foundation/` 为准。

## Mandatory Loop

每轮重要工作按顺序执行：

1. **Load Foundation**：读取本文件、`.foundation/README.md`、`.foundation/PRINCIPLES.md`、`.foundation/STATE.md`；重大改动前读取 `.foundation/CHECKS.md`。
2. **Align Before Action**：明确本轮目标、边界、影响范围和验收方式；信息不足时先问最小澄清问题。
3. **Plan With Boundary**：说明会触碰哪些文件或模块、依赖哪些文件或模块、不触碰哪些文件或模块。
4. **Execute With Validation**：优先用脚本、临时目录、最小样例、局部路径或静态检查验证；不可旁路时说明风险。
5. **Verify And Repair**：自检、修复、再验证，直到达到本轮验收标准或明确阻塞。
6. **Record By Route**：按 `.foundation/README.md` 的记忆路由更新 `STATE.md`、`LOG.md` 或 `SUGGESTIONS.md`。
7. **Foundation Suggestion Scan**：重要工作结束前，主动检查治理文件是否暴露出需要演进的建议；未裁决建议写入 `.foundation/SUGGESTIONS.md`。

## Hard Rules

- 不静默覆盖已有文件。发现冲突、旧结构或同名文件时，先说明影响并请求用户裁决。
- 不擅自修改 `.foundation/PRINCIPLES.md`。未裁决的原则演进先进入 `.foundation/SUGGESTIONS.md`。
- 不把 PRD、Specs、项目计划、测试矩阵或实现任务写入治理地基；这些内容应由对应流程或 skill 处理。
- `STATE.md` 只写当前接续信息，不写历史流水；完整历史写入 `LOG.md`。
- 如果用户要求使用真实 sub-agent 验收，而当前环境不可用，必须说明不可用，不能假装完成。
