## 2.4 矩陣運算規則 75

三步路徑由 A³ 計算，我們觀察到節點 2：

$\begin{bmatrix} 3 & 2 \\ 2 & 1 \end{bmatrix}^3$ 計算的是具有三個步驟的路徑：$\dots$ 1 到 1 到 1 到 2, 1 到 2 到 1 到 2 $\dots$ 2 到 1 到 1 到 2

這些 Aᵏ 包含斐波那契數 0, 1, 1, 2, 3, 5, 8, 13, ... (見 6.2 節)。
將 A 與 Aᵏ 相乘涉及斐波那契規則 Fₖ₊₂ = Fₖ₊₁ + Fₖ (例如 13 = 8 + 5)。

$A(A^k) = \begin{bmatrix} 1 & 1 \\ 1 & 0 \end{bmatrix} \begin{bmatrix} F_{k+1} & F_k \\ F_k & F_{k-1} \end{bmatrix} = \begin{bmatrix} F_{k+2} & F_{k+1} \\ F_{k+1} & F_k \end{bmatrix} = A^{k+1}$.

有 13 個六步路徑從節點 1 到節點 1，但我無法找出所有這些路徑。

Aᵏ 也計算單詞 aaba 的數量。一個像 1 到 1 到 2 到 1 對應於單詞 aaba。字母 b 不能重複出現，因為沒有從 2 到 2 的邊。Aᵏ 的 i, j 入口計算的是長度 k + 1 且以第 i 個字母開始並以第 j 個字母結束的單詞的數量。

## 問題集 2.4

問題 1-16 關於矩陣乘法的法則。

1  A 是 3x5，B 是 5x3，C 是 3x1，D 是 1x3。所有條目都是 1。哪些矩陣運算被允許，結果是什麼？

   BA   AB   ABD   DBA   A(B + C)

2  要找到以下內容，你需要哪些行或列或矩陣？

   (a) AB 的第三列
   (b) AB 的第一行
   (c) AB 的第 2 行第 4 列的條目
   (d) CDE 的第 1 行第 1 列的條目

3  計算 AB + AC 並與 A(B + C) 進行比較。

   $A = \begin{bmatrix} 1 & 5 \\ 2 & 3 \end{bmatrix}$  和  $B = \begin{bmatrix} 0 & 2 \\ 1 & 0 \end{bmatrix}$  和  $C = \begin{bmatrix} 3 & 1 \\ 0 & 0 \end{bmatrix}$.

4  在問題 3 中，將 A 乘以 BC。然後計算 AB 乘以 C。
