# 随机事件和概率

## 1. 概率的定义和性质

### (1) 概率的公理化定义  
设Ω为样本空间，A为事件，对每一个事件A都定义一个数 $ P(A) $，满足以下条件：  
1. $ 0 \leq P(A) \leq 1 $  
2. $ P(Ω) = 1 $  
3. 对于两个两两互不相容的事件 $ A_1, A_2, \ldots $，有：  
$$
P\left( \bigcup_{i=1}^\infty A_i \right) = \sum_{i=1}^\infty P(A_i)
$$  
**注：** 第3条称为概率的可加性。  

### (2) 古典概率（等可能概率）  
1. $ 0 \leq P(A) \leq 1 $  
2. $ P(Ω) = 1 $  

设样本空间Ω中的每个基本事件 $ \omega_i $ 的概率均为等可能，即  
$$
P(\omega_i) = \frac{1}{n}, \quad n \text{ 为基本事件个数}
$$  
设事件A包含的基本事件为 $ \omega_1, \omega_2, \ldots, \omega_m $，则  
$$
P(A) = P(\omega_1) + P(\omega_2) + \cdots + P(\omega_m) = \frac{m}{n}
$$  
其中 $ m $ 为A包含的基本事件数，$ n $ 为基本事件总数。

---

## 2. 五大公式（加法、减法、乘法、全概、贝叶斯）

### (1) 加法公式  
$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$  
当 $ P(A \cap B) = 0 $ 时，  
$$
P(A \cup B) = P(A) + P(B)
$$

