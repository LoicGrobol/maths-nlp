<!-- LTeX: language=fr -->

Fonctions
=========

```{math}
% Fix since mathjax doesn't support mleftright 😭
\newcommand\mleft{\mathopen{}\left}
\newcommand\mright{\right}

% Function restriction
\newcommand\restr[2]{{#1_{\mkern 1mu |\mkern2mu_{#2}}}}

% Function description
\newcommand\funct[5]{
	\left|\begin{array}{rrl}
		#1 :  & #2 & ⟶ #3 \\
			  & #4 & ⟼ #1\mleft(#4\mright) = #5
	\end{array}\right.
}
```

- Application, fonction, ensemble de départ (domaine) et d'arrivée (codomaine), image, antécédent.
- Définition d'une fonction par une formule.
- Notion de graphe et représentation graphique.
- Image directe, image réciproque.
- Injectivité, bijectivité, surjectivité.
- Fonction inverse.
- Restrictions d'une fonction.
- Fonction indicatrice d'un ensemble.

## Exercices

### Successeur

Soit $s$, la fonction

```{math}
\funct{s}{ℕ}{ℕ}{n}{n+1}
```

1. Donner le graphe de $s$ sous forme d'ensemble en compréhension.
2. Quelle est l'image de $3$ par $s$ ?
3. $2713$ a-t-elle des antécédents par $s$ ? Lesquels ?
4. $s$ est-elle injective ? Surjective ? Bijective ?
5. Que valent $s(\{1, 5, 6\})$, $s^{-1}(\{2, 7, 3, 1\})$, $s(\{0\})$ et $s^{-1}(\{0\})$ ?
6. $s$ est-elle inversible ? Si oui donner son inverse.

### Carré

Soit $f$, la fonction

```{math}
\funct{f}{ℝ}{ℝ}{x}{x^2}
```

1. Donner les images $0$, $-2$, $0.001$, $2^{2713}$ et $π$ par $f$
2. $4$ a-t-il des antécédents par $f$ ? Lesquels ? Même question pour $-4$ et pour $2$.
3. $f$ est-elle injective ? Surjective ? Bijective ?
4. Que valent $f(\{1, 5, 6\})$, $f^{-1}(\{2, 7, 3, 1\})$, $f(\{0\})$ et $f^{-1}(\{0\})$ ?
5. $f$ est-elle inversible ? Si oui donner son inverse. Sinon, a-t-elle une restriction bijective ?