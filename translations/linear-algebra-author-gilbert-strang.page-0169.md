166

(b) 對於所有 **b** 都有無限多解
(c) 對於某些 **b** 有解，對於其他 **b** 無解
(d) 對於所有 **b** 都有唯一解

問題 26-33 要求使用高斯-喬丹消去法（向上和向下）以及簡化階梯形矩陣 **R**。

26 繼續從 **U** 到 **R** 的消去。將除以主元，使新的主元為 1。然後產生零從主元到要達到的 **R**。

   U =  
   \begin{bmatrix}
   2 & 4 & 4 \\
   0 & 3 & 6 \\
   0 & 0 & 0
   \end{bmatrix}
   和 
   U = 
   \begin{bmatrix}
   2 & 4 & 4 \\
   0 & 3 & 6 \\
   0 & 0 & 5
   \end{bmatrix}

27 假設 **U** 是具有 *n* 個主元的（可逆矩陣）的方陣。解釋為什麼 **R** = **I**。

28 應用高斯-喬丹消去法來求解 **Ux** = **0** 和 **Rx** = **c**。求 **Rx** = **0** 和 **Rx** = **d** 的解。

   \begin{bmatrix}
   1 & 2 & 3 & 0 \\
   0 & 4 & 0 & 0
   \end{bmatrix}
   **U** = 
   \begin{bmatrix}
   1 & 2 & 3 & 5 \\
   0 & 0 & 4 & 8
   \end{bmatrix}
   **U**

   求解 **Rx** = **0** 以求 **x<sub>n</sub>**（它的自由變數是 x<sub>2</sub> = 1）。求解 **Rx** = **d** 以求 **x<sub>p</sub>**（它的自由變數是 x<sub>2</sub> = 0）。

29 應用高斯-喬丹消去法來簡化 **Rx** = **0** 和 **Rx** = **d**。

   \begin{bmatrix}
   3 & 0 & 6 & 0 \\
   0 & 2 & 0 & 0 \\
   0 & 0 & 0 & 0
   \end{bmatrix}
   **U** = 
   \begin{bmatrix}
   3 & 0 & 6 & 9 \\
   0 & 2 & 4 \\
   0 & 0 & 5
   \end{bmatrix}
   **U**

   求解 **Ux** = **0** 或 **Rx** = **0** 以求 **x<sub>n</sub>**（自由變數是 x<sub>3</sub> = 1）。什麼是 **Rx** = **d** 的解？

30 將 **Ux** = **c** 簡化（高斯消去法），然後 **Rx** = **d**（高斯-喬丹法）。

   **Ax** = 
   \begin{bmatrix}
   1 & 0 & 2 & 3 \\
   1 & 3 & 2 & 0 \\
   2 & 0 & 4 & 9
   \end{bmatrix}
   \begin{bmatrix}
   x<sub>1</sub> \\ x<sub>2</sub> \\ x<sub>3</sub> \\ x<sub>4</sub>
   \end{bmatrix}
   = 
   \begin{bmatrix}
   2 \\ 5 \\ 10
   \end{bmatrix}
   = **b**

   找到一個特定的解 **x<sub>p</sub>** 和所有同質解 **x<sub>n</sub>**。

31 找到矩陣 **A** 和 **B**，具有給定的屬性或解釋你為什麼不能：

   (a)  **Ax** = 
   \begin{bmatrix}
   1 & 2 \\
   3 & 6
   \end{bmatrix}
   **x** = 
   \begin{bmatrix}
   1 \\
   2
   \end{bmatrix}
   的唯一解是 **x** = 
   \begin{bmatrix}
   0 \\
   1
   \end{bmatrix}

   (b)  **Bx** = 
   \begin{bmatrix}
   1 & 1 \\
   3 & 3
   \end{bmatrix}
   **x** = 
   \begin{bmatrix}
   1 \\
   2
   \end{bmatrix}
   的唯一解是 **x** = 
   \begin{bmatrix}
   1 \\
   1
   \end{bmatrix}
