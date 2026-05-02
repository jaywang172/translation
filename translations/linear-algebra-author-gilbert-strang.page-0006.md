1.1. 向量與線性組合
3

線性組合

將加法與純量乘法結合，我們現在形成 $v$ 與 $w$ 的「線性組合」。將 $v$ 乘以 $c$，將 $w$ 乘以 $d$；然後將 $cv + dw$ 相加。

**定義** $cv$ 和 $dw$ 的和是 $v$ 和 $w$ 的線性組合。

四種特殊的線性組合是：和、差、零以及純量倍數 $cv$：
$1v + 1w = $ 圖 1.1a 中的向量和
$1v - 1w = $ 圖 1.1b 中的向量差
$0v + 0w = $ 零向量
$cv + 0w = $ 沿 $v$ 方向的向量 $cv$

零向量總是一個可能的組合（其係數為零）。每當我們看到一個向量「空間」時，那個零向量都會被包含在內。這種宏觀的視角，包含了 $v$ 和 $w$ 的所有組合，就是線性代數在發揮作用。

這些圖顯示了如何將向量視覺化。對於代數，我們只需要分量（例如 4 和 2）。箭頭向右移動 $v_1 = 4$ 個單位，向上移動 $v_2 = 2$ 個單位。它終止於 $x, y$ 座標為 4, 2 的點。這個點是向量的另一種表示——所以我們有三種方式來描述 $v$：

表示向量 $v$
兩個數字
從 (0, 0) 出發的箭頭
平面中的點

我們使用數字進行加法。我們使用箭頭來視覺化 $v + w$：
**向量加法**（首尾相接） 將 $w$ 的起點放在 $v$ 的終點。
$w = \begin{bmatrix} -1 \\ 2 \end{bmatrix}$
$v$
$w$
$v+w$
$v = \begin{bmatrix} 4 \\ 2 \end{bmatrix}$
2
4
$w = \begin{bmatrix} -1 \\ 2 \end{bmatrix}$
$v$
$v = \begin{bmatrix} 4 \\ 2 \end{bmatrix}$
$v-w$
$-w = \begin{bmatrix} 1 \\ -2 \end{bmatrix}$
5
0

$v + w = \begin{bmatrix} 4 \\ 2 \end{bmatrix} + \begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$
$v - w = \begin{bmatrix} 4 \\ 2 \end{bmatrix} - \begin{bmatrix} -1 \\ 2 \end{bmatrix} = \begin{bmatrix} 5 \\ 0 \end{bmatrix}$

圖 1.1：向量加法 $v + w = (3, 4)$ 產生一個平行四邊形的對角線。右側的線性組合是 $v - w = (5, 0)$。

我們沿著 $v$ 移動，然後沿著 $w$ 移動。或者我們沿著 $v + w$ 走捷徑。我們也可以沿著 $w$ 然後沿著 $v$ 移動。換句話說，$w + v$ 與 $v + w$ 給出相同的答案。
