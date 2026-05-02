## 108 章 2. 解線性方程式

正確答案 $BT$ 依列運算出一列。這裡的數字來自 $(AB)^T = B^T A^T$。

$AB = \begin{bmatrix} 1 & 5 \\ 0 & 9 \end{bmatrix} \begin{bmatrix} 5 & 0 \\ 1 & 1 \end{bmatrix}$ 且 $B^T A^T = \begin{bmatrix} 5 & 4 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 1 & 5 \\ 0 & 9 \end{bmatrix} = \begin{bmatrix} 5 & 9 \\ 0 & 1 \end{bmatrix}$。

反轉順序規則也適用於三個或更多個因子：$(ABC)^T = C^T B^T A^T$。

若 $A = LDU$ 則 $A^T = U^T D^T L^T$。樞軸矩陣 Has $D = D^T$。

現在將此乘積規則應用到 $A^T A = I$ 上。如果 $A^T$ 是 $I$ 的反矩陣，我們確認這個規則是正確的，因為它們產生的結果是 $I$。

**反矩陣的轉置** $A^{-1} A = I$ 被轉置為 $A^T (A^{-1})^T = I$。（5）

類似地，$AA^{-1} = I$ 導向 $(A^{-1})^T A^T = I$。我們恰好可以轉置反矩陣。請注意，特別是，$A^T$ 是可逆的，如果且僅如果 $A$ 是可逆的。

**範例 1**  $A = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$ 的 $A^{-1} = \begin{bmatrix} 0 & 1 \\ 1 & -1 \end{bmatrix}$。$A^T = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix}$。

$(A^{-1})^T$ 和 $(A^T)^{-1}$ 兩者都等於 $\begin{bmatrix} 0 & 1 \\ 1 & -1 \end{bmatrix}$。

## 內積的意義

我們知道 $x$ 和 $y$ 的點積（內積）是 $x_i y_i$ 的總和。現在我們有一個更好的方式來寫 $x \cdot y$，而無需使用未經專業訓練的點。使用矩陣表示法代替：

$T$ 在內側 **點積或內積** 是 $x^T y$  $(1 \times n)(n \times 1)$

$T$ 在外側 **秩一矩陣或外積** 是 $xy^T$  $(n \times 1)(1 \times n)$

$x^T y$ 是一個數字，$xy^T$ 是一個矩陣。量子力學會將其寫成 $\langle x | y \rangle$（內積）和 $|x \rangle \langle y |$（外積）。我認為世界是由數學支配的，物理學掩蓋了其背後的數學意義。以下是一些內積具有意義的例子：

| 從機械 | 工作 = (位移)(力) = $x^T f$ |
|---|---|
| 從電路 | 熱損失 = (電壓降)(電流) = $e^T y$ |
| 從經濟學 | 收入 = (數量)(價格) = $q^T p$ |

我們正在接近應用數學的核心，並且還有一個更深入的解釋。內積和轉置之間存在更深層次的聯繫。

我們定義 $A^T$ 通過翻轉主對角線上的矩陣來獲得。這不是數學，而是我們獲得 $A^T$ 的一種方式。$A^T$ 的矩陣表示這些內積提供了另一種方法：

$(A x)^T y = x^T A^T y$  **內積交換**  $x^T (A^T y) = (A x)^T y$ **內積交換律**
