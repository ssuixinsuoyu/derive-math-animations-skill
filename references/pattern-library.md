# Mathematical animation pattern library

Use this reference after mapping the input and before generating new ideas. A pattern is a reusable relation between mathematics and visible state, not a color palette or transition effect.

## Pattern record

Describe every claimed pattern with these fields:

| Field | Meaning |
|---|---|
| Mathematical job | What understanding or proof step it enables |
| Visible state | Objects and relations the viewer can inspect |
| Controlled change | What the animation changes |
| Preserved relation | Invariant, identity, dependency, or measurement |
| Evidence signal | Source operation, repeated example, or timestamp |
| Failure mode | How the pattern can mislead |

## 1. Invariant under transformation

- Mathematical job: prove equality or impossibility without symbol pushing.
- Visible state: pieces, areas, parity labels, counts, or graph structure.
- Controlled change: rearrange, deform, add a legal move, or relabel.
- Preserve: area, parity, connectivity, orientation, or another invariant.
- Strong use: Pythagorean rearrangement, checkerboard tiling, Euler characteristic.
- Failure mode: the supposedly preserved quantity changes during an unstated operation.

Evidence signals: `Transform`, `MoveToTarget`, shared object identity, live invariant label, before/after measurements.

## 2. Concrete-to-symbolic compression

- Mathematical job: make a formula feel inevitable.
- Visible state: small examples or manipulable objects.
- Controlled change: group, count, copy, or reorganize the objects.
- Preserve: one-to-one correspondence between concrete objects and symbolic terms.
- Strong use: subsets to generating functions, geometric pieces to algebraic identity.
- Failure mode: the formula appears before the viewer has seen what each term records.

Recommended ladder:

`single example → repeated operation → organized cases → compressed notation → generalized rule`

## 3. Representation bridge

- Mathematical job: reveal a relation hidden in the current representation.
- Visible state: the same object shown as geometry, algebra, graph, table, probability region, or state network.
- Controlled change: morph or copy components into the new representation.
- Preserve: identity of elements and relations.
- Strong use: binary choices to hypercube; complex multiplication to grid transformation.
- Failure mode: decorative morphing with no explicit correspondence.

Before switching, state what the new representation makes easier to see.

## 4. Parameter sweep with live measurement

- Mathematical job: expose a trend, convergence, threshold, or invariant.
- Visible state: parameter control plus dependent objects and one measurement.
- Controlled change: move one parameter continuously or over a designed sequence.
- Preserve: functional relationship among all dependent objects.
- Strong use: secant to tangent, Riemann refinement, sample frequency, polygon approximation.
- Failure mode: sampling only convenient values or implying proof from a finite simulation.

Evidence signals: trackers, updaters, repeated loops, counters, changing decimal labels.

## 5. Assumption swap

- Mathematical job: reveal that an informal phrase hides multiple mathematical models.
- Visible state: hold most of an experiment fixed.
- Controlled change: replace one definition, distribution, domain, or boundary condition.
- Preserve: question, measurement, and comparison layout.
- Strong use: Bertrand's random chord methods.
- Failure mode: changing several assumptions at once, making the cause ambiguous.

Use subclasses, configuration changes, or matched scenes when inspecting code.

## 6. Counterexample as adversarial move

- Mathematical job: refute a universal claim or show a strategy cannot exist.
- Visible state: a proposed rule and a legal response.
- Controlled change: choose the smallest input that violates the rule.
- Preserve: the original claim and its domain.
- Strong use: quantifier order, false converse, graph coloring, hidden division by zero.
- Failure mode: showing an example outside the stated domain.

For quantifiers, animate dependency and move order explicitly.

## 7. Plausible path, then fracture

- Mathematical job: locate the first invalid proof step.
- Visible state: a chain of apparently legal transformations.
- Controlled change: replay or zoom into the suspect transition.
- Preserve: all earlier valid steps.
- Strong use: false proofs, limit interchange, geometric diagrams that smuggle in an assumption.
- Failure mode: revealing the trick too early or merely announcing “wrong”.

Preferred sequence:

`plausible claim → viewer prediction → conflicting consequence → replay → first illegal step → repaired theorem`

## 8. Local-to-global camera semantics

- Mathematical job: compare microscopic behavior with global structure.
- Visible state: one consistent object at different scales.
- Controlled change: zoom, pan, or rotate viewpoint.
- Preserve: object identity and scale indicator.
- Strong use: derivative as local linearity, fractal scale, local error versus total error.
- Failure mode: camera motion that communicates no new relation.

## 9. Sample-space partition

- Mathematical job: make probability conditioning and regrouping inspectable.
- Visible state: area, population grid, tree, or weighted branches.
- Controlled change: partition, filter, normalize, or regroup.
- Preserve: total mass and explicit denominators.
- Strong use: Bayes, Monty Hall, Simpson's paradox, base-rate problems.
- Failure mode: resizing areas without preserving probability mass.

## 10. Algorithm-generated animation

- Mathematical job: show that a visual process follows a discrete rule rather than choreography.
- Visible state: data structure plus geometric realization.
- Controlled change: each algorithm step creates the next animation event.
- Preserve: correspondence between algorithm state and visible state.
- Strong use: union-find and cycles, BFS layers, recursive state graphs.
- Failure mode: algorithm output and displayed order silently diverge.

## 11. Productive objection

- Mathematical job: surface a likely misconception at the exact point it becomes relevant.
- Visible state: character, speech bubble, poll, or paused question.
- Controlled change: test the objection with an example or counterexample.
- Preserve: the viewer's original question until resolved.
- Strong use: “x is only a symbol”, “does this always work?”, “is this really random?”
- Failure mode: comic relief unrelated to the proof.

## 12. Semantic color and object identity

- Mathematical job: reduce working-memory load across representations.
- Visible state: stable colors and persistent object ancestry.
- Controlled change: position, form, or representation.
- Preserve: role meaning.
- Strong use: one variable, region, basis vector, or probability category keeps one color.
- Failure mode: reusing a color for a different role without an explicit handoff.

## Historical evidence: 3b1b/videos snapshot

Snapshot inspected: `3b1b/videos` commit `e1cd3ef171c1eb21fa7bc23511dc1e9a20fe4359`.

Corpus observations from AST inspection:

- 420 Python files and 513,518 lines.
- 5,802 classes with a `construct` method.
- 29,594 `self.play` and 18,934 `self.wait` calls.
- 100 direct `LinearTransformationScene` subclasses and 74 direct `GraphScene` subclasses.
- High-frequency operations include `Transform`, `ReplacementTransform`, `TransformFromCopy`, `MoveToTarget`, `add_updater`, `Brace`, and `SurroundingRectangle`.

Representative static evidence:

| Mechanism | Source |
|---|---|
| Area-preserving rearrangement | `_2015/pythagorean_proof.py`, `ShowRearrangementInBigSquare` |
| Assumption swap through common base scene | `_2021/bertrands_paradox.py`, `RandomChordScene` and subclasses |
| Limit counterexample and explicit error tracking | `_2022/visual_proofs/lies.py`, `SquareCircleExample`, `IntegralError` |
| Concrete subsets to hypercube and polynomial | `_2022/puzzles/subsets.py`, `ShowHypercubeConstruction`, `PolynomialConstruction` |
| Algorithmic state driving geometry | `_2026/monthly_mindbenders/strings.py`, `compute_join_sequence` |
| Domain-specific graph operations | `once_useful_constructs/graph_scene.py` |
| Domain-specific linear transformations | `once_useful_constructs/vector_space_scene.py` |

These are static findings. Do not claim render behavior or current-version compatibility without executing the relevant scene in a suitable environment.
