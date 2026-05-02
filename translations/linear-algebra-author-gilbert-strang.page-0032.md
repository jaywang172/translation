## 1.3. 矩陣

**問題集 1.3**

**1** 找出線性組合 $2\mathbf{s}_1 + 3\mathbf{s}_2 + 4\mathbf{s}_3 = \mathbf{b}$。然後將 $\mathbf{b}$ 寫成矩陣-向量乘積 $S\mathbf{x}$。計算 $\mathbf{S}$ 的列向量的點積（行向量）。

$\mathbf{s}_1 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$, $\mathbf{s}_2 = \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$, $\mathbf{s}_3 = \begin{bmatrix} 0 \\ 1 \\ 1 \end{bmatrix}$ 構成 $\mathbf{S}$ 的列向量。

**2** 解這些方程式 $S\mathbf{y} = \mathbf{b}$，其中 $\mathbf{b}$ 是 $\mathbf{s}_1$, $\mathbf{s}_2$, $\mathbf{s}_3$ 的列向量 $\mathbf{S}$：

$\begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} y_1 \\ y_2 \\ y_3 \end{bmatrix} = \begin{bmatrix} 1 \\ 4 \\ 9 \end{bmatrix}$

前 $n$ 個奇數的和是。

**3** 解這三個方程式，以 $y_1$, $y_2$, $y_3$ 表示 $B_1$, $B_2$, $B_3$：

$S\mathbf{y} = \mathbf{B}$，其中 $\begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix} \begin{bmatrix} y_1 \\ y_2 \\ y_3 \end{bmatrix} = \begin{bmatrix} B_1 \\ B_2 \\ B_3 \end{bmatrix}$。

將解 $\mathbf{y}$ 寫成 $A^{-1}$ 乘以向量 $\mathbf{B}$。$\mathbf{S}$ 的列向量是獨立的還是相依的？

**4** 找出一個組合 $x_1\mathbf{w}_1 + x_2\mathbf{w}_2 + x_3\mathbf{w}_3$ 得到零向量：

$\mathbf{w}_1 = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$, $\mathbf{w}_2 = \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}$, $\mathbf{w}_3 = \begin{bmatrix} 7 \\ 8 \\ 9 \end{bmatrix}$。

這些向量是（獨立的）(相依的)。這三個向量位於一個。矩陣 $\mathbf{W}$ 具有三個列向量，且不可逆。

**5** 矩陣 $\mathbf{r}_1$, $\mathbf{r}_2$, $\mathbf{r}_3$ 的行向量產生三個向量（我將它們寫成列向量）：

$\mathbf{r}_1 = \begin{bmatrix} 1 \\ 4 \\ 7 \end{bmatrix}$, $\mathbf{r}_2 = \begin{bmatrix} 2 \\ 5 \\ 8 \end{bmatrix}$, $\mathbf{r}_3 = \begin{bmatrix} 3 \\ 6 \\ 9 \end{bmatrix}$。

線性代數表明這些向量也必須位於一個平面上。存在許多組合 $y_1\mathbf{r}_1 + y_2\mathbf{r}_2 + y_3\mathbf{r}_3 = 0$。找出兩個這樣的 $\mathbf{y}$ 集合。

**6** 哪些值 $c$ 會使列相依（組合等於零）？

$\begin{bmatrix} 1 & 3 & 5 \\ 1 & 2 & 4 \\ 1 & c & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ 0 \end{bmatrix} = \begin{bmatrix} c \\ 2 \\ 1 \end{bmatrix}$, $\begin{bmatrix} 1 & 3 & 5 \\ 1 & 2 & 4 \\ 1 & c & 1 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix} = \begin{bmatrix} 5 \\ 3 \\ 6 \end{bmatrix}$。
