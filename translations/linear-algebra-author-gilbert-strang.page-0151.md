## 148 章 3. 向量空間與子空間

若左側僅保有單位矩陣：

$R\mathbf{x} = \mathbf{0}$ 表示 $\begin{bmatrix} \text{樞軸變數} \\ \text{自由變數} \end{bmatrix} = -F \begin{bmatrix} \text{樞軸變數} \\ \text{自由變數} \end{bmatrix}$ (6)

在每個特殊解中，自由變數為一欄的 $F$。樞軸變數為一欄的 $-F$。這些特殊解給出零空間矩陣 $N$。

這個想法仍然成立，若樞軸變數與自由變數混合在 $N$ 的不同欄中。然後 $I$ 與 $F$ 會被混合在一起。你可以看到 $-F$ 在解中。這裡有一個範例，其中 $I = [1]$ 優先，而 $F = [2 \ 3]$ 接著出現。

**範例 2**  $R\mathbf{x} = x_1 + 2x_2 + 3x_3 = 0$ 的特殊解是 $N$ 的欄：

$R = \begin{bmatrix} 1 & 2 & 3 \end{bmatrix}$,  $N = \begin{bmatrix} -2 & -3 \\ 1 & 0 \\ 0 & 1 \end{bmatrix}$.

這個秩為一。有 $n-r = 3-1 = 2$ 個特殊解 $(-2, 1, 0)$ 與 $(-3, 0, 1)$。

**最終註記**  我如何能確信地寫下 $R$，而不需知道 MATLAB 或 Maple 會如何執行？不同的方法非常相似。Matlab 與 Mathematica 和 Maple 可能會以不同的方式減少。但最終的 $R$ 總是相同的。

原始 $A$ 完全決定了樞軸欄 (包含位置 1 與 0) 與自由欄 (包含 $F$)。

為了證明這是一個“代數方法”——兩個規則與任何特定消去步驟無關。

1. 樞軸欄是早期欄的組合 (不包含樞軸欄的組合)。

2. 自由欄是早期欄的組合 (包含 $F$ 的組合)。

一個小範例，其秩為一，將顯示產生正確 $EA = R$ 的 $E$。

$A = \begin{bmatrix} 2 & 2 \end{bmatrix}$ 減少到 $R = \begin{bmatrix} 1 & 1 \end{bmatrix}$，且沒有其他 $R$。

你可以將 $A$ 的第一列乘以 $\frac{1}{2}$，並從第一列中減去第一列。

兩個步驟給 $E$：
$\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 1/2 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1/2 & 0 \\ -1/2 & 1 \end{bmatrix} = E$.

或者你可以交換 $A$ 的列，然後從第二列中減去第一列的兩倍。

兩個不同的步驟給 $E_{new}$：
$E_{new} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} 1 & -2 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ 1 & -2 \end{bmatrix}$.

乘法給 $EA = R$ 且 $E_{new}A = R$。不同的 $E$ 但相同的 $R$。
