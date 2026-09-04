<!-- Page 1 -->

2023

AP®

# AP® Calculus BC
## Sample Student Responses and Scoring Commentary

### Inside:

Free-Response Question 6

- ☑ Scoring Guidelines
- ☑ Student Samples
- ☑ Scoring Commentary

© 2023 College Board. College Board, Advanced Placement, AP, AP Central, and the acorn logo are registered trademarks of College Board. Visit College Board on the web: collegeboard.org.

AP Central is the official online home for the AP Program: apcentral.collegeboard.org.

<!-- Page 2 -->

AP® Calculus AB/BC 2023 Scoring Guidelines

## Part B (BC): Graphing calculator not allowed

### Question 6

9 points

#### General Scoring Notes

The model solution is presented using standard mathematical notation.

Answers (numeric or algebraic) need not be simplified. Answers given as a decimal approximation should be correct to three places after the decimal point. Within each individual free-response question, at most one point is not earned for inappropriate rounding.

The function $f$ has derivatives of all orders for all real numbers. It is known that $f(0) = 2$, $f'(0) = 3$,

$$f''(x) = -f(x^2), \text{ and } f'''(x) = -2x \cdot f'(x^2).$$

|  Model Solution | Scoring  |
| --- | --- |
|  (a) Find $f^{(4)}(x)$, the fourth derivative of $f$ with respect to $x$. Write the fourth-degree Taylor polynomial for $f$ about $x = 0$. Show the work that leads to your answer.  |   |
|  $f^{(4)}(x) = -2 \cdot f'(x^2) + (-2x)f''(x^2) \cdot 2x$ | Form of product rule 1 point  |
|   | $f^{(4)}(x)$ 1 point  |
|  $f''(0) = -f(0) = -2$ | Two terms of polynomial 1 point  |
|  $f'''(0) = -2(0) \cdot f'(0) = 0$ |   |
|  $f^{(4)}(0) = -2 \cdot f'(0) + 0 \cdot f''(0) \cdot 0 = -2 \cdot 3 + 0 = -6$ | Remaining terms 1 point  |
|  The fourth-degree Taylor polynomial for $f$ about $x = 0$ is $T_4(x) = 2 + 3x + \frac{-2}{2!}x^2 + \frac{0}{3!}x^3 + \frac{-6}{4!}x^4$ $= 2 + 3x - x^2 - \frac{1}{4}x^4$ |   |

#### Scoring notes:

- The first point is earned for a correct fourth derivative or for $f^{(4)}(x) = -2 \cdot f'(x^2) + (-2x)f''(x^2)$.
- The second point is earned only for a completely correct expression for $f^{(4)}(x)$.
- A response that earns the first point but not the second may evaluate the presented expression for $f^{(4)}(x)$ at $x = 0$ and use the consistent nonzero value in computing the coefficient of $x^4$ in the fourth-degree Taylor polynomial.
- A polynomial that includes a nonzero third-degree term, any terms of degree greater than four, or $+ \ldots$ does not earn the fourth point.

Total for part (a)

4 points

© 2023 College Board

<!-- Page 3 -->

AP® Calculus AB/BC 2023 Scoring Guidelines

(b) The fourth-degree Taylor polynomial for $f$ about $x = 0$ is used to approximate $f(0.1)$. Given that $\left|f^{(5)}(x)\right| \leq 15$ for $0 \leq x \leq 0.5$, use the Lagrange error bound to show that this approximation is within $\frac{1}{10^5}$ of the exact value of $f(0.1)$.

By the Lagrange error bound,

$$\begin{array}{l} \left| T _ {4} (0. 1) - f (0. 1) \right| \leq \frac {\max _ {0 \leq x \leq 0 . 1} \left| f ^ {(5)} (x) \right|}{5 !} \cdot (0. 1) ^ {5} \\ \leq \frac {1 5}{1 2 0} \cdot \frac {1}{1 0 ^ {5}} \leq \frac {1}{1 0 ^ {5}} \\ \end{array}$$

Form of error bound

1 point

Shows $|\text{Error}| \leq \frac{1}{10^5}$

1 point

# Scoring notes:

- The first point is earned for $\frac{\max_{0 \leq x \leq 0.1} \left| f^{(5)}(x) \right|}{5!} \cdot (0.1)^5$ or $\frac{15}{5!} (0.1)^5$. Subsequent errors in simplification will not earn the second point.
- To earn the second point a response must communicate the inequality $\text{Error} \leq \frac{15}{5!} \cdot (0.1)^5 \leq \frac{1}{10^5}$.
- A response that states $\text{Error} = \frac{15}{5!} \cdot (0.1)^5$ or $\text{Error} = \frac{1}{10^5}$ does not earn the second point.

