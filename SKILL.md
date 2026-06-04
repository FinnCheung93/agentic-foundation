---
name: aicoding-foundation
description: >-
  Initialize a lightweight governance foundation for new AI Coding projects before PRD writing,
  Spec generation, or implementation begins. Use when the user has created or chosen a fresh project
  folder and wants AGENTS.md plus a .foundation/ governance cockpit with project principles, state,
  log, checks, and human-reviewed suggestions. Also use for Chinese requests like 项目初始化,
  打地基, 治理舱, agent 工作灯塔, or 开工前结构. Do not use for PRD writing, SDD Specs generation,
  project planning, task breakdown, engineering architecture, or direct implementation. If the user
  is only discussing whether a governance foundation is useful, analyze only and do not write files.
metadata:
  short-description: Initialize AI Coding project governance
  version: v1.1.2
  updated: 2026-06-04
---

# AI Coding Foundation

这个 skill 用于在新 AI Coding 项目开工前初始化一套轻量治理地基：根目录 `AGENTS.md` + `.foundation/`。它让后续 agent 工作有入口协议、长期原则、当前状态、历史日志、检查清单和未裁决治理提案。

## 适用场景

适用：

- 用户刚创建或选定一个新项目目录，希望初始化 AI Coding 工作地基。
- 用户说“项目初始化 / 打地基 / 初始化项目地基 / 治理舱 / agent 工作灯塔 / agent 工作规则 / 开工前结构 / AI Coding foundation”。
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

不要新增其它治理文件，除非用户明确要求扩展。

## 生成物职责契约

这 7 个生成物必须各自只承担一个主职责：

| 文件 | 主职责 |
|---|---|
| `AGENTS.md` | agent 工作入口，只写 Mandatory Loop、Hard Rules 和冲突处理 |
| `.foundation/README.md` | 治理文件索引与记忆路由权威 |
| `.foundation/PRINCIPLES.md` | 长期原则、禁区和取舍依据 |
| `.foundation/STATE.md` | 当前接续快照，只回答“现在接手要知道什么” |
| `.foundation/LOG.md` | 历史账本，记录重要变更、决策、事故、验收和复盘 |
| `.foundation/CHECKS.md` | 检查清单，只检查是否按既定规则执行 |
| `.foundation/SUGGESTIONS.md` | 未裁决治理提案队列 |

硬边界：

- `README.md` 是唯一记忆路由。
- `STATE.md` 只写当前接续，不写历史流水。
- `LOG.md` 承载完整历史。
- `AGENTS.md` 不展开检查表。
- `CHECKS.md` 不重新定义路由。
- `PRINCIPLES.md` 不写状态、日志或检查步骤。

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
- `AGENTS.md` 只包含入口协议、Mandatory Loop、Hard Rules 和冲突处理，不展开详细检查表。
- `.foundation/README.md` 包含文件职责和唯一记忆路由表。
- `.foundation/PRINCIPLES.md` 只包含长期原则、禁区和取舍依据，不写状态/日志更新步骤。
- `.foundation/STATE.md` 使用“最近接续点”，最多保留 3-5 条恢复需要的信息，不使用完成流水栏目承载历史。
- `.foundation/LOG.md` 承载完整历史记录。
- `.foundation/CHECKS.md` 只做检查表，不重新定义文件职责或记忆路由。
- `.foundation/SUGGESTIONS.md` 是未裁决治理提案队列。
- `STATE.md`、`LOG.md`、`SUGGESTIONS.md` 的时间统一使用“日期 + 分钟 + 时区”，例如 `2026-06-02 14:35 CST`，不要求秒级。

如果检查发现职责重复，先修订模板，再重新用临时目录 dry run。

### 7. 完成回复

初始化完成后，只用自然语言告诉用户项目目录初始化完成，并列出生成的入口文件。不要顺手生成下一步项目计划。

## 旧项目更新检查

当用户说“同步 / 升级 / 有更新 / 检查 foundation 版本 / 更新治理地基”时：

1. 先读取目标项目 `.foundation/README.md` 的 Foundation 版本和最近检查更新时间。
2. 对照本 skill 的 `metadata.version`、当前模板和生成物职责契约，判断可能缺少哪些治理能力。
3. 只提出升级建议，或建议写入目标项目 `.foundation/SUGGESTIONS.md`。
4. 不自动覆盖目标项目的 `AGENTS.md`、`.foundation/PRINCIPLES.md`、`.foundation/STATE.md`、`.foundation/LOG.md`、`.foundation/CHECKS.md` 或 `.foundation/SUGGESTIONS.md`。
5. 若用户明确要求执行升级，只做增量修订，保留项目特有状态、背景和历史日志。

旧项目升级时，重点检查职责是否重复：

- `STATE.md` 是否正在充当历史日志。
- `README.md` 是否变成第二份 `AGENTS.md`。
- `AGENTS.md` 是否重复展开 `CHECKS.md`。
- `PRINCIPLES.md` 是否混入执行步骤。
- `CHECKS.md` 是否重新定义了文件职责。

## 治理演进规则

`PRINCIPLES.md` 是项目判断依据，不是 AI 可自由改写的笔记。`SUGGESTIONS.md` 不是普通建议箱，而是未裁决治理提案队列。

- AI 自发发现但尚未被用户裁决的治理变更，应进入 `SUGGESTIONS.md`。
- 用户当场明确裁决的治理修改，可以直接执行并记录到 `LOG.md`，不必先进入 `SUGGESTIONS.md`。
- 用户确认后，AI 才能把建议写入 `PRINCIPLES.md` 或其它正式文件。
- 为了当前任务省事、绕过检查、通过一次执行，不得修改原则。
- 变更、事故、迭代、周期性复盘后，应主动考虑是否需要提出治理演进建议。

## 完成检查

结束前确认：

- `AGENTS.md` 已指向 `.foundation/README.md`、`PRINCIPLES.md`、`STATE.md`。
- `.foundation/` 中 6 个文件均已生成。
- 7 个生成物符合职责契约，未出现明显重复承载。
- `PRINCIPLES.md` 明确“AI 只能提案，用户确认后修改”。
- `STATE.md` 没有生成详细项目计划或历史流水。
- `SUGGESTIONS.md` 是待裁决治理提案队列。
- 若存在冲突，未覆盖任何已有文件。
