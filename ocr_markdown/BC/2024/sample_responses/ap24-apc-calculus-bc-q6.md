<!-- Page 1 -->

2024

AP

# AP® Calculus BC
## Sample Student Responses and Scoring Commentary

### Inside:

Free-Response Question 6

- ☑ Scoring Guidelines
- ☑ Student Samples
- ☑ Scoring Commentary

© 2024 College Board. College Board, Advanced Placement, AP, AP Central, and the acorn logo are registered trademarks of College Board. Visit College Board on the web: collegeboard.org.

AP Central is the official online home for the AP Program: apcentral.collegeboard.org.

<!-- Page 2 -->

AP® Calculus AB/BC 2024 Scoring Guidelines

### Part B (BC): Graphing calculator not allowed

#### Question 6

9 points

#### General Scoring Notes

The model solution is presented using standard mathematical notation.

Answers (numeric or algebraic) need not be simplified. Answers given as a decimal approximation should be correct to three places after the decimal point. Within each individual free-response question, at most one point is not earned for inappropriate rounding.

The Maclaurin series for a function \( f \) is given by \( \sum_{n=1}^{\infty} \frac{(n+1)x^n}{n^2 6^n} \) and converges to \( f(x) \) for all \( x \) in the interval of convergence. It can be shown that the Maclaurin series for \( f \) has a radius of convergence of 6.

|  Model Solution | Scoring  |   |
| --- | --- | --- |
|  (a) Determine whether the Maclaurin series for \( f \) converges or diverges at \( x = 6 \). Give a reason for your answer.  |   |   |
|  At \( x = 6 \), the series is \( \sum_{n=1}^{\infty} \frac{(n+1)6^{n}}{n^{2}6^{n}} = \sum_{n=1}^{\infty} \frac{n+1}{n^{2}} \). | Considers \( \frac{(n+1)6^{n}}{n^{2}6^{n}} \) | 1 point  |
|  Because \( \frac{n+1}{n^{2}} > \frac{1}{n} \) for all \( n \geq 1 \) and the harmonic series \( \sum_{n=1}^{\infty} \frac{1}{n} \) diverges, the series \( \sum_{n=1}^{\infty} \frac{n+1}{n^{2}} \) diverges by the comparison test. | Answer with reason | 1 point  |

© 2024 College Board

<!-- Page 3 -->

AP® Calculus AB/BC 2024 Scoring Guidelines

# Scoring notes:

- To earn the first point using either the comparison or limit comparison test, a response must consider the term $\frac{(n+1)6^n}{n^26^n}$. This could be shown by considering the term $\frac{n+1}{n^2}$, either individually or as part of a sum.

- To earn the second point using the comparison test a response must demonstrate that the terms $\frac{n+1}{n^2}$ are larger than the terms in a divergent series.

o “$\frac{n+1}{n^2} > \frac{1}{n}$, diverges” earns both points.

o The response does not need to use the term “comparison test,” but the response cannot declare use of an incorrect test.

- Alternate solution (limit comparison test):

At $x = 6$, the series is $\sum_{n=1}^{\infty} \frac{(n+1)6^n}{n^26^n} = \sum_{n=1}^{\infty} \frac{n+1}{n^2}$.

Because $\lim_{n \to \infty} \frac{\frac{n+1}{n^2}}{\frac{1}{n}} = \lim_{n \to \infty} \frac{n^2 + n}{n^2} = 1$ and the harmonic series $\sum_{n=1}^{\infty} \frac{1}{n}$ diverges, the series

$\sum_{n=1}^{\infty} \frac{n+1}{n^2}$ diverges by the limit comparison test.

o To earn the second point using the limit comparison test, a response must correctly write the limit of the ratio of the terms in the given series to the terms of a divergent series and demonstrate that the limit of this ratio is 1.

o The response does not need to use the term “limit comparison test,” but the response cannot declare use of an incorrect test.

Total for part (a) 2 points

© 2024 College Board

<!-- Page 4 -->

AP® Calculus AB/BC 2024 Scoring Guidelines

(b)