Total for part (b)

2 points

(c) Let $g$ be the function such that $g(0) = 4$ and $g'(x) = e^x f(x)$. Write the second-degree Taylor polynomial for $g$ about $x = 0$.

$$g ^ {\prime \prime} (x) = e ^ {x} \cdot f (x) + e ^ {x} \cdot f ^ {\prime} (x)$$

$$g ^ {\prime} (0) = e ^ {0} \cdot f (0) = 2$$

$$g ^ {\prime \prime} (0) = e ^ {0} \cdot f (0) + e ^ {0} \cdot f ^ {\prime} (0) = 2 + 3 = 5$$

The second-degree Taylor polynomial for $g$ about $x = 0$ is

$$T _ {2} (x) = 4 + 2 x + \frac {5}{2} x ^ {2}.$$

$g''(x)$

1 point

First two terms of polynomial

1 point

Taylor polynomial

1 point

# Scoring notes:

- The first point is earned for $g''(x) = e^x \cdot f(x) + e^x \cdot f'(x)$, $g''(0) = e^0 \cdot f(0) + e^0 \cdot f'(0)$, or $g''(0) = f(0) + f'(0)$.
- A presented polynomial of the form $4 + 2x + ax^2$ earns the second point with or without any supporting work for the first two terms.
- A response that earned neither the first nor the second point only earns the third point for a polynomial of the form $a + bx + \frac{c}{2}x^2$, where $c \neq 0$ is declared to be $g''(0)$.
- A presented polynomial with no support for the coefficient of $x^2$ does not earn the third point.

© 2023 College Board

<!-- Page 4 -->

AP® Calculus AB/BC 2023 Scoring Guidelines

- A polynomial that includes any terms of degree greater than two, or + ..., does not earn the third point.
- Alternate solution:

$$e^x = 1 + x + \frac{x^2}{2} + \cdots$$

$$e^x f(x) = \left(1 + x + \frac{x^2}{2} + \cdots\right)\left(2 + 3x - x^2 + \cdots\right) = 2 + 5x + \cdots$$

$$g(x) = \int e^x f(x) \, dx = C + 2x + \frac{5}{2}x^2 + \cdots$$

$$g(0) = 4 \Rightarrow C = 4$$

$$g(x) \approx 4 + 2x + \frac{5}{2}x^2$$

○ A response that is using this alternate solution method earns the first point for $e^x f(x) = 2 + 5x + \cdots$, the second point for any two correct terms in a second-degree polynomial, and the third point for a completely correct second-degree Taylor polynomial with supporting work.
○ Note: There is not enough information to conclude that $f(x)$ is equal to its Maclaurin series on its interval of convergence. The second and third lines of the alternate solution are being accepted as identifications of the Maclaurin series for $e^x f(x)$ and $g(x)$, respectively.

Total for part (c)

3 points

Total for question 6

9 points

© 2023 College Board

<!-- Page 5 -->

1 of 2

Sample 6A

6 6 6 6 6 NO CALCULATOR ALLOWED 6 6 6 6 6

Answer QUESTION 6 parts (a) and (b) on this page.

Response for question 6(a)

