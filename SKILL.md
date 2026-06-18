---
name: agentic-foundation
description: >-
  Initialize a lightweight governance foundation for agentic projects, or review and incrementally
  sync an existing foundation to the current governance capability. Use when the user has chosen a
  project folder and wants AGENTS.md plus a .foundation/ governance cockpit with project principles,
  state, log, checks, and human-reviewed suggestions. Also use for Chinese requests like 项目初始化,
  打地基, 治理舱, agent 工作灯塔, 开工前结构, agentic foundation, 检查 foundation 版本, 同步治理地基, or 升级 foundation.
  Do not use for PRD writing, SDD Specs generation, project planning, task breakdown, engineering
  architecture, or direct implementation. If the user is only discussing whether a governance
  foundation is useful, analyze only and do not write files.
metadata:
  short-description: Initialize agentic project governance
  version: v1.7.0
  updated: 2026-06-18
---

# Agentic Foundation

这个 skill 用于在 agent 参与的项目开工前初始化一套轻量治理地基：根目录 `AGENTS.md` + `.foundation/`。它让后续 agent 工作有入口协议、长期原则、当前状态、历史日志、检查清单和未裁决治理提案。

## 适用场景

适用：

- 用户刚创建或选定一个新项目目录，希望初始化 agent 协作工作地基。
- 用户说“项目初始化 / 打地基 / 初始化项目地基 / 治理舱 / agent 工作灯塔 / agent 工作规则 / 开工前结构 / Agentic Foundation”。
- 用户需要一个跨会话续航和自进化机制，而不是只依赖当前对话上下文。

不适用：

- 写 PRD、修改 PRD、评审 PRD：交给 `pm-prd-copilot`。
- 生成或重组 Specs：交给 `aicoding-specpilot`。
- 项目计划、任务拆解、里程碑规划、工程架构设计、API 设计、测试矩阵、安全评审。
- 用户只是在讨论是否需要治理结构；此时只分析，不写文件。

## 输出结构

默认在目标项目根目录生成：

```text
AGENTS.md
.foundation/
  README.md
  PRINCIPLES.md
  STATE.md
  LOG.md
  CHECKS.md
  SUGGESTIONS.md
```

不要新增其它默认治理文件或目录，除非用户明确要求扩展。不要默认创建 handoff、learning records、out-of-scope、notes 等接续或记忆目录。

## 生成物职责契约

这 7 个生成物必须各自只承担一个主职责：

| 文件 | 主职责 |
|---|---|
| `AGENTS.md` | agent 工作入口，只写 Mandatory Loop、Governance Hooks、Hard Rules 和冲突处理 |
| `.foundation/README.md` | 治理文件索引与信息性质路由权威 |
| `.foundation/PRINCIPLES.md` | 长期原则、禁区和取舍依据 |
| `.foundation/STATE.md` | 当前接续快照，只回答“现在接手要知道什么” |
| `.foundation/LOG.md` | 历史账本，记录重要变更、决策、事故、验收和复盘 |
| `.foundation/CHECKS.md` | 检查清单，只检查是否按既定规则执行 |
| `.foundation/SUGGESTIONS.md` | 未裁决治理提案队列 |

硬边界：

- `README.md` 是唯一记忆路由，按信息性质引导 agent 判断写入位置。
- `STATE.md` 只写当前接手快照，不写历史流水，也不复制已有 artifact 全文。
- `LOG.md` 承载已发生的重要事件。
- `AGENTS.md` 不展开检查表，只保留工作循环、治理触发点和硬规则。
- `CHECKS.md` 不重新定义路由。
- `PRINCIPLES.md` 不写状态、日志或检查步骤。
- 扩展文档只登记职责、依赖性质和读取时机；foundation 不接管 PRD、Specs、任务拆分、架构设计或其它专业流程。

## 工作流

### 1. Intake Gate

开始前确认：

- 目标项目目录是否明确。
- 用户是否是在请求初始化治理地基，而不是 PRD、Specs 或项目计划。
- 目标目录是否已经存在 `AGENTS.md`、`.foundation/` 或目标同名文件。

如果用户没有给出目标目录，但当前工作目录明显就是目标项目，可以使用当前目录并说明。若当前目录不是用户项目或存在多个候选目录，先询问。

### 2. Write Authorization Gate

只有用户明确要求“初始化 / 创建 / 生成 / 应用 / 打地基 / 建治理舱”时，才写入文件。

如果用户只是问“怎么看 / 有没有必要 / 应该怎么设计 / 能不能优化”，只输出分析、建议或计划，不运行脚本、不创建文件。

### 3. 冲突检查

初始化前必须检查：

