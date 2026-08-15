# Quality rubric for mathematical animations

Apply hard gates first. Score only candidates that pass every gate.

## Hard gates

A candidate fails if any answer is no:

1. Is there one precise mathematical claim or question?
2. Are the domain, assumptions, and quantifier order stated?
3. Does the proposed visual preserve the mathematical relation it claims to show?
4. Is animation materially more useful than a static sentence or diagram?
5. Is the idea more than a surface copy of the source?
6. Can the crucial claim be checked before production?

Repair or reject failed candidates. Do not average a mathematical error away with other strengths.

## Scoring

Score each criterion from 0 to 5.

| Criterion | 0 | 3 | 5 |
|---|---|---|---|
| Logical rigor | false or undefined | mostly correct with one open condition | proof and edge cases checked |
| Visual necessity | motion is decorative | motion helps | state change is the argument |
| Viewer clarity | no stable mapping | understandable with explanation | mapping is immediately inspectable |
| Originality | near-copy | familiar mechanism on a new claim | new synthesis or revealing representation |
| Feasibility | unknown or blocked | buildable with some new primitives | clear route using available primitives |
| Reusability | one-off spectacle | some reusable pieces | creates a domain primitive or series format |

Default total: 30 points. Prefer 24 or above for production, but a lower-scoring candidate may proceed if the user has a strategic reason.

## Risk labels

Attach at least one risk to every finalist:

- `proof-risk`: a claim, domain, or edge case needs verification;
- `mapping-risk`: visual proximity may be mistaken for equality or causation;
- `scope-risk`: too many prerequisites for one animation;
- `production-risk`: requires unavailable rendering, typography, 3D, or simulation support;
- `originality-risk`: too close to a reference composition;
- `license-risk`: adaptation constraints are unclear.

## Storyboard schema

Create 6–10 beats. Use this table:

| Beat | Mathematical job | Before → after | Transition | Narration/question | Tracked relation |
|---:|---|---|---|---|---|

Every beat must advance the argument. Merge or remove beats that only decorate.

## Proof check

Before handoff, answer:

1. What exactly is being proved, disproved, estimated, or motivated?
2. Is the domain visible or stated?
3. Which steps are examples, and which steps establish the general result?
4. If simulation is used, what theorem or argument closes the gap?
5. Does every counterexample satisfy all premises?
6. Are strict and non-strict inequalities distinguished?
7. Does any variable depend on an earlier choice? If so, is the dependency visible?
8. Are limiting operations being interchanged? If so, under what condition?
9. Does a diagram rely on scale, orientation, or a special case?
10. What is the smallest edge case?

## Visual semantics check

- One role keeps one color until an explicit handoff.
- Equal-looking objects are not assumed equal without a relation.
- Area encodes quantity only when area is mathematically relevant.
- Position encodes order only when axes or orientation are clear.
- Object morphs preserve a stated correspondence.
- Camera movement reveals a new scale, dependency, or structure.
- Labels follow objects without obscuring the relation.
- The final frame preserves the proof's decisive evidence.

## Evidence and confidence check

For reverse-engineered findings:

- cite a source location or timestamp;
- seek a second independent example before calling a corpus-wide pattern validated;
- record parser or runtime failures;
- label render behavior as unverified when no render was performed;
- separate source facts from creative proposals.

## Implementation route

Choose one:

1. `reuse`: an existing domain abstraction already models the exact operation;
2. `adapt`: a generic pattern can be applied with new objects and proof checks;
3. `build`: the topic needs a new primitive such as a quantifier game, invariant tracker, or proof-state machine.

Name the minimum primitive set. Do not propose a framework before one storyboard demonstrates repeated need.
