## 3.3. 秩與簡化梯形式 153

**問題 12-14 都是關於 $r \times r$ 可逆矩陣 $A$ 內的。**

**12** 如果 $A$ 具有秩 $r$，則它有一個 $r \times r$ 子矩陣 $S$ 是可逆的。移除 $m-r$ 列和 $n-r$ 行以獲得一個可逆子矩陣 $S$ 包含在 $A$、$B$ 和 $C$ 內。你可以保留樞軸列和樞軸行。

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 1 & 2 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{bmatrix}, \quad C = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$

**13** 假設 $P$ 包含一個 $m \times n$ 矩陣 $P$ 的所有樞軸列。解釋為什麼這個 $m \times r$ 子矩陣 $P$ 具有秩 $r$。

**14** 對 $P$ 轉置在問題 13 中。然後找到 $P^T$ 的樞軸列。轉置回去，這會產生一個 $r \times r$ 可逆子矩陣 $S$ 包含在 $P$ 和 $A$ 內。

對於 $A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 2 & 4 & 7 \end{bmatrix}$，找到 $P$ (3 by 2) 然後找到可逆 $S$ (2 by 2)。

**問題 15-20 顯示 $\text{rank}(AB)$ 不會大於 $\text{rank}(A)$ 或 $\text{rank}(B)$。**

**15** 找到 $AB$ 和 $AC$ 的秩（找到一個矩陣乘以另一個矩陣的秩）。

$$A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix} \text{ and } B = \begin{bmatrix} 2 & 1 \\ 3 & 1.5 \end{bmatrix} \text{ and } C = \begin{bmatrix} 1 & b \\ c & bc \end{bmatrix}$$

**16** 秩 $uv^T$ 矩陣等於秩 $v^T u$ 矩陣，因為 $v^T u$ 是 $u^T v$ 的轉置。這個矩陣 $uv^T w^T$ 也具有相同的秩，除非 $\text{det} \begin{bmatrix} u & v & w \end{bmatrix}$ 等於 0。

**17** (a) 假設矩陣 $B$ 的列 $j$ 是先前列的線性組合。證明 $AB$ 的列 $j$ 是 $A$ 的先前列的相同線性組合。因此，$AB$ 沒有新的樞軸列，所以 $\text{rank}(AB) \le \text{rank}(B)$。

(b) 找到 $A_1$ 和 $A_2$ 使得 $\text{rank}(A_1 B) = 1$ 和 $\text{rank}(A_2 B) = 0$ for $B = \begin{bmatrix} 1 & 1 \end{bmatrix}$。

**18** 問題 17 證明了 $\text{rank}(AB) \le \text{rank}(B)$。然後使用相同的推理給出 $\text{rank}(B^T A^T) \le \text{rank}(A^T)$。如何證明 $\text{rank}(A^T B^T) \le \text{rank}(A^T)$？

**19** (重要!) 假設 $A$ 和 $B$ 是 $n \times n$ 矩陣，且 $AB = I$。證明 $\text{rank}(AB) \le \text{rank}(A)$ 且 $\text{rank}(AB) \le \text{rank}(B)$。 $A$ 是可逆的，並且 $B$ 是 $A$ 的逆矩陣。

**20** 如果 $A$ 是 $3 \times 3$ 且 $B$ 是 $3 \times 2$，則 $\text{rank}(A) = 3$ 和 $A$ 從它的秩中沒有失去任何東西。如果 $x = b$ 且 $A x = b$ 有解，則 $b$ 必須在 $A$ 的列空間中。給出一個例子，其中 $A$ 和 $B$ 使得 $\text{rank}(AB) < \text{rank}(A)$ 和 $\text{rank}(AB) < \text{rank}(B)$。
