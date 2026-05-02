## 62 章節 2. 解線性方程式

**解答** $E_{21}$ 移除第一欄的 4。但 4 在第一欄中再次出現。

$\begin{bmatrix} 1 & 2 & 2 & 1 \\ 4 & 8 & 9 & 3 \\ 0 & 3 & 2 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}$  和  $\begin{bmatrix} 1 & 2 & 2 & 1 \\ 0 & 0 & 1 & -1 \\ 0 & 3 & 2 & 1 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}$

現在 $P_{32}$ 交換第二和第三列。反向代入產生 $z$ 然後 $y$ 和 $x$。

$P_{32} E_{21} \begin{bmatrix} 4 & b \end{bmatrix} = \begin{bmatrix} 1 & 2 & 2 & 1 \\ 0 & 3 & 2 & 1 \\ 0 & 0 & 1 & -1 \end{bmatrix}$  和  $\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix}$

對於一次完成這兩個步驟的矩陣 $P_{32} E_{21}$，將 $P_{32}$ 應用於 $E_{21}$。

**一個矩陣**  $P_{32} E_{21}$ = 交換 $E_{21}$ 的列 = $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ -4 & 1 & 0 \end{bmatrix}$.
**兩個步驟**

## 2.3 C  將這些矩陣以兩種方式相乘。首先，行乘以 $B$ 的欄。其次，欄乘以 $A$ 的行。哪種方式需要兩個矩陣相加到 $AB$？需要多少個獨立的乘法運算？

**兩種方式**

$AB = \begin{bmatrix} 3 & 4 \\ 1 & 5 \\ 2 & 0 \end{bmatrix} \begin{bmatrix} 2 & 4 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 10 & 16 \\ 7 & 9 \\ 4 & 8 \end{bmatrix}$

**解答** 行乘以 $A$ 的欄是向量的點積：

(row 1) • (column 1) = $\begin{bmatrix} 3 & 4 \end{bmatrix} \begin{bmatrix} 2 \\ 1 \end{bmatrix} = 10$ 是 $AB$ 的 (1,1) 入口。

(row 2) • (column 1) = $\begin{bmatrix} 1 & 5 \end{bmatrix} \begin{bmatrix} 2 \\ 1 \end{bmatrix} = 7$ 是 $AB$ 的 (2,1) 入口。

我們需要 6 個點積，每個點積 2 個乘法，總共 12 個 (3 • 2 • 2)。相同的 $AB$ 來自欄乘以 $A$ 的行，一個欄是一個矩陣。

$AB = \begin{bmatrix} 3 \\ 1 \\ 2 \end{bmatrix} \begin{bmatrix} 2 & 4 \end{bmatrix} + \begin{bmatrix} 4 \\ 5 \\ 0 \end{bmatrix} \begin{bmatrix} 1 & 1 \end{bmatrix} = \begin{bmatrix} 6 & 12 \\ 2 & 4 \\ 4 & 8 \end{bmatrix} + \begin{bmatrix} 4 & 4 \\ 5 & 5 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 10 & 16 \\ 7 & 9 \\ 4 & 8 \end{bmatrix}$
