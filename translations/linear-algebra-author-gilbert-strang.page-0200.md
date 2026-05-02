4.1. 四個子空間的正交性 197

對於喜歡使用矩陣簡寫的讀者，這裡提供第二個關於正交性的證明。列空間中的向量是諸列的組合 $A^T\mathbf{y}$。將 $A^T\mathbf{y}$ 與零空間中的任意向量 $\mathbf{x}$ 取點積。這些向量是相互垂直的：

**零空間與列空間** $\quad \mathbf{x}^T(A^T\mathbf{y}) = (A\mathbf{x})^T\mathbf{y} = \mathbf{0}^T\mathbf{y} = 0. \quad (2)$

我們喜歡第一個證明。你可以看到方程式 (1) 中 $A$ 的那些列與 $\mathbf{x}$ 相乘產生零。第二個證明展示了為什麼 $A$ 和 $A^T$ 都出現在基本定理中。$A^T$ 與 $\mathbf{y}$ 搭配，而 $A$ 與 $\mathbf{x}$ 搭配。最後我們使用了 $A\mathbf{x} = \mathbf{0}$。

**範例 3** $A$ 的諸列與零空間中的 $\mathbf{x} = (1, 1, -1)$ 相互垂直：

$A\mathbf{x} = \begin{bmatrix} 1 & 3 & 4 \\ 5 & 2 & 7 \end{bmatrix} \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \quad \text{給出點積結果} \quad \begin{aligned} 1 + 3 - 4 &= 0 \\ 5 + 2 - 7 &= 0 \end{aligned}$

現在我們轉向另外兩個子空間。在本範例中，行空間是整個 $\mathbf{R}^2$。$A^T$ 的零空間僅包含零向量（與所有向量正交）。$A$ 的行空間與 $A^T$ 的零空間永遠是正交子空間。

$A^T$ 零空間中的每一個向量 $\mathbf{y}$ 都與 $A$ 的每一行垂直。**左零空間 $N(A^T)$ 與行空間 $C(A)$ 在 $\mathbf{R}^m$ 中是正交的。**

將原始證明應用於 $A^T$。其零空間與其列空間正交——而 $A^T$ 的列空間即為 $A$ 的行空間。證畢 (Q.E.D.)。

若要視覺化證明，請看 $A^T\mathbf{y} = \mathbf{0}$。$A$ 的每一行與 $\mathbf{y}$ 相乘均得到 0：

$C(A) \perp N(A^T) \quad A^T\mathbf{y} = \begin{bmatrix} (\text{第 1 行})^T \\ \dots \\ (\text{第 } n \text{ 行})^T \end{bmatrix} \begin{bmatrix} \mathbf{y} \end{bmatrix} = \begin{bmatrix} 0 \\ \dots \\ 0 \end{bmatrix}. \quad (3)$

$\mathbf{y}$ 與 $A$ 每一行的點積均為零。因此，左零空間中的 $\mathbf{y}$ 與每一行垂直——進而與整個行空間垂直。

**正交補空間**

**重要** 基本子空間不僅僅是（成對地）正交。它們的維度也剛好正確。在 $\mathbf{R}^3$ 中，兩條線可能是垂直的，但這兩條線不能同時是一個 $3 \times 3$ 矩陣的列空間和零空間。這些線的維度為 1 和 1，相加等於 2。正確的維度 $r$ 和 $n-r$ 必須相加等於 $n = 3$。
基本子空間的維度為 2 和 1，或 3 和 0。這些子空間不僅正交，它們還是**正交補空間**。

**定義** 子空間 $V$ 的**正交補空間**包含所有與 $V$ 垂直的向量。這個正交子空間記作 $V^\perp$（讀作 “$V$ perp”）。

根據此定義，零空間是列空間的正交補空間。每一個與諸列垂直的 $\mathbf{x}$ 均滿足 $A\mathbf{x} = \mathbf{0}$。
