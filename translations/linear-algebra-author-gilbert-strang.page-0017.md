14

第 1 章 向量介紹

**兩向量之間的夾角**

我們曾指出垂直向量的點積為 $\boldsymbol{v} \cdot \boldsymbol{w}=0$。當夾角為 $90^{\circ}$ 時，點積為零。為了說明這一點，我們必須將角度與點積聯繫起來。然後我們將展示 $\boldsymbol{v} \cdot \boldsymbol{w}$ 如何找出任意兩個非零向量 $\boldsymbol{v}$ 和 $\boldsymbol{w}$ 之間的夾角。

**直角**
當 $\boldsymbol{v}$ 垂直於 $\boldsymbol{w}$ 時，點積為 $\boldsymbol{v} \cdot \boldsymbol{w}=0$。

**證明** 當 $\boldsymbol{v}$ 和 $\boldsymbol{w}$ 垂直時，它們形成一個直角三角形的兩條邊。第三條邊是 $\boldsymbol{v}-\boldsymbol{w}$ (圖 1.8 中斜邊橫跨的邊)。直角三角形邊長的畢氏定理是 $a^2 + b^2 = c^2$：

垂直向量 $\| \boldsymbol{v} \|^2 + \| \boldsymbol{w} \|^2 = \| \boldsymbol{v} - \boldsymbol{w} \|^2$ (2)

將這些長度在二維空間中的公式寫出來，這個方程式是
$(\boldsymbol{v}_1^2 + \boldsymbol{v}_2^2) + (\boldsymbol{w}_1^2 + \boldsymbol{w}_2^2) = (\boldsymbol{v}_1 - \boldsymbol{w}_1)^2 + (\boldsymbol{v}_2 - \boldsymbol{w}_2)^2$ (3)

右側從 $\boldsymbol{v}_1^2 - 2\boldsymbol{v}_1\boldsymbol{w}_1 + \boldsymbol{w}_1^2$ 開始。然後 $\boldsymbol{v}_1^2$ 和 $\boldsymbol{w}_1^2$ 在等式兩邊，它們會抵消，剩下 $-2\boldsymbol{v}_1\boldsymbol{w}_1$。同樣地，$\boldsymbol{v}_2^2$ 和 $\boldsymbol{w}_2^2$ 也會抵消，剩下 $-2\boldsymbol{v}_2\boldsymbol{w}_2$。(在三維空間中，將會有 $-2\boldsymbol{v}_3\boldsymbol{w}_3$。)現在除以 $-2$：
$0 = -2\boldsymbol{v}_1\boldsymbol{w}_1 - 2\boldsymbol{v}_2\boldsymbol{w}_2$ 這導致 $\boldsymbol{v}_1\boldsymbol{w}_1 + \boldsymbol{v}_2\boldsymbol{w}_2 = 0$ (4)

**結論** 直角會產生 $\boldsymbol{v} \cdot \boldsymbol{w}=0$。當夾角為 $\theta=90^{\circ}$ 時，點積為零。則 $\cos \theta=0$。零向量 $\boldsymbol{v}=\boldsymbol{0}$ 垂直於每個向量 $\boldsymbol{w}$，因為 $\boldsymbol{0} \cdot \boldsymbol{w}$ 始終為零。

現在假設 $\boldsymbol{v} \cdot \boldsymbol{w}$ 不為零。它可能是正的，也可能是負的。$\boldsymbol{v} \cdot \boldsymbol{w}$ 的正負號立即告訴我們是小於還是大於直角。當 $\boldsymbol{v} \cdot \boldsymbol{w}$ 為正時，夾角小於 $90^{\circ}$。當 $\boldsymbol{v} \cdot \boldsymbol{w}$ 為負時，夾角大於 $90^{\circ}$。圖 1.8 的右側顯示了一個典型的向量 $\boldsymbol{v}=(3,1)$。與 $\boldsymbol{w}=(1,3)$ 的夾角小於 $90^{\circ}$，因為 $\boldsymbol{v} \cdot \boldsymbol{w}=6$ 為正。

$\boldsymbol{v} = \begin{bmatrix} -1 \\ 2 \end{bmatrix}$ $\boldsymbol{w} = \begin{bmatrix} 4 \\ 2 \end{bmatrix}$
$\sqrt{25}$
$\sqrt{5}$ $\sqrt{20}$
$\boldsymbol{v} \cdot \boldsymbol{w} < 0$
此半平面中角度大於 $90^{\circ}$
$\boldsymbol{v} \cdot \boldsymbol{w} = 0$
$\boldsymbol{v} \cdot \boldsymbol{w} > 0$
此半平面中角度小於 $90^{\circ}$
$5+20=25$

圖 1.8：垂直向量的點積為 $\boldsymbol{v} \cdot \boldsymbol{w}=0$。則 $\| \boldsymbol{v} \|^2 + \| \boldsymbol{w} \|^2 = \| \boldsymbol{v} - \boldsymbol{w} \|^2$。
