# Foundation

项目：`{{PROJECT_NAME}}`  
Foundation 版本：`{{FOUNDATION_VERSION}}`  
初始化时间：`{{INIT_TIME}}`  
最近检查更新：待记录

本文档是治理路由权威。它说明信息应放在哪里、什么时候读取、什么时候需要用户裁决。项目总地图见 `docs/README.md`。

## Core Files

| File | Responsibility | Update when |
|---|---|---|
| `AGENTS.md` | 短入口、硬底线和关键触发 | 入口协议或硬规则变化 |
| `README.md` | 项目门牌和文档地图入口 | 项目简介或文档入口变化 |
| `docs/README.md` | 项目地图和已启用模块索引 | 文档入口、模块、归档索引变化 |
| `docs/foundation/PRINCIPLES.md` | 当前长期原则、禁区、稳定偏好 | 已裁决且具备长期约束意义 |
| `docs/foundation/STATE.md` | 当前接手快照 | 当前目标、状态、阻塞或下一步变化 |
| `docs/foundation/LOG.md` | 重要历史账本和 artifact 引用 | 发生重要事件、裁决、升级、归档、事故、复盘 |

## Routing

| Information type | Prefer |
|---|---|
| 入口、最小读取、硬底线 | `AGENTS.md` |
| 项目是什么、文档地图在哪里 | `README.md` |
| 活跃入口、扩展模块、归档索引 | `docs/README.md` |
| 长期规则、禁区、稳定偏好、取舍依据 | `PRINCIPLES.md` |
| 当前目标、状态、范围、阻塞、下一步 | `STATE.md` |
| 已发生的重要事件、用户裁决、事故、验收、复盘、迁移 | `LOG.md` |
| 测试、检查、评审或验收标准变更的原因和依据 | `LOG.md`；若形成长期约束，同步到 `PRINCIPLES.md` |
| 决策理由且未来会疑惑 | ADR / decision record，未启用时先向用户建议 |
| 旧文档状态、替代关系、读取时机 | archive index，未启用时先向用户建议 |
| 未决问题需要跨轮追踪 | Open Questions artifact，未启用时先向用户建议 |

记录前先判断信息性质和已有 artifact。PRD、Specs、issue、review、handoff、外部文档已能承载细节时，foundation 只记录路径、状态、规则、决策摘要或读取时机。

## Read Policy

- 最小读取：`AGENTS.md`、`README.md`、`docs/README.md`、`STATE.md`。
- 缺少长期规则会影响判断时，读取 `PRINCIPLES.md`。
- 需要历史依据、已裁决方向、事故、验收或迁移记录时，读取 `LOG.md` 的相关片段。
- ADR、archive、review、open questions、coding guidance、hooks 等只在已启用且与本轮相关时读取。
- 读不到软依赖时继续工作并说明缺口；读不到会导致误判、越权、覆盖或无法验证的硬依赖时，先对齐。

## Self-Evolution

agent 应在以下情况做轻量治理判断：

- 用户要求记住、同步、升级、复盘、归档、ADR、hook、subagent 或不要重复某事。
- 修改稳定入口、文档地图、foundation 文件、模板、脚本、迁移路径或归档区前。
- 发现重复问题、事实漂移、过期路径、缺少依据、范围扩大、验证失败原因不清、无法验证或同类错误复现。
- 完成重要工作、迁移、归档、同步、subagent 审阅或模块追加后。
- 长任务接续、上下文压缩、切换 agent、阶段开始或阶段收尾时。

多数触发只需内部判断。只有需要写入、请求裁决、发现高风险或解释不行动时，才显式呈现。自进化不扩大写入授权；新增文件、迁移、结构变化和正式规则写入仍需用户确认。

## Add-on Modules

可追加模块不默认创建。agent 可以主动建议，但创建或登记前必须说明解决什么问题、创建或引用什么、何时读取、何时停用或复查，并等待用户确认。

| Module | Default path after confirmation |
|---|---|
| ADR | `docs/adr/README.md` and the first ADR |
| Archive | `docs/archive/README.md` |
| Open Questions | `docs/foundation/OPEN_QUESTIONS.md` |
| Subagent review | `docs/reviews/YYYY-MM-DD-topic.md` when traceability is needed |
| Hooks | project hook config plus rollback notes |
| Coding Guidance | `docs/foundation/CODING_GUIDANCE.md` |

不创建空目录、空 README、固定角色库或未启用流程文件。