It can be shown that $$f(-3) = \sum_{n=1}^{\infty} \frac{(n+1)(-3)^n}{n^2 6^n} = \sum_{n=1}^{\infty} \frac{n+1}{n^2} \left(-\frac{1}{2}\right)^n$$ and that the first three terms of this series sum to $$S_3 = -\frac{125}{144}$$. Show that $$|f(-3) - S_3| < \frac{1}{50}$$.

$$f(-3) = \sum_{n=1}^{\infty} \frac{(n+1)(-3)^n}{n^2 6^n} = \sum_{n=1}^{\infty} \frac{(n+1)}{n^2} \left(-\frac{1}{2}\right)^n$$ is an alternating series with terms that decrease in magnitude to 0.

By the alternating series error bound, $$\sum_{n=1}^{3} \frac{n+1}{n^2} \left(-\frac{1}{2}\right)^n = -\frac{125}{144}$$ approximates $$f(-3)$$ with error of at most

$$\left| \frac{4+1}{4^2} \left(-\frac{1}{2}\right)^4 \right| = \frac{5}{256} < \frac{5}{250} = \frac{1}{50}.$$

Thus, $$|f(-3) - S_3| < \frac{1}{50}$$.

|  Uses fourth term | 1 point  |
| --- | --- |
|  Verification | 1 point  |

# Scoring notes:

- The first point is earned for correctly using $$x = -3$$ in the fourth term. (Listing the fourth term as part of a polynomial is not sufficient.) Using $$x = -3$$ in any term of degree five or higher does not earn this point.
- The expression $$\frac{4+1}{4^2} \left(-\frac{1}{2}\right)^4$$ earns the first point, but just $$\frac{5}{256}$$ does not earn the first point.
- A response including the expression $$\frac{4+1}{4^2} \left(-\frac{1}{2}\right)^4$$ that is subsequently simplified incorrectly earns the first point but not the second.
- To earn the second point the response must state that the series for $$f(-3)$$ is alternating or that the alternating series error bound is being used.
  - A response of just “Error $$\le \frac{4+1}{4^2} \left(-\frac{1}{2}\right)^4 < \frac{1}{50}$$” (or any equivalent mathematical expression) earns both points, provided it is accompanied by an indication that the series is alternating.
- A response that declares the error is equal to $$\frac{5}{256}$$ (or any equivalent form of this value) does not earn the second point.

Total for part (b) 2 points

© 2024 College Board

<!-- Page 5 -->

AP® Calculus AB/BC 2024 Scoring Guidelines

(c) Find the general term of the Maclaurin series for $f'$, the derivative of $f$. Find the radius of convergence of the Maclaurin series for $f'$.

|  The general term of the Maclaurin series for $f'$ is $$\frac{(n+1)nx^{n-1}}{n^26^n} = \frac{(n+1)x^{n-1}}{n \cdot 6^n}.$$ | General term | **1 point**  |
| --- | --- | --- |
|  Because the radius of convergence of the Maclaurin series for $f$ is 6, the radius of convergence of the Maclaurin series for $f'$ is also 6. | Radius | **1 point**  |

# Scoring notes:

- A response of $\frac{(n+1)nx^{n-1}}{n^26^n}$ earns the first point. Any expression mathematically equivalent to this also earns the first point.
- The response need not simplify $\frac{(n+1)nx^{n-1}}{n^26^n}$, but any presented simplification must be correct in order to earn the first point.
- The second point is earned only for a supported answer of 6. The second point can be earned without the first.
- Alternate solution for second point (ratio test):

$$\lim_{n \to \infty} \left| \frac{\frac{(n+2)x^n}{(n+1)6^{n+1}}}{\frac{(n+1)x^{n-1}}{n \cdot 6^n}} \right| = \lim_{n \to \infty} \left| \frac{n(n+2)}{(n+1)^2} \cdot \frac{x}{6} \right| = \frac{|x|}{6} < 1 \Rightarrow |x| < 6$$

Therefore, the radius of convergence of the Maclaurin series for $f'$ is 6.

- Alternate solution for second point (root test):

