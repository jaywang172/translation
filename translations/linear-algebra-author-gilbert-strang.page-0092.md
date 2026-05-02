## 2.5. 反矩陣

**問題集 2.5**

**1** 求矩陣 A、B、C 的反矩陣（直接使用 2x2 公式或從頭計算）：

$A = \begin{bmatrix} 3 & 1 \\ 4 & 0 \end{bmatrix}$  和  $B = \begin{bmatrix} 2 & 0 \\ 4 & 2 \end{bmatrix}$  和  $C = \begin{bmatrix} 3 & 4 \\ 5 & 7 \end{bmatrix}$.

**2** 對於這些“置換矩陣”，通過試錯（使用 1 和 0）找到 $P^{-1}$：

$P = \begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}$  和  $P = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{bmatrix}$.

**3** 解 $A^{-1}$ 的第一列 (x, y) 和第二列 (z, t)：

$\begin{bmatrix} 10 & 20 \\ 20 & 50 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$  和  $\begin{bmatrix} 10 & 20 \\ 20 & 50 \end{bmatrix} \begin{bmatrix} z \\ t \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$.

**4** 證明 $\begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix}$ 不可逆，通過求解 $AA^{-1} = I$ 的第一列 $A^{-1}$。
(對於不同的 A，能否找到 $A^{-1}$ 的第一列？)

**5** 找到一個上三角矩陣（對角線以上為 0）使得 $U^2 = I$，其中 I 為單位矩陣。

**6** (a) 如果 A 可逆且 $AB = AC$，快速驗證 $B = C$。
(b) 如果 $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$，找到兩個不同的矩陣使得 $AB = AC$。

**7** (重要) 如果 A 有第 1 行 + 第 2 行 = 第 3 行，證明 A 不可逆：

(a) 說明為什麼 $Ax = (1, 0, 0)$ 沒有解。
(b) 右側向量 $(b_1, b_2, b_3)$ 可能允許解 $Ax = b$？
(c) 在消元法中會發生什麼？

**8** 如果 A 具有第 1 列 + 第 2 列 = 第 3 列，證明 A 不可逆：

(a) 找到一個非零解 $Ax = 0$。矩陣為 3x3。
(b) 消元法保持第 1 列 + 第 2 列 = 第 3 列。說明為什麼沒有主變量。

**9** 假設 A 可逆，並且你交換了它的第一行和第二行來得到 B。B 是可逆矩陣嗎？如何找到 $B^{-1}$ 從 $A^{-1}$？

**10** 找到反矩陣（以任何合法方式）：

$A = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 3 & 0 \\ 0 & 3 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}$  和  $B = \begin{bmatrix} 3 & 2 & 0 & 0 \\ 4 & 3 & 0 & 0 \\ 0 & 0 & 5 & 6 \\ 0 & 0 & 7 & 5 \end{bmatrix}$.
