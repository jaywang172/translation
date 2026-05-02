## 154 第 3 章 向量空間與子空間

**(b) 我們知道 $E_1A = R$ 且 $E_2B = R$。所以 $A$ 等於一個矩陣乘以 $B$。**

**22 表示 $A$ 和 $B$ 作為兩個矩陣的和：**

$\qquad A = \begin{bmatrix} 1 & 1 & 0 \\ 1 & 1 & 4 \\ 1 & 1 & 8 \end{bmatrix}$, 秩 = 2  $\qquad B = \begin{bmatrix} 2 & 2 \\ 2 & 3 \end{bmatrix}$

**23 回答與習題 3.3 C 相同的問題：**

$\qquad A = \begin{bmatrix} 1 & 2 & 2 \\ 2 & 4 & 4 \\ 1 & 2 & 2 \end{bmatrix}$  和  $\qquad B = \begin{bmatrix} c & 2 \\ 0 & 2-c \end{bmatrix}$.

**24 什麼是零空間 $N$（包含特殊解）對於 $A$、$B$、$C$？**

$\qquad A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$  和  $\qquad B = \begin{bmatrix} 1 & 7 \\ 0 & 0 \end{bmatrix}$  和  $\qquad C = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$.

**25 整潔的事實：每個 $m \times n$ 矩陣的秩 $r$ 需要 $r$ 次 (由 $r \times n$ 矩陣) 的行運算。**

$\qquad A = (\text{pivot columns of } A) (\text{first } r \text{ rows of } R) = (\text{COL}(ROW))$.

寫出本節方程式 (1) 中的 $3 \times 4$ 矩陣 $A$ 等於從 $R$ 的前 2 欄和 $4 \times 2$ 矩陣 $R$ 的乘積。

## 挑戰問題

**26 假設 $A$ 是 $m \times n$ 矩陣的秩 $r$。它的簡化階梯形式是 $R$。描述來自 $R$ 的轉置的簡化階梯形式 $R^T$ (prime means transpose) 的矩陣 $Z$（它的形狀和所有條目）。**

$\qquad R = \text{rref}(A) \quad \text{and} \quad Z = (\text{rref}(R^T))^T$.

**27 假設 $R$ 是 $m \times n$ 的秩 $r$，具有先導列在最前面：**

$\qquad R = \begin{bmatrix} I & F \\ 0 & 0 \end{bmatrix}$.

**(a) 這些四個區塊的形狀是什麼？**
**(b) 找到一個右逆 $B$ 使得 $RB = I$ 如果 $m = n$。**
**(c) 找到一個左逆 $C$ 使得 $CR = I$ 如果 $r = n$。**
**(d) $R^T$ 的簡化階梯形式是什麼（形狀）？**
**(e) $R^T R$ 的簡化階梯形式是什麼（形狀）？**

證明 $R^T R$ 具有與 $A$ 相同的零空間。後來我們將證明 $A^T A$ 總是具有相同的零空間。

**28 假設你允許基本列運算，就像你允許基本行運算一樣。這將是“行-和-列運算”對於 $m \times n$ 矩陣的秩 $r$。”**
