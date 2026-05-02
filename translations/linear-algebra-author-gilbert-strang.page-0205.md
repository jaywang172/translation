202                                                                                    第 4 章 正交性

(c) 另外請找出一條與 $P$ 垂直的直線 $P^\perp$ 的基底。

(d) 將 $v = (6, 4, 5)$ 分解為其在 $P$ 中的零空間分量 $v_n$ 以及其在 $P^\perp$ 中的列空間分量 $v_r$。

**解答**

(a) 方程式 $x - 3y - 4z = 0$ 可表示為 $Ax = 0$，其中 $A$ 為 $1 \times 3$ 矩陣 $A = [1 \ -3 \ -4]$。

(b) 第 2 行與第 3 行是自由的（唯一的主元是 1）。當自由變數分別為 1 和 0 時，在平面 $P = N(A)$ 中的特解為 $s_1 = (3, 1, 0)$ 與 $s_2 = (4, 0, 1)$。

(c) $A$ 的列空間是方向為列向量 $z = (1, -3, -4)$ 的直線 $P^\perp$。

(d) 若要將 $v$ 分解為 $v_n + v_r = (c_1s_1 + c_2s_2) + c_3z$，解得 $c_1 = 1, c_2 = 1, c_3 = -1$。

$$\begin{bmatrix} 6 \\ 4 \\ 5 \end{bmatrix} = \begin{bmatrix} 3 & 4 & 1 \\ 1 & 0 & -3 \\ 0 & 1 & -4 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix} \begin{matrix} v_n = s_1 + s_2 = (7, 1, 1) \text{ 位於 } P = N(A) \\ v_r = -s_3 = (-1, 3, 4) \text{ 位於 } P^\perp = C(A^T) \\ v = (6, 4, 5) \text{ 等於 } (7, 1, 1) + (-1, 3, 4) \end{matrix}$$

此方法將每個子空間的基底合併為一個總基底 $s_1, s_2, z$。第 4.2 節也將探討將 $v$ 投影到子空間 $S$。在那裡，我們將不需要垂直子空間 $S^\perp$ 的基底。

**習題集 4.1**

問題 1–12 是基於包含四個子空間的圖 4.2 與 4.3 延伸而來。

1. 構造任意一個秩（rank）為 1 的 $2 \times 3$ 矩陣。複製圖 4.2 並在每個子空間中放入一個向量（零空間中放入兩個）。哪些向量是正交的？

2. 為一個秩 $r = 2$ 的 $3 \times 2$ 矩陣重新繪製圖 4.3。哪個子空間是 $Z$（僅含零向量）？$\mathbb{R}^2$ 中任意向量 $x$ 的零空間部分為 $x_n = \text{__________}$。

3. 構造具有要求屬性的矩陣，或說明為何不可能：

    (a) 行空間包含 $\begin{bmatrix} 1 \\ 2 \\ -3 \end{bmatrix}$ 和 $\begin{bmatrix} 2 \\ -3 \\ 5 \end{bmatrix}$，零空間包含 $\begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$

    (b) 列空間包含 $\begin{bmatrix} 1 \\ 2 \\ -3 \end{bmatrix}$ 和 $\begin{bmatrix} 2 \\ -3 \\ 5 \end{bmatrix}$，零空間包含 $\begin{bmatrix} 1 \\ 0 \\ 1 \end{bmatrix}$

    (c) $Ax = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}$ 有解，且 $A^T \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$

    (d) 每一列都與每一行正交（$A$ 不是零矩陣）

    (e) 各行相加為零向量，各列相加為 1 的向量。

4. 若 $AB = 0$，則 $B$ 的各行位於 $A$ 的 $\text{__________}$ 中。$A$ 的各列位於 $B$ 的 $\text{__________}$ 中。為什麼 $A$ 和 $B$ 不能都是秩為 2 的 $3 \times 3$ 矩陣？
