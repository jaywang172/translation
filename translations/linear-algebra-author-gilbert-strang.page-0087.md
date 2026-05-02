## 84

第 2 章：解線性方程式

高斯-喬丹法透過解 *n* 個方程式來計算 *A*<sup>-1</sup>。通常，這個“增廣矩陣”[*A* | *I*] 具有一個額外的列數 *n*。現在我們有三個右側邊 *e<sub>1</sub>, e<sub>2</sub>, e<sub>3</sub>* (當 *A* 是 3x3 時)。它們是列向量 *I* 的。所以，增廣矩陣實際上是塊矩陣 [*A* | *I*]。讓我來反轉我最喜歡的矩陣 *K*，並將 2 放在主對角線上，-1 放在它的 2's 旁邊：

[*K* = *e<sub>1</sub>* *e<sub>2</sub>* *e<sub>3</sub>*] = 
$\begin{bmatrix}
2 & -1 & 0 & | & 1 & 0 & 0 \\
-1 & 2 & -1 & | & 0 & 1 & 0 \\
0 & -1 & 2 & | & 0 & 0 & 1
\end{bmatrix}$

開始高斯-喬丹法於 *K*

$\rightarrow$
$\begin{bmatrix}
2 & -1 & 0 & | & 1 & 0 & 0 \\
0 & \frac{3}{2} & -1 & | & \frac{1}{2} & 1 & 0 \\
0 & -1 & 2 & | & 0 & 0 & 1
\end{bmatrix}$

(½ 行 1 + 行 2)

$\rightarrow$
$\begin{bmatrix}
2 & -1 & 0 & | & 1 & 0 & 0 \\
0 & \frac{3}{2} & -1 & | & \frac{1}{2} & 1 & 0 \\
0 & 0 & \frac{4}{3} & | & \frac{1}{3} & \frac{2}{3} & 1
\end{bmatrix}$

(⅔ 行 2 + 行 3)

我們已經完成到 *K*<sup>-1</sup>。矩陣的第一個三個列是 *U* (上三角)。樞軸 2, ⅔, ⅘ 都在它的對角線上。高斯會用回代來完成。喬丹的貢獻是繼續消去！他會走到“簡約階梯形”形式。行被加到行上以消除它們，以產生這些樞軸之上的零。

(零在上方
第三個樞軸)

$\rightarrow$
$\begin{bmatrix}
2 & -1 & 0 & | & 1 & 0 & 0 \\
0 & \frac{3}{2} & -1 & | & \frac{1}{2} & 1 & 0 \\
0 & 0 & \frac{4}{3} & | & \frac{1}{3} & \frac{2}{3} & 1
\end{bmatrix}$

(⅘ 行 3 + 行 2)

(零在上方
第二個樞軸)

$\rightarrow$
$\begin{bmatrix}
2 & 0 & 0 & | & \frac{4}{3} & \frac{2}{3} & 0 \\
0 & \frac{3}{2} & 0 & | & \frac{3}{4} & \frac{5}{4} & \frac{1}{2} \\
0 & 0 & \frac{4}{3} & | & \frac{1}{3} & \frac{2}{3} & 1
\end{bmatrix}$

(⅘ 行 2 + 行 1)

最後的高斯-喬丹步驟是除以每個樞軸。新的樞軸是 1。我們已經到達 *I* 在矩陣的左半部分，因為 *K* 是可逆的。*K*<sup>-1</sup> 的三個列在第二半 *K*<sup>-1</sup>：

(除以 2)
$\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}$

$\begin{bmatrix}
\frac{2}{3} & \frac{1}{3} & 0 \\
\frac{3}{8} & \frac{5}{12} & \frac{1}{4} \\
\frac{1}{4} & \frac{1}{2} & \frac{3}{4}
\end{bmatrix}$

= [*x<sub>1</sub>* *x<sub>2</sub>* *x<sub>3</sub>*] = [*K*<sup>-1</sup>*]

從 3x3 的矩陣開始，我們得到了 *K*<sup>-1</sup>。現在我們有完整的喬丹過程，可以驗證 *K* *K*<sup>-1</sup> = *I*。以下是這個驗證：

$\begin{bmatrix}
2 & -1 & 0 \\
-1 & 2 & -1 \\
0 & -1 & 2
\end{bmatrix}$

$\begin{bmatrix}
\frac{2}{3} & \frac{1}{3} & 0 \\
\frac{3}{8} & \frac{5}{12} & \frac{1}{4} \\
\frac{1}{4} & \frac{1}{2} & \frac{3}{4}
\end{bmatrix}$

=

$\begin{bmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}$
