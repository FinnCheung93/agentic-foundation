# Foundation README

项目：`{{PROJECT_NAME}}`  
Foundation 版本：`{{FOUNDATION_VERSION}}`  
初始化时间：`{{INIT_TIME}}`  
最近检查更新：待记录

这里是本项目的 AI Coding 治理地基。它不负责写 PRD、不生成 Specs、不制定项目计划；它负责让后续 agent 的工作有原则、有状态、有记录、有检查、有待裁决建议。

## 文件职责

| 文件 | 作用 | 更新时机 |
|---|---|---|
| `AGENTS.md` | agent 工作入口，定义 Mandatory Loop、Hard Rules 和冲突处理 | agent 工作协议变化且用户确认后 |
| `PRINCIPLES.md` | 长期原则、禁区和取舍依据 | 用户确认原则变更后 |
| `STATE.md` | 当前接续快照，回答“现在接手要知道什么” | 每次重要工作结束、跨会话或上下文混乱前 |
| `LOG.md` | 历史账本，记录重要变更、决策、事故、验收和复盘 | 每次重要变更、验收或事故后 |
| `CHECKS.md` | 检查清单，用于执行前、执行中、完成后自检 | 检查规则变化且用户确认后 |
| `SUGGESTIONS.md` | 未裁决治理提案队列，覆盖 `AGENTS.md` 和 `.foundation/` 下任一治理文件 | agent 自发发现治理文件需要演进但尚未获得用户裁决时 |

## 记忆路由表

本文档是唯一记忆路由权威。其它治理文件可以引用或检查本表，不应重新定义路由。

| 信息类型 | 写入位置 |
|---|---|
| 当前进展、当前工作焦点、阻塞、下次接续点 | `STATE.md` |
| 重要变更、决策、事故、复盘、真实 sub-agent 验收结果 | `LOG.md` |
| 未裁决的治理文件改进建议 | `SUGGESTIONS.md` |
| 验证规则变化 | 先写 `SUGGESTIONS.md`，用户确认后再改 `CHECKS.md` |
| 项目长期原则或禁区 | 先写 `SUGGESTIONS.md`，用户确认后再改 `PRINCIPLES.md` |

不确定该写到哪里时，先说明判断并请用户裁决。不要把所有信息都塞进同一个文件。

## 读取规则

- 每轮开工前读：`AGENTS.md`、本文件、`PRINCIPLES.md`、`STATE.md`。
- 重大改动前读：`CHECKS.md`。
- 发生变更、事故、迭代或复盘后，按记忆路由表判断是否记录。

## 当前项目简述

{{PROJECT_PURPOSE}}
