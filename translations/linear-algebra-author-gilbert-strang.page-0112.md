## 2.7. 轉置與排列

**範例 2** 從 $A = \begin{bmatrix} 1 & 1 & 0 \\ -1 & 1 & 0 \end{bmatrix}$ 開始，以及 $x = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$， $y = \begin{bmatrix} y_1 \\ y_2 \end{bmatrix}$。

在這一側我們有 $Ax$ 乘以 $y$：$(x_2 - x_1)y_1 + (x_3 - x_2)y_2$。 這一邊與 $x_1(y_1 - y_2) + x_2(y_1 - y_2) + x_3(y_2)$ 相同。現在我們正在將 $A^T y$ 乘上。

$A^T y$ 必須是 $\begin{bmatrix} -y_1 \\ y_1 - y_2 \\ y_2 \end{bmatrix}$，這與我們預期的一樣，因為 $A^T = \begin{bmatrix} 1 & -1 & 0 \\ 1 & 1 & 0 \end{bmatrix}$。

**範例 3**  你會允許我使用一點微積分嗎？它有多重要？我不會離開線性代數。（導數是 $A = d/dt$ 的線性代數形式，對於函數 $x(t)$。） 差分會從 $dx/dt$ 變為 $(x, -dy/dt)$。

內積從有限和 $\sum x_i y_i$ 變為積分 $\int x(t)y(t) dt$。

**函數的內積**  $x^T y = (x, y) = \int x(t) y(t) dt$  定義如下。

**轉置規則**  $(Ax)^T y = x^T A^T y$

$\int_{-\infty}^{\infty} x(t) y'(t) dt = x(t) \left( -\frac{dy}{dt} \right) \Big|_{-\infty}^{\infty}$  顯示 $A^T$ (6)

我希望你認可“分部積分”。導數從第一個函數 $x(t)$ 移動到第二個函數 $y(t)$。這表示轉置“導數”是微積分的最小值。

導數是反對稱的；$A = d/dt$ 且 $A^T = -d/dt$。對稱矩陣有 $A^T = A$，反對稱矩陣有 $A^T = -A$。在某種程度上，2x3 差分矩陣遵循這種模式。3x2 矩陣 $A^T$ 減去一個 2x2 差分矩陣。它產生 $y_1 - y_2$ 在中間成分。

**對稱矩陣**

對於對稱矩陣，轉置 $A$ 到 $A^T$ 不會產生任何變化。因此 $A^T = A$。Its (j,i) entry across the main diagonal equals its (i,j) entry。在我的觀點中，這些是矩陣中最重要的屬性。

**定義** 一個對稱矩陣的其元素是 $a_{ij} = a_{ji}$。這表示 $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ 且 $D = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = I$。

**對稱矩陣**  一個對稱矩陣 $A$ 的逆矩陣 $A^{-1}$ 也是對稱矩陣。例如，如果 $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$，則 $A^{-1} = \begin{bmatrix} -2 & 1 \\ 1 & -1/2 \end{bmatrix}$ 也是對稱的。

**反對稱矩陣**  一個反對稱矩陣 $A$ 的逆矩陣 $A^{-1}$ 也是反對稱矩陣。例如，如果 $A = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$，則 $A^{-1} = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$ 也是反對稱的。