$$\lim_{n \to \infty} \sqrt[n]{\frac{(n+1)|x|^{n-1}}{n \cdot 6^n}} = \lim_{n \to \infty} \left( \frac{n+1}{n} \right)^{1/n} \cdot |x|^{-1/n} \cdot \frac{|x|}{6} = 1 \cdot 1 \cdot \frac{|x|}{6} < 1 \Rightarrow |x| < 6$$

Therefore, the radius of convergence of the Maclaurin series for $f'$ is 6.

Total for part (c) 2 points

© 2024 College Board

<!-- Page 6 -->

AP® Calculus AB/BC 2024 Scoring Guidelines

(d)

Let $g(x) = \sum_{n=1}^{\infty} \frac{(n+1)x^{2n}}{n^2 3^n}$. Use the ratio test to determine the radius of convergence of the Maclaurin series for $g$.

|  $\left| \frac{(n+2)x^{2n+2}}{(n+1)^2 3^{n+1}} \right| = \left| \frac{(n+2)x^{2n+2}}{(n+1)^2 3^{n+1}} \cdot \frac{n^2 3^n}{(n+1)x^{2n}} \right|$ | Sets up ratio | 1 point  |
| --- | --- | --- | --- | --- | --- | --- |
|  $\lim_{n \to \infty} \left| \frac{(n+2)n^2}{(n+1)^3} \right| \cdot \left| \frac{x^2}{3} \right| = \left| \frac{x^2}{3} \right|$ | Limit | 1 point  |
|  $\left| \frac{x^2}{3} \right| < 1 \Rightarrow x^2 < 3 \Rightarrow |x| < \sqrt{3}$ The radius of convergence of $g$ is $\sqrt{3}$. | Radius of convergence | 1 point  |

# Scoring notes:

- The first point is earned by presenting a correct ratio with or without absolute values. Once earned, this point cannot be lost. Any errors in simplification or evaluation of the limit will not earn the second point.
- The first point is earned for ratios mathematically equivalent to any of the following:

$$\frac{\frac{(n+2)x^{2n+2}}{(n+1)^2 3^{n+1}}}{\frac{(n+1)x^{2n}}{n^2 3^n}}, \frac{(n+2)x^{2n+2}}{(n+1)^2 3^{n+1}} \cdot \frac{n^2 3^n}{(n+1)x^{2n}}, \frac{\frac{(n+1)x^{2n}}{n^2 3^n}}{\frac{nx^{2n-2}}{(n-1)^2 3^{n-1}}}, \text{ or } \frac{(n+1)x^{2n}}{n^2 3^n} \cdot \frac{(n-1)^2 3^{n-1}}{nx^{2n-2}}.$$

- The first point is also earned for ratios mathematically equivalent to the following reciprocal ratios:

$$\frac{\frac{(n+1)x^{2n}}{n^2 3^n}}{\frac{(n+2)x^{2n+2}}{(n+1)^2 3^{n+1}}}, \frac{(n+1)x^{2n}}{n^2 3^n} \cdot \frac{(n+1)^2 3^{n+1}}{(n+2)x^{2n+2}}, \frac{\frac{nx^{2n-2}}{(n-1)^2 3^{n-1}}}{\frac{(n+1)x^{2n}}{n^2 3^n}}, \text{ or } \frac{nx^{2n-2}}{(n-1)^2 3^{n-1}} \cdot \frac{n^2 3^n}{(n+1)x^{2n}}.$$

Responses including any of these reciprocal ratios can earn the second point for using limit notation to correctly find a limit of the absolute value of their ratio to be $\left| \frac{3}{x^2} \right|$. Such responses earn the third point only for a final answer of $\sqrt{3}$ with a valid explanation for reporting the reciprocal of $\frac{1}{\sqrt{3}}$.

- To earn the second point a response must use the ratio and correctly evaluate the limit of the ratio, using correct limit notation.
- The third point is earned only for an answer of $\sqrt{3}$ with supporting work.

Total for part (d) 3 points

Total for question 6 9 points

© 2024 College Board

<!-- Page 7 -->

