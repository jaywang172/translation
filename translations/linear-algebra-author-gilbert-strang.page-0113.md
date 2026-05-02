## 110
### 第 2 章：解線性方程組

**對稱積 $R^TR$ 與 $LDL^T$**

選擇任何矩陣 $R$，可能為矩形。將 $R^T$ 乘以 $R$。則乘積 $R^TR$ 是一個自動對稱的方陣：

The transpose of $R^TR$ is $(R^TR)^T$ which is $R^T(R^T)^T = R^TR$. (7)

這是一個快速驗證 $R^TR$ 對稱性的方法。我們可以觀察到 $(i, j)$ 入口是 $R^TR$ 的點積，即第 $i$ 列的 $R^T$ (第 $i$ 列的 $R$ 的列) 與第 $j$ 列的 $R$ 的點積。因此，第 $(j, i)$ 入口是相同的，所以 $R^TR$ 是對稱的。

矩陣 $RR^T$ 也是對稱的。（$R$ 和 $R^T$ 的形狀允許矩陣乘法。）但 $RR^T$ 是一個與矩陣 $R$ 的形狀不同的矩陣，而 $R^TR$ 則不然。在科學計算中，我們經常從一個矩形矩陣 $R$ 結束，或在最小二乘法中，使用 $R^T R$ 或 $RR^T$ 中的一個。

**例題 4** 設 $R = \begin{bmatrix} 2 & -1 \\ 1 & 0 \end{bmatrix}$ 和 $R^T = \begin{bmatrix} 2 & 1 \\ -1 & 0 \end{bmatrix}$ 在兩者中。

$R^TR = \begin{bmatrix} 5 & 2 \\ 2 & 1 \end{bmatrix}$ 和 $RR^T = \begin{bmatrix} 5 & -2 \\ -2 & 1 \end{bmatrix}$ 都是對稱矩陣。

乘積 $R^TR$ 是 $n \times n$。在相反的順序中，$RR^T$ 是 $m \times m$。兩者都是對稱的，具有正對角線元素（為什麼？）。但如果 $m \neq n$，則它們不一定是 $R^TR = RR^T$。等式可能成立，但它是不正常的。

**對稱矩陣的消去法**

$A = A$ 使得消去法更快，因為我們可以跳過矩陣的半部分（對角線以上）。這意味著上三角矩陣 $U$ 可能不是對稱的。**三重積** $A = LDU$。記住如何將對角矩陣 $D$ 的元素分成 $1$ 的元素，將 $1$ 放在對角線上，並將 $L$ 和 $U$ 放在對角線以下和對角線以上。

$\begin{bmatrix} 1 & 2 \\ 2 & 7 \end{bmatrix}$ $LU$ 錯失了 $A$ 的對稱性。

$\begin{bmatrix} 1 & 2 \\ 2 & 7 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 0 & 3 \end{bmatrix} \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ $LDU$ 捕捉了對稱性。

$\begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}$ 是 $U$ 的轉置。

當 $A$ 是對稱的，通常形式 $A = LDU$ 變成 $A = LDL^T$。最終的 $U$（連同對角線上的 $1$）是 $L$ 的轉置。因此，我們得到一個對角矩陣 $D$（連同對角線上的 $1$）。對角矩陣 $D$ 包含的資訊是 $A$ 的對稱性。

如果 $A = A^T$ 則被分解為 $LDL^T$，則沒有任何交換，因此 $L$ 是精確的。

**摘要**

The symmetric $A$ is factored into $LDL^T$ in a naturally (U is skipped). The numeric that happen in $LDL^T$ is approximately (L is skipped) in $LU$ also. Note that the transpose of $U$ in $LDL^T$ from $LDU$ multiplication is $L^T$ instead of the equivalent in $LDL^T$ can help and $3/3$ multiplication operation.
