## 82

**Note 6** 一個對角線矩陣若其對角線元素不為零，則其反矩陣的對角線元素為零：

If  $A = \begin{bmatrix} d_1 \\ & \ddots \\ & & d_n \end{bmatrix}$ then $A^{-1} = \begin{bmatrix} 1/d_1 \\ & \ddots \\ & & 1/d_n \end{bmatrix}$

**Example 1**  2x2 矩陣 $A = \begin{bmatrix} 1 & 1 \\ 2 & 2 \end{bmatrix}$  不可逆。它在 Note 5 中失敗，因為 $ad - bc$ 等於 $2 - 2 = 0$。它在 Note 3 中也失敗，因為 $x = 0$ 時 $x = (2-1)$。它沒有兩個樞軸，如 Note 1 所要求。
消去法將此矩陣的第二列變成零列。

**The Inverse of a Product *AB***

對於兩個非零數字 *a* 和 *b*，*a* + *b* 的和可能不可逆。數字 *a* = 3 和 *b* = -3 具有反數 $\frac{1}{3}$ 和 $-\frac{1}{3}$。它們的總和 *a* + *b* = 0 沒有反數。但乘積 *ab* = -9 具有反數，即 $\frac{1}{3}$ 乘以 $-\frac{1}{3}$。

對於兩個矩陣 *A* + *B*，情況類似。很難說 *A* + *B* 的可逆性。重要的是，如果兩個因子 *A* 和 *B* 分別可逆（且尺寸相同），則 $A^{-1}$ 和 $B^{-1}$ 以相反順序出現。

If *A* and *B* are invertible then so is *AB*. The inverse of a product *AB* is

$(AB)^{-1} = B^{-1}A^{-1}$.  (4)

To see why the order is reversed, multiply *AB* times $B^{-1}A^{-1}$. Inside that is $BB^{-1} = I$:

Inverse of *AB*  $(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = AIA^{-1} = I$.

We moved parentheses to multiply $BB^{-1}$ first. Similarly $B^{-1}A^{-1}$ times *AB* equals *I*. This illustrates a basic rule of mathematics: Inverses come in reverse order. It is also common sense: If you put on socks and then shoes, the first to be taken off are the . . . The same reverse order applies to three or more matrices:

Reverse order  $(ABC)^{-1} = C^{-1}B^{-1}A^{-1}$. (5)

**Example 2**  Inverse of an elimination matrix. If *E* subtracts 5 times row 2 from row 2, then $E^{-1}$ adds 5 times row 1 to row 2:

$E = \begin{bmatrix} 1 & 0 \\ -5 & 1 \end{bmatrix}$ and $E^{-1} = \begin{bmatrix} 1 & 0 \\ 5 & 1 \end{bmatrix}$.

Multiply $E^{-1}$ to get the identity matrix *I*. Also multiply $E$ to get $E(E^{-1}) = I$ and subtracting the same 5 times row 1, which has an inverse that subtracts 5 times adding or multiply each row by the same *k* = 1. We’ll keep the rule in mind.
