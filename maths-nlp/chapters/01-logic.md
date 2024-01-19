<!-- LTeX: language=fr -->

Logique
=======

- Logique formelle comme modèle simplifié de la logique usuelle.
- Symboles $\operatorname{VRAI}$ et $\operatorname{FAUX}$
- Opérateurs logiques $\operatorname{ET}$, $\operatorname{OU}$, $\operatorname{NON}$
- Formules logiques et prédicats
- Calcul booléen et tables de vérités
- Équivalence entre prédicats
- Commutativité, associativité, idempotence de  $\operatorname{NON}$
- Lois de De Morgan
- Opérateurs $\operatorname{XOR}$, $\operatorname{NAND}$, $\operatorname{NOR}$, $⇒$,
  $\operatorname{⇔}$
- Universalité de $\operatorname{NAND}$
- Notations $¬$, $∧$, $∨$, $⊗$.

À faire :

- tautologie, contradiction
- tiers exclu

## Exercices

### Calcul booléen

Développer et simplifier au maximum les formules logiques suivantes

1. $\operatorname{VRAI} \operatorname{ET} \operatorname{VRAI}$
2. $\operatorname{VRAI} \operatorname{ET} (\operatorname{VRAI} \operatorname{OU} \operatorname{FAUX})$
3. $\operatorname{VRAI} \operatorname{ET} A$
4. $A \operatorname{OU} \operatorname{FAUX}$
5. $ζ \operatorname{OU} (\operatorname{NON} ζ)$
6. $(A \operatorname{OU} (\operatorname{NON} B)) \operatorname{OU} B$
7. $\operatorname{NON} (A \operatorname{OU} B \operatorname{OU} \operatorname{FAUX})$

### Tautologies

On dit qu'un prédicat est une tautologie s'il est vrai quelle que soit la valeur donnée à ses variables. On dit qu'il est une contradiction s'il est faux quelle que soit la valeur donnée à ses variables. Attention : un prédicat peut n'être ni l'un ni l'autre.

Pour chacune des expressions suivantes, déterminer à l'aide d'une table de vérité s'il s'agit d'une
tautologie, d'une contradiction, ou ni l'une ni l'autre.

1. $(A \operatorname{OU} B) \operatorname{OU} (\operatorname{NON} A)$
2. $((\operatorname{NON} A) \operatorname{OU} B) \operatorname{OU} (\operatorname{NON} A)$
3. $(\operatorname{NON} (A \operatorname{OU} B)) \operatorname{OU} A$
4. $(A \operatorname{OU} B) \operatorname{ET} C$

### Équivalences

Démontrer la deuxième loi de De Morgan de deux façons différentes.
