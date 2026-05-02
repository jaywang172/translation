## 1.3. 矩陣 23

這裡有一個關於數列差異的例子（x 中的平方數，b 中的奇數）：

\[
x = \begin{bmatrix} 1 \\ 4 \\ 9 \end{bmatrix} \text{ squares} \quad Ax = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 1 \\ 4-1 \\ 9-4 \end{bmatrix} = \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} = b.
\]

這個模式會繼續形成一個 4x4 的差異矩陣。下一個平方數將是 16。下一個差異將是 x₄ - x₃ = 16 - 9 = 7（這是一個奇數）。這個矩陣同時會顯示所有差異。

**重要提示：** 您可能已經學會了如何將 Ax 乘以向量。可能以不同的方式解釋，使用行而不是列。通常，我們採用點積的方式計算 row with x：

**使用行計算點積**
\[
Ax = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} (1,0,0) \cdot (x_1, x_2, x_3) \\ (-1,1,0) \cdot (x_1, x_2, x_3) \\ (0,-1,1) \cdot (x_1, x_2, x_3) \end{bmatrix}
\]

這些點積與在等式 (4) 中我們寫的 x₁ 和 x₂ - x₁ 和 x₃ - x₂ 相同。新的方法是將 Ax 視為對一個向量進行線性變換。線性變換的關鍵在於，輸出 Ax 是列的線性組合。

使用數字，我們可以將 Ax 乘以向量（我將在後續使用 row）。使用字母，列是好的方式。第 2 章將重複這些矩陣乘法的規則，並解釋底層的想法。我們將會使用矩陣同時處理兩者。

## 線性方程式

觀點上的轉變至關重要。到目前為止，數字 x₁, x₂, x₃ 都是已知的（最初 c, d, e）。現在右側 b 未知。我們發現向量的差異是由乘以 A 的 x₁、x₂、x₃ 得到的。我們現在知道 b，並尋找 x。

**舊問題：** 計算線性組合 x₁ + x₂x + x₃w 以找到 b。
**新問題：** 哪個 x, u, v 的組合可以產生特定的向量 b？

這是逆問題——找到輸入 x 給定輸出 b。您可能已經看到這是一個線性方程式的系統，右側是 x₁, x₂, x₃。我們想要解決這個系統以找到 x₁, x₂, x₃。

\[
Ax = b \quad \Rightarrow \quad
\begin{cases}
x_1 = b_1 \\
x_1 + x_2 = b_2 \\
x_1 + x_2 + x_3 = b_3
\end{cases}
\quad \text{Solution} \quad
\begin{cases}
x_1 = b_1 \\
x_2 = b_2 - b_1 \\
x_3 = b_3 - b_2
\end{cases}
\]

這個解決方案只對 Ax = b 的特定 A 有效。為了找到 x，我們需要做什麼？
**The first equation gives x₁ = b₁. The second equation gives x₂ = b₂ - b₁. The last equation gives x₃ = b₃ - b₂.**
