<!-- LTeX: language=fr -->

Logique
=======

- Logique formelle comme modèle simplifié de la logique usuelle..
- Symboles $\operatorname{VRAI}$ et $\operatorname{FAUX}$.
- Opérateurs logiques $\operatorname{et}$, $\operatorname{ou}$, $\operatorname{non}$.
- Formules logiques et prédicats.
- Calcul booléen et tables de vérités.
- Tautologie, contradiction.
- Équivalence entre prédicats.
- Commutativité, associativité, idempotence de  $\operatorname{non}$.
- Lois de De Morgan.
- Opérateurs $\operatorname{xor}$, $\operatorname{nand}$, $\operatorname{nor}$, $⇒$,.
	$\operatorname{⇔}$.
- Universalité de $\operatorname{nand}$.
- Notations $¬$, $∧$, $∨$, $⊗$.

À faire :

- Tiers exclu.

## Exercices

### Calcul booléen

Développer et simplifier au maximum les formules logiques suivantes

1. $\operatorname{VRAI}\,\operatorname{et}\,\operatorname{VRAI}$
2. $\operatorname{VRAI}\,\operatorname{et} (\operatorname{VRAI}\,\operatorname{ou}
	 \operatorname{FAUX})$
3. $\operatorname{VRAI}\,\operatorname{et} A$
4. $A \operatorname{ou}\,\operatorname{FAUX}$
5. $ζ \operatorname{ou}\,(\operatorname{non} ζ)$
6. $(A \operatorname{ou}\,(\operatorname{non} B)) \operatorname{ou} B$
7. $\operatorname{non}\,(A \operatorname{ou}\,B\,\operatorname{ou}\,\operatorname{FAUX})$

:::{admonition} Solutions
:class: dropdown

1\.

$\operatorname{VRAI}\,\operatorname{et}\,\operatorname{VRAI} = \operatorname{VRAI}$ par définition
	 de $\operatorname{et}$

2\. 

$$
\begin{align}
	\operatorname{VRAI}\,\operatorname{et}\,(\operatorname{VRAI}\,\operatorname{ou}
	\operatorname{FAUX})
		&= \operatorname{VRAI}\,\operatorname{et}\,\operatorname{VRAI}
			& \text{par définition de $\operatorname{ou}$}\\
		&= \operatorname{VRAI}
\end{align}
$$

3\.

$\operatorname{VRAI}\,\operatorname{et} A = A$ (faire une table de vérité si besoin).

4\.

$A \operatorname{ou}\,\operatorname{FAUX} = A$ (faire une table de vérité si besoin).

5\.

$ζ \operatorname{ou}\,(\operatorname{non}\,ζ) = \operatorname{VRAI}$

(on appelle cette relation **tiers exclus**)

6\. 

$$
\begin{align}
	(A \operatorname{ou}\,(\operatorname{non} B)) \operatorname{ou} B
		&= A \operatorname{ou}\,((\operatorname{non} B) \operatorname{ou} B)
			& \text{par associativité de $\operatorname{ou}$}\\
		&= A\operatorname{ou}\,\operatorname{VRAI}\\
		&= A
\end{align}
$$

7\. 

