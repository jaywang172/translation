## 178 章節 3. 向量空間與子空間

現在假設 $c \neq 1$。則矩陣 $M$ 是可逆的。如果 $x$ 是一個非零向量，我們知道 $Mx$ 是非零的。由於 $x = WM$，這表示 $x$ 不在 $V$ 的零空間中。換句話說，$v_1, v_2, v_3$ 是獨立的。

這個一般規則是“獨立的 $w$’s 從 $w$’s 的基底 $M$ 是可逆的”。如果這些向量在 $\mathbb{R}^3$ 中，它們不僅獨立，而且也是 $\mathbb{R}^3$ 的基底。“$w$’s 基底從 $w$’s 的基底當變換矩陣 $M$ 是可逆的”。

**3.5 C (重要範例)** 假設 $v_1, \dots, v_n$ 是 $\mathbb{R}^n$ 的基底，且 $n \times n$ 矩陣 $A$ 是可逆的。證明 $Av_1, \dots, Av_n$ 也是 $\mathbb{R}^n$ 的基底。

**解答** 以矩陣語言：將基底向量 $v_1, \dots, v_n$ 放在可逆矩陣 $V$ 的欄中。則 $Av_1, \dots, Av_n$ 是 $AV$ 的欄。由於 $A$ 是可逆的，所以 $AV$ 及其欄也是可逆的。

以向量語言：假設 $c_1Av_1 + \dots + c_nA v_n = 0$。則 $A(c_1v_1 + \dots + c_nv_n) = 0$。由於 $A$ 是可逆的，乘以 $A^{-1}$ 得到 $c_1v_1 + \dots + c_nv_n = 0$。由於 $v_1, \dots, v_n$ 獨立，因此所有 $c_i = 0$。這表示 $Av_1, \dots, Av_n$ 是獨立的。

為了證明 $Av$’s 跨越 $\mathbb{R}^n$，解 $c_1Av_1 + \dots + c_nA v_n = b$ 等同於 $c_1v_1 + \dots + c_nv_n = A^{-1}b$。由於 $v_1, \dots, v_n$ 是基底，這必須可解。

**問題集 3.5**

問題 1-10 關於線性獨立與線性相依。

**1** 證明 $v_1, v_2, v_3$ 是獨立的，但 $v_1, v_2, v_3, v_4$ 是相依的：

$v_1 = \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}$, $v_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}$, $v_3 = \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}$, $v_4 = \begin{bmatrix} 2 \\ 3 \\ 4 \\ 0 \end{bmatrix}$

**2** 解 $c_1v_1 + c_2v_2 + c_3v_3 + c_4v_4 = 0$ 或 $Ax = 0$。The $v$'s go in the columns of $A$.

**(推薦解答)** 找到任何與以下向量可能的線性獨立向量：

$v_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}$, $v_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \\ 0 \end{bmatrix}$, $v_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}$, $v_4 = \begin{bmatrix} 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}$, $v_5 = \begin{bmatrix} 1 \\ 1 \\ 1 \\ 1 \end{bmatrix}$, $v_6 = \begin{bmatrix} 1 \\ 0 \\ 1 \\ 0 \end{bmatrix}$

**3** 證明 $v_1 = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$, $v_2 = \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}$, $v_3 = \begin{bmatrix} 7 \\ 8 \\ 9 \end{bmatrix}$ 是線性相依的。

$U = \begin{bmatrix} 1 & 4 & 7 \\ 2 & 5 & 8 \\ 3 & 6 & 9 \end{bmatrix}$

**4** 證明 $v_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$, $v_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}$, $v_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}$ 是線性獨立的。
