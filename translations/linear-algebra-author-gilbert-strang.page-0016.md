1.2. 長度與點積

13

圖 1.6：二維與三維向量的長度 $\sqrt{v \cdot v}$。

$(0, 2)$
$(1, 2)$
$\sqrt{5}$
$2$
$1$
$(1, 0)$

$v \cdot v = v_1^2 + v_2^2 + v_3^2$
$5 = 1^2 + 2^2$
$14 = 1^2 + 2^2 + 3^2$

$(0, 0, 3)$
$(1, 2, 3)$ 的長度為 $\sqrt{14}$
$(0, 2, 0)$
$(1, 2, 0)$ 的長度為 $\sqrt{5}$
$(1, 0, 0)$

例題 4 沿 $x$ 軸和 $y$ 軸的標準單位向量寫作 $i$ 和 $j$。在 $xy$ 平面中，與 $x$ 軸成「θ」角的單位向量為 $(\cos \theta, \sin \theta)$：

單位向量
$i = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ 且 $j = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$ 且 $u = \begin{bmatrix} \cos \theta \\ \sin \theta \end{bmatrix}$。

當 $\theta = 0$ 時，水平向量 $u$ 是 $i$。當 $\theta = 90^\circ$ ($\frac{\pi}{2}$ 弧度) 時，垂直向量是 $j$。在任何角度下，分量 $\cos \theta$ 和 $\sin \theta$ 產生 $u \cdot u = 1$ 因為 $\cos^2 \theta + \sin^2 \theta = 1$。這些向量延伸到圖 1.7 中的單位圓。因此，$\cos \theta$ 和 $\sin \theta$ 只是該點在單位圓上、角度為 $\theta$ 時的坐標。
由於 $(2, 2, 1)$ 的長度為 3，向量 $(\frac{2}{3}, \frac{2}{3}, \frac{1}{3})$ 的長度為 1。請驗證 $u \cdot u = \frac{4}{9} + \frac{4}{9} + \frac{1}{9} = 1$。對於單位向量，將任何非零向量 $v$ 除以其長度 $||v||$。

單位向量
$u = v/||v||$ 是一個與 $v$ 同方向的單位向量。

$j = (0, 1)$
$v = (1, 1)$
$u = (\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}) = \frac{v}{||v||}$
$i = (1, 0)$
$-i$
$-j$

$j$
$u = \begin{bmatrix} \cos \theta \\ \sin \theta \end{bmatrix}$
$1$
$\theta$
$\sin \theta$
$i$
$\cos \theta$

圖 1.7：坐標向量 $i$ 和 $j$。位於 $45^\circ$ 角的單位向量 $u$（左圖）是將 $v = (1, 1)$ 除以其長度 $||v|| = \sqrt{2}$ 得到。單位向量 $u = (\cos \theta, \sin \theta)$ 位於角度 $\theta$。
