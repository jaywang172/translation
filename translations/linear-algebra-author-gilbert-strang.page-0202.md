4.1. 四個子空間的正交性 $\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\quad 199$

[圖表內容翻譯]
- $\dim r$ $\rightarrow$ 維度 $r$
- row space $\rightarrow$ 列空間
- $x_r$ $\rightarrow$ $x_r$
- $A x_r = b$ $\rightarrow$ $A x_r = b$
- $b$ $\rightarrow$ $b$
- column space $\rightarrow$ 行空間
- $\dim r$ $\rightarrow$ 維度 $r$
- $A x$ $\rightarrow$ $A x$
- $x = x_r + x_n$ $\rightarrow$ $x = x_r + x_n$
- $\mathbf{R}^n$ $\rightarrow$ $\mathbf{R}^n$
- $\mathbf{R}^m$ $\rightarrow$ $\mathbf{R}^m$
- $x_n$ $\rightarrow$ $x_n$
- $A x_n = 0$ $\rightarrow$ $A x_n = 0$
- nullspace $\rightarrow$ 零空間
- $\dim n - r$ $\rightarrow$ 維度 $n - r$
- nullspace of $A^T$ $\rightarrow$ $A^T$ 的零空間
- $\dim m - r$ $\rightarrow$ 維度 $m - r$

圖 4.3：這是對圖 4.2 的更新，展示了 $A$ 對於 $x = x_r + x_n$ 的真實作用。列空間向量 $x_r$ 映射到行空間，零空間向量 $x_n$ 映射到零。

不僅如此：行空間中的每一個向量 $b$ 都來自列空間中唯一的一個向量。證明：如果 $Ax_r = Ax'_r$，則差值 $x_r - x'_r$ 位於零空間中。它同時也位於 $x_r$ 與 $x'_r$ 所屬的列空間中。由於零空間與列空間正交，這個差值必須是零向量。因此 $x_r = x'_r$。

如果我們去掉兩個零空間，在 $A$ 內部隱藏著一個 $r \times r$ 的可逆矩陣。從列空間到行空間，$A$ 是可逆的。「偽逆」（pseudoinverse）將在 7.3 節中對其進行反轉。

範例 4 每個對角矩陣都有一個 $r \times r$ 的可逆子矩陣：

$$A = \begin{bmatrix} 3 & 0 & 0 & 0 & 0 \\ 0 & 5 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} \text{ 包含子矩陣 } \begin{bmatrix} 3 & 0 \\ 0 & 5 \end{bmatrix}.$$

其他十一個零則對應於零空間。$B$ 的秩（rank）同樣為 $r = 2$：

$$B = \begin{bmatrix} 1 & 2 & 3 & 4 & 5 \\ 1 & 2 & 4 & 5 & 6 \\ 1 & 2 & 4 & 5 & 6 \end{bmatrix} \text{ 包含 } \begin{bmatrix} 1 & 3 \\ 1 & 4 \end{bmatrix} \text{ 在主元行與主元列中。}$$

當我們為 $\mathbf{R}^n$ 和 $\mathbf{R}^m$ 選擇合適的基底時，每個 $A$ 都能變成一個對角矩陣。這種奇異值分解（Singular Value Decomposition）在應用中已變得極其重要。