1 of 2

Sample 6A

6 6 6 6 6 NO CALCULATOR ALLOWED 6 6 6 6 6

Answer QUESTION 6 parts (a) and (b) on this page.

Response for question 6(a)

$$x = 6 : \sum_{n=1}^{\infty} \frac{(n+1) 6^n}{n^2 6^n} = \sum_{n=1}^{\infty} \frac{(n+1)}{n^2}$$
compare with $$\sum_{n=1}^{\infty} \frac{1}{n}$$ Harmonic series diverges

$$\lim_{n \to \infty} \left| \frac{n+1}{n^2} \cdot \frac{n}{1} \right| = 1 > 0$$

$$\sum_{n=1}^{\infty} \frac{(n+1) 6^n}{n^2 6^n}$$ diverges by the LCT.

Response for question 6(b)

f(-3) is an alternating series whose terms decrease in absolute value to 0.

$$|Error| \le \left| \frac{5}{16} (-\frac{1}{2})^4 \right| < \frac{1}{50}$$

Page 14

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

0003176

Q5229/14

<!-- Page 8 -->

2 of 2

Sample 6A

6 6 6 6 6 NO CALCULATOR ALLOWED 6 6 6 6 6

Answer QUESTION 6 parts (c) and (d) on this page.

Response for question 6(c)

general term for $$f' = \frac{n(n+1)x^{n-1}}{n^2 6^n}$$

$$\lim_{n \to \infty} \left| \frac{(n+2)x^n}{(n+1)6^{n+1}} \cdot \frac{n 6^n}{(n+1)x^{n-1}} \right| = \left| \frac{x}{6} \right| < 1$$
$$-6 < x < 6$$
$$R = 6$$

Response for question 6(d)

$$\lim_{n \to \infty} \left| \frac{(n+2)x^{2n+2}}{(n+1)^2 3^{n+1}} \cdot \frac{n^2 3^n}{(n+1)x^{2n}} \right| = \left| \frac{x^2}{3} \right| < 1$$
$$-3 < x^2 < 3$$
$$|x| < \sqrt{3}$$
$$-\sqrt{3} < x < \sqrt{3}$$
$$R = \sqrt{3}$$

Page 15

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

Q5229/15

<!-- Page 9 -->

1 of 2

Sample 6B

6 6 6 6 6 NO CALCULATOR ALLOWED 6 6 6 6 6

Answer QUESTION 6 parts (a) and (b) on this page.

Response for question 6(a)

at x = 6

$$\sum_{n=1}^{\infty} \frac{(n+1)6^n}{n^2 6^n} = \sum_{n=1}^{\infty} \frac{(n+1)}{n^2}$$

$$a_i = \frac{1}{n}$$ diverges

By LCT:

$$a_n = \frac{1}{n}$$

$$b_n = \frac{n+1}{n^2}$$

$$\lim_{n \to \infty} \frac{n+1}{n^2} \cdot \frac{n}{1} = \lim_{n \to \infty}$$

$$\frac{n+1}{n} = \frac{1}{n} \text{ so LCT applies}$$

because 1 is finite and positive

at x = 6 the Maclaurin series

diverges, when using the Limit Comparison Test

Response for question 6(b)

$$a_n = \frac{n+1}{n^2} \left(-\frac{1}{2}\right)^n$$

$$a_4 = \frac{4+1}{4^2} \left(-\frac{1}{2}\right)^4$$

$$|S - S_n| < a_{n+1}$$

$$= \left(\frac{5}{16}\right)\left(\frac{1}{16}\right) = \frac{5}{16^2}$$

$$|f(-3) - S_3| < a_4$$

$$a_4 = \frac{5}{256}$$

because $$a_4 = \frac{5}{256}$$ and $$|f(-3) - S_3| < a_4$$ and

$$\frac{5}{256} < \frac{1}{50} \quad |f(-3) - S_3| < \frac{1}{50}$$

Page 14

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

0003509

Q5228/14

<!-- Page 10 -->

2 of 2

Sample 6B