### (2) 减法公式  
$$
P(A - B) = P(A) - P(A \cap B)
$$  
当 $ B \subseteq A $ 时，  
$$
P(A - B) = P(A) - P(B)
$$  
当 $ A \cap B = 0 $ 时，  
$$
P(B') = 1 - P(B)
$$

### (3) 条件概率和乘法公式  
定义：设 $ A, B $ 是两个事件，且 $ P(A) > 0 $，则在事件 $ A $ 发生的条件下，事件 $ B $ 发生的条件概率，记为  
$$
P(B | A) = \frac{P(AB)}{P(A)}
$$  
**注：** 条件概率是概率的更新，所有概率的性质适合于条件概率。

### (4) 全概率公式  
设事件 $ B_1, B_2, \ldots, B_n $ 满足：  
- $ B_1, B_2, \ldots, B_n $ 两两互不相容，  
- $ P(B_i) > 0 \, (i = 1, 2, \ldots, n) $，  
- $ A \subseteq \bigcup_{i=1}^n B_i $。  

则  
$$
P(A) = P(B_1)P(A|B_1) + P(B_2)P(A|B_2) + \cdots + P(B_n)P(A|B_n)
$$  
**此公式即为全概率公式。**

### (5) 贝叶斯公式  
设事件 $ B_1, B_2, \ldots, B_n $ 及 $ A $ 满足：  
- $ B_1, B_2, \ldots, B_n $ 两两互不相容，$ P(B_i) > 0 \, (i = 1, 2, \ldots, n) $；  
- $ A \subseteq \bigcup_{i=1}^n B_i $。  

$$
P(B_i | A) = \frac{P(B_i)P(A | B_i)}{\sum_{j=1}^n P(B_j)P(A | B_j)}, \quad i = 1, 2, \ldots, n
$$  
- $ P(B_i | A) $：后验概率  
- $ P(A | B_i) $：似然概率  
- $ P(B_i) $：先验概率

---

## 3. 事件的独立性和伯努利试验

### (1) 两个事件的独立性  
设事件 $ A, B $ 满足  
$$
P(AB) = P(A)P(B)
$$  
则称事件 $ A, B $ 是相互独立的（这个性质不是概念的定义）。  

**注意：**  
- 若事件 $ A, B $ 互不相容，则 $ AB = \emptyset $，有 $ P(AB) = 0 $，因此 $ A, B $ 不能独立。  
- 若事件 $ A, B $ 相互独立，则有：  
$$
P(B | A) = P(B), \quad P(A | B) = P(A)
$$

### (2) 多个事件的独立性  
设 $ A, B, C $ 是三个事件，如果满足两两独立，则称为多个事件的独立性。

## 伯努利试验与随机变量分布

### 伯努利试验

定义：我们进行了 $ n $ 次独立、重复试验。  
- 每次试验只有两种可能结果：A发生或A不发生；  
- 每次试验是独立的，即A发生的概率 $ p $ 在每次试验中相同。  
- 设事件A发生的概率为 $ p $，则A不发生的概率为 $ q = 1-p $。  

记：  
- $ p $：事件A发生的概率  
- $ q = 1-p $：事件A不发生的概率  

若事件A在 $ n $ 次试验中恰好发生 $ k $ 次，其概率为：  
$$
P(X=k) = C_n^k p^k q^{n-k}, \quad k=0,1,2,\ldots,n
$$

---

## 随机变量及其分布

### 1. 随机变量的分布函数

定义：对于任意随机变量 $ X $，称函数  
$$
F(x) = P(X \leq x)
$$  
为随机变量 $ X $ 的分布函数。

性质：  
1. $ 0 \leq F(x) \leq 1, \, -\infty < x < \infty $  
2. $ F(x) $ 是非减函数。  
3. $ F(+\infty) = \lim_{x \to \infty} F(x) = 1, \quad F(-\infty) = 0 $  
4. 若 $ F(x) $ 在 $ x $ 处连续，则 $ P(X=x)=0 $。

---

### 2. 离散型随机变量的分布率

设离散型随机变量 $ X $ 的取值为 $ x_k \, (k=1,2,\ldots) $。  
各个值的概率为：  
$$
P(X=x_k) = p_k
$$  

条件：  
1. $ p_k \geq 0, \, k=1,2,\ldots $  
2. $\sum_{k=1}^\infty p_k = 1$

---

### 3. 连续型随机变量的密度函数

定义：若存在非负函数 $ f(x) $，使得：  
$$
F(x) = \int_{-\infty}^x f(t) \, dt
$$  
则称 $ X $ 为连续型随机变量，$ f(x) $ 为概率密度函数。

性质：  
1. $ f(x) \geq 0 $  
2. $\int_{-\infty}^\infty f(x) \, dx = 1$  
3. $ F(x_2) - F(x_1) = \int_{x_1}^{x_2} f(x) \, dx $  

---

## 2. 常见分布

### (1) 0-1 分布  
$$
P(X=1) = p, \quad P(X=0) = q
$$

---

### (2) 二项分布  
在重复试验中，若事件A发生的概率为 $ p $，事件A发生的次数随机变量 $ X $ 服从二项分布：  
$$
P(X=k) = C_n^k p^k q^{n-k}, \quad q=1-p
$$  
记作： $ X \sim B(n, p) $。

---

### (3) 泊松分布  
$$
P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k=0,1,2,\ldots, \lambda>0
$$  
称随机变量 $ X $ 服从参数 $ \lambda $ 的泊松分布，记作： $ X \sim P(\lambda) $。

---

### (4) 超几何分布  
$$
P(X=k) = \frac{C_M^k C_{N-M}^{n-k}}{C_N^n}, \quad k=0,1,2,\ldots
$$  
随机变量 $ X $ 服从参数 $ N, M, n $ 的超几何分布。

---

### (5) 几何分布  
$$
P(X=k) = q^{k-1}p, \quad k=1,2,3,\ldots
$$  
其中 $ q = 1-p $。

---

### (6) 均匀分布  
$$
f(x) =
\begin{cases}
\frac{1}{b-a}, & a \leq x \leq b \\
0, & \text{其他}
\end{cases}
$$  
随机变量 $ X $ 服从区间 $ [a, b] $ 上的均匀分布。

---

## 3. 指数分布

设随机变量 $ X $ 的密度函数为：  
$$
f(x) = 
\begin{cases} 
\lambda e^{-\lambda x}, & x \geq 0, \\
0, & x < 0.
\end{cases}
$$  
其中 $ \lambda > 0 $，则 $ X $ 服从参数为 $ \lambda $ 的指数分布。

分布函数为：  
$$
F(x) = 
\begin{cases} 
1 - e^{-\lambda x}, & x \geq 0, \\
0, & x < 0.
\end{cases}
$$

---

## 4. 正态分布

设随机变量 $ X $ 的密度函数为：  
$$
f(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}, \quad -\infty < x < \infty
$$  
其中 $ \mu $ 为均值，$ \sigma > 0 $ 为标准差，称 $ X $ 服从参数为 $ \mu, \sigma^2 $ 的正态分布，记为 $ X \sim N(\mu, \sigma^2) $。

**标准正态分布：**  
当 $ \mu = 0, \sigma = 1 $ 时，密度函数为：  
$$
\phi(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}.
$$

---

## 5. 随机变量函数的分布

### (1) $ X $ 是离散型随机变量  
已知 $ X $ 的分布列为：  

| $ X $ | $ x_1 $ | $ x_2 $ | $ \cdots $ | $ x_n $ |
| ----- | ------- | ------- | ---------- | ------- |
| $ P $ | $ p_1 $ | $ p_2 $ | $ \cdots $ | $ p_n $ |

若 $ Y = g(X) $，则 $ Y $ 的分布为：  
$$
P(Y = y_j) = \sum_{i \in A_j} P(X = x_i)
$$  
其中 $ A_j $ 是使 $ g(x_i) = y_j $ 成立的所有 $ x_i $。

### (2) $ X $ 是连续型随机变量  
若 $ X $ 的密度函数为 $ f(x) $，且 $ Y = g(X) $，则 $ Y $ 的密度函数为：  
$$
f_Y(y) = f_X(x) \left| \frac{dx}{dy} \right|.
$$

# 三、二维随机变量及其分布

## 1. 二维随机变量的基本概念

### (1) 二维随机变量的联合分布函数  
设二维随机变量 $\xi = (X, Y)$，其联合分布函数为：  
$$
F(x, y) = P(X \leq x, Y \leq y)
$$  

### (2) 条件分布  
若 $X, Y$ 是离散型随机变量，则条件概率为：  
$$
P(Y = y_j \mid X = x_i) = \frac{p_{ij}}{p_i}
$$  
其中 $p_i = \sum_j p_{ij}$。

对于连续型随机变量，若联合密度为 $f(x, y)$，则条件密度为：  
$$
f_{Y|X}(y | x) = \frac{f(x, y)}{f_X(x)}
$$  
其中 $f_X(x) = \int_{-\infty}^\infty f(x, y) \, dy$。

---

## 2. 随机变量的独立性

### (1) 连续型随机变量  
设 $f(x, y) = f_X(x)f_Y(y)$，则 $X$ 和 $Y$ 相互独立。

### (2) 二维正态分布  
设随机变量 $(X, Y)$ 的联合密度函数为：  
$$
f(x, y) = \frac{1}{2\pi\sigma_X\sigma_Y\sqrt{1-\rho^2}} 
\exp\left( -\frac{1}{2(1-\rho^2)} 
\left[ \frac{(x-\mu_X)^2}{\sigma_X^2} + \frac{(y-\mu_Y)^2}{\sigma_Y^2} - \frac{2\rho(x-\mu_X)(y-\mu_Y)}{\sigma_X\sigma_Y} \right] \right)
$$  
其中 $\rho$ 为相关系数。

---

# 四、随机变量的数字特征

## 1. 一维随机变量的期望

### (1) 离散型随机变量  
若 $X$ 为离散型随机变量，取值为 $x_k$，概率为 $p_k$，则：  
$$
E(X) = \sum_{k=1}^n x_k p_k
$$  

### (2) 连续型随机变量  
若 $X$ 为连续型随机变量，密度函数为 $f(x)$，则：  
$$
E(X) = \int_{-\infty}^\infty x f(x) \, dx
$$  

---

## 2. 方差  
方差定义为：  
$$
D(X) = E\left[(X - E(X))^2\right]
$$  

性质：  
1. $D(C) = 0, \, E(C) = C$  
2. $D(aX) = a^2 D(X)$  
3. $D(X + Y) = D(X) + D(Y)$，当 $X$ 和 $Y$ 独立时。  

---

## 3. 协方差与相关系数

### (1) 协方差  
设 $X$ 和 $Y$ 为随机变量，其协方差为：  
$$
\text{cov}(X, Y) = E[(X - E(X))(Y - E(Y))]
$$  

### (2) 相关系数  
相关系数定义为：  
$$
\rho_{XY} = \frac{\text{cov}(X, Y)}{\sqrt{D(X)D(Y)}}
$$  
其中 $-1 \leq \rho_{XY} \leq 1$。

---

# 五、大数定律和中心极限定理

## 1. 切比雪夫不等式  
设随机变量 $X$ 具有数学期望 $E(X) = \mu$ 和方差 $D(X) = \sigma^2$，则对于任意 $\varepsilon > 0$：  
$$
P(|X - \mu| \geq \varepsilon) \leq \frac{\sigma^2}{\varepsilon^2}
$$  

---

## 2. 伯努利大数定律  
设事件 $A$ 在 $n$ 次独立试验中发生的概率为 $p$，则：  
$$
\lim_{n \to \infty} P\left( \left| \frac{X_n}{n} - p \right| < \varepsilon \right) = 1
$$  
其中 $X_n$ 表示事件 $A$ 发生的次数。

---

## 3. 中心极限定理  
设 $X_1, X_2, \dots, X_n$ 相互独立，服从相同的分布，且具有数学期望和方差：  
$$
E(X_i) = \mu, \quad D(X_i) = \sigma^2
$$  
则：  
$$
\lim_{n \to \infty} P\left( \frac{\sum_{i=1}^n X_i - n\mu}{\sigma\sqrt{n}} \leq x \right) = \int_{-\infty}^x \frac{1}{\sqrt{2\pi}} e^{-t^2 / 2} \, dt
$$  
即样本均值服从正态分布。

---

# 六、数理统计的基本概念

## 1. 总体、个体和样本  
- **总体**：统计研究的对象集合。  
- **个体**：总体中的每一个元素。  
- **样本**：从总体中抽取的一个子集。  

---

## 2. 统计量

### (1) 样本均值  
设样本为 $x_1, x_2, \dots, x_n$，则样本均值为：  
$$
\bar{X} = \frac{1}{n} \sum_{i=1}^n x_i
$$  

### (2) 样本方差  
样本方差定义为：  
$$
S^2 = \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{X})^2
$$  

