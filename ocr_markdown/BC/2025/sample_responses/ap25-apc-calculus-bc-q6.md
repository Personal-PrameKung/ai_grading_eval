<!-- Page 1 -->

2025

AP

# AP® Calculus BC
## Sample Student Responses and Scoring Commentary

**Inside:**

**Free-Response Question 6**

- ☑ Scoring Guidelines
- ☑ Student Samples
- ☑ Scoring Commentary

© 2025 College Board. College Board, Advanced Placement, AP, AP Central, and the acorn logo are registered trademarks of College Board. Visit College Board on the web: collegeboard.org.

AP Central is the official online home for the AP Program: apcentral.collegeboard.org.

<!-- Page 2 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

### Part B (BC): Graphing calculator not allowed

#### Question 6

9 points

#### General Scoring Notes

- The model solution is presented using standard mathematical notation.
- Answers (numeric or algebraic) need not be simplified. Answers given as a decimal approximation should be accurate to three places after the decimal point. Within each individual free-response question, at most one point is not earned for inappropriate rounding.

The Taylor series for a function \( f \) about \( x = 4 \) is given by

\[
\sum_ {n = 1} ^ {\infty} \frac {(x - 4) ^ {n + 1}}{(n + 1) 3 ^ {n}} = \frac {(x - 4) ^ {2}}{2 \cdot 3} + \frac {(x - 4) ^ {3}}{3 \cdot 3 ^ {2}} + \frac {(x - 4) ^ {4}}{4 \cdot 3 ^ {3}} + \dots + \frac {(x - 4) ^ {n + 1}}{(n + 1) 3 ^ {n}} + \dots \text { and   converges   to } f (x) \text { on   its }
\]

interval of convergence.

|   | Model Solution | Scoring  |   |
| --- | --- | --- | --- |
|  A | Using the ratio test, find the interval of convergence of the Taylor series for \( f \) about \( x = 4 \). Justify your answer.  |   |   |
|   |  \( \left| \frac{(x-4)^{n+2}}{(n+2)3^{n+1}} \cdot \frac{(n+1)3^n}{(x-4)^{n+1}} \right| = \left| \frac{(x-4)(n+1)}{3(n+2)} \right| \) | Sets up ratio | Point 1 (P1)  |
|   |  \( \lim_{n \to \infty} \left| \frac{(x-4)(n+1)}{3(n+2)} \right| = \left| \frac{x-4}{3} \right| \lim_{n \to \infty} \frac{n+1}{n+2} = \left| \frac{x-4}{3} \right| \) | Limit of ratio | Point 2 (P2)  |
|   |  \( \left| \frac{x-4}{3} \right| < 1 \) when \( -3 < x - 4 < 3 \). | Interior of interval of convergence | Point 3 (P3)  |
|   |  Thus, the series converges when \( 1 < x < 7 \). |  |   |
|   |  When \( x = 1 \), the series is \( \sum_{n=1}^{\infty} \frac{(-1)^{n+1} \cdot 3}{n+1} \), which converges by the alternating series test.When \( x = 7 \), the series is \( \sum_{n=1}^{\infty} \frac{3}{n+1} \), which diverges by limit comparison to the harmonic series.Therefore, the series converges for \( 1 \leq x < 7 \). | Considers both endpointsAnalysis and interval of convergence | Point 4 (P4)Point 5 (P5)  |

© 2025 College Board

<!-- Page 3 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

### Scoring Notes for Part A

- **P1** is earned by presenting a correct ratio with or without absolute values. Once earned, **P1** is banked (i.e., subsequent errors in simplification or evaluation do not impact scoring for **P1**). **P2** is not earned if there are any errors in simplification or evaluation of the limit.
- **P1** is earned for ratios mathematically equivalent to any of the following:

$$\frac{(x-4)^{n+2}}{(n+2)3^{n+1}} \cdot \frac{(n+1)3^n}{(x-4)^{n+1}}, \frac{\frac{(x-4)^{n+2}}{(n+2)3^{n+1}}}{\frac{(x-4)^{n+1}}{(n+1)3^n}}, \frac{(x-4)^{n+1}}{(n+1)3^n} \cdot \frac{n3^{n-1}}{(x-4)^n}, \text{ or } \frac{\frac{(x-4)^{n+1}}{(n+1)3^n}}{\frac{(x-4)^n}{n3^{n-1}}}.$$

- **P1** is also earned for ratios mathematically equivalent to the following reciprocal ratios:

