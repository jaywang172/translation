## 2.4. 矩陣運算規則

**69**

的欄。這就是矩陣乘法的欄圖像：

矩陣 A 乘以矩陣 B  $A \begin{bmatrix} b_1 & \dots & b_p \end{bmatrix} = \begin{bmatrix} Ab_1 & \dots & Ab_p \end{bmatrix}$.

行圖像被反轉。每個 row of A 乘以整個矩陣 B。結果是 AB 的一行。它是 B 的行的組合。

行矩陣  $[row \ i \ of \ A] \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix} = [row \ i \ of \ AB]$.

我們看到在消去法中 (E 乘以 A) 我們使用欄。我們將 A 乘以欄。無論是 row-column 圖像還是 dot product of rows with columns。相信它或不，there is also a column-row picture. Not everybody knows that columns $1, \dots, n$ of A multiply rows $1, \dots, n$ of B and add up to the same answer AB. Worked Example 2.3C had numbers for $n = 2$. Example 3 will show how to multiply AB using columns times rows.

## 矩陣運算定律

我可以記錄下矩陣遵守的定律，同時強調一個它們不遵守的方程式。矩陣可以是方形或矩形的，涉及 A + B 的定律非常簡單且都成立。以下是一些加法定律：

A + B = B + A  (交換律)
c(A + B) = cA + cB  (分配律)
A + (B + C) = (A + B) + C  (結合律)

三個定律對於乘法成立，但 AB ≠ BA。 (通常將 “law” 稱為 “定理”)
C(A + B) = CA + CB  (從左邊分配律)
(A + B)C = AC + BC  (從右邊分配律)
A(BC) = (AB)C  (對於 ABC 的結合律，括號不是必需的)

當 A 和 B 不是方形矩陣時，AB 的大小與 BA 不同。這些矩陣不能相等。當 A 和 B 都是方形矩陣時，AB 是一個例子顯示 BA 是不同的 from BA:

$AB = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$ but $BA = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$.

事實是 $AI = IA$. 所有方形矩陣與 $I$ commute with $I$ and also with $cI$. Only these matrices $cI$ commute with all other matrices.

The law A(B + C) = AB + AC is easy to prove. Similarly A(B - C) = AB - AC. 
The law $(A + B)C = AC + BC$ is similarly easy. The important one is $(AB)C = A(BC)$. 
The rightmost is proved in the text. The law $A(BC) = (AB)C$ means you can compute AB first. Then dispatch (AB)C. Or you can compute BC first. Then dispatch A(BC). 

**70**
