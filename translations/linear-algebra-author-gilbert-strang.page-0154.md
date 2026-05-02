## 3.3. 秩與行簡化形式 151

**3.3 C** 求行簡化形式 *R* 以及矩陣 *A* 和 *B* 的秩 *r* (這些依賴於 *c*)。哪些是 *A* 的樞軸列？求特殊解以及矩陣 *N*。

求特殊解

$$A = \begin{bmatrix} 1 & 2 & 1 \\ 3 & 6 & 3 \\ 4 & 8 & c \end{bmatrix} \quad \text{and} \quad B = \begin{bmatrix} c & c \\ c & c \end{bmatrix}$$

**解** 矩陣 *A* 的秩為 *r* = 2，若 *c* ≠ 4。樞軸列在第 1 列和第 3 列。第二個變數 *x₂* 是自由變數。注意 *R* 的形式：

$$c \neq 4 \quad R = \begin{bmatrix} 1 & 2 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix} \quad c = 4 \quad R = \begin{bmatrix} 1 & 2 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}$$

兩個樞軸留下一個自由變數 *x₂*。但當 *c* = 4 時，唯一的樞軸在第 1 列 (秩為一)。第二個和第三個變數是自由變數，產生兩個特殊解。

$$c \neq 4 \quad \text{特殊解，當 } x_2 = 1 \text{ 時} \quad N = \begin{bmatrix} -2 \\ 1 \\ 0 \end{bmatrix}$$

$$c = 4 \quad \text{另一個特殊解} \quad N = \begin{bmatrix} -2 \\ -1 \\ 1 \end{bmatrix}$$

矩陣 $$ \begin{bmatrix} c & c \\ c & c \end{bmatrix} $$ 的秩為 *r* = 1，若 *c* ≠ 0。當秩為零時，*c* = 0。

$$c \neq 0 \quad R = \begin{bmatrix} 1 & 1 \\ 0 & 0 \end{bmatrix} \quad \text{and} \quad N = \begin{bmatrix} -1 \\ 1 \end{bmatrix} \quad \text{Nullspace = line}$$

當 *c* = 0 時，矩陣沒有樞軸列。兩個變數都是自由的：

$$c = 0 \quad R = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} \quad \text{and} \quad N = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \quad \text{Nullspace = } \mathbb{R}^2$$

**問題集 3.3**

1.  下列哪一條規則給出了矩陣 *A* 秩的正確定義？

    (a) *R* 中非零列的數量。
    (b) 總列數減去總行數。
    (c) 列數減去自由變數的數量。
    (d) 矩陣 *R* 中 1 的數量。
