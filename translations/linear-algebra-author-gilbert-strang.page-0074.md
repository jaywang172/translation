## 2.4 矩陣運算規則 71

**例題 3 (重要特殊情況)** 令 *A* 的區塊有 *m* 行，*B* 的區塊有 *n* 行。則區塊乘法 *AB* 將各區塊的列數相加：

列數
乘以
行數
$\begin{bmatrix} a_1 & \cdots & a_n \\ \end{bmatrix} \begin{bmatrix} b_1 \\ \vdots \\ b_n \end{bmatrix} = a_1 b_1 + \cdots + a_n b_n$ (2)

這也是計算矩陣乘積的一種方式。將 *A* 的第一行與 *B* 的第一列相乘，得到一個數值（而非單一數字）。考慮以下例子：

$\begin{bmatrix} 1 & 4 & 3 & 2 \\ 1 & 5 & 1 & 0 \end{bmatrix} = \begin{bmatrix} 1 & 1 \end{bmatrix} \begin{bmatrix} 3 \\ 2 \end{bmatrix} + \begin{bmatrix} 4 & 1 \end{bmatrix} \begin{bmatrix} 5 \\ 0 \end{bmatrix}$

Column 1 times row 1
+ Column 2 times row 2
$= \begin{bmatrix} 3 & 2 \end{bmatrix} + \begin{bmatrix} 4 & 0 \end{bmatrix} = \begin{bmatrix} 7 & 2 \end{bmatrix}$ (3)

我們停止將 *A* 視為由列組成的乘法矩陣。如果 *A* 是 2x1 矩陣（一個列矩陣），而 *B* 是 2x2 矩陣，則結果是 2x2。點積是內積（這些是結果的 2 個數值）。頂端左角的數值是 3 + 4 = 7。這與 (1,4) 與 (3,1) 的行-列點積相符。

總結：通常，行數乘以列數，給出整個矩陣的點積數（8 個乘法）。新的方式，列數乘以列數，給出兩個滿矩陣（相同的 8 個乘法）。這 8 個乘法，以及這 4 個加法，只是以不同的順序執行。

**例題 4 (消除由區塊)** 假設第一個矩陣 *A* 包含 1, 3, 4。要將 3 和 4 消除到 0，乘以主元 3 和 4 並相減。這些運算實際上是乘以消除矩陣 $E_{21}$ 和 $E_{31}$：

One at a time
$E_{21} = \begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$ and $E_{31} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ -4 & 0 & 1 \end{bmatrix}$

“區塊想法”是將矩陣 *E* 與一個矩陣 *A* 相乘。該矩陣 *E* 清除主元為 1 的第一列。

$E = \begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ -4 & 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & x & x \\ 3 & x & x \\ 4 & x & x \end{bmatrix} = \begin{bmatrix} 1 & x & x \\ 0 & x & x \\ 0 & x & x \end{bmatrix}$

使用反矩陣，對於 2.5，一個區塊矩陣 *E* 可以通過消除整個 (block) 列來獲得 *A*。假設 *A* 有四個區塊 $\begin{bmatrix} I & x \\ 0 & x \end{bmatrix}$。 匹配如下，則 *E* 將會是：

$\begin{bmatrix} I & 0 \\ C & D \end{bmatrix}^{-1} = \begin{bmatrix} I & 0 \\ -C D^{-1} & D^{-1} \end{bmatrix}$ (4)

這個公式適用於更大的矩陣，只要 *D* 可以反轉。為了使 *A* 變成上三角矩陣，我們需要 *C* = 0。
