---
name: derive-math-animations
description: Reverse-engineer mathematical or logic animations from Manim source repositories, scene files, storyboards, transcripts, or videos; extract reusable visual and narrative mechanisms; then generate original, rigorous math or logic topics, ranked concepts, storyboards, and implementation routes. Use when asked to 拆解、逆向、借鉴、发散、改编 or design educational math/logic animations. Do not route binary or security reverse engineering here.
---

# Derive Math Animations

## Overview

Turn an existing mathematical explanation into a reusable animation grammar, then derive new content from the grammar instead of copying the original surface style. Keep every mathematical claim traceable to evidence or mark it as a hypothesis.

## Core rules

1. Reverse the explanatory mechanism, not the creator's visual identity.
2. Preserve mathematical meaning across every visual transformation.
3. Prefer direct source evidence over impressions about style.
4. Distinguish source-validated findings, runtime-validated findings, and unverified hypotheses.
5. Use animation only when state change, continuity, scale, dependency, or failure matters.
6. Respect source licenses and identify when adaptation or attribution constraints apply.
7. Do not install render dependencies or execute untrusted project code unless the user asks and the scope permits it.

## Route the input

Choose the smallest applicable route:

| Input | First action |
|---|---|
| Manim repository | Snapshot it, run the static analyzer, then sample representative scenes |
| One or more scene files | Read imports, bases, `construct`, helper methods, and key transforms |
| Video plus transcript | Build a timestamped table of claim, visible state, transition, and narration |
| Storyboard or script | Map each beat to its mathematical job and state change |
| Topic only | Skip source reverse-engineering and start from the pattern library and divergence matrix |

If the input is a repository, use `scripts/analyze_manim_repo.py` before broad manual reading:

```powershell
python scripts/analyze_manim_repo.py C:\path\to\repo
```

The analyzer parses Python without importing the target project. Record parse failures instead of silently dropping them.

## Workflow

### 1. Freeze scope

Record the input path or URL, Git commit when available, relevant license, files inspected, and whether runtime rendering is in scope. Do not claim compatibility from static inspection alone.

### 2. Map the corpus

For repositories, identify:

- project/year/topic boundaries;
- scene count and dominant scene bases;
- shared domain abstractions;
- common animation operations;
- environment-specific configuration and version coupling;
- parse errors or inaccessible material.

Avoid reading every file sequentially. Use corpus statistics to choose samples.

### 3. Select contrasting samples

Choose at least three samples that expose different mechanisms. Prefer this spread:

1. a constructive proof or direct derivation;
2. a counterexample, paradox, or failure case;
3. a parameter sweep, simulation, or algorithm-driven scene;
4. a representation change, when available.

Explain why each sample is representative. Do not infer a corpus-wide rule from one attractive scene.

### 4. Extract four layers

For every sample, fill this map:

| Layer | Question |
|---|---|
| Semantic | What mathematical object or claim does each visible object represent? |
| State | What can change, and what must remain invariant? |
| Transition | Which operation carries the proof from one state to the next? |
| Narrative | What question, prediction, objection, reveal, or conclusion motivates the transition? |

Read `references/pattern-library.md` before naming the reusable patterns.

### 5. Ground findings

Attach evidence to every important finding:

- source location, class, function, or timestamp;
- corpus count or second independent example;
- runtime observation, if rendering was actually performed.

Use these labels:

- `validated-static`: supported by two independent static observations;
- `validated-runtime`: directly observed during render or playback;
- `candidate`: plausible but supported by only one source;
- `boundary`: unavailable or outside the current scope.

Never upgrade a runtime claim from source code alone.

### 6. Build the explanatory grammar

Summarize reusable mechanisms as verbs, not aesthetics. Examples:

- rearrange while preserving area;
- vary a parameter while tracking an invariant;
- hold the experiment fixed and change one definition;
- move an object between geometric, combinatorial, and symbolic representations;
- stage a plausible proof and expose its first illegal step;
- let a counterexample act as an adversarial move;
- externalize a likely objection through a character or prompt.

### 7. Diverge systematically

Generate candidates across at least four axes from `references/ideation-matrix.md`:

- theorem or claim;
- representation;
- hidden assumption;
- scale or dimension;
- parameter;
- failure mode or counterexample;
- application context.

Unless the user requests another number, produce 12 distinct seeds. Reject mere skin swaps and near-copies.

### 8. Rank before expanding

Read `references/quality-rubric.md`. Apply the hard gates, score surviving ideas, rank the top three, and state one risk for each. Do not use a high total score to hide a mathematical flaw.

### 9. Storyboard the winner

Create one 6–10 beat storyboard. Each beat must contain:

1. the mathematical job;
2. the visible state before and after;
3. the transition;
4. the narration or viewer question;
5. the invariant, measurement, or dependency being tracked.

Finish with a proof check and an implementation route: reuse an existing abstraction, adapt a generic pattern, or build a new domain primitive.

### 10. Verify the handoff

Before reporting completion:

- check symbols, quantifiers, domains, assumptions, and edge cases;
- ensure colors and object identities keep one meaning;
- ensure every camera move carries information;
- distinguish inspiration from adaptation;
- state whether code was parsed, imported, rendered, or only read;
- state blockers plainly.

## Default output

When the user gives a broad request, return:

1. scope and confidence boundary;
2. corpus or artifact map;
3. evidence-backed pattern library;
4. 12 original math/logic animation seeds;
5. ranked top three with risks;
6. one complete storyboard;
7. implementation and license notes.

Keep the main response decision-oriented. Put large inventories or detailed evidence in a separate report when working in a filesystem.

## Resources

- `scripts/analyze_manim_repo.py`: read-only AST inventory for Python/Manim repositories.
- `references/pattern-library.md`: reusable mathematical animation mechanisms and evidence signals.
- `references/ideation-matrix.md`: controlled divergence axes and math/logic seed bank.
- `references/quality-rubric.md`: hard gates, scoring, storyboard, and final verification checks.