- 根目录是否已有 `AGENTS.md`。
- 根目录是否已有 `.foundation/`。
- `.foundation/` 下是否已有计划生成的同名文件。

只要存在冲突，就停止自动写入，并请用户决策：保留、备份后替换、手动合并，或改用其它目录。不要静默覆盖、合并或删除已有内容。

### 4. 最小访谈

无冲突后，先收集最少动态信息。只问会影响治理地基内容的问题，不做项目规划。

最低信息：

- 项目要做什么：一句话即可。
- 主要风险：用户最担心 agent 乱动、误解或破坏的点。
- 工作偏好：用户希望 agent 如何先思考、汇报、确认和记录。

如果用户已经给出这些信息，可以直接使用，不要重复提问。信息不足但用户要求“按默认来”，可用保守默认值生成，并在 `STATE.md` 标注待补充。

### 5. 生成骨架

使用脚本生成固定骨架：

```text
python scripts/init_foundation.py <target_dir> --project-name <name> --language zh
```

可选参数：

```text
--purpose "<项目要做什么>"
--risks "<主要风险>"
--preferences "<工作偏好>"
```

脚本只负责创建固定结构和写入模板，不生成 PRD、Specs、项目计划或任务拆解。

目标目录默认必须已经存在。只有用户明确要求同时创建目标目录时，才传入 `--create-target`。

### 6. 验证生成物

生成后检查：

- 脚本仍只生成 `AGENTS.md` + `.foundation/` 下 6 个文件。
- `AGENTS.md` 只包含入口协议、Mandatory Loop、Governance Hooks、Hard Rules 和冲突处理，不展开详细检查表。
- `.foundation/README.md` 包含文件职责和唯一记忆路由表，路由按信息性质表达，不写成机械 if-else。
- `.foundation/README.md` 包含扩展文档登记、硬依赖 / 软依赖判断，并说明共享语言文档只做术语，不承载 spec、实现细节或计划。
- `.foundation/PRINCIPLES.md` 只包含长期原则、禁区和取舍依据，不写状态/日志更新步骤。
- `.foundation/PRINCIPLES.md` 包含长期文档抗过期、临时验证产物不自动成为长期结构、foundation 不接管专业流程。
- `.foundation/STATE.md` 使用“最近接续点”，最多保留 3-5 条恢复需要的信息。
- `.foundation/STATE.md` 包含当前目标、当前状态、下一步建议、关键约束、验收方式和范围外事项；引用已有 artifact，不复制全文。
- `.foundation/STATE.md` 包含“治理脉冲”，以 3 个合格治理信号为阈值触发治理复盘；`STATE.md` 通过修订保持当前接手快照，不追加成历史流水。
- `.foundation/LOG.md` 记录已发生的重要事件、决策、变更、事故、验收和复盘。
- `.foundation/LOG.md` 支持记录“不做 / 拒绝 / 暂不支持”的裁决、原因和取舍，避免未来重复重开。
- `.foundation/CHECKS.md` 只做检查表，不重新定义文件职责或记忆路由。
- `.foundation/CHECKS.md` 包含治理钩子检查、长期原则误投扫描、自进化运行检查和发布一致性检查。
- `.foundation/CHECKS.md` 包含反馈环优先、临时验证产物归宿、重要决策沉淀判断和长期文档抗过期检查。
- `.foundation/CHECKS.md` 包含接手快照更新、引用优先、复制膨胀检查、范围边界检查和不做事项复现检查。
- `.foundation/SUGGESTIONS.md` 是未裁决治理提案队列，不吞掉已裁决且应生效的正式规则。
- `.foundation/SUGGESTIONS.md` 支持已替代状态，旧提案或旧理解被新裁决取代时保留历史但标记替代。
- `LOG.md` 和 `SUGGESTIONS.md` 没有被改造成 ADR 文件；不得默认创建 `docs/adr/` 或其它扩展目录。
- 不默认创建 `MISSION.md`、`learning-records/`、`NOTES.md`、`.out-of-scope/` 或 handoff 文档。
- `STATE.md`、`LOG.md`、`SUGGESTIONS.md` 的时间统一使用“日期 + 分钟 + 时区”，例如 `2026-06-02 14:35 CST`，不要求秒级。

如果检查发现职责重复，先修订模板，再重新用临时目录 dry run。

### 7. 完成回复

初始化完成后，只用自然语言告诉用户项目目录初始化完成，并列出生成的入口文件。不要顺手生成下一步项目计划。

## 旧项目更新检查

当用户说“同步 / 升级 / 有更新 / 检查 foundation 版本 / 更新治理地基”时：

