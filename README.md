<div align="center">

## Agentic Foundation

为 agent 参与的项目建立轻量文档地图和治理地基。  
默认生成 `AGENTS.md`、根 `README.md`、`docs/README.md` 和 `docs/foundation/`。

<sub>Project Map · Principles · State · Log · Optional Modules</sub>

<br>

<p><kbd>Codex Skill</kbd> <kbd>Version v2.0.1</kbd> <kbd>Language 中文</kbd> <kbd>Mode Foundation</kbd></p>

</div>

```text
Agentic Foundation 用于初始化、检查、增量同步或扩展项目地基。
它不写 PRD、Specs、计划或架构；它负责入口、地图、路由、当前接手快照和重要历史账本。
```

## 它能帮你做什么

- 建立 agent 开工入口和项目文档地图
- 记录长期原则、当前状态和重要历史
- 保护测试、检查、评审和验收标准不被实现反向驯服
- 把 ADR、archive、hooks、subagent workflow 等作为按需追加模块管理
- 检查已有 `.foundation/`、`docs/foundation/` 或旧 `SUGGESTIONS.md` / `CHECKS.md`，在授权后增量同步
- 保留用户内容、项目特有规则和历史记录，不整文件覆盖

## 默认结构

```text
AGENTS.md
README.md
docs/
  README.md
  foundation/
    README.md
    PRINCIPLES.md
    STATE.md
    LOG.md
```

不默认创建 `SUGGESTIONS.md`、`CHECKS.md`、ADR、归档、review、hooks、QA 或 TDD 目录。

## 使用方式

把本目录作为 Codex skill 安装或放入你的 skills 目录中，由 Codex 在项目初始化、同步或追加地基模块时触发。

<sub>未提供开源许可证，默认保留所有权利。</sub>
