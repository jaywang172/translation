## 2.5. 反矩陣 93

**42** 直接乘法 1-4 給出 M⁻¹ = I，並且我建議進行第 4 個。M⁻¹ 顯示了當一個矩陣被減去來自 A 的東西時，A⁻¹ 的變化。

1  M = I - uvᵀ  和  M⁻¹ = I + uvᵀ/(1 - vᵀu) (rank 1 change in A)
2  M = A - uvᵀ  和  M⁻¹ = A⁻¹ + A⁻¹uvᵀA⁻¹/(1 - vᵀA⁻¹u)
3  M = I - UV  和  M⁻¹ = I + U(Im - VU)⁻¹V
4  M = A - UW - WV  和  M⁻¹ = A⁻¹ + A⁻¹U(W - VA⁻¹U)⁻¹VA⁻¹

Woodbury-Morrison 公式 4 是工程學中的“矩陣反演引理”。卡爾曼濾波器用於求解步進三對角系統，公式 4 在每個步驟中都會用到。這四個矩陣 M⁻¹ 是對角區塊，當反演這些區塊矩陣時（u 是 1 x n，v 是 n x 1，U 和 V 是 n x n，I 是 n x n）。

[圖片：四個矩陣公式，包含 u, v, U, V, I, A, W]

**43** 第二個差分矩陣具有更漂亮的特性，因為它們從 T₁₁ = 1 (而不是 T₁₁ = 2) 開始。這裡是一個 3 x 3 的三對角矩陣 T 及其反矩陣：

T₁₁ = 1
T =  [ 1  -1   0 ]
     [ -1   2  -1 ]
     [  0  -1   2 ]

T⁻¹ = [ 3  2  1 ]
      [ 2  2  1 ]
      [ 1  1  1 ]

一種方法是使用高斯-若爾丹消去法反演 [T]。這太機械化了。我更願意將 T 表示為第一差分矩陣 L 的乘積乘以 L 的轉置。L 和 U 在 Worked Example 2.5 A 中是稀疏矩陣，所以這裡有 T 和 T⁻¹。

L = [ 1  1  0 ]
    [ -1  1  1 ]
    [ 0  -1  1 ]

U = [ 1  0  0 ]
    [ -1  1  0 ]
    [ 0  -1  1 ]

difference  difference

Question: (4 by 4) What are both of T? What is its 4 by 4 inverse?
The reverse order UL gives what matrix T? What is the inverse of T?

**44** 這裡有兩個更重要的矩陣。但它們是可逆的？

Cyclic C = [ 2 -1  0 ]
            [ -1  2 -1 ]
            [  0 -1  2 ]

Free ends F = [ 1  0  0 ]
               [ 0  1  0 ]
               [ 0  0  1 ]

One test is elimination—the fourth pivot for an banded system is zero.
For the cyclic matrix, the last row is a linear combination of the first two rows.
The free ends F is not zero. Do mesh analysis, and you’ll discover the difference.

What do the matrices represent? C represents a cyclic network, and F represents a free ends network.
Which one is solvable, and which one is not?