$$\frac{(x-4)^{n+1}}{(n+1)3^n} \cdot \frac{(n+2)3^{n+1}}{(x-4)^{n+2}}, \frac{\frac{(x-4)^{n+1}}{(n+1)3^n}}{\frac{(x-4)^{n+2}}{(n+2)3^{n+1}}}, \frac{(x-4)^n}{n3^{n-1}} \cdot \frac{(n+1)3^n}{(x-4)^{n+1}}, \text{ or } \frac{\frac{(x-4)^n}{n3^{n-1}}}{\frac{(x-4)^{n+1}}{(n+1)3^n}}.$$

A response that presents any of these reciprocal ratios earns **P1** and is eligible for **P2**, **P3**, and **P4**, but not **P5**.

- A response that does not present a ratio is not eligible for **P2**.
- A response that does not use the absolute value of a ratio can earn both **P1** and **P2**.
- A response that does not use absolute value in computing the limit is eligible for **P3** if the expression $$-1 < \frac{x-4}{3} < 1$$ or an equivalent inequality is presented.
- A response that presents an incorrect limit of form $$\frac{|x-4|}{b}$$, where $$b > 0$$, is eligible for **P3**.

**P3** is then earned for correctly finding an interval with interior $$(1, 7)$$ or $$(4 - b, 4 + b)$$.

Note: $$|x - 4| < b$$ is not sufficient to earn **P3**. $$x - 4 < b$$ can earn **P3** if this is resolved to $$-b + 4 < x < b + 4$$.

- **P4** is earned for considering both endpoints of the correct interval or both endpoints of an incorrect interval that has earned **P3**.

- To earn **P5**, a response must correctly analyze the series at $$x = 1$$ and $$x = 7$$, and present the correct interval of convergence. Naming of an appropriate test is sufficient for the analysis at each endpoint. In addition to the tests listed in the model solution, the direct comparison test to an appropriate series or the integral test may also be used.

© 2025 College Board

<!-- Page 4 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

