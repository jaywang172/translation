## 3.4. 完整解 Ax = b

**問題集 3.4**

**1** (推薦) 執行 3.4 範例中六個步驟，以描述 *A* 的行空間和零空間，以及 *Ax = b* 的完整解。

$$A = \begin{bmatrix} 2 & 4 & 6 & 4 \\ 2 & 5 & 7 & 6 \\ 2 & 3 & 5 & 2 \end{bmatrix}, \quad b = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix} = \begin{bmatrix} 4 \\ 5 \\ 3 \end{bmatrix}$$

**2** 對此矩陣 *A* 執行相同的六個步驟，你將找到關於 *b<sub>1</sub>*, *b<sub>2</sub>*, *b<sub>3</sub>* 的條件，使得 *Ax = b* 可解。將這些條件放在 *b* 之中，將其置於  空間（兩個平面給定一條線）之中。

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 3 & 9 \\ 4 & 2 & 6 \end{bmatrix}, \quad b = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix} = \begin{bmatrix} 10 \\ 30 \\ 20 \end{bmatrix}$$

**問題 3-15 均關於解 *Ax = b*。遵循書中步驟，以 *x<sub>p</sub>* 和 *x<sub>n</sub>* 的形式表示。使用帶有最後一欄的增廣矩陣。**

**3** 以 *x<sub>p</sub>* 加上零空間的任何倍數 *s* 的形式寫出完整解。

$$x + 3y + 3z = 1$$
$$2x + 6y + 9z = 5$$
$$-x - 3y + 3z = 5$$

**4** 找出 (也稱為一般解) 以下系統的完整解：

$$\begin{bmatrix} 1 & 3 & 2 \\ 2 & 6 & 4 \\ 0 & 0 & 2 & 4 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \\ t \end{bmatrix} = \begin{bmatrix} 1 \\ 3 \\ 1 \end{bmatrix}$$

**5** 在 *b<sub>1</sub>*, *b<sub>2</sub>*, *b<sub>3</sub>* 上有什麼條件，使得此系統可解？將 *b* 作為第四欄進行消去法。找出在該條件成立時的所有解。

$$x + 2y - 2z = b_1$$
$$2x + 5y - 4z = b_2$$
$$4x + 9y - 8z = b_3$$

**6** 在 *b<sub>1</sub>*, *b<sub>2</sub>*, *b<sub>3</sub>*, *b<sub>4</sub>* 上有什麼條件，使得每個系統可解？在這種情況下，找出 *x<sub>1</sub>* 和 *x<sub>2</sub>*。

$$\begin{bmatrix} 1 & 2 & 3 & 1 \\ 2 & 4 & 6 & 2 \\ 2 & 5 & 9 & 3 \\ 3 & 9 & b_4 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \\ b_4 \end{bmatrix}$$
