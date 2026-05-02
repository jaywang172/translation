## 第 30 頁

**第 7 題**

如果矩陣 $Ax$ 的欄向量組合為 0，則每一欄向量 $r_i$ 與 $x$ 的點積為 0：

$\begin{bmatrix} a_1 & a_2 & a_3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = 0$

$\begin{bmatrix} r_1 \cdot x \\ r_2 \cdot x \\ r_3 \cdot x \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$

這三條列向量也位於一個平面上。為什麼這個平面垂直於 $x$？

**第 8 題**

將一個 4 階差分方程式 $Ax = b$ 轉換為求 $x_1, x_2, x_3, x_4$ 的解。寫出這個解的公式為 $x = A^{-1}b$。

$Ax = \begin{bmatrix} 1 & 0 & 0 & 0 \\ -1 & 1 & 0 & 0 \\ 0 & -1 & 1 & 0 \\ 0 & 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \\ b_4 \end{bmatrix} = b$

**第 9 題**

什麼是循環的 4 階差分矩陣 $C$？它將每一列都填入 1。找到所有解 $x = (x_1, x_2, x_3, x_4)$ 使得 $Cx = 0$。這四個 $C$ 的欄向量位於一個“三維超平面”內，嵌入於四維空間中。

**第 10 題**

一個前向差分矩陣 $\Delta z$ 是上三角矩陣：

$\Delta z = \begin{bmatrix} -1 & 1 & 0 & 0 \\ 0 & -1 & 1 & 0 \\ 0 & 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} z_1 \\ z_2 \\ z_3 \end{bmatrix} = \begin{bmatrix} z_2 - z_1 \\ z_3 - z_2 \\ 0 - z_3 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix} = b$

找到 $z_1, z_2, z_3$ 從 $b_1, b_2, b_3$。什麼是逆矩陣 $\Delta z^{-1}$ 在 $z = \Delta^{-1}b$ 中？

**第 11 題**

證明前向差分 $(f(1) + 1)^2 - f(1)^2$ 是 $2f(1) + 1$ 的奇數。在微積分中，$(f+1)^n - f^n$ 將以 $f^n$ 的導數開始。

**第 12 題**

第 16 題的例題的最後幾行表明，4 階中心差分矩陣是可逆的。求解 $Cx = (b_1, b_2, b_3, b_4)$ 以找到它的逆矩陣 $C^{-1}b$。

## Challenge Problems (挑戰問題)

**第 13 題**

例題的最後幾行表明，5 階中心差分矩陣不可逆。寫下 5 個方程式 $Cx = b$。找到一組 $b_1, b_2, b_3, b_4, b_5$ 的組合使得等式為零。什麼組合的 $b_1, b_2, b_3, b_4, b_5$ 使得 $C x = 0$？（這 5 個欄向量位於一個“四維超平面”內，嵌入於五維空間中。）

**第 14 題**

如果 $(a, b)$ 是 $(c, d)$ 的一個倍數，其中 $abcd \neq 0$，那麼 $(a, b)$ 也是 $(d, c)$ 的一個倍數。證明這個定理。這是一個關於線性獨立性的提示。在向量空間中，如果 $v_1, v_2, v_3$ 是線性獨立的，那麼 $a_1 v_1 + a_2 v_2 + a_3 v_3 = 0$ 意味著 $a_1 = a_2 = a_3 = 0$。