|  B | Find the first three nonzero terms and the general term of the Taylor series for \( f' \), the derivative of \( f \), about \( x = 4 \).  |   |   |
| --- | --- | --- | --- |
|   |  \( f'(x) = \frac{(x-4)}{3} + \frac{(x-4)^2}{9} + \frac{(x-4)^3}{27} + \cdots + \frac{(x-4)^n}{3^n} + \cdots \) | First three terms | Point 6 (P6)  |
|   |   |  General term | Point 7 (P7)  |
|  Scoring Notes for Part B  |   |   |   |
|  P6 is earned by presenting the first three nonzero terms in a list or as part of a polynomial or series.P7 is earned by identifying the correct general term (either individually or as part of a polynomial or series).  |   |   |   |
|  C | The Taylor series for \( f' \) described in part B is a geometric series. For all \( x \) in the interval of convergence of the Taylor series for \( f' \), show that \( f'(x) = \frac{x-4}{7-x} \).  |   |   |
|   |  The Taylor series for \( f' \) is a geometric series with first term \( \frac{x-4}{3} \) and common ratio \( \frac{x-4}{3} \).\( f'(x) = \frac{\frac{x-4}{3}}{1 - \frac{x-4}{3}} = \frac{x-4}{3 - (x-4)} = \frac{x-4}{7-x} \) | Verification | Point 8 (P8)  |
|   |  Scoring Notes for Part C  |   |   |
|  A response of \( f'(x) = \frac{\frac{x-4}{3}}{1 - \frac{x-4}{3}} \) is sufficient to earn P8.  |   |   |   |

© 2025 College Board

<!-- Page 5 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

D It is known that the radius of convergence of the Taylor series for $f$ about $x = 4$ is the same as the radius of convergence of the Taylor series for $f'$ about $x = 4$. Does the Taylor series for $f'$ described in part B converge to $f'(x) = \frac{x - 4}{7 - x}$ at $x = 8$? Give a reason for your answer.

It follows from the work in part A that the interior of the interval of convergence of the Taylor series for $f'$ is $1 < x < 7$.

Therefore, $x = 8$ would be outside the interval of convergence of $f'$, and the Taylor series for $f'$ would not converge to

$$f'(x) = \frac{x - 4}{7 - x} \text{ at } x = 8.$$

Answer with reason Point 9 (P9)

### Scoring Notes for Part D

- A response of “no, $x = 8$ is outside the interval of convergence” is sufficient to earn P9.
- P9 can be earned with a response consistent with an incorrect interval of convergence imported from part A.
- Alternate solutions:

○ Because the series for $f'(x)$ is geometric, this converges to $f(x)$ for all values of $x$ such that the common ratio $\frac{x - 4}{3}$ is between $-1$ and $1$.

$$-1 < \frac{x - 4}{3} < 1 \Rightarrow -3 < x - 4 < 3 \Rightarrow 1 < x < 7$$

○ Because $x = 8$ is outside the interval $1 < x < 7$, the series for $f'$ does not converge to $f'(x) = \frac{x - 4}{7 - x}$ at $x = 8$.

○ For $x = 8$, the series is given by $\sum_{n=1}^{\infty} \left(\frac{4}{3}\right)^n$, which is a geometric series with $r = \frac{4}{3} > 1$.

Therefore, the series diverges for $x = 8$.

© 2025 College Board

<!-- Page 6 -->

Sample 6A 1 of 2

Q6

# NO CALCULATOR ALLOWED

Q6

Answer QUESTION 6 PARTS A and B on this page.

PART A

$$\sum_{n=1}^{\infty} \frac{(x-4)^{n+1}}{(n+1)3^n}$$

$$\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| < 1$$

$$\lim_{n \to \infty} \left| \frac{(x-4)^{n+2}}{(n+2)3^{n+1}} \cdot \frac{3^n(n+1)}{(x-4)^{n+1}} \right| = \lim_{n \to \infty} \left| \frac{x-4}{3} \frac{(n+1)}{(n+2)} \right|$$

$$\left| \frac{x-4}{3} \right| < 1$$

$$-1 < x - \frac{4}{3} < 1$$

$$\frac{-3 < x - 4 < 3}{1 \le x < 7}$$

$$x=1: \sum_{n=1}^{\infty} \frac{(-3)^{n+1}}{(n+1)3^n} = \frac{(-3)^{n+1} - 3}{n+1}$$

$$\lim_{n \to \infty} \frac{\frac{3}{n+1}}{\frac{3}{n}} = 1 \quad 0 < 1 < \infty \quad \text{diverges by LCT to}$$

$$\text{AST: } \lim_{n \to \infty} \frac{3}{n+1} = 0, \quad \frac{3}{n+1} > \frac{3}{n+2} \checkmark$$

$$x=7: \sum_{n=1}^{\infty} \frac{3^{n+1}}{(n+1)3^n} = \sum_{n=1}^{\infty} \frac{3}{n+1}$$

Diverges by LCT

PART B

$$f = \frac{(x-4)^2}{6} + \frac{(x-4)^3}{27} + \frac{(x-4)^4}{4 \cdot 27}$$

$$f' = \frac{2(x-4)}{6} + \frac{3(x-4)^2}{27} + \frac{4(x-4)^3}{4 \cdot 27} + \dots \quad \sum_{n=1}^{\infty} \frac{(x-4)^n}{3^n}$$

$$f' = \frac{x-4}{3} + \frac{(x-4)^2}{3^2} + \frac{(x-4)^3}{3^3} + \dots \frac{(x-4)^n}{3^n}$$

Page 14

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

0002795

Q5525/14

<!-- Page 7 -->

Sample 6A 2 of 2

Q6

☑

# NO CALCULATOR ALLOWED

Q6

Answer QUESTION 6 PARTS C and D on this page.

# PART C

Geometric series $$\sum_{n=1}^{\infty} \frac{(x-4)^n}{3^n}$$
In the interval of convergence, $$|r|<1$$, and the series converges to $$\frac{a}{1-r}$$
$$r = \frac{x-4}{3}$$, and $$a = a_1 = \frac{x-4}{3}$$.

$$\frac{a}{1-r} = \frac{\frac{x-4}{3}}{1 - \frac{x-4}{3}} = \frac{\frac{x-4}{3}}{\frac{3-x+4}{3}} = \frac{x-4}{7-x}$$

# PART D

No. The interval of convergence for f about x=4 is

$$1 \le x < 7$$, and x=8 is outside of that range. Since

the radius of convergence is the same for f' and f,

and both are centered about x=4, 8 must be out

of the interval of convergence for f' as well.

Therefore, it must diverge and cannot converge to

$$f'(x) = \frac{x-4}{7-x} \text{ at } x=8.$$

check: geometric

$$|r|<1 \quad -1 < \frac{x-4}{3} < 1$$

$$-1 < x < 7$$

geometric, so not

$$-1 \le x < 7$$

Page 15

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

Q5685/15

<!-- Page 8 -->

Sample 6B 1 of 2

Q6

# NO CALCULATOR ALLOWED

Q6

Answer QUESTION 6 PARTS A and B on this page.

PART A

$$\lim_{n \to \infty} \left| \frac{\frac{(x-4)^{n+2}}{(n+2)3^{n+1}}}{\frac{(x-4)^{n+1}}{(n+1)3^n}} \right| = \lim_{n \to \infty} \left| \frac{\frac{(x-4)^n}{(n+1)3^{n+1}}}{\frac{(x-4)^n}{(n+2)3}} \right| = |x-4| \lim_{n \to \infty} \left| \frac{n+1}{3(n+2)} \right|$$

due to radio test.

$$|x-4| \cdot \frac{1}{3} < 1, -3 < x-4 < 3, \quad 1 < x < 7$$

PART B

$$f' \approx \frac{2(x-4)}{2 \cdot 3} + \frac{3(x-4)^2}{3 \cdot 3^2} + \frac{4(x-4)^3}{4 \cdot 3^3} + \dots + \frac{(n+1)(x-4)^n}{(n+1)3^n} + \dots$$

$$f' \approx \frac{(x-4)^2}{3} + \frac{(x-4)^2}{3^2} + \frac{(x-4)^3}{3^3} + \dots + \frac{(x-4)^n}{3^n} + \dots$$

Page 14

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

0118979

Q5825/14

<!-- Page 9 -->

Sample 6B 2 of 2

Q6

# NO CALCULATOR ALLOWED

Q6

Answer QUESTION 6 PARTS C and D on this page.

# PART C

Since $f'$ is Geometric series $(S = \frac{a}{1-r})$. ($\left|\frac{x-4}{3}\right| < 1$ H Converges to

$a = \frac{(x-4)}{3} \quad r = \frac{x-4}{3}$.

$S = \frac{\left(\frac{(x-4)}{3}\right)}{\left(\frac{3-x+4}{3}\right)} = \frac{x-4}{7-x}$

$\frac{\frac{x-4}{3}}{1 - \left(\frac{x-4}{3}\right)}$

$\therefore f'(x) = \frac{x-4}{7-x}$

# PART D

$f'(x) = \frac{x-4}{7-x}$ @ $x=8$?

No. Since $f'(x) = \frac{x-4}{7-x}$ is derived from where $x=4$ (center is

4) the $T(x)$ form is $\frac{(x-4)^n}{3^n}$. However, since the center general

is shifted to $x=8$, In $T(x)$, $(x-8)$ is needed to be used

instead of $(x-4)$. Leading to different $f'(x)$ formula.

convergence

Page 15

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

Q5625/15

<!-- Page 10 -->

Sample 6C 1 of 2

Q6

# NO CALCULATOR ALLOWED

Q6

Answer QUESTION 6 PARTS A and B on this page.

PART A

$$\lim_{x \to \infty} \left| \frac{\frac{(x-4)^{n+2}}{(n+2)3^{n+1}}}{\frac{\frac{(x-4)^{n+1}}{(n+1)3^n}} } \right| \lim_{n \to \infty} \left| \frac{\frac{(x-4)^{n+2}}{(n+2)3^{n+1}} \cdot \frac{(n+1)(3^n)}{(x-4)^{n+2}}} \right|$$

$$\lim_{n \to \infty} |x-4| \quad -1 < x-4 < 1 \\ +4 \quad +4 \quad +4$$

$$3 < x < 5 \quad (3,5)$$

$$x=3$$

$$\lim_{n \to \infty} \frac{(-1)^{n+1}}{(n+1)(3^n)}$$ Converges

PART B

$$f'(x) = \frac{(x-4)^2}{12} + \frac{(x-4)^3}{81} + \frac{(x-4)^4}{16 \cdot 3^3} + \dots +$$

$$\frac{(x-4)^{n+1}}{(2(n+1))3^n}$$

Page 14

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

0070656

Q5529/14

<!-- Page 11 -->

Sample 6C 2 of 2

Q6

☑

# NO CALCULATOR ALLOWED

Q6

Answer QUESTION 6 PARTS C and D on this page.

PART C

lim
x→∞

$$\left| \frac{(x-4)^{n+2}}{(2n+4)3^{n+1}} \right|$$
$$\frac{(x-4)^{n+1}}{(2n+2)3^n}$$

$$\lim_{x \to \infty} \left| \frac{(x-4)^{n+2}}{(2n+4)3^{n+1}} \cdot \frac{(2n+2)3^n}{(x-4)^{n+1}} \right|$$

$$\lim_{x \to \infty}$$

![img-0.jpeg](ap25-apc-calculus-bc-q6_assets/page-11-img-0.jpeg)

![img-1.jpeg](ap25-apc-calculus-bc-q6_assets/page-11-img-1.jpeg)

PART D

No, since x=8 is not in the interval
of convergence which is (3,5),
the Taylor series cannot
converge at that value.

Page 15

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

Q5626/15

<!-- Page 12 -->

AP CALCULUS BC 2025 • SCORING COMMENTARY

# Question 6

**Note:** Student samples are quoted verbatim and may contain spelling and grammatical errors.

## Overview

**NEW for 2025:** The question overviews can be found in the *Chief Reader Report on Student Responses* on AP Central.

### Sample: 6A

**Score: 9 (1-1-1-1-1-1-1-1-1)**

The response earned 9 points: 5 points in part A, 2 points in part B, 1 point in part C, and 1 point in part D.

In part A the response earned **P1** with the presentation of the correct ratio on the left side of line 2. The response earned **P2** with the result of the limit, $\left| \frac{x-4}{3} \right|$, in line 3. The response earned **P3** with the presentation of the interval $1 \leq x < 7$ in line 6 that has the correct interior $1 < x < 7$. The response earned **P4** with the first two infinite sums on the right after the expressions $x = 1$ and $x = 7$. The response earned **P5** with the correct analysis of the endpoints $x = 1$ and $x = 7$. For $x = 1$, the statement “converges conditionally by AST” and for $x = 7$ the statement “diverges by LCT to $\sum_{n=1}^{\infty} \frac{3}{n}$”, demonstrates that $x = 1$ is included in the interval of convergence but that $x = 7$ is not included. The correct interval is presented in the boxed statement on the left.

In part B the response earned **P6** with the correct presentation of the three terms in line 2. It is not necessary to simplify the expression, but the response is correctly simplified in line 3. The response earned **P7** with the correct presentation of the general term as part of the series expression on the right.

In part C the response earned **P8** with the verification in line 5.

In part D the response earned **P9** in lines 1 and 2 with the statement “No. The interval of convergence for $f$ about $x = 4$ is $1 \leq x < 7$, and $x = 8$ is outside of that range.”

### Sample: 6B

**Score: 6 (1-1-1-0-0-1-1-1-0)**

The response earned 6 points: 3 points in part A, 2 points in part B, 1 point in part C, and 0 points in part D.

In part A the response earned **P1** with the presentation of the correct ratio in line 1 on the left. The response earned **P2** with the correct limit of the ratio in line 2 on the left. The response earned **P3** with the presentation of the correct interior of convergence $1 < x < 7$ in the box. The response did not earn **P4** because the endpoints are not checked. The response did not earn **P5** because **P4** is not earned.

In part B the response earned **P6** with the correct presentation of the three terms in line 1. It is not necessary to simplify the expression, but it is correctly simplified and presented in line 2. The response earned **P7** with the correct presentation of the general term in line 1. It is not necessary to simplify the expression, but it is correctly simplified and presented in line 2.

In part C the response earned **P8** in line 2 on the right after $S =$.

In part D the response did not earn **P9** because the stated reason for the answer “No” is based on shifting the center of the interval, which is incorrect.

© 2025 College Board.

Visit College Board on the web: collegeboard.org.

<!-- Page 13 -->

AP CALCULUS BC 2025 • SCORING COMMENTARY

## Question 6 (continued)

**Sample: 6C**

**Score: 3 (1-0-1-0-0-0-0-0-1)**

The response earned 3 points: 2 points in part A, 0 points in part B, 0 points in part C, and 1 point in part D.

In part A the response earned **P1** with the presentation of the correct ratio on the left side of line 1. The response did not earn **P2** because an incorrect limit of $|x - 4|$ is computed. The response earned **P3** with the presentation of the correct interior $3 < x < 5$ based on the identification of $|x - 4|$ as the limit. The response did not earn **P4** because there was no attempt to check the endpoints. Note that the work in the lower left corner is crossed out. The response did not earn **P5** because **P4** was not earned.

In part B the response did not earn **P6** because the three terms presented in line 1 are incorrect. The response did not earn **P7** because the general term presented in line 2 is incorrect.

In part C the response did not earn **P8** because the correct expression is not used.

In part D the response earned **P9** with the statement “No, since $x = 8$ is not in the interval of convergence, which is $(3, 5)$, the Taylor series cannot converge at that value.” This answer is consistent with the interval found in part A.

© 2025 College Board.

Visit College Board on the web: collegeboard.org.
