<!-- Page 1 -->

2025

AP

# AP® Calculus BC
## Sample Student Responses and Scoring Commentary

**Inside:**

**Free-Response Question 5**

- ☑ Scoring Guidelines
- ☑ Student Samples
- ☑ Scoring Commentary

© 2025 College Board. College Board, Advanced Placement, AP, AP Central, and the acorn logo are registered trademarks of College Board. Visit College Board on the web: collegeboard.org.

AP Central is the official online home for the AP Program: apcentral.collegeboard.org.

<!-- Page 2 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

### Part B (BC): Graphing calculator not allowed

#### Question 5

9 points

##### General Scoring Notes

- The model solution is presented using standard mathematical notation.
- Answers (numeric or algebraic) need not be simplified. Answers given as a decimal approximation should be accurate to three places after the decimal point. Within each individual free-response question, at most one point is not earned for inappropriate rounding.

Let \( y = f(x) \) be the particular solution to the differential equation \( \frac{dy}{dx} = (3 - x)y^2 \) with initial condition \( f(1) = -1 \).

|   | Model Solution | Scoring  |   |
| --- | --- | --- | --- |
|  A | Find \( f''(1) \), the value of \( \frac{d^2y}{dx^2} \) at the point \( (1, -1) \). Show the work that leads to your answer.  |   |   |
|   |  \( \frac{d^2y}{dx^2} = -y^2 + (3 - x)2y\frac{dy}{dx} \) | Product rule | Point 1 (P1)  |
|   |   |  Chain rule | Point 2 (P2)  |
|   |  \( f'(1) = \left.\frac{dy}{dx}\right|_{(x,y)=(1,-1)} = (3-1)(-1)^2 = 2 \) | \( f''(1) \) | Point 3 (P3)  |
|   |  \( f''(1) = \left.\frac{d^2y}{dx^2}\right|_{(x,y)=(1,-1)} = -(-1)^2 + (3-1)(2)(-1)(2) = -9 \) |  |   |

© 2025 College Board

<!-- Page 3 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

# Scoring Notes for Part A

- The expression $$\frac{d^2y}{dx^2} = -y^2 + (3 - x)2y$$ or $$\frac{d^2y}{dx^2} = 6y - y^2 - 2xy$$ earns P1 but not P2. Such a response is not eligible for P3.
- The expression $$\frac{d^2y}{dx^2} = -2y\frac{dy}{dx}$$ or $$\frac{d^2y}{dx^2} = 6y\left(\frac{dy}{dx}\right) - 2y\left(\frac{dy}{dx}\right)$$ earns P2 but not P1. Such a response is eligible for P3 for a consistent answer of $$f''(1) = 4$$ or $$f''(1) = -8$$, respectively, which is found by correctly substituting correct values for $$x, y$$, and $$\frac{dy}{dx}$$.
- A response of $$-(-1)^2 + (3 - 1)(2)(-1)(2)$$ earns P1, P2, and P3 regardless of any subsequent errors in simplification.
- Alternate approach (using separation of variables):

The particular solution for the differential equation that passes through the point $$(1, -1)$$ is

$$y = \frac{2}{x^2 - 6x + 3}.$$ Therefore, $$\frac{dy}{dx} = \frac{-2(2x - 6)}{(x^2 - 6x + 3)^2}.$$

This response has not yet earned P1, P2, or P3.

○ A response that correctly applies the quotient rule (or product rule) and the chain rule to find that $$\frac{d^2y}{dx^2} = \frac{-4(x^2 - 6x + 3)^2 + 4(2x - 6)(x^2 - 6x + 3)(2x - 6)}{(x^2 - 6x + 3)^4}$$ earns P1 and P2 and is eligible to earn P3 for the correct answer of $$f''(1) = -9$$.

○ A response that correctly applies the quotient rule (or product rule) but does not correctly apply the chain rule (e.g., $$\frac{d^2y}{dx^2} = \frac{-4(x^2 - 6x + 3)^2 + 4(2x - 6)(x^2 - 6x + 3)}{(x^2 - 6x + 3)^4}$$) earns P1, does not earn P2, and is not eligible to earn P3.

○ A response that does not correctly apply the quotient rule (or product rule) but does correctly apply the chain rule (e.g., $$\frac{d^2y}{dx^2} = \frac{-4}{2(x^2 - 6x + 3)(2x - 6)}$$) does not earn P1, earns P2, and is eligible to earn P3 for a consistent answer.

© 2025 College Board

<!-- Page 4 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

B Write the second-degree Taylor polynomial for f about x = 1.

|  f'(1) = 2 and f''(1) = -9 | Two terms | Point 4 (P4)  |
| --- | --- | --- |
|   |  Remaining term | Point 5 (P5)  |
|  P₂(x) = -1 + 2(x - 1) - 9/2(x - 1)² |  |   |

# Scoring Notes for Part B

- P4 and P5 can be earned with an answer consistent with incorrect values of f'(1) and f''(1) imported from part A.
- Any terms of degree greater than two or “+…” does not earn P5.
- A response of -1 + 2(x - 1) - 9/2(x - 1)² earns P4 and P5, regardless of any subsequent algebraic simplification.
- A response that does not present the polynomial as powers of (x - 1) but instead presents a correct expanded/simplified form of the polynomial (e.g., -9/2 x² + 11x - 15/2) earns P4 but not P5.

C The second-degree Taylor polynomial for f about x = 1 is used to approximate f(1.1). Given that |f'''(x)| ≤ 60 for all x in the interval 1 ≤ x ≤ 1.1, use the Lagrange error bound to show that this approximation differs from f(1.1) by at most 0.01.

|  |f(1.1) - P₂(1.1)| ≤ (max |f'''(x)| / 3!) |1.1 - 1|³ ≤ 60/6 (0.1)³ = 0.01 | Form of error bound | Point 6 (P6)  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|   |  Analysis | Point 7 (P7)  |

