194                                                                         第 3 章 向量空間與子空間

**26** （$AB$ 的秩）若 $AB = C$，則 $C$ 的列（rows）是 \_\_\_\_\_ 的列之組合。因此 $C$ 的秩不大於 \_\_\_\_\_ 的秩。由於 $B^T A^T = C^T$，故 $C$ 的秩亦不大於 \_\_\_\_\_ 的秩。

**27** 若給定 $a, b, c$ 且 $a \neq 0$，您會如何選擇 $d$ 使得 $\begin{bmatrix} a & b \\ c & d \end{bmatrix}$ 的秩為 1？找出列空間（row space）與零空間（nullspace）的一組基底。證明它們相互垂直！

**28** 求 $8 \times 8$ 棋盤矩陣 $B$ 與西洋棋矩陣 $C$ 的秩：

$$B = \begin{bmatrix} 1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 \\ 1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 \\ \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot & \cdot \\ 0 & 1 & 0 & 1 & 0 & 1 & 0 & 1 \end{bmatrix} \quad \text{以及} \quad C = \begin{bmatrix} r & n & b & q & k & b & n & r \\ p & p & p & p & p & p & p & p \\ \text{四個零列} \\ p & p & p & p & p & p & p & p \\ r & n & b & q & k & b & n & r \end{bmatrix}$$

數字 $r, n, b, q, k, p$ 均互不相同。找出 $B$ 與 $C$ 的列空間與左零空間（left nullspace）的基底。挑戰問題：找出 $C$ 的零空間之基底。

**29** 井字遊戲（tic-tac-toe）能否在矩陣 $A$ 中填入 5 個 1 和 4 個 0，使得 $\text{rank}(A) = 2$ 但雙方都沒有錯過獲勝的機會？

### 挑戰問題

**30** 若 $A = uv^T$ 是一個秩為 1 的 $2 \times 2$ 矩陣，請重新繪製圖 3.5 以清晰地展示四個基本子空間。若 $B$ 產生相同的四個子空間，則 $B$ 與 $A$ 之間的確切關係是什麼？

**31** $\mathbf{M}$ 是 $3 \times 3$ 矩陣的空間。將 $\mathbf{M}$ 中的每個矩陣 $X$ 乘以

$$A = \begin{bmatrix} 1 & 0 & -1 \\ -1 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix} \text{。注意到：} A \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix} \text{。}$$

(a) 哪些矩陣 $X$ 會導致 $AX = \text{零矩陣}$？
(b) 哪些矩陣具有 $AX$ 的形式（對於某些矩陣 $X$）？

(a) 找出該運算 $AX$ 的「零空間」，而 (b) 找出其「列空間」。這兩個 $\mathbf{M}$ 子空間的維度是多少？為什麼維度之和為 $(n - r) + r = 9$？

**32** 假設 $m \times n$ 矩陣 $A$ 與 $B$ 具有相同的四個子空間。如果它們都處於列簡化階梯形（row reduced echelon form），證明 $F$ 必須等於 $G$：

$$A = \begin{bmatrix} I & F \\ 0 & 0 \end{bmatrix} \quad B = \begin{bmatrix} I & G \\ 0 & 0 \end{bmatrix}$$
