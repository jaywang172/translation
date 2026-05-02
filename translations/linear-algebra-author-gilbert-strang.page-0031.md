## 31

**1.3C 從一個中心差分產生一個差分，改變 C 矩陣。**

將 $C$ 矩陣從一個中心差分轉換為一個差分，產生一個新的矩陣。

$C = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & -2 & 1 \end{bmatrix}$

這個矩陣 $C$ 執行的是 $x_3 - 2x_2 + x_1 = b_1$、$x_2 - 2x_1 = b_2$、$x_1 = b_3$。

我們想要將這個矩陣轉換為一個差分矩陣，它執行的是 $x_3 - x_2 = b_1$、$x_2 - x_1 = b_2$、$x_1 = b_3$。

為了做到這一點，我們需要將 $C$ 矩陣乘以一個矩陣 $E$，使得 $EC$ 執行所需的差分。

$EC = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$

我們需要找到 $E$ 矩陣。

$C = \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & -2 & 1 \end{bmatrix}$

$E = \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix}$

$EC = \begin{bmatrix} a & b & c \\ d & e & f \\ g & h & i \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & -2 & 1 \end{bmatrix} = \begin{bmatrix} a-2b & b-2c & c \\ d-2e & e-2f & f \\ g-2h & h-2i & i \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$

從這個矩陣等式中，我們可以得到以下方程組：

$a - 2b = 1$
$b - 2c = 0$
$c = 0$

$d - 2e = 0$
$e - 2f = 1$
$f = 0$

$g - 2h = 0$
$h - 2i = 0$
$i = 1$

解這個方程組，我們可以得到：

$c = 0$
$b = 2c = 0$
$a = 1 + 2b = 1$

$f = 0$
$e = 1 + 2f = 1$
$d = 2e = 2$

$i = 1$
$h = 2i = 2$
$g = 2h = 4$

因此，$E$ 矩陣是：

$E = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 2 & 1 \end{bmatrix}$

驗證：

$EC = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 2 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ -2 & 1 & 0 \\ 0 & -2 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$

因此，這個矩陣 $E$ 確實將 $C$ 矩陣轉換為一個差分矩陣。
