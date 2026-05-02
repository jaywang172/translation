124

第 3 章 向量空間與子空間

定義 欄向量空間由欄的線性組合組成。所有可能的 Ax 組合填滿欄空間 C(A)。

這個欄向量空間對整本書至關重要，這也是為什麼我們要解 Ax = b，就是為了表達 b 是欄的組合。右側的 b 必須在 A 左側產生的欄空間中，否則無解！

如果 b 在欄空間中，則系統 Ax = b 可解。

當 b 在欄空間中時，它就是欄的組合。該組合中的係數給出了系統 Ax = b 的解。

假設 A 是一個 m x n 矩陣。它的欄有 n 個分量（而不是 m）。所以欄屬於 R<sup>m</sup>。A 的欄空間是 R<sup>m</sup> 的一個子空間（而不是 R<sup>n</sup>）。所有欄的線性組合都滿足規則 (i) 和 (ii) 以形成子空間。當我們將線性組合相加或乘以標量時，我們仍然會產生欄的組合。這個詞“子空間”就是通過進行線性組合來定義的。

這裡有一個 3x2 矩陣 A，它的欄空間是 R<sup>3</sup> 的一個子空間。A 的欄空間在圖 3.2 中是一個平面。

範例 4

Ax 是
\[
\begin{bmatrix}
1 & 0 \\
4 & 3 \\
2 & 3
\end{bmatrix}
\begin{bmatrix}
x_1 \\
x_2
\end{bmatrix}
\]
，這等於
\[
x_1
\begin{bmatrix}
1 \\
4 \\
2
\end{bmatrix}
+ x_2
\begin{bmatrix}
0 \\
3 \\
3
\end{bmatrix}
\]

\[
A =
\begin{bmatrix}
1 & 0 \\
4 & 3 \\
2 & 3
\end{bmatrix}
\]

\[
b = x_1
\begin{bmatrix}
1 \\
4 \\
2
\end{bmatrix}
+ x_2
\begin{bmatrix}
0 \\
3 \\
3
\end{bmatrix}
\]

平面 = C(A) = 所有 Ax

圖 3.2：欄空間 C(A) 是一個包含兩個欄的平面。如果 b 在該平面上，則 Ax = b 可解，b 是欄的組合。
