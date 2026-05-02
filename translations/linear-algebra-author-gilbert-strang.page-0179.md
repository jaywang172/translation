176

第 3 章：向量空間與子空間

這三個矩陣 $A_1$、$A_2$、$A_4$ 是一個**子空間**——上三角矩陣的基底。它的維度是 3。$A_1$ 和 $A_4$ 是上三角矩陣的基底。什麼是對稱矩陣的基底呢？保留 $A_1$ 和 $A_4$，並將 $A_2 + A_3$ 加入。

為了更進一步，思考一個由所有 $n \times n$ 矩陣組成的空間。一個可能的基底使用只有一個非零元素（該元素是 1）。存在 $n^2$ 個這樣的基底矩陣。

**整個 $n \times n$ 矩陣空間的維度是 $n^2$。**

**上三角矩陣子空間的維度是 $\frac{n^2}{2} + \frac{n}{2}$。**

**對稱矩陣子空間的維度是 $\frac{n^2}{2} + \frac{n}{2}$（為什麼？）。**

函數空間。方程式 $y'' = 0$ 和 $y'' = -y$ 以及 $y'' = y$ 涉及二階導數。在微積分中，我們求解函數 $y(x)$：

$y'' = 0$  是通過任何線性函數 $y = cx + d$ 求解的。
$y'' = -y$  是通過任何組合 $y = c \sin x + d \cos x$ 求解的。
$y'' = y$  是通過任何組合 $y = ce^x + de^{-x}$ 求解的。

對於 $y'' = -y$ 這個解空間有兩個基底函數：$\sin x$ 和 $\cos x$。這個空間對於 $y'' = 0$ 有 $x$ 和 1。它是“零空間”的基底，第二個導數為 0。維度是 2 在每個情況下（這些是二階方程式）。

$y'' = 2$ 的解形成一個子空間——右側是 2，而不是 0。一個特定的解是 $y(x) = x^2$。完整的解是 $y(x) = x^2 + cx + d$。那些函數滿足 $y'' = 2$。注意到特定的解加上任何函數 $cx + d$ 在零空間中。一個線性微分方程式就像一個線性矩陣方程式 $Ax = b$。但我們通過微積分來解決線性代數。

我們回到一個包含零向量的空間 $Z$。這個空間的維度是 0。空集合（不包含任何向量）是 $Z$ 的基底。我們永遠無法將零向量加入到這個基底中，因為線性獨立性會被破壞。

---

**關鍵概念回顧**

1.  The columns of $A$ are independent if $x = 0$ is the only solution to $Ax = 0$.
    $A$ 的列是獨立的，如果 $Ax = 0$ 的唯一解是 $x = 0$。

2.  The vectors $v_1, ..., v_n$ span a space if their combination $c_1v_1 + ... + c_nv_n$ can produce any vector.
    向量 $v_1, ..., v_n$ 跨越一個空間，如果它們的組合 $c_1v_1 + ... + c_nv_n$ 可以產生任何向量。

3.  A basis for a space contains the smallest number of vectors. The number of vectors in a basis is the dimension of the space.
    一個空間的基底包含最少數量的向量。基底中的向量數量是空間的維度。

4.  The nullspace of $A$ consists of all solutions to $Ax = 0$. It is a subspace.
    $A$ 的零空間由所有 $Ax = 0$ 的解組成。它是一個子空間。

5.  If the only solution to $Ax = b$ is a particular solution, then $b$ is in the column space of $A$.
    如果 $Ax = b$ 的唯一解是一個特定的解，那麼 $b$ 在 $A$ 的列空間中。
