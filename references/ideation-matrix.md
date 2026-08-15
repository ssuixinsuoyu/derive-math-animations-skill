# Ideation matrix for original math and logic animations

Use this after extracting the source's explanatory grammar. Generate across several axes before selecting a topic.

## Divergence axes

| Axis | Questions | Useful transformations |
|---|---|---|
| Claim | What other theorem has the same proof action? | equality → impossibility; existence → uniqueness |
| Representation | Which view reveals a hidden relation? | set ↔ graph ↔ table ↔ formula ↔ geometry |
| Assumption | Which premise carries the result? | remove, weaken, strengthen, or swap one premise |
| Scale/dimension | Does behavior change with size? | finite → infinite; local → global; 2D → 3D |
| Parameter | What can move while one relation is measured? | sample size, error, angle, threshold, probability |
| Failure | What is the smallest legal counterexample? | edge case, adversarial response, illegal proof step |
| Application | Where does the same structure recur? | locks, networks, voting, routing, games, coding |

Generate at least one candidate from four different axes. Combining axes is encouraged, but each candidate needs one dominant explanatory mechanism.

## Transformation prompts

### From a constructive proof

- Keep the invariant and replace the objects.
- Keep the operation and ask when it fails.
- Raise the dimension and identify what no longer transfers.
- Reverse the construction and ask whether it is unique.

### From a simulation

- Hold the random process fixed and change the sampling definition.
- Compare finite evidence with the actual theorem.
- Search for a heavy-tail or boundary case where convergence intuition fails.
- Replace frequency with a sample-space or combinatorial proof.

### From a representation bridge

- Add a third representation that resolves a remaining ambiguity.
- Animate exactly which relation survives the translation.
- Find an object that looks simple in one view and complicated in another.
- Turn the bridge into a reversible “translation machine”.

### From a false proof or paradox

- Identify the first illegal move, not merely the false conclusion.
- Vary the hidden assumption until the theorem becomes true.
- Let the viewer choose between “claim false”, “axioms inconsistent”, and “proof flawed”.
- Construct the smallest counterexample and then a family of counterexamples.

## Seed bank

Treat these as starting structures, not fixed scripts.

### Logic and proof

| Topic | Visual mechanism | Critical check |
|---|---|---|
| `∀x∃y` vs `∃y∀x` | move-order game and dependency arrow | keep domain explicit |
| Necessary vs sufficient | nested sets plus moving counterexample | arrow direction must stay consistent |
| Universal claim and one counterexample | validation gate with adversarial sample | counterexample must be in-domain |
| Converse vs contrapositive | four truth states or state square | distinguish inverse and converse |
| Validity vs truth | inference machine separate from inputs | do not imply valid means sound |
| De Morgan's laws | synchronized sets, gates, and truth table | complement universe must be fixed |
| Proof by contradiction | constraints collapse to no legal state | identify the negated conclusion precisely |
| Proof by cases | exhaustive partition of state space | prove mutual coverage, not just examples |
| Mathematical induction | base node plus closure over all successor edges | do not replace proof with domino imagery |
| Hidden division by zero | legal-operation indicator along derivation | locate the first invalid step |
| Diagonal argument | construct a new row by guaranteed mismatch | define the listed object class precisely |
| Russell's paradox | unstable membership graph | separate naive from axiomatic set theory |
| Boolean satisfiability | hypercube of assignments with constraints removing vertices | avoid implying exhaustive search is always efficient |

### Discrete mathematics

| Topic | Visual mechanism | Critical check |
|---|---|---|
| Pigeonhole principle | capacity meter and forced collision | distinguish weak and generalized forms |
| Checkerboard tiling | color/parity invariant | legal tile moves must preserve it |
| Bipartite graphs | alternating colors around a cycle | show why odd cycles fail |
| Generating functions | weighted object choices become exponents | coefficient meaning must stay visible |
| Inclusion-exclusion | live overcount ledger | signs and intersections must match |
| Euler characteristic | deform or simplify while counts update | specify graph/polyhedron conditions |
| Hanoi recursion | physical state to shortest-path graph | separate construction from optimality proof |
| Equivalence classes | relation edges collapse into quotient nodes | verify relation is reflexive, symmetric, transitive |
| Hall's theorem | subsets and available neighbors | avoid claiming necessity alone proves sufficiency |

### Analysis, geometry, and algebra

| Topic | Visual mechanism | Critical check |
|---|---|---|
| Limit of lengths vs length of limit | shape convergence beside length measurement | name the convergence notion |
| Pointwise vs uniform convergence | error peak moves while sup error stays large | domains and norms must be explicit |
| Derivative as local linearity | zoom with normalized error | do not claim every continuous function is differentiable |
| Harmonic series divergence | group 1, 2, 4, 8 terms into fixed lower bounds | inequalities must face the right direction |
| Complex multiplication | grid rotates and scales | orientation and angle addition must be consistent |
| Sum of odd numbers | add L-shaped borders to a square | maintain one-to-one area count |
| AM-GM | rearrangement or rectangle deformation | positivity assumptions must be visible |
| Fractal dimension | count pieces as scale changes | distinguish heuristic from formal definition |

### Probability and statistics

| Topic | Visual mechanism | Critical check |
|---|---|---|
| Base-rate fallacy | population grid filtered by test outcomes | use conditional probabilities correctly |
| Monty Hall | partition outcomes before and after information | host policy must be specified |
| Simpson's paradox | fixed group trends with changing weights | expose group sizes |
| Bertrand paradox | matched experiment with alternate sampling rules | never say “uniform” without a measure |
| Gambler's fallacy | history moves while next-step distribution stays fixed | only for independent trials |
| Law of large numbers vs CLT | mean concentration vs rescaled shape | distinguish the two conclusions |

## Reject these weak derivations

- Same proof and composition with different labels.
- A color or character swap presented as a new idea.
- A simulation treated as proof without an argument.
- A topic whose main relation is already clearer in one static diagram.
- A spectacular transition with no preserved mathematical identity.
- A paradox that depends on hiding the domain from the viewer.
- A broad subject name without one precise claim.

## Candidate card

Use this compact format for each seed:

```text
Claim:
Viewer misconception:
Visible objects:
Controlled change:
Invariant or measurement:
Representation bridge:
Counterexample or edge case:
Source pattern reused:
Originality boundary:
Proof risk:
```
