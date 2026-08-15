# Derive Math Animations

一个用于数学与逻辑学动画逆向分析、内容发散和分镜设计的 Codex Skill。

本项目不是 3Blue1Brown 或 3b1b 的官方项目，也不包含 `3b1b/videos` 的源代码、视频或场景文件。它借鉴公开项目中的解释机制研究，重新组织为可复用的分析流程。

## 能做什么

- 分析 Manim 源代码、动画场景、分镜、讲稿或视频。
- 提取动画中的语义、状态、转场和叙事机制。
- 从一个数学解释发散出新的数学、逻辑学、物理和量子物理动画选题。
- 生成候选选题、评分、分镜和实现路线。
- 区分静态分析、实际渲染验证和未经验证的假设。
- 在涉及第三方素材时记录来源和许可证边界。

## 文件结构

```text
SKILL.md                         Skill 主指令
agents/openai.yaml              Codex 界面元数据
references/pattern-library.md   可复用的动画机制
references/ideation-matrix.md   发散维度与选题矩阵
references/quality-rubric.md    质量检查与评分标准
scripts/analyze_manim_repo.py   只读的 Manim Python AST 分析器
THIRD_PARTY_NOTICES.md          第三方来源说明
```

## 使用方式

将整个目录放入 Codex 的 skills 目录，然后在任务中使用：

```text
使用 $derive-math-animations 分析这个数学动画，并发散出三个新的动画方案。
```

也可以直接提出类似请求：

```text
逆向分析一个 Manim 仓库，提取它的证明动画机制，再生成关于极限的原创分镜。
```

## 环境说明

这个 Skill 的分析器不需要导入目标项目，默认进行静态 AST 分析。Manim、ManimGL、FFmpeg 和 LaTeX 不随本仓库提供；只有在实际渲染动画时才需要单独安装和配置它们。

## 来源与许可证

本仓库的原创内容采用 MIT License。与 `3b1b/videos` 的关系和第三方许可说明见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。本项目不代表 3b1b，也不暗示获得其背书。

