## 74 第 2 章：解線性方程式

**2.4 B** 對於這些矩陣，何時 $AB = BA$? 何時 $BC = CB$? 何時 $BC$ 乘以 $AB$ 等於 $A$ 乘以 $C$? 說明其進入 $p, q, r, z$ 的條件。

$A = \begin{bmatrix} p & q \\ r & z \end{bmatrix}$, $B = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$, $C = \begin{bmatrix} 0 & z \\ 0 & 0 \end{bmatrix}$

如果 $p, q, r, z$ 是 4x4 的數值區塊，答案會改變。

**解答** 首先， $AB$ 總是等於 $BA$ 的時機。括號並不必要在 $A(BC) = (AB)C = ABC$ 中，但我們必須按照此順序執行：

通常 $AB \neq BA$
$AB = \begin{bmatrix} p & q \\ r & z \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} p & p+q \\ r & r+z \end{bmatrix}$
$BA = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} p & q \\ r & z \end{bmatrix} = \begin{bmatrix} p+r & q+z \\ r & z \end{bmatrix}$

藉由 $BC = CB$
$BC = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & z \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & z \\ 0 & 0 \end{bmatrix}$
$CB = \begin{bmatrix} 0 & z \\ 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & z \\ 0 & 0 \end{bmatrix}$

$B$ 和 $C$ 能夠交換律的部分解釋在於 $B$ 的對角線是 1，而 $B$ 與 $C$ 交換律發生在 2x2 矩陣中。當 $p, q, r, z$ 是 4x4 的數值區塊且 1 出現在 $I$ 中，所有這些乘積都是正確的。答案是相同的。

**2.4 C** 一個連通圖形從 $n$ 個節點開始。其 $n$ x $n$ 相鄰矩陣定義為 $a_{ij} = 1$ 當且僅當邊從節點 $i$ 離開並進入節點 $j$；如果沒有邊則 $a_{ij} = 0$。

[圖：節點 1 到節點 2，節點 1 到節點 1，節點 2 到節點 2]
$A = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$ = 相鄰矩陣

計數 $A^2$ 的 $i, j$ 進入項 $a_{ik}a_{kj}$。這是 $a_{i1}a_{1j} + \dots + a_{in}a_{nj}$。為什麼這計算了從節點 $i$ 到節點 $j$ 的兩步路徑？ $A^k$ 的 $i, j$ 進入項計算了 $k$ 步路徑。

$\begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}^2 = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}$  計算了具有 **兩條邊** 的路徑：[1 到 2 到 1, 1 到 1 到 1, 2 到 1 到 2]

列出所有從節點之間的三步路徑並與 $A^3$ 比較。

**解答** 數字 $a_{ik}a_{kj}$ 將會是 “1” 如果從節點 $i$ 到節點 $k$ 有一條邊，並且從節點 $k$ 到節點 $j$ 有一條邊。這是一個兩步路徑。數字 $a_{ik}a_{kj}$ 將會是 “0” 如果任何一條邊缺失（從 $i$ 到 $k$ 或從 $k$ 到 $j$）。因此， $a_{ik}a_{kj}$ 是兩步路徑的數量從節點 $i$ 到節點 $j$。矩陣乘法是 $a_{ik}a_{kj}$ 的總和。
