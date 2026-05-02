## 38 章節 2. 解線性方程式

我們可以從 *A* (一個較小的矩陣) 中挑選出第一列。對這個 3x3 子矩陣 *A*(1,1) 來說，第一列的符號保持第一列不變。

以時間為軸的列 *b* = [*A*(1,1) *x*; *A*(2,1) *x*; *A*(3,1) *x*]

每一項都是一個點積，列乘以列，1x3 矩陣乘以 3x1 矩陣。
這個進入方式是將列乘以矩陣的列。第一列乘以 3x1 子矩陣 *A*(:,1)。現在，冒號符號 : 表示保持所有列的第 1 列。這個列乘以 *x*(1) 並且其他列乘以 *x*(2) 和 *x*(3)。

以時間為軸的列 *b* = *A*(:,1) *x*(1) + *A*(:,2) *x*(2) + *A*(:,3) *x*(3)

我想這表示矩陣是以列為單位運算的。然後，將一列乘以一個向量會比將一列乘以一個向量快一點。*A* *x* 實際上是以列為單位運算的。

你可以在更低階語言中看到相同的結構，例如使用 “do loop”。當外部迴圈遍歷每一列數字 *J* 時，乘法是按時間進行的。內部迴圈 *J* = 1,3 遍歷每一列。

當外部迴圈使用 *J* 時，乘法是一個向量。我將在 MATLAB (需要額外兩行 “end” 和 “end” 來關閉 “for” 迴圈) 中展示這一點。

**FORTRAN by rows** | **MATLAB by columns**
------- | --------
DO 10 *J* = 1,3 | for *j* = 1:3
DO 10 *I* = 1,3 | for *i* = 1:3
10 *B*(*I*) = *B*(*I*) + *A*(*I*,*J*) * *x*(*J*) | *b*(*i*) = *b*(*i*) + *A*(*i*,*j*) * *x*(*j*)

請注意，MATLAB 區分大小寫 (大寫字母和小寫字母)。如果矩陣是 *A*，那麼它的元素是 *a*(i,j)，而不是 *A*(i,j)。
我認為你更喜歡較高的層次 *A* *x*。FORTRAN 不會出現在本書中。Maple 和 Mathematica 和繪圖計算器也以相同的方式運算 *A* *x*。
乘法是 *A* *x* 在 Mathematica 中。它是以列為單位運算的。在 Maple 中，這些語言會自動執行列運算。它們不允許任何實數。在 MATLAB 的 Symbolic Toolbox 中，它們會執行符號答案。

---

## REVIEW OF THE KEY IDEAS

1.  The basic operation of linear algebra is multiplication between a matrix and a vector.
2.  Together these operations can be summarized as *cv* + *dw*.
3.  A convenient way to factor *A* *x* = *b* is to demand that the columns of *A* are independent. This is the condition for a unique solution.
4.  The columns of *A* are linearly independent if no combination of the columns equals the zero vector, except the combination *c*<sub>1</sub> = *c*<sub>2</sub> = ... = *c*<sub>n</sub> = 0.
5.  Typically we want to solve *A* *x* = *b* for *x*. If *A* is invertible, then *x* = *A*<sup>-1</sup> *b*.
