## 24 章：向量導論

看看兩個特定的選擇 0, 0, 0 和 1, 3, 5 作為右側的 b₁、b₂、b₃：

$\qquad \mathbf{b} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$ 給予 $\mathbf{x} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$, $\qquad \mathbf{b} = \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix}$ 給予 $\mathbf{x} = \begin{bmatrix} 1 \\ 1+3 \\ 1+3+5 \end{bmatrix} = \begin{bmatrix} 1 \\ 4 \\ 9 \end{bmatrix}$.

第一個解（全零向量）比看起來更重要。用文字來說：如果輸出為 $\mathbf{b} = \mathbf{0}$，則輸入必須為 $\mathbf{x} = \mathbf{0}$。對於這個矩陣 A 來說，該陳述是成立的。但這並非對所有矩陣都成立。我們的第二個例子將會顯示（對於不同的矩陣 C）如何才能有 $C\mathbf{x} = \mathbf{0}$ 當 $\mathbf{x} \neq \mathbf{0}$ 時。

這個矩陣 A 是“可逆的”。從 $\mathbf{b}$ 我們可以恢復 $\mathbf{x}$。

### 反矩陣

讓我們重複解在式 (6) 中的解。一個求和矩陣會出現！

$A\mathbf{x} = \mathbf{b}$ 由以下解出：
$\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}$. (7)

如果 $\mathbf{x}$ 的差是 $\mathbf{b}$ 的，那麼 $\mathbf{b}$ 的和是 $\mathbf{x}$ 的。這對所有向量都成立。求和矩陣 S 在式 (7) 中是矩陣 A 的反矩陣。

例子：如果 $\mathbf{b} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$，那麼 $\mathbf{x} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$。$S\mathbf{b} = A\mathbf{x}$ 且 $\mathbf{x} = S\mathbf{b}$:

$A\mathbf{x} = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$ 且 $S\mathbf{b} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} = \begin{bmatrix} 1 \\ 3 \\ 6 \end{bmatrix}$.

式 (7) 中的解向量 $\mathbf{x} = (x_1, x_2, x_3)$ 告訴我們兩個重要事實：

1. 對於每個 $\mathbf{b}$ 都有一個解 $\mathbf{x}$ 使得 $A\mathbf{x} = \mathbf{b}$。 2. 矩陣 S 產生 $\mathbf{x} = S\mathbf{b}$。

接下來的章節將會探討方程式 $A\mathbf{x} = \mathbf{b}$。是否有解？如何計算？在線性代數中，反矩陣的表示為 $A^{-1}$。

$A\mathbf{x} = \mathbf{b}$ 由以下解出 $\qquad \mathbf{x} = A^{-1}\mathbf{b} = S\mathbf{b}$.

現在到微積分。讓我們連接這些特殊的矩陣 A 和 S 到微積分。向量的差變成一個函數的 $\mathbf{x}$。這些差 $A\mathbf{x}$ 變成導數 $dx/dt = b(t)$。在反矩陣的定義中，求和 S 變成差分運算子 $Δ$。基本原理如下：

$\qquad \frac{dx}{dt} = b(t) \qquad \text{且} \qquad \Delta x = b(t)$.
