<!-- Page 1 -->

2024

AP

# AP® Calculus BC
## Sample Student Responses and Scoring Commentary

### Inside:

Free-Response Question 5

- ☑ Scoring Guidelines
- ☑ Student Samples
- ☑ Scoring Commentary

© 2024 College Board. College Board, Advanced Placement, AP, AP Central, and the acorn logo are registered trademarks of College Board. Visit College Board on the web: collegeboard.org.

AP Central is the official online home for the AP Program: apcentral.collegeboard.org.

<!-- Page 2 -->

AP® Calculus AB/BC 2024 Scoring Guidelines

## Part B (BC): Graphing calculator not allowed

### Question 5

9 points

#### General Scoring Notes

The model solution is presented using standard mathematical notation.

Answers (numeric or algebraic) need not be simplified. Answers given as a decimal approximation should be correct to three places after the decimal point. Within each individual free-response question, at most one point is not earned for inappropriate rounding.

|  x | 0 | \( \pi \) | \( 2\pi \)  |
| --- | --- | --- | --- |
|  \( f'(x) \) | 5 | 6 | 0  |

The function \( f \) is twice differentiable for all \( x \) with \( f(0) = 0 \). Values of \( f' \), the derivative of \( f \), are given in the table for selected values of \( x \).

(a)

|  Model Solution | Scoring  |   |
| --- | --- | --- |
|  For \( x \geq 0 \), the function \( h \) is defined by \( h(x) = \int_{0}^{x} \sqrt{1 + (f'(t))^2} dt \). Find the value of \( h'(\pi) \). Show the work that leads to your answer.  |   |   |
|  \( h'(x) = \sqrt{1 + (f'(x))^2} \) | Fundamental Theorem of Calculus | 1 point  |
|  \( h'(\pi) = \sqrt{1 + (f'(\pi))^2} = \sqrt{1 + 6^2} = \sqrt{37} \) | Answer | 1 point  |

##### Scoring notes:

• A response of  \( \sqrt{1 + (f'(\pi))^{2}} \)  earns the first point.
• A response of  \( \sqrt{1+6^{2}} \)  alone earns both points.
- A response such as \( h'(x) = \sqrt{1 + (f'(x))^2} = \sqrt{37} \), that equates a variable expression to a numeric value, earns at most 1 of the 2 points.
- A response that equates \( h'(x) \) or \( h'(\pi) \) to a derivative of a constant, such as \( h'(x) = \frac{d}{dx} \int_0^\pi \sqrt{1 + (f'(t))^2} dt \), earns at most 1 of the 2 points.

Total for part (a) 2 points

© 2024 College Board

<!-- Page 3 -->

AP® Calculus AB/BC 2024 Scoring Guidelines

(b)

