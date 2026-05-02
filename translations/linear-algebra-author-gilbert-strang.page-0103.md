## 100 第 2 章：求解線性方程組

**函數** `[L, U] = slu(A)`
% 對沒有列交換的 A 進行 LU 分解
`[n, n] = size(A);` `tol = 1e-6;`
**for** `k = 1 : n`
**if** `abs(A(k, k)) < tol`
  **end** % 無法繼續，沒有列交換就停止
`L(k, k) = 1;`
**for** `i = k + 1 : n`
  `L(i, k) = A(i, k) / A(k, k);` % 將第 k 列的乘數放入 L
**for** `j = k + 1 : n` % 消去第 k 列及第 k 列以外的元素
  `A(i, j) = A(i, j) - L(i, k) * A(k, j);` % 修改矩陣 A
**end**
**end**
**for** `j = k : n`
  `U(k, j) = A(k, j);` % 第 k 列已確定，命名為 U
**end**
**end**

**函數** `x = slv(A, b)`
% 使用來自 `slu(A)` 的 L 和 U 求解 `Ax = b`
`[L, U] = slu(A);` `s = 0;` % 沒有列交換！
**for** `k = 1 : n` % 前向消去求解 `Lc = b`
**for** `j = 1 : k - 1`
  `s = s + L(k, j) * c(j);` % 將較早的 c(j) 加到 c(k)
**end**
`c(k) = (b(k) - s) / A(k, k);` % 找到 c(k) 並重置 s 以供下一個 k 使用
**end**
**for** `k = n : -1 : 1` % 反向代入求解 `Ux = c`
**for** `j = k + 1 : n`
  `t = t + U(k, j) * x(j);` % U 乘以較晚的 x(j)
**end**
`x(k) = (c(k) - t) / U(k, k);` % 除以樞軸
**end**
`x = x';` % 轉置為列向量

**求解 `Ax = b` 需要多長時間？** 對於一個隨機矩陣，其階數為 `n = 1000`，典型的時間為 1 秒。參見 [web.mit.edu/18.06](http://web.mit.edu/18.06) 和 [math.mit.edu/linearalgebra](http://math.mit.edu/linearalgebra) 了解在 MATLAB、Maple、Mathematica、SciLab、Python 和 R 中的時間。它被約 8 次乘以時，會被乘以 2。對於專業代碼，如 netlib.org。

根據 `n^3` 的規則，矩陣的階數是 10 倍，其大小為 `(10,000)`，將會花費數百秒。這使得它對更大的矩陣（例如，具有數百萬個元素的矩陣）太過於昂貴，以至於在超級電腦上執行。在這種情況下，需要使用其他方法。大多數矩陣實踐在稀疏（少於 0 或 0.1 的非零元素），這使得 `Ax = b` 的求解變得更快。

對於三角矩陣或對稱正定矩陣，也可以使用三角分解來求解。