6 6 6 6 6 NO CALCULATOR ALLOWED 6 6 6 6 6

Answer QUESTION 6 parts (c) and (d) on this page.

Response for question 6(c)

$$f \text{ general term} = \frac{(n+1)(x^n)}{n^2 6^n}$$

$$f' \text{ general term} = \frac{(n+1)}{n^2 6^n} \cdot n x^{n-1} = \frac{(n+1)(n x^{n-1})}{n^2 6^n}$$

ratio test:

$$\lim_{n \to \infty} \left| \frac{((n+1)+1)((n+1)x^{n+1})}{(n+1)^2 6^{n+1}} \cdot \frac{n^2 6^n}{(n+1)(n x^{n-1})} \right| < 1 =$$

$$\lim_{n \to \infty} \left| \frac{(n+2)(n+1)(x^n)}{n+1} \right| < 1 \Rightarrow \lim_{n \to \infty} \left| \frac{x}{6} \right| \cdot \lim_{n \to \infty} \frac{(n+2)(n+2)}{(n+1)^2 (n)}$$

$$\lim_{n \to \infty} |\frac{x}{6}| < 1 \Rightarrow |\frac{x}{6}| < 1 \Rightarrow |x| < 6$$

$$R = 6 \text{ the radius of convergence is } \boxed{6} \text{ for } f'$$

Response for question 6(d)

$$\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| < 1$$

ratio test:

$$\lim_{n \to \infty} \left| \frac{((n+1)+1)(\chi^2(n+1)^2)}{(n+1)^2 3^{n+1}} \cdot \frac{n^2 3^n}{(n+1)(x^{2n})} \right| < 1 =$$

$$\lim_{n \to \infty} \left| \frac{(n+2)(\chi^{2n+2}) n^2 3^n}{(n+1)^3 (\chi^{2n}) \text{ beyond } 2} \right| < 1 = \lim_{n \to \infty} \left| \frac{\chi^2}{3} \frac{(n+2)(n^2)}{(n+1)^3} \right| < 1$$

$$= \lim_{n \to \infty} |\frac{\chi^2}{3}| \cdot \lim_{n \to \infty} \left| \frac{(n+2)(n^2)}{(n+1)^3} \right| < 1 \Rightarrow |\frac{\chi^2}{3}| < 1$$

$$\text{The radius of convergence is } \boxed{\sqrt{3}} = |\chi^2| < 3 \quad |x| < \sqrt{3}$$

Page 15

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

Q5228/15

<!-- Page 11 -->

1 of 2

Sample 6C

6 6 6 6 6 NO CALCULATOR ALLOWED 6 6 6 6 6

Answer QUESTION 6 parts (a) and (b) on this page.

Response for question 6(a)

$$x = 6, \sum_{n=1}^{\infty} \frac{(n+1)6^n}{n^2 6^n} \rightarrow \frac{(n+1)}{n^2} \rightarrow \text{behaves like } \sum_{n=1}^{\infty} \frac{1}{n} = b_n, \text{ which}$$

$$\text{diverges. Since } b_n < \sum_{n=1}^{\infty} \frac{n+1}{n^2}, \text{ then the series must}$$

$$\text{also diverge.}$$

Response for question 6(b)

$$f(-3) = \sum_{n=1}^{\infty} \frac{n+1}{n^2} (-\frac{1}{2})^n \quad \frac{a}{1-r} = \frac{\frac{n+1}{n^2}}{1-(-\frac{1}{2})} = \frac{\frac{n+1}{n^2}}{\frac{3}{2}} = \frac{2(n+1)}{3n^2}$$

$$\frac{2(3+1)}{3(3)^2} = \frac{8}{27} \quad f(-3) = -1 + \frac{3}{8} - \frac{4}{72} + \frac{5}{16.72}$$

$$|\frac{8}{27} - (-\frac{125}{144})| = 1$$

Page 14

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

0049722

Q5228/14

<!-- Page 12 -->

2 of 2

Sample 6C

6 6 6 6 6 NO CALCULATOR ALLOWED 6 6 6 6 6

Answer QUESTION 6 parts (c) and (d) on this page.