What information does $$\int_0^\pi \sqrt{1 + (f'(x))^2} \, dx$$ provide about the graph of $$f$$?

$$\int_0^\pi \sqrt{1 + (f'(x))^2} \, dx$$ is the arc length of the graph of $$f$$ on $$[0, \pi]$$.

Arc length of $$f$$

1 point

Interval $$[0, \pi]$$

1 point

# Scoring notes:

- A response of “arc length” or “length” earns the first point. Such a response does not need to reference $$f$$. However, if the response references a different function, the response does not earn the first point and is eligible to earn the second point.
- A response referring to distance explicitly connected to the graph or $$f$$ (or equivalent) earns the first point. For example, a response of “distance along the curve” or “distance traveled by a particle moving along $$f$$” earns the first point and is eligible to earn the second point.
- A response referring to distance that is not explicitly connected to the graph of $$f$$ does not earn the first point but is eligible to earn the second point. For example, a response of “distance” or “distance traveled” does not earn the first point but is eligible to earn the second point.
- To earn the second point a response must connect the interval $$[0, \pi]$$ to arc length, length, or distance.

Total for part (b) 2 points

© 2024 College Board

<!-- Page 4 -->

AP® Calculus AB/BC 2024 Scoring Guidelines

(c) Use Euler's method, starting at $x = 0$ with two steps of equal size, to approximate $f(2\pi)$. Show the computations that lead to your answer.

|  $f(\pi) \approx f(0) + \pi f'(0) = 0 + 5\pi = 5\pi$ | Euler's method | **1 point**  |
| --- | --- | --- |
|  $f(2\pi) \approx f(\pi) + \pi f'(\pi)$ |  |   |
|  $\approx 5\pi + 6\pi = 11\pi$ | Answer | **1 point**  |

# Scoring notes:

- To earn the first point a response must demonstrate two Euler's steps, with use of the correct expression for $\frac{dy}{dx}$, and at most one error. If there is an error, the second point is not earned.
- In order to earn the first point, a response that presents a single error in computing the approximation of $f(\pi)$ must import the incorrect value in computing the approximation of $f(2\pi)$.
- The two Euler's steps may be explicit expressions or may be presented in a table. For example:

|  $x$ | $y$ | $\frac{dy}{dx} \cdot \Delta x$ (or $\frac{dy}{dx} \cdot \pi$)  |
| --- | --- | --- |
|  $0$ | $0$ | $5\pi$  |
|  $\pi$ | $5\pi$ | $6\pi$  |
|  $2\pi$ | $11\pi$ |   |

In the presence of a correct answer, a table does not need to be labeled in order to earn both points. In the presence of no answer or an incorrect answer, such a table must be correctly labeled in order to earn the first point.

- Both points are earned for $5\pi + 6\pi$.
- The response may report the final answer as $(2\pi, 11\pi)$.

Total for part (c) 2 points

© 2024 College Board

<!-- Page 5 -->

AP® Calculus AB/BC 2024 Scoring Guidelines

(d)

Find $$\int (t + 5)\cos \left(\frac{t}{4}\right)dt$$. Show the work that leads to your answer.

|  $$u = t + 5$$ $$dv = \cos \left(\frac{t}{4}\right) dt$$ | $$u$$ and $$dv$$ | **1 point**  |
| --- | --- | --- |
|  $$du = dt$$ $$v = 4 \sin \left(\frac{t}{4}\right)$$ |  |   |
|  $$\int (t + 5)\cos \left(\frac{t}{4}\right) dt = 4(t + 5)\sin \left(\frac{t}{4}\right) - \int 4\sin \left(\frac{t}{4}\right) dt$$ | $$uv - \int v \, du$$ | **1 point**  |
|  $$= 4(t + 5)\sin \left(\frac{t}{4}\right) + 16\cos \left(\frac{t}{4}\right) + C$$ | Answer | **1 point**  |

# Scoring notes:

- The first and second points are earned with an implied $$u$$ and $$dv$$ in the presence of $$4(t + 5)\sin \left(\frac{t}{4}\right) - \int 4\sin \left(\frac{t}{4}\right)dt$$ or a mathematically equivalent expression.

- The tabular method may be used to show integration by parts. In this case, the first point is earned by columns (labeled or unlabeled) that begin with $$t + 5$$ and $$\cos \left(\frac{t}{4}\right)$$. The second point is earned for $$4(t + 5)\sin \left(\frac{t}{4}\right) - \int 4\sin \left(\frac{t}{4}\right)dt$$ or a mathematically equivalent expression.

- The third point is earned only for an expression mathematically equivalent to $$4(t + 5)\sin \left(\frac{t}{4}\right) + 16\cos \left(\frac{t}{4}\right) + C$$ (such as $$4t\sin \left(\frac{t}{4}\right) + 20\sin \left(\frac{t}{4}\right) + 16\cos \left(\frac{t}{4}\right) + C$$) in the presence of correct supporting work.

- To earn the third point a response must have a final answer that includes a constant of integration.

- Alternate solution:

$$\int (t + 5)\cos \left(\frac{t}{4}\right) dt = \int t\cos \left(\frac{t}{4}\right) dt + \int 5\cos \left(\frac{t}{4}\right) dt$$

$$u = t \quad dv = \cos \left(\frac{t}{4}\right) dt$$

$$du = dt \quad v = 4\sin \left(\frac{t}{4}\right)$$

$$\int t\cos \left(\frac{t}{4}\right) dt + \int 5\cos \left(\frac{t}{4}\right) dt = 4t\sin \left(\frac{t}{4}\right) - \int 4\sin \left(\frac{t}{4}\right) dt + \int 5\cos \left(\frac{t}{4}\right) dt$$

$$= 4t\sin \left(\frac{t}{4}\right) + 16\cos \left(\frac{t}{4}\right) + 20\sin \left(\frac{t}{4}\right) + C$$

- A response can earn the first and second points for correctly applying integration by parts to $$\int t\cos \left(\frac{t}{4}\right)dt$$. The tabular method may be used to show integration by parts. The third point is earned for the correct answer.

Total for part (d) 3 points

Total for question 5 9 points

© 2024 College Board

<!-- Page 6 -->

1 of 2

Sample 5A

5 5 5 5 5 NO CALCULATOR ALLOWED 5 5 5 5 5

Answer QUESTION 5 parts (a) and (b) on this page.

|  x | 0 | π | 2π  |
| --- | --- | --- | --- |
|  f'(x) | 5 | 6 | 0  |

Response for question 5(a)

$$h(x) = \int_{0}^{x} \sqrt{1 + (f'(t))^2} \, dt \quad h'(x) = \sqrt{1 + (f'(x))^2}$$

$$h'(x) = \sqrt{1 + (f'(x))^2} = \sqrt{1 + (6)^2} = \sqrt{1 + 36} = \boxed{\sqrt{37}}$$

Response for question 5(b)

The $$\int_{0}^{x} \sqrt{1 + (f'(x))^2} \, dx$$ evaluates the arc length of

$$f(x)$$ from $$x=0$$ to $$x=\pi$$.

Page 12

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

0027251

Q5228/12

<!-- Page 7 -->

2 of 2

Sample 5A

5 5 5 5 5 NO CALCULATOR ALLOWED 5 5 5 5 5

Answer QUESTION 5 parts (c) and (d) on this page.

Response for question 5(c)

|  x | y | f'(x) | Δy  |
| --- | --- | --- | --- |
|  0 | 0 | 5 | 5π  |
|  π | 5π | 6 | 6π  |
|  2π | 11π |  |   |

$$\Delta y = \Delta x f'(x)$$

$$y = y_0 + \Delta y$$

$$(5)(\pi) = 5\pi \quad 5\pi + 0 = 5\pi$$

$$(6)(\pi) = 6\pi$$

$$f'(\pi) = 6 \quad f'(0) = 5$$

$$5\pi + 6\pi = 11\pi$$

$$f(2\pi) \approx 11\pi$$

Response for question 5(d)

$$\int (t+5) \cos(\frac{t}{4}) dt = (t+5) 4 \sin(\frac{t}{4}) - \int 4 \sin(\frac{t}{4}) dt$$
$$v = t+5 \quad dV = \cos(\frac{t}{4}) dt$$
$$dv = dt \quad V = 4 \sin(\frac{t}{4}) = 4 t \sin(\frac{t}{4}) + 2 \cos(\frac{t}{4}) + 16 \cos(\frac{t}{4}) + C$$

$$\int (t+5) \cos(\frac{t}{4}) dt = 4 t \sin(\frac{t}{4}) + 2 \cos(\frac{t}{4}) + 16 \cos(\frac{t}{4}) + C$$

Page 13

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

Q5228/13

<!-- Page 8 -->

1 of 2

Sample 5B

5 5 5 5 5 NO CALCULATOR ALLOWED 5 5 5 5 5

Answer QUESTION 5 parts (a) and (b) on this page.

|  x | 0 | π | 2π  |
| --- | --- | --- | --- |
|  f'(x) | 5 | 6 | 0  |

Response for question 5(a)

$$h'(x) = \sqrt{1 + (f'(x))^2}$$ by fund thm of calc

$$h'(x) = \sqrt{1 + (f'(x))^2}$$

$$h'(x) = \boxed{\sqrt{37}}$$

Response for question 5(b)

Accumulates on interval 0<x<x

Page 12

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

0045608

Q5228/12

<!-- Page 9 -->

2 of 2

Sample 5B

5

5

5

5

5

NO CALCULATOR ALLOWED

5

5

5

5

5

Answer QUESTION 5 parts (c) and (d) on this page.

Response for question 5(c)

|   | og y | slope step | new  |
| --- | --- | --- | --- |
|  0 | 0 | 5π | 5π  |
|  π | 5π | 6π | 11π  |
|  2π | 11π |  |   |

11π

Response for question 5(d)

$$\int (t+5) \cos(\frac{\pi}{4}) dt$$

$$(t+5) \cdot 4 \sin(\frac{\pi}{4}) + 16 \cos(\frac{\pi}{4})$$

$$\begin{array}{c|c} D & I \\ \hline t+5 & \cos(\frac{\pi}{4}) \\ 1 & 4 \sin(\frac{\pi}{4}) \\ 0 & 16 \cos(\frac{\pi}{4}) \end{array}$$

Page 13

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

Q5228/13

<!-- Page 10 -->

1 of 2

Sample 5C

5 5 5 5 5 NO CALCULATOR ALLOWED 5 5 5 5 5

Answer QUESTION 5 parts (a) and (b) on this page.

|  x | 0 | π | 2π  |
| --- | --- | --- | --- |
|  f'(x) | 5 | 6 | 0  |

Response for question 5(a)

$$h(x) = \int_{0}^{x} \sqrt{1 + (f'(t))^2} \, dt$$

$$n'(x) = \sqrt{1 + (f'(x))^2}$$

$$n'(\pi) = \sqrt{1 + (f'(\pi))^2}$$

$$n'(\pi) = \sqrt{1 + (6)^2} = \sqrt{37}$$

Response for question 5(b)

$$\int_{0}^{\pi} \sqrt{1 + (f'(x))^2}$$, provides the sum of the change in the function

$$\sqrt{1 + (f'(x))^2}$$ over the interval $$0 \le x \le \pi$$.

Page 12

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

0069252

Q5228/12

<!-- Page 11 -->

2 of 2

Sample 5C

5 5 5 5 NO CALCULATOR ALLOWED 5 5 5 5 5

Answer QUESTION 5 parts (c) and (d) on this page.

Response for question 5(c)

$$f(0) = 0$$

$$f'(0) = 5$$

$$y_1 = 0 + 5(x - 0)$$

$$y_1 = 0 + 5(\pi - 0)$$

$$y_1 = 5\pi$$

$$f(\pi) = 5\pi$$

$$f'(\pi) = 6$$

$$y_2 = 5\pi + 6(x - \pi)$$

$$y_2 = 5\pi + 6(\pi)$$

$$y_2 = 11\pi = f(2\pi)$$

Response for question 5(d)

$$\int (t+5) \cos(\frac{t}{4})$$

$$v = t + 5 \quad v = \cos \frac{t}{4}$$

$$dv = dt \quad dv = \frac{1}{4} \sin \frac{t}{4} dt$$

$$(t+5)(cos \frac{t}{4}) - \int \frac{1}{4} \sin \frac{t}{4} dt$$

Page 13

Use a pencil or a pen with black or dark blue ink. Do NOT write your name. Do NOT write outside the box.

Q5228/13

<!-- Page 12 -->

AP® Calculus BC 2024 Scoring Commentary

# Question 5

Note: Student samples are quoted verbatim and may contain spelling and grammatical errors.

# Overview

In this question, students were told that the function $f$ is twice differentiable and that $f(0) = 0$. A table of selected values of $x$ and $f'(x)$ was provided.

In part (a) students were told that for $x \geq 0$, the function $h$ is defined by $h(x) = \int_0^x \sqrt{1 + (f'(t))^2} \, dt$ and were asked to find the value of $h'(\pi)$. A correct response will use the Fundamental Theorem of Calculus to find $h'(x) = \sqrt{1 + (f'(x))^2}$, then will evaluate this expression at $x = \pi$.

In part (b) students were asked what information the expression $\int_0^\pi \sqrt{1 + (f'(x))^2} \, dx$ provides about the graph of $f$. A correct response indicates that this is the expression for the arc length of the graph of $f$ on the interval $[0, \pi]$.

In part (c) students were told to use Euler's method to approximate $f(2\pi)$, starting at $x = 0$, with two steps of equal size. A correct response will use the line tangent to the graph of $f$ at $(0, 0)$ to find an approximation for $f(\pi)$, then use the line tangent to the graph of $f$ at $(\pi, f(\pi))$ to approximate the value of $f(2\pi)$.

In part (d) students were asked to find $\int (t + 5)\cos\left(\frac{t}{4}\right) \, dt$. A correct response will use the technique of integration by parts to find an answer of $4(t + 5) \cdot \sin\left(\frac{t}{4}\right) + 16\cos\left(\frac{t}{4}\right) + C$.

# Sample: 5A

# Score: 9

The response earned 9 points: 2 points in part (a), 2 points in part (b), 2 points in part (c), and 3 points in part (d).

In part (a) the response earned the first point with the correct application of the Fundamental Theorem of Calculus in line 1 on the right. The response would have earned the second point with the expression $\sqrt{1 + (6)^2}$. In this case, the response correctly simplifies to the expression $\sqrt{37}$ at the end of line 2 and earned the second point.

In part (b) the response earned the first point with the phrase "arc length of $f(x)$." The response earned the second point with the interval "from $x = 0$ to $x = \pi$" in line 2.

In part (c) the response earned the first point with two correct Euler's steps in the table. The response earned the second point with the boxed answer $f(2\pi) \approx 11\pi$.

In part (d) the response earned the first point with the correct identification of $u$ and $dv$ in line 2. The response earned the second point with the correct application of integration by parts on the right side of line 1. The response earned the third point with the boxed answer.

© 2024 College Board.

Visit College Board on the web: collegeboard.org.

<!-- Page 13 -->

AP® Calculus BC 2024 Scoring Commentary

## Question 5 (continued)

**Sample: 5B**

**Score: 6**

The response earned 6 points: 2 points in part (a), no points in part (b), 2 points in part (c), and 2 points in part (d).

In part (a) the response earned the first point with the correct application of the Fundamental Theorem of Calculus in line 1. The response earned the second point with the boxed solution $\sqrt{37}$ at the end of line 3.

In part (b) the response did not earn the first point with the phrase “Accumulates” because this phrase does not reference arc length. The response did not earn the second point because the second point cannot be earned without a connection to arc length.

In part (c) the response earned the first point with two correct Euler’s steps in the table. The response earned the second point with the boxed answer of $11\pi$.

In part (d) the response earned the first point with the table on the right which begins with the columns $t + 5$ and $\cos\left(\frac{t}{4}\right)$. The response earned the second point with the correct application of integration by parts on the left in line 2. The response did not earn the third point because the boxed answer does not include a constant of integration.

**Sample: 5C**

**Score: 4**

The response earned 4 points: 2 points in part (a), no points in part (b), 2 points in part (c), and no points in part (d).

In part (a) the response earned the first point with the correct application of the Fundamental Theorem of Calculus in line 2. The response would have earned the second point with the expression $\sqrt{1 + (6)^2}$ in line 4. In this case, the response correctly simplifies to the solution $\sqrt{37}$ at the end of line 4 and earned the second point.

In part (b) the response did not earn the first point with the phrase “the sum of the change in the function” because this phrase does not reference arc length. The response did not earn the second point because the second point cannot be earned without a connection to arc length.

In part (c) the response earned the first point with two correct Euler’s steps in line 4 and line 9. The response earned the second point with the answer of $y_2 = 11\pi = f(2\pi)$ in line 10.

In part (d) the response did not earn the first point with the incorrect identification of $dv$ in line 3. The response did not earn the second point because the response applies integration by parts with the incorrect function for $v$ in line 4. The response did not earn the third point because the integration is not complete.

© 2024 College Board.

Visit College Board on the web: collegeboard.org.
