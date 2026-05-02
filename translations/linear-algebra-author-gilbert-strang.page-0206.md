4.1. 四個子空間的正交性 $\quad$ 203

5 $\quad$ (a) 如果 $Ax = b$ 有解且 $A^T y = 0$，那麼是 $(y^T x = 0)$ 還是 $(y^T b = 0)$？
$\quad$ (b) 如果 $A^T y = (1, 1, 1)$ 有解且 $Ax = 0$，那麼 \_\_\_\_\_\_。

6 $\quad$ 這個方程式系統 $Ax = b$ 沒有解（它們會導致 $0 = 1$）：
$\quad \quad \quad \quad \quad \quad \quad \quad x + 2y + 2z = 5$
$\quad \quad \quad \quad \quad \quad \quad \quad 2x + 2y + 3z = 5$
$\quad \quad \quad \quad \quad \quad \quad \quad 3x + 4y + 5z = 9$

$\quad$ 找出數字 $y_1, y_2, y_3$ 用以乘上這些方程式，使它們相加等於 $0 = 1$。你找到的向量 $y$ 在哪個子空間中？它的點積 $y^T b$ 是 1，因此沒有解 $x$。

7 $\quad$ 每個沒有解的系統都像問題 6 中的那樣。存在數字 $y_1, \dots, y_m$ 可乘上這 $m$ 個方程式，使它們相加等於 $0 = 1$。這被稱為弗雷德霍姆替代定理 (Fredholm's Alternative)：

$\quad \quad \quad \quad \quad \quad \quad$ **這兩個問題中恰好只有一個有解**
$\quad \quad \quad \quad \quad \quad \quad \quad Ax = b \quad \textbf{或} \quad A^T y = 0$ 且 $y^T b = 1$。

$\quad$ 如果 $b$ 不在 $A$ 的欄空間中，它就與 $A^T$ 的零空間不正交。將方程式 $x_1 - x_2 = 1$、$x_2 - x_3 = 1$ 以及 $x_1 - x_3 = 1$ 乘上選定的數字 $y_1, y_2, y_3$，使得這些方程式相加等於 $0 = 1$。

8 $\quad$ 在圖 4.3 中，我們如何知道 $Ax_r$ 等於 $Ax$？我們如何知道這個向量在欄空間中？如果 $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$ 且 $x = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$，那麼 $x_r$ 是什麼？

9 $\quad$ 如果 $A^T Ax = 0$ 則 $Ax = 0$。原因：$Ax$ 在 $A^T$ 的零空間中，同時也在 $A$ 的 \_\_\_\_\_\_ 中，而這些空間是 \_\_\_\_\_\_。結論：$A^T A$ 與 $A$ 具有相同的零空間。這個關鍵事實將在下一節中重複提及。

10 $\quad$ 假設 $A$ 是一個對稱矩陣 ($A^T = A$)。
$\quad \quad$ (a) 為什麼它的欄空間與其零空間垂直？
$\quad \quad$ (b) 如果 $Ax = 0$ 且 $Az = 5z$，哪些子空間包含這些「特徵向量」$x$ 和 $z$？對稱矩陣具有垂直的特徵向量 $x^T z = 0$。

11 $\quad$ (推薦) 繪製圖 4.2 以正確顯示以下矩陣的每個子空間：
$\quad \quad \quad \quad \quad \quad \quad \quad A = \begin{bmatrix} 1 & 2 \\ 3 & 6 \end{bmatrix} \quad \text{以及} \quad B = \begin{bmatrix} 1 & 0 \\ 3 & 0 \end{bmatrix}$。

12 $\quad$ 找出分量 $x_r$ 與 $x_n$，並在下列條件下正確繪製圖 4.3：
$\quad \quad \quad \quad \quad \quad \quad \quad A = \begin{bmatrix} 1 & -1 \\ 0 & 0 \\ 0 & 0 \end{bmatrix} \quad \text{以及} \quad x = \begin{bmatrix} 2 \\ 0 \end{bmatrix}$。