Response for question 6(c)

$$f(x) = \frac{(n+1)x^n}{n^2 6^n} = \frac{x^n n + x^n}{n^2 6^n} \quad f'(x) = \frac{x^n n + x^n}{n^2 6^n}$$

Response for question 6(d)

$$g(x) = \sum_{n=1}^{\infty} \frac{(n+1)x^{2n}}{n^2 3^n} \rightarrow \lim_{n \to \infty} \left| \frac{(n+2)x^{2n+2}}{(n+1)^2 3^{n+1}} \cdot \frac{n^2 \cdot 3^{n}}{(n+1) x^3 x^2} \right| = \lim_{n \to \infty} \left| \frac{(n+2)x^2 n^2}{(n+1)^3 \cdot 3} \right|$$
$$= \lim_{n \to \infty} \left| \frac{x^2 n^3 + 2x^2 n^2}{3(n+1)^3} \right| = \left| \frac{x^2}{3} \right| < 1 \rightarrow -1 < \frac{x^2}{3} < 1 \rightarrow -3 < x^2 < 3$$
$$\rightarrow \sqrt{-3} < x < \sqrt{3}$$

Page 15

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

Q5228/15

<!-- Page 13 -->

AP® Calculus BC 2024 Scoring Commentary

## Question 6

**Note:** Student samples are quoted verbatim and may contain spelling and grammatical errors.

### Overview

In this question, students are told that the Maclaurin series for a function $f$ is given by $\sum_{n=1}^{\infty} \frac{(n+1)x^n}{n^2 6^n}$. Furthermore, the series converges to $f(x)$ for all $x$ in the interval of convergence and the radius of that interval of convergence is 6.

In part (a) the students are asked to determine whether the Maclaurin series for $f$ converges or diverges at $x = 6$ and to give a reason for their answer. A correct response will determine that at $x = 6$, the series is $\sum_{n=1}^{\infty} \frac{(n+1)}{n^2}$ and that for all $n \geq 1$, the terms of this series are larger than the terms of the divergent harmonic series. Therefore, this series diverges by the comparison test.

In part (b) students are told that $f(-3) = \sum_{n=1}^{\infty} \frac{(n+1)}{n^2} \cdot \left(-\frac{1}{2}\right)^n$ and that the first three terms of this series sum to $S_3 = -\frac{125}{144}$. Students are asked to show that $|f(-3) - S_3| < \frac{1}{50}$. A correct response will observe that the series for $f(-3)$ is alternating with terms that decrease in magnitude to 0. Therefore, by the alternating series error bound, $S_3$ approximates $f(-3)$ with an error that is no more than the value of the fourth term of the series. The fourth term is $\left| \frac{4+1}{4^2} \cdot \left(-\frac{1}{2}\right)^4 \right| = \frac{5}{256}$, which is less than $\frac{1}{50}$.

In part (c) students are asked to find the general term of the Maclaurin series for $f'$ and to find the radius of convergence of the Maclaurin series for $f'$. A correct response will differentiate the general term of the Maclaurin series for $f$ to find a general term of $\frac{(n+1)x^{n-1}}{n \cdot 6^n}$ and will note that the radius of convergence of the Maclaurin series for $f'$ must be 6, because this is the radius of convergence of the Maclaurin series of $f$.

In part (d) students are given a new Maclaurin series, $g(x) = \sum_{n=1}^{\infty} \frac{(n+1)x^{2n}}{n^2 3^n}$, and asked to use the ratio test to determine the radius of convergence. A correct response will set up a ratio of consecutive terms, $\frac{a_{n+1}}{a_n}$, find the limit of the absolute value of that ratio as $n \to \infty$, and determine for what values of $x$ the limit is less than 1.

© 2024 College Board.

Visit College Board on the web: collegeboard.org.

<!-- Page 14 -->

AP® Calculus BC 2024 Scoring Commentary

### Question 6 (continued)

**Sample: 6A**

**Score: 9**

The response earned 9 points: 2 points in part (a), 2 points in part (b), 2 points in part (c), and 3 points in part (d).

