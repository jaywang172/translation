2
第 1 章 向量導論

1.1 向量與線性組合

「你不能把蘋果和橘子相加。」說來奇怪，這就是向量的緣由。我們有兩個獨立的數字 v_1 和 v_2。這對數字產生一個二維向量 v：

**列向量**
$$
\boldsymbol{v}=\left[\begin{array}{l}
v_{1} \\
v_{2}
\end{array}\right] \quad \begin{array}{l}
v_{1}=\text { 第一分量 } \\
v_{2}=\text { 第二分量 }
\end{array}
$$

我們將 v 寫成列的形式，而不是行的形式。到目前為止，重點是讓這對數字 v_1 和 v_2（淺色斜體）用單一字母 v（粗體斜體）表示。

即使我們不將 v_1 加到 v_2，我們仍然會將向量相加。v 和 w 的第一分量與第二分量保持獨立：

**向量加法**
$$
\boldsymbol{v}=\left[\begin{array}{l}
v_{1} \\
v_{2}
\end{array}\right] \quad \text { 和 } \quad \boldsymbol{w}=\left[\begin{array}{l}
w_{1} \\
w_{2}
\end{array}\right] \quad \text { 相加得到 } \quad \boldsymbol{v}+\boldsymbol{w}=\left[\begin{array}{l}
v_{1}+w_{1} \\
v_{2}+w_{2}
\end{array}\right] .
$$

你明白了原因。我們想要蘋果加蘋果。向量的減法也遵循相同的想法：v - w 的分量是 v_1 - w_1 和 v_2 - w_2。

另一個基本運算叫做純量乘法。向量可以乘以 2、乘以 -1，或乘以任何數字 c。有兩種方法可以將向量加倍。一種方法是將 v + v 相加。另一種方法（通常的方式）是將每個分量乘以 2：

**純量乘法**
$$
2 \boldsymbol{v}=\left[\begin{array}{l}
2 v_{1} \\
2 v_{2}
\end{array}\right] \quad \text { 和 } \quad -\boldsymbol{v}=\left[\begin{array}{l}
-v_{1} \\
-v_{2}
\end{array}\right] .
$$

cv 的分量是 cv_1 和 cv_2。數字 c 被稱為「純量」。

請注意，-v 和 v 的和是零向量。這是 0，它與數字零不同！向量 0 具有分量 0 和 0。請原諒我一直強調向量及其分量之間的差異。線性代數就是建立在這些運算 v + w 和 cv—向量加法和純量乘法之上的。

加法的順序沒有差別：v + w 等於 w + v。透過代數驗證：第一個分量是 v_1 + w_1，它等於 w_1 + v_1。也透過一個例子驗證：
$$
\boldsymbol{v}+\boldsymbol{w}=\left[\begin{array}{l}
1 \\
5
\end{array}\right]+\left[\begin{array}{l}
3 \\
3
\end{array}\right]=\left[\begin{array}{l}
4 \\
8
\end{array}\right] \quad \boldsymbol{w}+\boldsymbol{v}=\left[\begin{array}{l}
3 \\
3
\end{array}\right]+\left[\begin{array}{l}
1 \\
5
\end{array}\right]=\left[\begin{array}{l}
4 \\
8
\end{array}\right] .
$$