# Scoring Notes for Part C

- P6 is earned for presenting either (max |f'''(x)| / 3!) |1.1 - 1|³ or (60/6 (0.1)³). Subsequent errors in simplification will not earn P7.
- To earn P7, a response must have earned P6 and must explicitly connect the error bound with 0.01; for example by communicating Error ≤ 0.01, Error Bound = 0.01, or equivalent.
- A response that declares the error is equal to 0.01 (or any equivalent form of this value) does not earn P7.

© 2025 College Board

<!-- Page 5 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

D Use Euler's method, starting at $x = 1$ with two steps of equal size, to approximate $f(1.4)$. Show the work that leads to your answer.

$$\begin{array}{l} f(1.2) \approx f(1) + (1.2 - 1) \cdot \frac{dy}{dx} \bigg|_{(1, -1)} \\ = -1 + 0.2(2) = -0.6 \end{array}$$

$$f(1.4) \approx f(1.2) + (1.4 - 1.2) \cdot \frac{dy}{dx} \bigg|_{(1.2, -0.6)}$$

$$\approx -0.6 + 0.2(3 - 1.2)(-0.6)^2 = -0.4704$$

An approximation of $f(1.4)$ is $-0.47$.

First step of Euler's method

Point 8 (P8)

Answer with supporting work

Point 9 (P9)

### Scoring Notes for Part D

- To earn P8, a response must demonstrate the first step of Euler's method, with the correct initial condition, correct step size, and correct (or imported) expression for the derivative.

Note: Any subsequent error in simplification or rounding will not affect the scoring for P8.

- The two steps of Euler's method may be explicit expressions or may be presented in a table. For example:

|  x | y | $$\frac{dy}{dx} \cdot \Delta x$$ (or $$\frac{dy}{dx} \cdot 0.2$$)  |
| --- | --- | --- |
|  1 | -1 | 0.4  |
|  1.2 | -0.6 | 0.1296  |
|  1.4 | -0.4704 |   |

Note: In the presence of a correct answer, a table does not need to be labeled to earn both P8 and P9. In the presence of no answer or an incorrect answer, such a table must be correctly labeled to earn P8.

- A response of $-0.6 + 0.2(3 - 1.2)(-0.6)^2$ earns P9, regardless of any subsequent errors in simplification or rounding.
- A response that imports an incorrect value for $f'(1)$ from part A or part B is eligible to earn P9 with a consistent answer.
- A response may report the final answer as $-0.47$, $(1.4, -0.47)$, $-\frac{294}{625}$, or equivalent.

© 2025 College Board

<!-- Page 6 -->

Sample 5A 1 of 2

Q5

# NO CALCULATOR ALLOWED

Q5

Answer QUESTION 5 PARTS A and B on this page.

PART A

$$f''(x) = \frac{d^2y}{dx^2} = \frac{d}{dx}[(3-x)y^2] = -y^2 + 2(3-x)y\frac{dy}{dx} = 2(3-x)^2y^3 - y^2$$

$$f''(1) = 2(2)^2(-1)^3 - (-1)^2$$

PART B

$$T_2(x) = f(1) + f'(1)(x-1) + \frac{f''(1)}{2}(x-1)^2 = -1 + 2(x-1) - \frac{9}{2}(x-1)^2$$

$$f'(1) = (3-1)(-1)^2 = 2$$

Page 12

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

0025353

Q5525/12

<!-- Page 7 -->

Sample 5A 2 of 2

Q5

# NO CALCULATOR ALLOWED

Q5

Answer QUESTION 5 PARTS C and D on this page.

PART C

$$|f(1,1) - T_2(1,1)| \le \left| \frac{60}{3!} (1,1-1)^3 \right| \le 0.01$$

PART D

$$\Delta x = \frac{1.4-1}{2} = 0.2$$

$$f(1,2) \approx -1 + 0.2((3-1)(-1)^2) = -0.6$$

$$f(1,4) \approx -0.6 + 0.2((3-1,2)(-0.6)^2)$$

Page 13

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

Q5625/13

<!-- Page 8 -->

Sample 5B 1 of 2

Q5

☑

# NO CALCULATOR ALLOWED

Q5

Answer QUESTION 5 PARTS A and B on this page.

PART A

$$f''(x) = \frac{d^2y}{dx^2} \quad f'(x) = (3-x)y^2$$
$$f''(x) = (3-x)2y + y^2(-1)$$

$$f''(1) = \frac{d^2y}{dx^2} \Bigg|_{(1,-1)} = (3-1)2(-1) + (-1)^2(-1)$$
$$= (2)(-2) - 1 = -5$$

PART B

$$f'(x) \quad f'(1) = (3-1)$$

$$\frac{dy}{dx} \Bigg|_{(1,-1)} = (3-1)(-1)^2 = 2.$$

$$f(x) + f'(x)x + f''(x)x^2 \quad (cx.)$$

$$-1 + 2(x-1) \quad -\frac{5(x-1)^2}{2!}$$

Page 12

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

0035020

Q5525/12

<!-- Page 9 -->

Sample 5B 2 of 2

Q5

☒

# NO CALCULATOR ALLOWED

Q5

Answer QUESTION 5 PARTS C and D on this page.

PART C

Lagrange error bound *

|Error| ≤ 60/3 |1.1-1|³

PART D

(1,-1) | y+1=2(x-1) | (1.2,-.6)
(1.2,-.6) | y+.6=81/125(x-1.2) | (1.4,

dy/dx = (3-x)(y²)

f(1.4) ~ 81/125 (1.4-1.2)-6 (1/10) + 10/10

(3-1.2)(.6)²

(99/120/100/25)(9/36/100/5) = 81/125

2.8

f(1.4) ~ (3-1.2)(-.6)²(1.4-1.2)-.6

~ (1.8)(-.6)²(.2)-.6

(2/10)(2) = 1/10 + 10/10 = -6/10

Page 13

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

Q8625/13

<!-- Page 10 -->

Sample 5C 1 of 2

Q5

# NO CALCULATOR ALLOWED

Q5

Answer QUESTION 5 PARTS A and B on this page.

# PART A

$$\frac{dy}{dx} = (3-x)(y^2)$$

$$\frac{1}{3} + 1 = c$$

$$\int y^{-2} dy = \int (3-x) dx$$

$$c = \frac{4}{3}$$

$$-\frac{1}{3}y^{-3} = -1 + c$$

$$\frac{1}{3y^3} = -1 + \frac{4}{3}$$

$$-\frac{1}{3y^3} = -1 + c$$

$$\frac{1}{3y^3} = 1 - \frac{4}{3}$$

$$\frac{1}{y^3} = 3 - 4$$

$$\frac{1}{3(-1)^3} = -1 + c$$

$$\frac{1}{y^3} = -1$$

$$f''(1) = -1$$

$$\frac{-1}{-3} = -1 + c$$

$$1 = -y^3$$

$$-1 = y^3 \quad y = -1$$

?

# PART B

$$f(1) = -1$$

$$\frac{f'(x)(x-c)^n}{n!}$$

$$f'(1) =$$

$$f''(1) = -1$$

Page 12

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

0152110

Q5526/12

<!-- Page 11 -->

Sample 5C 2 of 2

Q5

☒

# NO CALCULATOR ALLOWED

Q5

Answer QUESTION 5 PARTS C and D on this page.

PART C

$$\frac{f(z)(x-c)^{n+1}}{(n+1)!} \rightarrow \frac{(60)(0.1)^3}{3!} \le 0.01$$

$$\begin{array}{c} 0.1 \\ \frac{0.4}{0.1} \\ \frac{0.00}{0.01} \\ \frac{0.4}{0.01} \\ \frac{0.00}{0.001} \end{array}$$

$$\frac{60(0.001)}{6}$$

$$10(0.001) \le 0.01$$

$$0.01 \le 0.01$$

PART D

$$\Delta x = 0.2 \quad \frac{dy}{dx} = (3-x)(y^2)(dx)$$

$$(1, -1)(3-1)(-1^2)(0.2) = (2)(0.2) = 0.4$$

$$(1.2, -0.6)(3-1.2)(-0.6)^2)(0.2) = (1.8)(0.36)(0.2)$$

$$(1.4, -0.470)$$

$$f(1.4) \le -0.470$$

$$\begin{array}{c} 3 \\ 0.6 \\ 0.6 \\ \frac{36}{0.0} \end{array} \quad \begin{array}{c} 1.8 \\ 0.8 \\ \frac{36}{0.8} \end{array} \quad \begin{array}{c} 1.8 \\ 0.36 \\ 0.36 \\ \frac{216}{0.68} \\ \frac{1296}{1296} \end{array}$$

$$0.68010$$

$$\frac{.1296}{4704}$$

Page 13

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

Q3625/13

<!-- Page 12 -->

AP CALCULUS BC 2025 • SCORING COMMENTARY

## Question 5

**Note:** Student samples are quoted verbatim and may contain spelling and grammatical errors.

### Overview

**NEW for 2025:** The question overviews can be found in the *Chief Reader Report on Student Responses* on AP Central.

### Sample: 5A

**Score: 9 (1-1-1-1-1-1-1-1-1)**

The response earned 9 points: 3 points in part A, 2 points in part B, 2 points in part C, and 2 points in part D.

In part A the response earned **P1** with the correct application of the product rule in the expression

$-y^2 + 2(3 - x)y\frac{dy}{dx}$ in line 1. The response earned **P2** with the correct application of the chain rule in the expression $-y^2 + 2(3 - x)y\frac{dy}{dx}$ in line 1. The response earned **P3** with the equation $f''(1) = 2(2)^2(-1)^3 - (-1)^2$ in line 2.

In part B the response earned **P4** with the two correct terms, $-1$ and $2(x - 1)$, of the Taylor polynomial in line 1. The response earned **P5** with the third correct term, $-\frac{9}{2}(x - 1)^2$, in line 1.

In part C the response earned **P6** with the expression $\left|\frac{60}{3!}(1.1 - 1)^3\right|$ in line 1. The response earned **P7** by connecting the expression for error, $|f(1.1) - T_2(1.1)|$, and 0.01 to the value of the error bound with a correct inequality.

In part D the response earned **P8**. The first step of Euler's method is shown on line 2 with the expression $f(1.2) \approx -1 + 0.2\left((3 - 1)(-1)^2\right)$. The response earned **P9** with the expression $f(1.4) \approx -0.6 + 0.2\left((3 - 1.2)(-0.6)^2\right)$ on line 3.

### Sample: 5B

**Score: 6 (1-0-0-1-1-1-0-1-1)**

The response earned 6 points: 1 point in part A, 2 points in part B, 1 point in part C, and 2 points in part D.

In part A the response earned **P1** with the equation $f''(x) = (3 - x)2y + y^2(-1)$ in line 2. The response did not earn **P2**. The response does not present the chain rule factor of $\frac{dy}{dx}$ with the first term in the product rule. The response did not earn **P3**. The response is not eligible for this point because **P2** is not earned.

In part B the response earned **P4** with the two correct terms, $-1$ and $2(x - 1)$, of the Taylor polynomial in line 4. The response earned **P5** with the term $\frac{-5(x - 1)^2}{2!}$, which is consistent with the value of $f''(1)$ imported from part A.

© 2025 College Board.

Visit College Board on the web: collegeboard.org.

<!-- Page 13 -->

AP CALCULUS BC 2025 • SCORING COMMENTARY

## Question 5 (continued)

In part C the response earned **P6** with the expression $\frac{60}{3!}|1.1 - 1|^3$. The response did not earn **P7** because there is no explicit connection to 0.01.

In part D the response earned **P8**. The first step of Euler's method is shown on line 1 of the table with the presentation of the correct local linearization $y + 1 = 2(x - 1)$ and its evaluation to produce the point $(1.2, -.6)$. The response earned **P9** with the expression $f(1.4) \approx (3 - 1.2)(-0.6)^2(1.4 - 1.2) - .6$ in the second to last line.

### Sample: 5C

### Score: 3 (0-0-0-0-0-1-0-1-1)

The response earned 3 points: 0 points in part A, 0 points in part B, 1 point in part C, and 2 points in part D.

In part A the response did not earn **P1**, **P2**, or **P3**. In an attempt at the alternate solution using separation of variables, the response produces an incorrect solution for the function $y$ and is not eligible for any points in part A.

In part B the response did not earn **P4** or **P5** because no terms of the Taylor polynomial are presented.

In part C the response earned **P6** with the expression $\frac{(60)(0.1)^3}{3!}$ in the middle of line 1. The response did not earn **P7** because there is no explicit connection to error or error bound.

In part D the response earned **P8**. The first step of Euler's method is started on line 2 with the presentation of the correct initial value, value of the derivative, and correct step size. It is completed with the presentation of the point $(1.2, -0.6)$ on line 3. The response earned **P9** with the correct work on line 3 and the presentation of the answer $f(1.4) \approx -0.470$ on line 5.

© 2025 College Board.

Visit College Board on the web: collegeboard.org.
