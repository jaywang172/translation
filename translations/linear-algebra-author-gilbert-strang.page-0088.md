## 2.5. 逆矩陣 85

消去法在改變 *A* 的同時計算逆矩陣 *A*<sup>-1</sup>。對於大型矩陣，我們可能不需要 *A*<sup>-1</sup>。但對於小型矩陣，計算 *A*<sup>-1</sup> 可能是值得的。我們想要提出三個關於此特定矩陣 *K*<sup>-1</sup> 的觀察，因為它是一個重要的例子。我們介紹對稱矩陣、三對角矩陣和行列式：

1. *K* 在其主對角線對稱。因此 *K*<sup>-1</sup> 也是對稱的。
2. *K* 是三對角矩陣（只有三個非零對角線）。但 *K*<sup>-1</sup> 是一個稠密矩陣，沒有零。這就是我們不常計算帶狀矩陣的逆矩陣的原因。帶狀矩陣的逆矩陣通常是一個稠密矩陣。
3. 樞軸的乘積是 2(3)(3) = 4。這個數字 4 是 *K* 的行列式。

*K*<sup>-1</sup> 涉及除以行列式

K<sup>-1</sup> =  
[ 1  3  2 ]
[ 2  4  2 ]
[ 4  1  2 ]

(8)

這是一個可逆矩陣，因為矩陣不能有零行列式。

**例題 4** 求 *A*<sup>-1</sup>，使用高斯-喬丹消去法從 *A* = [ 2 3 1 ; 4 7 0 ; 2 0 -1 ] 開始。有兩次列運算，然後除以樞軸 1。

[ 2 3 1 0 ]  (這是 [ *U*  *L*<sup>-1</sup> ])
[ 4 7 0 0 ]  →  [ 0 -1 -2 1 ]
[ 2 0 -1 0 ]  →  [ 0 1 7/3 -1 ]  (這是 [ *I*  *A*<sup>-1</sup> ])

因此 *A*<sup>-1</sup> 涉及除以行列式 ad - bc = 2 * 7 - 3 * 4 = 2。The code for *X* = inverse(*A*) can use rref, the “row reduced echelon form” from Chapter 3:

```
I = eye(n);           % Define the n by n identity matrix
R = rref([A | I]);    % Eliminate on the augmented matrix [A | I]
X = R(:,n+1:n+n);     % Pick A^-1 from the last n columns of R
```

*A* 必須可逆，或消去法不能產生 *I* 在左側。
高斯-喬丹顯示 *A*<sup>-1</sup> 是昂貴的。我們必須求解 *n* 個方程式以找到 *n* 個列。

為了求解 *Ax* = *b* 而不使用 *A*<sup>-1</sup>，我們處理一個列向量 *b* 以找到一個列向量 *x*。

在 *A*<sup>-1</sup> 的防禦中，我們想要計算其成本是 *n* 次而不是 *n* 的三個系統。
*Ax* = *b*。令人驚訝的是，為了求解 *n* 個列向量 *b*，使用 *A*<sup>-1</sup> 的成本與使用
高斯消去法（*n* 個系統）的成本大致相同。重要的是，在許多應用中，右側
邊是相對簡單的，並且 *A* 的消去法只需要完成一次。The next
section completely changes our elimination plan to solve a broad range of problems.
