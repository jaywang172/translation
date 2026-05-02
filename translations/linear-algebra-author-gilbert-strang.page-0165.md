162

在情況 A 中，A 必須有 n = 3 欄。以 (1, 0, 1) 在第四欄的零空間中，第四欄是欄 1 的倍數，因此零空間包含另一個特殊解。因此 A 的秩為 3 - 1 = 2。必要時 A 有 m ≥ 2 列。右側 b 是欄 1 + 欄 2。

在情況 5 中，有無限多個解。零空間包含非零向量。秩 r 必須小於 n (非完全列秩)，且 b 必須在欄空間中。

3.4 C 找到完整的解 x = x<sub>p</sub> + x<sub>n</sub>，透過前向消去 [A b]。

$\begin{bmatrix} 1 & 2 & 1 & 0 \\ 2 & 4 & 4 & 8 \\ 4 & 8 & 6 & 8 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} 4 \\ 2 \\ 10 \end{bmatrix}$

找到數字 y<sub>1</sub>, y<sub>2</sub>, y<sub>3</sub>，使得 y<sub>1</sub> (row 1) + y<sub>2</sub> (row 2) + y<sub>3</sub> (row 3) = zero row。檢查 b = (4, 2, 10) 是否滿足條件 y<sub>1</sub>b<sub>1</sub> + y<sub>2</sub>b<sub>2</sub> + y<sub>3</sub>b<sub>3</sub> = 0。這是此方程式可解且 b 在欄空間中的條件。

解 前向消去 [A b] 產生 [U c]，第三方程式變成 0 = 0，方程式一致且可解：

$\begin{bmatrix} 1 & 2 & 1 & 0 & 4 \\ 2 & 4 & 4 & 8 & 2 \\ 4 & 8 & 6 & 8 & 10 \end{bmatrix} \xrightarrow{} \begin{bmatrix} 1 & 2 & 1 & 0 & 4 \\ 0 & 0 & 2 & 8 & -6 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$

欄 1 和 3 包含樞軸。變數 x<sub>2</sub> 和 x<sub>4</sub> 是自由變數。如果我們將它們設為零，我們可以透過反向代入求解特定解 x<sub>p</sub> = (7, 0, -3, 0)。我們看到 7 - 3 再次以消去方式繼續沿著路徑 [R d]。

$\begin{bmatrix} 1 & 2 & 1 & 0 & 4 \\ 0 & 0 & 2 & 8 & -6 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} \xrightarrow{} \begin{bmatrix} 1 & 2 & 0 & -8 & 7 \\ 0 & 0 & 1 & 4 & -3 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$

零空間的特殊解來自 x<sub>2</sub> = 1, x<sub>4</sub> = 0 和 x<sub>2</sub> = 0, x<sub>4</sub> = 1。

對於 x<sub>2</sub> = 1, x<sub>4</sub> = 0，我們有 2x<sub>2</sub> + x<sub>1</sub> = 7，因此 x<sub>1</sub> = 7 - 2(1) = 5。x<sub>3</sub> + 4x<sub>2</sub> = -3，因此 x<sub>3</sub> = -3 - 4(1) = -7。因此零空間中的特殊解是 x<sub>n1</sub> = (5, 1, -7, 0)。

對於 x<sub>2</sub> = 0, x<sub>4</sub> = 1，我們有 x<sub>1</sub> = 7，x<sub>3</sub> = -3。因此零空間中的特殊解是 x<sub>n2</sub> = (7, 0, -3, 1)。

完整的解是 x = x<sub>p</sub> + c<sub>1</sub>x<sub>n1</sub> + c<sub>2</sub>x<sub>n2</sub> = (7, 0, -3, 0) + c<sub>1</sub>(5, 1, -7, 0) + c<sub>2</sub>(7, 0, -3, 1)。

檢查：
如果 c<sub>1</sub> = c<sub>2</sub> = 0，則 x = (7, 0, -3, 0)。
1(7) + 2(0) + 1(-3) + 0(0) = 7 - 3 = 4
2(7) + 4(0) + 4(-3) + 8(0) = 14 - 12 = 2
4(7) + 8(0) + 6(-3) + 8(0) = 28 - 18 = 10

如果 c<sub>1</sub> = 1, c<sub>2</sub> = 0，則 x = (12, 1, -10, 0)。
1(12) + 2(1) + 1(-10) + 0(0) = 12 + 2 - 10 = 4
2(12) + 4(1) + 4(-10) + 8(0) = 24 + 4 - 40 = -12 ≠ 2。

我們犯了一個錯誤。讓我們重新檢查反向代入。

$\begin{bmatrix} 1 & 2 & 0 & -8 & 7 \\ 0 & 0 & 1 & 4 & -3 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$

x<sub>1</sub> + 2x<sub>2</sub> - 8x<sub>4</sub> = 7
x<sub>3</sub> + 4x<sub>4</sub> = -3

x<sub>1</sub> = 7 - 2x<sub>2</sub> + 8x<sub>4</sub>
x<sub>3</sub> = -3 - 4x<sub>4</sub>

x = $\begin{bmatrix} 7 - 2x_2 + 8x_4 \\ x_2 \\ -3 - 4x_4 \\ x_4 \end{bmatrix} = \begin{bmatrix} 7 \\ 0 \\ -3 \\ 0 \end{bmatrix} + x_2 \begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} + x_4 \begin{bmatrix} 8 \\ 0 \\ -4 \\ 1 \end{bmatrix}$

零空間的基底是 {(-2, 1, 0, 0), (8, 0, -4, 1)}。