In part (a) the response earned the first point in the first line for the term $$\frac{(n+1)6^n}{n^26^n}$$. The response earned the second point in the second, third, and fourth lines by correctly evaluating the limit of the ratio of our series with the harmonic series, stating that the “harmonic series diverges”, and concluding that our series diverges.

In part (b) the response earned the first point in the second line for the term $$\left|\frac{5}{16}\left(-\frac{1}{2}\right)^4\right|$$. The response earned the second point by stating “$$f(-3)$$ is an alternating series” and presenting the inequality $$|\text{Error}| \leq \left|\frac{5}{16}\left(-\frac{1}{2}\right)^4\right| < \frac{1}{50}$$.

In part (c) the response earned the first point in the first line for the correct general term of the derivative $$\frac{n(n+1)x^{n-1}}{n^26^n}$$. The response earned the second point in the second and fourth lines for the limit of the ratio with absolute values, correct evaluation, and the answer.

In part (d) the response earned the first point in the first line for the term $$\left|\frac{(n+2)x^{2n+2}}{(n+1)^23^{n+1}} \cdot \frac{n^23^n}{(n+1)x^{2n}}\right|$$. The response earned the second point in the first line by correctly evaluating the limit with the term $$\left|\frac{x^2}{3}\right|$$. The response earned the third point for the correct answer of $$\sqrt{3}$$ with correct supporting work.

**Sample: 6B**

**Score: 6**

The response earned 6 points: 1 point in part (a), 1 point in part (b), 2 points in part (c), and 2 points in part (d).

In part (a) the response earned the first point in the second line on the left for the term $$\frac{(n+1)6^n}{n^26^n}$$. The response did not earn the second point because the response did not reference that the series $$\sum_{n=1}^{\infty} \frac{1}{n}$$ diverges and instead only referenced the term $$\frac{1}{n}$$.

In part (b) the response earned the first point in the second line on the right for the term $$\frac{4+1}{4^2}\left(\frac{-1}{2}\right)^4$$. The response did not earn the second point since the response did not reference alternating series or alternating series error bound.

© 2024 College Board.

Visit College Board on the web: collegeboard.org.

<!-- Page 15 -->

AP® Calculus BC 2024 Scoring Commentary

### Question 6 (continued)

In part (c) the response earned the first point in the second line for the term $$\frac{(n+1)}{n^2 6^n} \cdot nx^{n-1}$$. The response earned the second point for a correct application of the ratio test together with the correct answer.

In part (d) the response earned the first point in the third line for the term $$\left| \frac{((n+1)+1)(x^{2(n+1)})}{(n+1)^2 3^{n+1}} \cdot \frac{n^2 3^n}{(n+1)(x^{2n})} \right|$$.

The response did not earn the second point because in the fourth line there is a missing $$3^{n+1}$$ in the denominator. The response earned the third point for a correct radius of convergence with correct supporting work.

**Sample: 6C**

**Score: 3**

The response earned 3 points: 1 point in part (a), no points in part (b), no points in part (c), and 2 points in part (d).

In part (a) the response earned the first point in the first line for the term $$\frac{(n+1)6^n}{n^2 6^n}$$. The response did not earn the second point because the response presented an inequality that compares series instead of terms of series.

In part (b) the response did not earn the first point because the response did not correctly use the fourth term of the series. The response did not earn the second point because the response did not reference alternating series.

In part (c) the response did not earn the first point because the presented derivative is incorrect. The response did not earn the second point because the response did not present a radius of convergence.

In part (d) the response earned the first point in the first line for the term $$\left| \frac{(n+2)x^{2n+2}}{(n+1)^2 3^{n+1}} \cdot \frac{n^2 \cdot 3^n}{(n+1)x^{2n}} \right|$$. The response earned the second point in the second line for the correct evaluation of the limit as $$\left| \frac{x^2}{3} \right|$$. The response did not earn the third point because the response presented an imaginary number $$\sqrt{-3}$$ in the third line.

© 2024 College Board.

Visit College Board on the web: collegeboard.org.
