## 2.6. 消去法 = 分解因式 = *LU* 分解 105

**問題 15-16 使用 *L* 和 *U* (不需要求 *A*) 來解 *Ax = b*。**

**15** 解 *Lc = b* 來求 *c*。然後解 *Ux = c* 來求 *x*。
   
   *L* =  $\begin{bmatrix} 1 & 0 \\ 4 & 1 \end{bmatrix}$  和  *U* = $\begin{bmatrix} 2 & 4 \\ 0 & 1 \end{bmatrix}$  和  *b* = $\begin{bmatrix} 2 \\ 5 \end{bmatrix}$。

   為了安全起見，將 *LU* 相乘並解 *Ax = b*，圈出你看到的單位矩陣。

**16** 解 *Lc = b* 來求 *c*。然後解 *Ux = c* 來求 *x*。 *A* 是什麼？

   *L* = $\begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}$  和  *U* = $\begin{bmatrix} 1 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 1 \end{bmatrix}$  和  *b* = $\begin{bmatrix} 4 \\ 7 \\ 6 \end{bmatrix}$。

**17** (a) 當你對 *L* 應用通常的消去法時，你到達什麼矩陣？

   *L* = $\begin{bmatrix} 1 & 0 & 0 \\ \ell_{21} & 1 & 0 \\ \ell_{31} & \ell_{32} & 1 \end{bmatrix}$。

   (b) 當你對 *I* 應用相同的步驟時，你到達什麼矩陣？

   (c) 當你對 *LU* 應用相同的步驟時，你到達什麼矩陣？

**18** 如果 *A = LDU* 且所有因子都是可逆的，那麼 *L = L₁* 和 *D = D₁* 且 *U = U₁*。“三個因子是唯一的。”

   推導等式 *L₁⁻¹LD = D₁U₁⁻¹*。這兩個三角形是否是對角矩陣？推導 *L = L₁* 且 *U = U₁* (它們都是對角線 1 的矩陣)。因此 *D = D₁*。

**19** 三對角矩陣除了主對角線和兩個相鄰對角線上的元素外，其餘元素都為零。將這些分解成 *A = LU* 和 *A = LDLᵀ*。

   *A* = $\begin{bmatrix} 1 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 2 & 2 \end{bmatrix}$  和  *A* = $\begin{bmatrix} a & a & 0 \\ a & a+b & b \\ 0 & b & b+c \end{bmatrix}$。

**20** 當 *A* 是三對角矩陣時，其 *L* 和 *U* 因子只有七個非零元素。你將如何利用已知零元素，在一個用於高斯消去法的程式碼中？求 *L* 和 *U*。

   三對角矩陣：

   $\begin{bmatrix} 1 & 2 & 0 & 0 \\ 2 & 3 & 1 & 0 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 3 & 4 \end{bmatrix}$

**21** 如果 *A* 和 *B* 在標記為 *x* 和 *y* 的位置上非零 (標記為 *o*)，而其他位置為零，那麼這些零在 *L* 和 *U* 中會保留嗎？

   *A* = $\begin{bmatrix} x & x & 0 & 0 \\ 0 & x & x & 0 \\ 0 & 0 & x & x \\ 0 & 0 & 0 & x \end{bmatrix}$  *B* = $\begin{bmatrix} x & 0 & y & 0 \\ 0 & x & 0 & y \\ y & 0 & x & 0 \\ 0 & y & 0 & x \end{bmatrix}$。
