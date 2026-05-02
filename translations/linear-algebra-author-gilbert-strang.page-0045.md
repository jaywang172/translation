## 42 第 2 章：解線性方程式

**14** 將 $2x + 3y + z + 5t = 8$ 表達為一個矩陣 $A$ 乘以一個行向量 $\mathbf{x} = \begin{bmatrix} x \\ y \\ z \\ t \end{bmatrix}$。有多少行？解描述了在 4 維空間中的一個超平面與一個 3 維空間的體積。這個平面是 3 維空間中的一個體積。

**問題 15-22 詢問作用於向量的特殊方式的矩陣。**

**15** (a) 什麼是 2 x 2 的單位矩陣？ $I$ 乘以 $\begin{bmatrix} x \\ y \end{bmatrix}$ 等於 $\begin{bmatrix}  \\  \end{bmatrix}$。
(b) 什麼是 2 x 2 的交換矩陣？ $P$ 乘以 $\begin{bmatrix} x \\ y \end{bmatrix}$ 等於 $\begin{bmatrix}  \\  \end{bmatrix}$。

**16** (a) 什麼是 2 x 2 矩陣 $R$ 旋轉 90°？ $R$ 乘以 $\begin{bmatrix} x \\ y \end{bmatrix}$ 等於 $\begin{bmatrix}  \\  \end{bmatrix}$。
(b) 什麼是 2 x 2 矩陣 $R$ 旋轉 180°？

**17** 找出矩陣 $P$ 乘以 $\begin{bmatrix} x \\ y \\ z \end{bmatrix}$ 產生 $\begin{bmatrix} y \\ z \\ x \end{bmatrix}$。找出矩陣 $Q$ 乘以 $\begin{bmatrix} y \\ z \\ x \end{bmatrix}$ 產生 $\begin{bmatrix} x \\ y \\ z \end{bmatrix}$。

**18** 什麼是 2 x 2 矩陣 $E$ 提取第二個分量？什麼是 3 x 3 矩陣做同樣的事？

$E = \begin{bmatrix} 3 & 3 \\ 5 & 2 \end{bmatrix}$ 和 $E = \begin{bmatrix} 3 & 7 \\ 2 &  \end{bmatrix}$

**19** 什麼是 3 x 3 矩陣 $E$ 乘以 $\begin{bmatrix} x \\ y \\ z \end{bmatrix}$ 產生 $\begin{bmatrix} x \\ y \\ z \end{bmatrix}$？什麼矩陣 $E^{-1}$ 乘以 $\begin{bmatrix} x \\ y \\ z \end{bmatrix}$ 產生 $\begin{bmatrix} x \\ y \\ z \end{bmatrix}$？如果你將 $(3, 4, 5)$ 乘以 $E$ 然後將結果乘以 $E^{-1}$，這兩個結果是 $(\quad)$ 和 $(\quad)$。

**20** 什麼是 2 x 2 矩陣 $P_1$ 將向量 $\begin{bmatrix} x \\ y \end{bmatrix}$ 投影到 x 軸以產生 $\begin{bmatrix} x \\ 0 \end{bmatrix}$？什麼是 2 x 2 矩陣 $P_2$ 將向量投影到 y 軸以產生 $\begin{bmatrix} 0 \\ y \end{bmatrix}$？如果將 $\begin{bmatrix} 5 \\ 7 \end{bmatrix}$ 乘以 $P_1$ 然後乘以 $P_2$，你得到 $(\quad)$。

**21** 什麼是 2 x 2 矩陣 $R$ 旋轉向量 $y$ 軸 45°？向量 $\begin{bmatrix} 1 \\ 0 \end{bmatrix}$ 變成 $\begin{bmatrix} \frac{\sqrt{2}}{2} \\ \frac{\sqrt{2}}{2} \end{bmatrix}$。向量 $\begin{bmatrix} 0 \\ 1 \end{bmatrix}$ 變成 $\begin{bmatrix}  \\  \end{bmatrix}$。因此確定矩陣 $\frac{1}{\sqrt{2}} \begin{bmatrix}  &  \\  &  \end{bmatrix}$。繪製向量 $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$ 在 $R$ 作用後的 xy 平面上，並找到 $R$。

**22** 寫下點積的定義。將 $\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$ 和 $\begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}$ 的點積計算出來。矩陣乘法 $A\mathbf{x}$ 是點積的組合。矩陣 $A = \begin{bmatrix} 1 & 2 & 3 \end{bmatrix}$ 和 $\mathbf{x} = \begin{bmatrix} 4 \\ 5 \\ 6 \end{bmatrix}$ 的矩陣乘法是 $\quad$。

**23** 在 MATLAB 中，矩陣 $A$ 的逆可以通過命令 `inv(A)` 找到。如果沒有逆矩陣，MATLAB 會顯示一個警告信息，並返回 `Inf` 或 `NaN`。

$A = \begin{bmatrix} 2 & 4 \\ 1 & 2 \end{bmatrix}$， $A^{-1} = \begin{bmatrix}  &  \\  &  \end{bmatrix}$

**24** 在 MATLAB 中，計算 $A^{-1}b$ 的命令是 `inv(A)*b`。使用 MATLAB 驗證 $A^{-1}b$ 的結果。
計算矩陣 $A = \begin{bmatrix} 2 & 4 \\ 1 & 2 \end{bmatrix}$ 的逆，並將其乘以向量 $\mathbf{b} = \begin{bmatrix} 3 \\ 4 \end{bmatrix}$。
