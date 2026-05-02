## 3.2. 矩陣 A 的零空間：解 Ax = 0

133

這是描述零空間的最佳方式，透過計算 Ax = 0 的特殊解來進行。
這個例子有一個特殊解，而零空間是一條線。

零空間由所有特殊解的線性組合組成。

在範例 1 中，平面 x + 2y + 3z = 0 有兩個特殊解：

$\begin{bmatrix} 1 & 2 & 3 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = 0$ 有特殊解 $s_1 = \begin{bmatrix} -2 \\ 0 \\ 1 \end{bmatrix}$ 和 $s_2 = \begin{bmatrix} -3 \\ 1 \\ 0 \end{bmatrix}$。

這些向量 $s_1$ 和 $s_2$ 位於平面 x + 2y + 3z = 0，這是矩陣 $\begin{bmatrix} 1 & 2 & 3 \end{bmatrix}$ 的零空間。
所有向量都在這個平面上，是 $s_1$ 和 $s_2$ 的線性組合。
注意，什麼是特殊向量 $s_1$ 和 $s_2$。它們是 1 和 0 的組合，在最後兩個分量中。
這些分量是“自由的”，我們選擇它們。最後兩個分量 -2 和 -3 是由方程式 Ax = 0 決定的。
矩陣 $\begin{bmatrix} 1 & 2 & 3 \end{bmatrix}$ 的第一欄包含樞軸元，因此第一個分量 x 不是自由的。
這八個分量對應於不包含樞軸元的欄位。這種特殊解的描述可以完成，但我們選擇的是自由變數。
特殊解（非零）僅存在於自由變數中。

**範例 3** 描述以下三個矩陣 A、B、C 的零空間：

$A = \begin{bmatrix} 1 & 2 \\ 3 & 8 \end{bmatrix}$, $B = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$, $C = \begin{bmatrix} 1 & 2 & 4 \\ 3 & 8 & 16 \end{bmatrix}$

**解** 方程式 Ax = 0 只有零解 x = 0。零空間是 {Z}。
它只包含單點 x = $\begin{bmatrix} 0 \\ 0 \end{bmatrix}$。這來自消去法：

$\begin{bmatrix} 1 & 2 \\ 3 & 8 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}$ 產生 $\begin{bmatrix} 1 & 2 \\ 0 & 2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$ 和 $\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$。

A 是可逆的。沒有特殊解。A 的所有欄位都是樞軸元。

矩陣 B 具有相同的零空間。第一個方程式 Bx = 0 再次需要 x = 0。
最後兩個方程式變成 0 = 0。
當我們添加額外的方程式時，零空間會變得更大。
自由變數的數量會增加。
矩陣 B 的向量 x = t $\begin{bmatrix} -2 \\ 1 \end{bmatrix}$。

矩陣 C 具有不同的零空間。矩陣 C 的樞軸元是第一和第二欄。
矩陣 C 的向量 x 有一個自由變數。
消去法如下：

$\begin{bmatrix} 1 & 2 & 4 \\ 3 & 8 & 16 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix}$ 產生 $\begin{bmatrix} 1 & 2 & 4 \\ 0 & 2 & 4 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$。

產生 $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 2 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$，因此 $x = 0$ 和 $y + 2z = 0$。
$y = -2z$。
因此，零空間由向量 $\begin{bmatrix} 0 \\ -2 \\ 1 \end{bmatrix}$ 產生，或者說零空間是 span{$\begin{bmatrix} 0 \\ -2 \\ 1 \end{bmatrix}$ }。
