## 2.3. 使用矩陣的消去法 65

**19** 將列交換矩陣依序乘以 P Q 和 Q P，其中
$$P = \begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix} \quad \text{和} \quad Q = \begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$$
找出另一個非對角矩陣，其平方等於單位矩陣 $M^2 = I$。

**20** (a) 假設 $B$ 的所有列都相同。那麼 $EB$ 的所有列也相同，因為每個 $E$ 都是 $E$。
(b) 假設 $B$ 的所有行都為 [1 2 4]。舉例說明 $EB$ 的所有行都為 [1 2 4]。

**21** 如果 $E$ 將第 1 行加到第 2 行，而 $F$ 將第 2 行加到第 1 行，那麼 $EF$ 等於 $FE$ 嗎？

**22** 矩陣 $A$ 和向量 $x$ 的元素分別為 $a_{ij}$ 和 $x_j$。因此，$Ax$ 的第一個分量為 $\sum_{j=1}^n a_{1j}x_j = a_{11}x_1 + \dots + a_{1n}x_n$。如果 $E_{21}$ 從第 2 行減去第 1 行，請寫出一個公式來計算：
(a) 第三個分量
(b) $E_{21}A$ 的 (2, 1) 分量
(c) $E_{21}(E_{21}A)$ 的 (2, 1) 分量
(d) $E_{21}Ax$ 的第一個分量

**23** 消去矩陣 $E = \begin{bmatrix} 1 & 0 \\ -2 & 1 \end{bmatrix}$ 從第 2 行減去第 1 行的 2 倍。結果是 $EA$。那麼 $E(EA)$ 的效果是什麼？以相反的順序 $AE$，我們正在從 $A$ 減去 $B$ 的 2 倍。（舉例說明）

問題 24-27 包含增廣矩陣 [A b] 的列向量 b。

**24** 將消去法應用於 2x3 增廣矩陣 [A b]。求 $Ax = c$ 的解。
$$Ax = \begin{bmatrix} 2 & 3 \\ 4 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 1 \\ 17 \end{bmatrix}$$

**25** 將消去法應用於 3x4 增廣矩陣 [A b]。如何知道該系統有解？將最後的數字 6 換成其他數字，看看該系統是否有解。
$$Ax = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 3 & 4 \\ 3 & 5 & 7 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 6 \end{bmatrix}$$

**26** 方程 $Ax = b$ 和 $Ax = b^*$ 具有相同的矩陣 $A$。什麼時候雙增廣矩陣 $Ax$ 可以用消去法來同時求解兩個方程？
求解以下方程組，使用如下的 A 和 b 矩陣：
$$ \begin{bmatrix} 4 & 1 \\ 8 & 5 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 4 \\ 17 \end{bmatrix} \quad \text{和} \quad \begin{bmatrix} 4 & 1 \\ 8 & 5 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 4 \\ 20 \end{bmatrix}$$
