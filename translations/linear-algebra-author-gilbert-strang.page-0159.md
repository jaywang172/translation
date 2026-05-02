156

第 3 章：向量空間與子空間

為了使解存在，R 中的零列必須為零。因為在主列和主變數的列中，x 的特定分量 d 來自：

$R_x = \begin{bmatrix} 1 & 3 & 0 & 2 \\ 0 & 0 & 1 & 4 \\ 0 & 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 1 \\ 0 \\ 6 \\ 0 \end{bmatrix}$  主變數 1, 6
                                                                自由變數 0, 0

注意我們如何選擇自由變數（為零）並求解主變數。在列簡化為 R 後，這些步驟很快。當主變數已經在右側向量 d 中時，主變數已經為零。

$x_{\text{particular}}$  特定解求解  $A x_p = b$
$x_{\text{nullspace}}$  零空間解求解  $A x_n = 0$

該特定解為 (1, 0, 6, 0)。兩個特殊（零空間）解為 3, 2, 和 4。請注意 0 來自 R 的兩列反向的列。請注意如何寫出完整的解 $x = x_p + x_n$，使得 $Ax = b$：

完整解
一個 $x_p$
許多 $x_n$

$x = x_p + x_n = \begin{bmatrix} 1 \\ 0 \\ 6 \\ 0 \end{bmatrix} + x_2 \begin{bmatrix} -3 \\ 1 \\ 0 \\ 0 \end{bmatrix} + x_4 \begin{bmatrix} -2 \\ 0 \\ -4 \\ 1 \end{bmatrix}$

問題  假設 A 是一個可逆的方陣，即 $n = m = r$。那麼 $x_p$ 和 $x_n$ 是什麼？
答案  特定解是唯一的，只有一個解 $A^{-1} b$。不存在零空間解。零空間中的唯一向量是 $x_n = 0$。完整的解是 $x = x_p + x_n = A^{-1} b + 0$。

這是我們在第 2 章中遇到的情況。我們沒有在零空間中找到任何東西。N(A) 包含零向量。從 $[A \ b]$ 簡化到 $[I \ A^{-1} b]$。原始 $Ax = b$ 簡化為 $x = A^{-1} b$。這是一個特殊情況。因為 $A$ 是可逆的，所以這些矩陣的方式是我們在數學上看到的。請參閱本章的開頭。

例如，MATLAB 會以這種方式求解 $[A \ b]$。對於大型矩陣，MATLAB 會執行部分 LU 分解（不一定需要樞軸）。這是一個例子，其中包含完整解（注意列的總和為零）。

例子 1  找到條件數的伴隨矩陣 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ 的主變數。

$A x = b$
$\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \end{bmatrix}$

這可以簡化為：
$\begin{bmatrix} 1 & 2 \\ 0 & -2 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 - 3b_1 \end{bmatrix}$
