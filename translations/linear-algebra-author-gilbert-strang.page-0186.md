3.5. 獨立性、基底與維度                                                                   183

**挑戰問題**

41  將 $3 \times 3$ 單位矩陣寫成其他五個置換矩陣的線性組合！接著證明這五個矩陣是線性獨立的。（假設一個組合給出 $c_1 P_1 + \cdots + c_5 P_5 = \text{零矩陣}$，並檢查各個分量以證明 $c_i$ 為零。）這五個置換矩陣構成了所有行和與列和皆相等的 $3 \times 3$ 矩陣子空間的一組基底。

42  在 $\mathbb{R}^4$ 中選擇 $x = (x_1, x_2, x_3, x_4)$。它有 24 種重新排列，例如 $(x_2, x_1, x_3, x_4)$ 和 $(x_4, x_3, x_1, x_2)$。這 24 個向量（包含 $x$ 本身）生成一個子空間 $\mathbf{S}$。請找出特定的向量 $x$，使得 $\mathbf{S}$ 的維度為：(a) 零，(b) 一，(c) 三，(d) 四。

43  交集與和滿足 $\dim(\mathbf{V}) + \dim(\mathbf{W}) = \dim(\mathbf{V} \cap \mathbf{W}) + \dim(\mathbf{V} + \mathbf{W})$。從交集 $\mathbf{V} \cap \mathbf{W}$ 的一組基底 $u_1, \dots, u_r$ 開始。將其擴展為 $\mathbf{V}$ 的基底 $u_1, \dots, u_r, v_1, \dots, v_s$，以及分別擴展為 $\mathbf{W}$ 的基底 $u_1, \dots, u_r, w_1, \dots, w_t$。證明 $u$、$v$ 和 $w$ 的集合共同地是**獨立的**。則維度滿足 $(r + s) + (r + t) = (r) + (r + s + t)$，正如所期望的。

44  Mike Artin 建議針對問題 43 的維度公式提供一個精妙的高階證明。對於所有來自 $\mathbf{V}$ 的輸入 $v$ 和來自 $\mathbf{W}$ 的輸入 $w$，「和轉換」會產生 $v + w$。這些輸出填滿了空間 $\mathbf{V} + \mathbf{W}$。零空間包含所有滿足 $v = u, w = -u$ 的 pair $(v, w)$，其中向量 $u \in \mathbf{V} \cap \mathbf{W}$。（此時 $v + w = u - u = \mathbf{0}$。）因此 $\dim(\mathbf{V} + \mathbf{W}) + \dim(\mathbf{V} \cap \mathbf{W})$ 等於 $\dim(\mathbf{V}) + \dim(\mathbf{W})$（來自 $\mathbf{V}$ 和 $\mathbf{W}$ 的輸入維度），這符合關鍵公式：

$\text{輸出維度} + \text{零空間維度} = \text{輸入維度}$

問題：對於一個秩為 $r$ 的 $m \times n$ 矩陣，這三個維度分別是什麼？輸出 = 列空間。這個問題將在 3.6 節中解答，你現在能做到嗎？

45  在 $\mathbb{R}^n$ 中，假設 $\text{dimension}(\mathbf{V}) + \text{dimension}(\mathbf{W}) > n$。證明存在某個非零向量同時在 $\mathbf{V}$ 和 $\mathbf{W}$ 中。

46  假設 $A$ 是 $10 \times 10$ 矩陣且 $A^2 = 0$（零矩陣）。這意味著 $A$ 的列空間包含在 ______ 之中。若 $A$ 的秩為 $r$，則這些子空間的維度滿足 $r \le 10 - r$。因此秩為 $r \le 5$。

（此問題添加於第二次印刷：若 $A^2 = 0$，則它說明 $r \le n/2$。）
