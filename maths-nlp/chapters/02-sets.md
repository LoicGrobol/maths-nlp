<!-- LTeX: language=fr -->

Ensembles
=========

Fait :

- Définitions : ensemble, $∈$, $∉$, complémentaire absolu ($⋅^c$), $⊂$, parties d'un ensemble,
  ensemble vide.
- Notations $⊃$, $\not⊂$ et $∋$.
- Égalités entre ensembles.
- Intersection $∩$ et union $∪$.
- Définitions en intension et en extension d'un ensemble.
- Soustractions d'ensembles (complémentaire relatif).
- Propriété des opérateurs ensemblistes.
  - Associativité.
  - Distributivité
  - Lois de De Morgan.
- Ensembles de nombres usuels $ℕ$, $ℤ$, $ℚ$, $ℝ$.
  - Notation $ℕ^*$
  - Propriété de récurrence (énoncé).
  - Écriture décimale.
  - Intervalles réels.
- Produit cartésien $×$ et $n$-uplets

À faire :

- Notation $ℝ^*$
- Opérations sur les tuples (concaténation, soustraction, multiplication scalaire).

## Exercices

### Opérations ensemblistes

1\. Calculez les résultats des opérations suivantes :

1. $\{0, 1, 2, 3, 4\} ∩ \{0, 2, 4, 6, 8\}$
2. $\{0, 1, 2, 3, 4\} ∪ \{0, 2, 4, 6, 8\}$
3. $\{0, 1, 2, 3, 4\} ∖ \{0, 2, 4, 6, 8\}$
4. $\{a, b\} × \{c, a\}$.

2\. Si $A$ est l'ensemble des langues celtiques, $B$ l'ensemble des langues d'Europe continentale,
et $C$ l'ensemble des langues vivantes, écrire en extension :

1. $A \cap B \cap C$
2. $(A ∖ C) \cap B$


:::{admonition} Solutions
:class: dropdown

1\.

1. $\{0, 1, 2, 3, 4\} ∩ \{0, 2, 4, 6, 8\} = \{0, 2, 4\}$
2. $\{0, 1, 2, 3, 4\} ∪ \{0, 2, 4, 6, 8\} = \{0, 1, 2, 3, 4, 6, 8\}$
3. $\{0, 1, 2, 3, 4\} ∖ \{0, 2, 4, 6, 8\} = \{1, 3\}$
4. $\{a, b\} × \{c, a\} = \{(a,c), (a, a), (b, c), (b, a)\}$.

2\.

1. $\{\text{Breton}\}$
2. $\{\text{Gaulois}, \text{Celtibère}, \text{Lépontique}, \text{Gallaïque}, \text{Norique},
   \text{Galate}\}$ (en l'état actuel des connaissances).

:::

### Ensembles en compréhension

Écrire en extension

1. $A = \{x ∈ \{0, 1, 2, 3, 4\}\,\vert\,x < 3\}$
2. $\{x ∈ A\,\vert\,x > 0\}$
3. $\{3α\,\vert\,α \in A\}$
4. $\{2x\,\vert\,x ∈ ℕ\} ∩ \{x ∈ ℕ\,\vert\,x ≤ 5\}$

:::{admonition} Solutions
:class: dropdown

1. $A = \{0, 1, 2\}$
2. $\{1, 2\}$
3. $\{0, 3, 6\}$
4. $\{0, 2, 4\}$.

:::


### Opérations sur les intervalles

Soit des réels $a$, $b$, $c$, $d$, $e$ tels que

$$
a ⩽ e ⩽ b ⩽ c ⩽ d
$$

Simplifier si c'est possible :

1. $[-2, 3] ∩ [1, 2]$
2. $[13, 27] ∖ [15, 30]$
3. $[a, b] ∩ [e, c]$
4. $[a, b] ∖ [e, c]$
5. $[a, b] ∪ [e, c]$
6. $[a, b] ∪ [c, d]$
7. $[b, c] ∖ [c, d]$

:::{admonition} Solutions
:class: dropdown

1. $[1, 2]$
2. $[15, 27]$
3. $[e, b]$
4. $[a, e[$
5. $[a, c]$
6. $[a, b] ∪ [c, d]$
7. $[b, c[$

:::