$$
\begin{align}
	\operatorname{non}\,(A \operatorname{ou}\,B\,\operatorname{ou}\,\operatorname{FAUX})
		&= \operatorname{non}\,(A \operatorname{ou}\,B)\\
		&= (\operatorname{non}\,A) \operatorname{et}\,(\operatorname{non}\,B)
			& \text{d'après les lois de De Morgan}\\
\end{align}
$$

:::

### Tautologies

On dit qu'un prédicat est une tautologie s'il est vrai quelle que soit la valeur donnée à ses
variables. On dit qu'il est une contradiction s'il est faux quelle que soit la valeur donnée à ses
variables. Attention : un prédicat peut n'être ni l'un ni l'autre.

Pour chacune des expressions suivantes, déterminer s'il s'agit d'une tautologie, d'une
contradiction, ou ni l'une ni l'autre. Utiliser une table de vérité et/ou des simplifications en
utilisant les propriétés des opérateurs logiques

1. $P_1(A, B) = (A \operatorname{ou}\,B) \operatorname{ou}\,(\operatorname{non}\,A)$
2. $P_2(A, B) = ((\operatorname{non}\,A) \operatorname{ou}\,B)
	 \operatorname{ou}\,(\operatorname{non} A)$
3. $P_3(A, B) = (\operatorname{non}\,(A \operatorname{ou}\,B)) \operatorname{et}\,A$
4. $P_4(A, B, C) = (A \operatorname{ou}\,B) \operatorname{et}\,C$

::::{admonition} Solutions
:class: dropdown

Il y a plusieurs solutions pour chacune des questions, ce qui suit n'est donc qu'une suggestion.

1\.

:::{table}
:widths: auto
:align: center

| $A$ | $B$ | $A \operatorname{ou}\,B$ | $\operatorname{non}\,A$ | $P_1(A,B)$ |
| :-: | :-: | :----------------------: | :---------------------: | :--------: |
| $0$ | $0$ |           $0$            |           $1$           |    $1$     |
| $0$ | $1$ |           $1$            |           $1$           |    $1$     |
| $1$ | $0$ |           $1$            |           $0$           |    $1$     |
| $1$ | $1$ |           $1$            |           $0$           |    $1$     |
:::

$P_1(A, B)$ est vrai quelles que soient les valeurs de $A$ et de $B$, $P_1$ est
donc une tautologie.

2\.

$$
\begin{align}
	P_2(A, B)
		&= ((\operatorname{non}\,A) \operatorname{ou}\,B) \operatorname{ou}\,(\operatorname{non} A)\\
		&= B \operatorname{ou}\,((\operatorname{non}\,A) \operatorname{ou}\,(\operatorname{non} A)) &\\
		&= B \operatorname{ou}\,(\operatorname{non}\,A)
\end{align}
$$

Par conséquent

- $P(\operatorname{VRAI}, \operatorname{FAUX}) =
\operatorname{FAUX}\,\operatorname{ou}\,(\operatorname{non}\,\operatorname{VRAI}) =
\operatorname{FAUX}$
- $P(\operatorname{VRAI}, \operatorname{VRAI}) =
\operatorname{VRAI}\,\operatorname{ou}\,(\operatorname{non}\,\operatorname{VRAI}) =
\operatorname{VRAI}$

$P_2$ n'est donc ni une contradiction, ni une tautologie.

3\.

:::{table}
:widths: auto
:align: center

| $A$ | $B$ | $A \operatorname{ou}\,B$ | $ \operatorname{non}\,(A \operatorname{ou}\,B)$ | $P_3(A,B)$ |
| :-: | :-: | :----------------------: | :---------------------------------------------: | :--------: |
| $0$ | $0$ |           $0$            |                       $1$                       |    $0$     |
| $0$ | $1$ |           $1$            |                       $0$                       |    $0$     |
| $1$ | $0$ |           $1$            |                       $0$                       |    $0$     |
| $1$ | $1$ |           $1$            |                       $0$                       |    $0$     |
:::

$P_3$ est donc une contradiction.

4\.

:::{table}
:widths: auto
:align: center

| $A$ | $B$ | $C$ | $A \operatorname{ou}\,B$ | $P_4(A,B,C)$ |
| :-: | :-: | :-: | :----------------------: | :----------: |
| $0$ | $0$ | $0$ |           $0$            |     $0$      |
| $0$ | $0$ | $1$ |           $0$            |     $0$      |
| $0$ | $1$ | $0$ |           $1$            |     $0$      |
| $0$ | $1$ | $1$ |           $1$            |     $1$      |
| $1$ | $0$ | $0$ |           $1$            |     $0$      |
| $1$ | $0$ | $1$ |           $1$            |     $1$      |
| $1$ | $1$ | $0$ |           $1$            |     $0$      |
| $1$ | $1$ | $1$ |           $1$            |     $1$      |
:::

$P_4$ n'est donc ni une contradiction, ni une tautologie.

::::

### Équivalences

Démontrer la deuxième loi de De Morgan de deux façons différentes.

::::{admonition} Solutions
:class: dropdown

Version 1: tables de vérité

:::{table}
:widths: auto
:align: center

| $A$ | $B$ | $A\,\operatorname{ou}\,B$ | $\operatorname{non}\,(A \operatorname{ou}\,B)$ |
| :-: | :-: | :----------------------: | :--------------------------------------------: |
| $0$ | $0$ |           $0$            |                      $1$                       |
| $0$ | $1$ |           $1$            |                      $0$                       |
| $1$ | $0$ |           $1$            |                      $0$                       |
| $1$ | $1$ |           $1$            |                      $0$                       |
:::

| $A$ | $B$ | $\operatorname{non}\,A$ | $\operatorname{non}\,B$ | $(\operatorname{non}\,A)\,\operatorname{et}\,(\operatorname{non}\,B)$ |
| :-: | :-: | :---------------------: | :---------------------: | :-------------------------------------------------------------------: |
| $0$ | $0$ |           $1$           |           $1$           |                                  $1$                                  |
| $0$ | $1$ |           $1$           |           $0$           |                                  $0$                                  |
| $1$ | $0$ |           $0$           |           $1$           |                                  $0$                                  |
| $1$ | $1$ |           $0$           |           $0$           |                                  $0$                                  |
:::

Version 2: en utilisant l'autre

$$
\begin{align}
	\operatorname{non}\,(A \operatorname{ou}\,B)
		&= \operatorname{non}\,(
			(\operatorname{non}\,(\operatorname{non}\,A))\,
			\operatorname{ou}\,
			(\operatorname{non}\,(\operatorname{non}\,B))
		)\\
		&= (\operatorname{non}\,A)\,\operatorname{et}\,(\operatorname{non}\,B)\\
\end{align}
$$

::::