1. 先读取目标项目 `.foundation/README.md` 的 Foundation 版本和最近检查更新时间。
2. 对照本 skill 的 `metadata.version`、当前模板和生成物职责契约，判断可能缺少哪些治理能力。
3. 做一次升级覆盖完整性审计：逐一判断 7 个生成物如何增量对齐当前版本能力；每个生成物都要留下处置结论和依据。
4. 只提出升级建议，或建议写入目标项目 `.foundation/SUGGESTIONS.md`。
5. 不重新初始化，不整文件覆盖，不删除初始化后用户新增的内容、手写规则、历史日志、状态或提案。
6. 若用户明确要求执行升级，只做增量修订，把新版能力补入相关生成物，同时保留项目特有状态、背景和历史日志。
7. 若某个生成物没有可适用的新能力，也要留下“已检查、无需变更”的依据。
8. 只有当 7 个生成物均已完成增量对齐，或有明确保留依据，才能把目标项目标记为已同步到新版本。

升级审计建议使用轻量矩阵，避免只说“已检查”：

| 生成物 | 当前观察 | 版本差异 / 能力缺口 | 增量动作 | 保留内容 | 依据 | 是否需用户裁决 |
|---|---|---|---|---|---|---|
| `AGENTS.md` |  |  | 更新 / 保留 / 建议 |  |  | 是 / 否 |
| `.foundation/README.md` |  |  | 更新 / 保留 / 建议 |  |  | 是 / 否 |
| `.foundation/PRINCIPLES.md` |  |  | 更新 / 保留 / 建议 |  |  | 是 / 否 |
| `.foundation/STATE.md` |  |  | 更新 / 保留 / 建议 |  |  | 是 / 否 |
| `.foundation/LOG.md` |  |  | 更新 / 保留 / 建议 |  |  | 是 / 否 |
| `.foundation/CHECKS.md` |  |  | 更新 / 保留 / 建议 |  |  | 是 / 否 |
| `.foundation/SUGGESTIONS.md` |  |  | 更新 / 保留 / 建议 |  |  | 是 / 否 |

版本标记规则：

- 审计完成不等于已同步。
- 部分文件更新不等于已同步。
- 只有 7 个生成物均已增量处理，或有清楚的保留依据，且 `LOG.md` 记录了本次同步，才能更新目标项目 `.foundation/README.md` 的 Foundation 版本和最近检查时间。
- 如果只是检查并提出建议，不更新目标项目 Foundation 版本。

旧项目升级时，重点检查职责是否重复：

- 根目录入口文件是否仍能触发当前版本的工作循环和记录判断。
- `STATE.md` 是否正在充当历史日志。
- `README.md` 是否变成第二份 `AGENTS.md`。
- `AGENTS.md` 是否重复展开 `CHECKS.md`。
- `PRINCIPLES.md` 是否混入执行步骤。
- `CHECKS.md` 是否重新定义了文件职责。
- `SUGGESTIONS.md` 是否仍能承接未裁决治理提案。
- 是否保留了用户初始化后新增的额外内容和项目特有规则。

## 治理演进规则

`PRINCIPLES.md` 是项目判断依据，不是 AI 可自由改写的笔记。`SUGGESTIONS.md` 不是普通建议箱，而是未裁决治理提案队列。

- AI 自发发现但尚未被用户裁决的治理变更，应进入 `SUGGESTIONS.md`。
- 具备长期约束意义且裁决清晰的信息，可以进入对应正式治理文件，并记录到 `LOG.md`。
- 未裁决、影响不清或只是 AI 自发发现的建议，先进入 `SUGGESTIONS.md` 或请求用户裁决。
- 为了当前任务省事、绕过检查、通过一次执行，不得修改原则。
- 变更、事故、迭代、周期性复盘后，应主动考虑是否需要提出治理演进建议。

## 完成检查

结束前确认：

- `AGENTS.md` 已指向 `.foundation/README.md`、`PRINCIPLES.md`、`STATE.md`。
- `.foundation/` 中 6 个文件均已生成。
- 7 个生成物符合职责契约，按信息性质路由，未出现明显重复承载。
- `PRINCIPLES.md` 区分裁决清晰的长期约束和未裁决治理建议。
- `STATE.md` 没有生成详细项目计划或历史流水。
- `STATE.md` 是当前接手快照，包含下一步、约束、验收和范围外事项；最近接续点保持 3-5 条当前恢复信息。
- `SUGGESTIONS.md` 是待裁决治理提案队列。
- 扩展文档、共享语言和重要决策判断被吸收到现有治理体系中，未新增默认目录。
- 接续和机构记忆规则被吸收到现有治理体系中，未新增 handoff、learning records、out-of-scope 或 notes 目录。
- 若存在冲突，未覆盖任何已有文件。
