## 22 章節 1. 向量導論

### 1.3 矩陣

本節基於兩個精心選擇的例子。我將使用三個向量 **u**、**v** 和 **w**，並使用矩陣來表示它們的組合。第一個例子中的三個向量如下：

**第一個例子**
$\mathbf{u} = \begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}$, $\mathbf{v} = \begin{bmatrix} 0 \\ 1 \\ -1 \end{bmatrix}$, $\mathbf{w} = \begin{bmatrix} 0 \\ 0 \\ -1 \end{bmatrix}$

它們在三維空間中的線性組合是 $cu + dv + ew$：

**組合**
$c \begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix} + d \begin{bmatrix} 0 \\ 1 \\ -1 \end{bmatrix} + e \begin{bmatrix} 0 \\ 0 \\ -1 \end{bmatrix} = \begin{bmatrix} c \\ -c+d \\ -d-e \end{bmatrix}$ (1)

現在重要的事情來了：用矩陣的形式重寫這個組合。向量 **u**、**v**、**w** 進入矩陣 **A** 的列，該矩陣“乘以”一個向量：

**相同的組合現在是 A 乘以 x**
$\begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & -1 \end{bmatrix} \begin{bmatrix} c \\ d \\ e \end{bmatrix} = \begin{bmatrix} c \\ -c+d \\ -d-e \end{bmatrix}$ (2)

數值 $c$、$d$、$e$ 是向量 **x** 的分量。矩陣 **A** 乘以向量 **x** 等於 **x** 的三個列向量的組合 $cu + dv + ew$。

**矩陣乘以向量**
$Ax = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & -1 \end{bmatrix} \begin{bmatrix} c \\ d \\ e \end{bmatrix} = cu + dv + ew$. (3)

這不僅僅是 $Ax$ 的定義，因為重寫帶來了觀點上的重大變化。一開始，數值 $c$、$d$、$e$ 是乘以向量的。現在矩陣是乘以這些數值。矩陣 **A** 作用於向量 **x**。結果 $Ax$ 是 **x** 的列向量的組合 $b_1$、$b_2$、$b_3$。

為了表示這個動作，我將使用 $x_1$、$x_2$、$x_3$ 代替 $c$、$d$、$e$。我將用字母 $b_1$、$b_2$、$b_3$ 表示 **A** 的分量。

$Ax = \begin{bmatrix} 1 & 0 & 0 \\ -1 & 1 & 0 \\ 0 & -1 & -1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} x_1 \\ -x_1+x_2 \\ -x_2-x_3 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}$. (4)

輸入是 **x**，輸出是 **b** = $Ax$。這個矩陣“差分”運算式包含輸入向量 **x** 的差。頂部的差是 $x_1 - x_0 = x_1 - 0$。
