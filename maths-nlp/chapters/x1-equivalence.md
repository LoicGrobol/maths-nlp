<!-- LTeX: language=fr -->

DTL: applications linéaires
===========================

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

On appelle *application linéaire* toute fonction $u:ℝ^n\longrightarrow ℝ^m$ telle que

1. Pour tout $x∈ℝ^n$ et pour tout $λ∈ℝ$, $u(λx) = λu(x)$.
2. Pour tout $x∈ℝ^n$ et $y∈ℝ^n$, $u(x+y) = u(x) + u(y)$.

Par exemple : la fonction

$$\funct{u}{ℝ^3}{ℝ}{x}{2x_1 - x_2}$$

est linéaire. Pour le prouver, considérons $x∈ℝ^3$, $y∈ℝ^3$ et $λ∈ℝ$ quelconques.

On a

$$
    \begin{align}
        u(λx)
            &= 2(λx_1) - (λx_2)\\
            &= λ(2x_1 - x_2)\\
            &= λu(x)
    \end{align}
$$

et

$$
    \begin{align}
        u(x+y)
            &= 2(x_1+y_1) - (x_2+y_2)\\
            &= 2x_1+2y_1 - x_2-y_2\\
            &= (2x_1- x_2) + (2y_1-y_2)\\
            &= u(x) + u(y)
    \end{align}
$$

L'ensemble des applications linéaires de $E$ dans $F$ est noté $𝓛(E,F)$.

## 1. Exemples

**1.1** Montrer que les application suivantes sont linéaires

$$\funct{f_1}{ℝ^5}{ℝ}{x}{x_3}$$

$$\funct{f_2}{ℝ^3}{ℝ^2}{x}{\begin{pmatrix}2x_1-x_2\\3x_1\end{pmatrix}}$$

$$\funct{z}{ℝ^{12}}{ℝ^4}{x}{\begin{pmatrix}0\\0\\0\\0\end{pmatrix}}$$

$$\funct{L}{ℝ^3}{ℝ^2}{Y}{\begin{pmatrix}2&7&1\\3&0&0\end{pmatrix}×Y}$$

$$\funct{h}{ℝ^n}{ℝ^n}{x}{ax}$$

pour $n∈ℕ^*$ et $a∈ℝ$ quelconques.  

**1.2** Montrer que pour toute matrice $M∈\mathcal{Mat}_{m,n}(ℝ)$, la fonction

$$\funct{u_M}{ℝ^n}{ℝ^m}{X}{MX}$$

est une application linéaire.

L'objectif de la suite de ce travail est de montrer que la réciproque est vraie : pour toute
application linéaire $u$, il existe une matrice $M$ telle que pour tout $x$, $u(x) = Mx$.

## 2. Base canonique et applications linéaires

On appelle *base canonique de $ℝ^n$*, la famille de vecteurs $(e_1, …, e_n)$ de $ℝ^n$ définie par

$$
    \begin{align}
        e_1 &= \begin{pmatrix}1\\0\\\vdots\\0\end{pmatrix}\\
        e_2 &= \begin{pmatrix}0\\1\\0\\\vdots\\0\end{pmatrix}\\
        \vdots\\
        e_n &= \begin{pmatrix}0\\\vdots\\0\\1\end{pmatrix}
    \end{align}
$$

(ou encore $e_i = (\mathbb{1}_{j=i})_i$).

Tout vecteur $x$ de coordonnées $(x_1, …, x_n)$ peut alors s'écrire comme une somme pondérée des $e_i$:

$$
    \begin{align}
        x
            &= \begin{pmatrix}x_1\\\vdots\\x_n\end{pmatrix}\\
            &= x_1\begin{pmatrix}1\\0\\\vdots\\0\end{pmatrix} + … + x_n\begin{pmatrix}0\\\vdots\\0\\1\end{pmatrix}\\
            &= x_1e_1 + … + x_ne_n\\
            &= \sum_{i=1}^n x_ie_i
    \end{align}
$$

(cette décomposition est par ailleurs unique : il n'y a pas d'autres coefficients $a_i$ pour
lesquels $x= \sum_{i=1}^n a_ie_i$.)

**2.1** On considère deux applications linéaires $u$ et $v$ telles que pour tout $i$, $u(e_i)=v(e_i)$.
Montrer alors que pour tout $x$, on a $u(x)=v(x)$.

La réciproque est immédiate : si pour tout $x$, $u(x)=v(x)$, alors en particulier pour tout $i$,
$u(e_i)=v(e_i)$. On a donc la propriété suivante :

*Deux applications linéaires sont égales si et seulement si elles sont égales sur la base canonique.*

## 3. Correspondance matrice-application

**3.1** Soit $u: ℝ^2\longrightarrow ℝ²$ $, une application linéaire telle que

$$
    \begin{align}
        u(e_1) &= \begin{pmatrix}2\\1\end{pmatrix}\\
        u(e_2) &= \begin{pmatrix}-1\\0\end{pmatrix}
    \end{align}
$$

**3.1.1** Trouver une matrice $M$ telle que $Me_1 = u(e_1)$ et $Me_2=u(e_2)$.

**3.1.2** Que peut-on dire de la fonction $u_M$ définie comme précédemment ?

**3.2** Soit $M∈\mathcal{Mat}_{n,m}(ℝ)$, à quoi correspond le vecteur $Me_1$ par rapport à $M$ ? Et $Me_i$ ?

**3.3** Soit $u∈𝓛(ℝ^n, ℝ^m)$, une application linéaire. Déterminer une matrice
$M∈\mathcal{Mat}_{m,n}(ℝ)$ telle que pour tout $i$, $Me_i = u(e_i)$. Que peut-on alors dire des
fonctions $u$ et $u_M$ ?

On dit alors que $M$ est la *matrice de $u$ entre les bases canoniques de $ℝ^n$ et $ℝ^m$*, ce que
l'on note (entre autres) $M=\mathcal{Mat}_{ℝ^m←ℝ^n}(u)$.

Finalement : *la multiplication par une matrice est une opération linéaire, et réciproquement, tout
application linéaire peur s'écrire comme le produit par une matrice.

## 4. Une dernière propriété

Pour les avides de savoir : soit $u∈𝓛(E,F)$ et $v∈(F,G)$, montrer que

$$\mathcal{Mat}_{G←E}(v∘u)=\mathcal{Mat}_{G←F}(v)×\mathcal{Mat}_{F←E}(u)$$