$$f^{(4)}(x) = \frac{d}{dx} f''(x) = \frac{d}{dx} (-2x \cdot f'(x^2))$$

$$= -2 f'(x^2) - 4x^2 \cdot f''(x^2)$$

$$f''(0) = -2; \quad f'''(0) = 0; \quad f^{(4)}(0) = -6$$

$$f(x) \approx 2 + 3x - x^2 - \frac{x^4}{4}$$

Response for question 6(b)

$$|E| \le \left| \frac{15 \cdot (0.1)^5}{5!} \right| = \frac{1}{8 \cdot 10^5} < \frac{1}{10^5}$$

Page 14

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

0003678

Q5217/14

<!-- Page 6 -->

2 of 2

Sample 6A

6 6 6 6 6 NO CALCULATOR ALLOWED 6 6 6 6 6

Answer QUESTION 6 part (c) on this page.

Response for question 6(c)

$$e^x \approx 1 + x \quad (\text{first 2 Taylor terms})$$

$$f(x) \approx 2 + 3x$$

$$e^x f(x) \approx 2 + 5x \quad (\text{first 2 terms})$$

$$g(x) = \int e^x f(x) \approx 2x + \frac{5x^2}{2} + C$$

$$g(0) = 4, \quad g(x) \approx 4 + 2x + \frac{5x^2}{2}$$

Page 15

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

Q5217/15

<!-- Page 7 -->

1 of 2

Sample 6B

6 6 6 6 6 NO CALCULATOR ALLOWED 6 6 6 6 6

Answer QUESTION 6 parts (a) and (b) on this page.

Response for question 6(a)

$$f^4(x) = \frac{d}{dx}(-2 \times f'(x^2))$$

$$(-2x)(2x)f''(x^2)$$

$$f^4(x) = -4x^2f''(x^2)$$

$$\frac{2(x)^0}{0!} + \frac{3(x)}{1!} + \frac{-f(0)x^2}{2!} - \frac{2 \times f'(0)x^3}{3!} - \frac{4 \times^2 f''(x^2)}{4!}x^3$$

$$2 \cdot + 3x - \frac{f(0)x^2}{2} - \frac{2 \times^4 f'(0)}{6} - \frac{4 \times^6 f''(0)}{4!} = P_4(x)$$

Response for question 6(b)

$$\frac{15(0-1)^5}{5!}$$

$$15(-\frac{1}{10})^5$$

$$\frac{-15}{10^5} \times \frac{1}{8 \times 4 \times 8 \times 2 \times 1}$$

$$\frac{-1}{8 \cdot 10^5} \left(\frac{5}{10}\right)^5 \frac{\frac{5}{10^5}}{5!}$$

$$\frac{f^5(x)(x-1)^5}{5!} < \frac{1}{10^5}$$

$$\frac{15(-\frac{1}{10})^5}{5!}$$

$$\left(\frac{-1}{10}\right)^5 \left[ 8 \cdot \frac{-1}{10^5} < \frac{1}{10^5} \right]$$

Page 14

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

0018897

Q5178/14

<!-- Page 8 -->

2 of 2

Sample 6B

6 6 6 6 6 NO CALCULATOR ALLOWED 6 6 6 6 6

Answer QUESTION 6 part (c) on this page.

Response for question 6(c)

$$\begin{array}{l} q(0) = 4 \\ q'(0) = e^{\circ} f(0) = f(0) \\ q''(0) = f'(0) + f(0) \end{array}$$

$$\begin{array}{l} e^{\pi} f(x) \\ e^{\pi} f'(x) + e^{\pi} f(x) \\ e^{\pi} f'(0) + e^{\pi} f(0) \end{array}$$

$$f_4(0) = 4 + f(0)x + \frac{(f'(0) + f(0))x^2}{2}$$

Page 15

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

Q5178/15

<!-- Page 9 -->

1 of 2

Sample 6C

6 6 6 6 6 NO CALCULATOR ALLOWED 6 6 6 6 6

Answer QUESTION 6 parts (a) and (b) on this page.

Response for question 6(a)

Taylor polynomial = f(0) + f'(0)x + \frac{f''(0)x^2}{2!} + \frac{f'''(0)x^3}{3!} + \frac{f'''(0)x^4}{4!}

f(4)(x) = (-2 \cdot f'(x^2)) + (-2 \times (\cdot f''(x^2) \cdot 2x))

Response for question 6(b)

Laguna Error bound \le \left| \frac{f^{(n+1)}(z)(x-c)^{n+1}}{(n+1)!} \right|

\le \left| \frac{0.5(0.5 - 0.1)}{5!} \right| = \frac{-0.5}{5!} \le \frac{1}{10^5} \checkmark

Page 14

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

0074871

Q8179/14

<!-- Page 10 -->

2 of 2

Sample 6C

6 6 6 6 6 NO CALCULATOR ALLOWED 6 6 6 6 6

Answer QUESTION 6 part (c) on this page.

Response for question 6(c)

Taylor polynomial for g about x = 0 →

degree

$$f(0) + f'(0)x + \frac{f'(0)x^2}{2}$$

$$= 4 + e^0 f(0) \cdot x + (e^0 f(0) + e^0 f'(0))$$

$$= 4$$

$$= g(0) + g'(0)x + \frac{g''(0)x^2}{2}$$

Page 15

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

Q8178/15

<!-- Page 11 -->

AP® Calculus BC 2023 Scoring Commentary

# Question 6

Note: Student samples are quoted verbatim and may contain spelling and grammatical errors.

# Overview

In this problem students were told that the function $f$ has derivatives of all orders for all real numbers and that $f(0) = 2$, $f'(0) = 3$, $f''(x) = -f(x^2)$, and $f'''(x) = -2x \cdot f'(x^2)$.

In part (a) students were asked to find $f^{(4)}(x)$ and then to write the fourth-degree Taylor polynomial for $f$ about $x = 0$. A correct response will use the product and chain rules to find $f^{(4)}(x) = -2 \cdot f'(x^2) + (-2x)f''(x^2) \cdot 2x$. The response will then evaluate the first four derivatives of $f$ at $x = 0$ and use these values to write the fourth-degree Taylor polynomial $T_4(x) = f(0) + f'(0) \cdot x + \frac{f''(0)}{2!} \cdot x^2 + \frac{f'''(0)}{3!} \cdot x^3 + \frac{f^{(4)}(0)}{4!} \cdot x^4$, which is $T_4(x) = 2 + 3x - x^2 - \frac{1}{4}x^4$.

In part (b) students were asked to use the Lagrange error bound to show that the approximation of $f(0.1)$ found using the fourth-degree Taylor polynomial is within $\frac{1}{10^5}$ of the exact value, given that $|f^{(5)}(x)| \le 15$ for $0 \le x \le 0.5$. A correct response will indicate that the Lagrange error bound limits the absolute value of the difference between the approximation and the exact value to $\frac{\max_{0 \le x \le 0.1} |f^{(5)}(x)|}{5!} \cdot (0.1)^5 \le \frac{15}{120} \cdot \frac{1}{10^5}$ which is less than $\frac{1}{10^5}$.

In part (c) students were told that $g$ is a function with $g(0) = 4$ and $g'(x) = e^x f(x)$ and asked to write the second-degree Taylor polynomial for $g$ about $x = 0$. A correct response will use the product rule to find $g''(0) = e^0 \cdot f'(0) + e^0 \cdot f(0) = 5$, evaluate $g'(0) = e^0 f(0) = 2$, and then put these two values together with the given value of $g(0) = 4$ to write the polynomial $T_2(x) = 4 + 2x + \frac{5}{2!}x^2$.

# Sample: 6A

# Score: 9

The response earned 9 points: 4 points in part (a), 2 points in part (b), and 3 points in part (c).

In part (a) the response earned the first and second points in the second line of work. The polynomial presented in the fourth line of work earned the response the third and fourth points.

In part (b) the response earned the first and second points with the inequality presented. Note that “$E$” does not require absolute value because the term error may be used to represent the magnitude of difference.

In part (c) the response earned the first point for the alternate solution with the expression in the third line of work. The response earned the second and third points with the correct polynomial in the last line of work. The response did not lose a point for not including the $dx$ in the integral expression in the fourth line of work.

© 2023 College Board.

Visit College Board on the web: collegeboard.org.

<!-- Page 12 -->

AP® Calculus BC 2023 Scoring Commentary

## Question 6 (continued)

**Sample: 6B**

**Score: 4**

The response earned 4 points: 1 point in part (a), no points in part (b), and 3 points in part (c).

In part (a) the response did not earn the first or second point because there is no evidence of the product rule. The response earned the third point with the first two terms of the Taylor polynomial presented in the fourth line. The response did not earn the fourth point because there are only two correct terms in the polynomial presented.

In part (b) the response did not earn the first point because the expression in the first line of work is negative. If the base of the power was positive, the response would have earned the first point. The response is not eligible to earn the second point.

In part (c) the response earned the first point with $g''(0) = f'(0) + f(0)$ in the third line. The second and third points were earned with the correct polynomial presented because the prompt states that $f(0) = 2$ and $f'(0) = 3$.

**Sample: 6C**

**Score: 2**

The response earned 2 points: 2 points in part (a), no points in part (b), and no points in part (c).

In part (a) the response earned the first and second points with the derivative presented in the last line of work. The response did not earn the third or fourth points because the coefficients in the Taylor polynomial are not evaluated.

In part (b) the response did not earn the first point because the Lagrange error bound is not properly used. The response is ineligible to earn the second point.

In part (c) the response did not earn the first point because $g''(x)$ is not presented. The response did not earn the second or third points because the coefficients in the Taylor polynomial are not presented.

© 2023 College Board.

Visit College Board on the web: collegeboard.org.
