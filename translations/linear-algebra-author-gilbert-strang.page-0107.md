## 104 第 2 章：解線性方程組

**9** 當零出現在樞軸位置時，A 無法被分解成 LU (我們要求樞軸位置的非零元素)。直接分解會產生這兩種不可能的情況：

$$\begin{bmatrix} 0 & e \\ 2 & 3 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ l & 1 \end{bmatrix} \begin{bmatrix} 1 & d \\ 2 & f \end{bmatrix} = \begin{bmatrix} 1 & d \\ l & 2 \end{bmatrix}$$

這個困難可以通過行交換來解決，這需要一個“置換”矩陣 P。

**10** 哪個數字 c 會導致在第二個樞軸位置出現零？行交換是必要的，且 A = LU 將無法實現。哪個 c 會在第三個樞軸位置產生零？然後一個行交換無法幫助消去過程？

$$A = \begin{bmatrix} 1 & c & 0 \\ 2 & 4 & 1 \\ 3 & 5 & 1 \end{bmatrix}$$

**11** 對於這個矩陣 A，求 L 和 D (對角樞軸矩陣) 是什麼？A = LU 且 A = LDU？

$$A = \begin{bmatrix} 2 & 4 & 8 \\ 0 & 3 & 9 \\ 0 & 0 & 7 \end{bmatrix} \quad \text{已經是三角矩陣}$$

**12** A 和 B 對於對角線樞軸元素而言是對稱的 (因為 4 = -4)。求它們的三因子分解 LDU，並說明 U 與 L 對於這些對稱矩陣的關係。

$$\text{對稱} \quad A = \begin{bmatrix} 2 & 4 \\ 4 & 11 \end{bmatrix} \quad \text{和} \quad B = \begin{bmatrix} 1 & 4 & 0 \\ 4 & 12 & 4 \\ 0 & 4 & 0 \end{bmatrix}$$

**13** (推薦) 對於對稱矩陣 A，計算 L 和 U。

$$A = \begin{bmatrix} a & a & a \\ a & b & b \\ a & b & c \end{bmatrix}$$

求四個條件 a, b, c, d，使得 A = LU 具有四個樞軸。

**14** 這個非對稱矩陣將具有與問題 13 相同的 L 和 A。

求 L 和 U。

$$A = \begin{bmatrix} a & r & r \\ a & b & s \\ a & b & c \end{bmatrix}$$

求四個條件 a, b, c, d, r, s, t，使得 A = LU 具有四個樞軸。
