<!-- Page 1 -->

2025

![img-0.jpeg](ap25-sg-calculus-bc_assets/page-1-img-0.jpeg)

# AP® Calculus BC
## Scoring Guidelines

© 2025 College Board. College Board, Advanced Placement, AP, AP Central, and the acorn logo are registered trademarks of College Board. Visit College Board on the web: collegeboard.org.

AP Central is the official online home for the AP Program: apcentral.collegeboard.org.

<!-- Page 2 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

### Part A (AB or BC): Graphing calculator required

#### Question 1

9 points

##### General Scoring Notes

- The model solution is presented using standard mathematical notation.
- Answers (numeric or algebraic) need not be simplified. Answers given as a decimal approximation should be accurate to three places after the decimal point. Within each individual free-response question, at most one point is not earned for inappropriate rounding.

An invasive species of plant appears in a fruit grove at time \( t = 0 \) and begins to spread. The function \( C \) defined by \( C(t) = 7.6\arctan (0.2t) \) models the number of acres in the fruit grove affected by the species \( t \) weeks after the species appears. It can be shown that \( C'(t) = \frac{38}{25 + t^2} \).

(Note: Your calculator should be in radian mode.)

|   | Model Solution | Scoring  |   |
| --- | --- | --- | --- |
|  A | Find the average number of acres affected by the invasive species from time \( t = 0 \) to time \( t = 4 \) weeks.Show the setup for your calculations.  |   |   |
|   |  \( \frac{1}{4-0}\int_{0}^{4}C(t)dt \) | Average value formula | Point 1 (P1)  |
|   |  \( =\frac{1}{4}(11.112896)=2.778224 \)From time \( t = 0 \) to \( t = 4 \) weeks, the average number of acres affected by the invasive species was 2.778 acres. | Answer | Point 2 (P2)  |

© 2025 College Board

<!-- Page 3 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

### Scoring Notes for Part A

- **P1** is earned for the correct integral, with or without the differential, along with evidence of division by 4. In the presence of the correct integral, the correct answer will suffice as evidence of division by 4. These may appear all in one step, as in the model solution, or in multiple steps.
- **P2** is earned for the correct answer, with or without supporting work. A reported answer should be accurate to three places after the decimal point, rounded or truncated. An inappropriately rounded answer does not earn the point.
- Incorrect or unclear communication between the correct integral and the correct answer is treated as scratch work and is not considered in scoring. For example:

○ $$\int_{0}^{4} C(t) \, dt = 11.112896$$ so the average velocity is 2.778224.

Note: This response earns **P1** for the correct integral with the correct answer as evidence of division by 4. It also earns **P2** for the correct answer.

○ $$\int_{0}^{4} C(t) \, dt = \frac{11.112896}{4} = 2.778224$$

Note: This response earns **P1** for the correct integral with the correct answer as evidence of division by 4. It also earns **P2** for the correct answer. (In this instance, incorrect linkage is not considered in scoring.)

○ $$\int_{0}^{4} C(t) \, dt = 2.778224$$

Note: This response earns **P1** for the correct integral with the correct answer as evidence of division by 4. It also earns **P2** for the correct answer. (In this instance, incorrect linkage is not considered in scoring.)

- Note that the values $$\frac{1}{4}(11.112)$$ and $$\frac{1}{4}(11.113)$$ are accurate to three digits after the decimal and therefore earn **P2**.

© 2025 College Board

<!-- Page 4 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

B

Find the time $t$ when the instantaneous rate of change of $C$ equals the average rate of change of $C$ over the time interval $0 \leq t \leq 4$. Show the setup for your calculations.

$$\frac{C(4) - C(0)}{4 - 0} = 1.282008$$

$$C'(t) = \frac{38}{25 + t^2} = 1.282008 \Rightarrow t = 2.154298$$

The instantaneous rate of change of $C$ equals the average rate of change of $C$ over the interval $0 \leq t \leq 4$ at time $t = 2.154$.

Uses average rate of change

Point 3 (P3)

Answer with supporting work

Point 4 (P4)

### Scoring Notes for Part B

- P3 may be earned by presenting the expression or value for the average rate of change. Note that

because $C(0) = 0$ and the interval is $0 \leq t \leq 4$, any of the following will earn P3: $\frac{\int_0^4 C'(t) \, dt}{4}$, $\frac{C(4) - C(0)}{4 - 0}$, $\frac{C(4)}{4}$, $\frac{5.128 - 0}{4 - 0}$, $\frac{5.128}{4}$, or 1.282. However, neither P3 nor P4 is earned by just presenting $t = 1.282$.

- P4 is earned for the correct answer supported by the appropriate equation. A reported answer should be accurate to three places after the decimal point, rounded or truncated. An inappropriately rounded answer does not earn the point, unless an earlier point was not earned due to inappropriate rounding.

The following response, for example, earns both P3 and P4: $C'(t) = \frac{C(4) - C(0)}{4}$ when $t = 2.154$.

C

Assume that the invasive species continues to spread according to the given model for all times $t > 0$. Write a limit expression that describes the end behavior of the rate of change in the number of acres affected by the species. Evaluate this limit expression.

$$\lim_{t \to \infty} C'(t) = \lim_{t \to \infty} \frac{38}{25 + t^2}$$

$$= 0$$

Limit expression

Point 5 (P5)

Value

Point 6 (P6)

### Scoring Notes for Part C

- P5 can be earned for either $\lim_{t \to \infty} C'(t)$ or $\lim_{t \to \infty} C(t)$.

- A response that includes $\lim_{t \to \infty} C(t)$ is not eligible to earn P6.

- For P6, arithmetic with infinity, e.g., $\frac{38}{25 + \infty^2} = 0$, will be considered as scratch work and will not be considered in scoring.

© 2025 College Board

<!-- Page 5 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

D

At time $t = 4$ weeks after the invasive species appears in the fruit grove, measures are taken to counter the spread of the species. The function $A$, defined by $A(t) = C(t) - \int_{4}^{t} 0.1 \cdot \ln(x) \, dx$, models the number of acres affected by the species over the time interval $4 \leq t \leq 36$. At what time $t$, for $4 \leq t \leq 36$, does $A$ attain its maximum value? Justify your answer.

$$A'(t) = C'(t) - 0.1 \cdot \ln t$$

Considers $A'(t) = 0$ Point 7 (P7)

For $4 \leq t \leq 36$, the maximum value of $A(t)$ occurs when $A'(t) = 0$ or at an endpoint.

$$A'(t) = C'(t) - 0.1 \cdot \ln t = 0 \Rightarrow C'(t) = 0.1 \cdot \ln t$$

$$\Rightarrow t = 11.441700$$

Justification Point 8 (P8)

|  t | A(t)  |
| --- | --- |
|  4 | 5.128031  |
|  11.441700 | 7.316978  |
|  36 | 1.743056  |

Therefore, the number of acres affected by the species is a maximum at time $t = 11.442$ (or 11.441) weeks.

Answer with Supporting work Point 9 (P9)

### Scoring Notes for Part D

- P7 is earned for considering $A'(t) = 0$, $C'(t) - 0.1 \cdot \ln t = 0$, or $C'(t) = 0.1 \cdot \ln t$. P7 is not earned by just presenting $t = 11.441700$.

A response that discusses the sign of $A'(t)$ changing or uses the phrase “critical points of $A$” also earns P7.

- To earn P8 using a candidates test, a response must make a global argument by correctly evaluating $A(t)$ at $t = 4$, $t = 11.441700$, and $t = 36$. The evaluations must be correct to the first digit after the decimal, rounded or truncated.

- Alternate justifications:

  - $A'(t) > 0$ for $4 < t < 11.442$, and $A'(t) < 0$ for $11.442 < t < 36$. Therefore, $t = 11.442$ is the location of the absolute maximum for $A$ on the interval $4 \leq t \leq 36$.

  - Because $A'(t)$ changes sign from positive to negative at $t = 11.442$ (this might be presented as “$A'(t) > 0$ for $t < 11.442$, and $A'(t) < 0$ for $t > 11.442$”), it is the location of a relative maximum for $A$. And because $t = 11.442$ is the only critical point of $A$ in the interval $4 \leq t \leq 36$, it is the location of the absolute maximum for $A$ on the interval.

- A response that presents a local argument (such as a First Derivative Test or a Second Derivative Test) or an incorrect global argument does not earn P8 but is eligible for P9 with the correct answer. A reported answer should be accurate to three places after the decimal point, rounded or truncated. An inappropriately rounded answer does not earn the point, unless an earlier point was not earned due to inappropriate rounding.

© 2025 College Board

<!-- Page 6 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

### Part A (BC): Graphing calculator required

#### Question 2

9 points

##### General Scoring Notes

- The model solution is presented using standard mathematical notation.
- Answers (numeric or algebraic) need not be simplified. Answers given as a decimal approximation should be accurate to three places after the decimal point. Within each individual free-response question, at most one point is not earned for inappropriate rounding.

Curve \( C \) is defined by the polar equation \( r(\theta) = 2\sin^2\theta \) for \( 0 \leq \theta \leq \pi \). Curve \( C \) and the semicircle \( r = \frac{1}{2} \) for \( 0 \leq \theta \leq \pi \) are shown in the \( xy \)-plane.

![img-1.jpeg](ap25-sg-calculus-bc_assets/page-6-img-1.jpeg)

(Note: Your calculator should be in radian mode.)

|   | Model Solution | Scoring  |   |
| --- | --- | --- | --- |
|  A | Find the rate of change of \( r \) with respect to \( \theta \) at the point on curve \( C \) where \( \theta = 1.3 \). Show the setup for your calculations.  |   |   |
|   | \( \left.\frac{dr}{d\theta}\right|_{\theta=1.3} = 1.031003 \)The rate of change of \( r \) with respect to \( \theta \) at the point on curve \( C \) where \( \theta = 1.3 \) is 1.031. | Answer with setup | Point 1 (P1)  |

© 2025 College Board

<!-- Page 7 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

### Scoring Notes for Part A

- An exact answer of $\left.\frac{dr}{d\theta}\right|_{\theta=1.3} = 4\sin(1.3)\cos(1.3)$ earns P1.
- To earn P1, a response must indicate differentiation of $r$ and provide the correct answer. A reported answer should be accurate to three places after the decimal point, rounded or truncated. An inappropriately rounded answer does not earn the point.

○ Examples of responses with correct communication include $\left.\frac{dr}{d\theta}\right|_{\theta=1.3} = 1.031$ and $r'(1.3) = 1.031$.

○ Responses with incorrect communication, such as $r'(\theta) = 1.031$, $r' = 1.031$, or $\frac{dr}{d\theta} = 1.031$, are sufficient to earn P1.

B

Find the area of the region that lies inside curve $C$ but outside the graph of the polar equation $r = \frac{1}{2}$. Show the setup for your calculations.

For $0 \le \theta \le \pi$, $r(\theta) = \frac{1}{2}$ for $\theta = \theta_1 = \frac{\pi}{6} = 0.523599$ and $\theta = \theta_2 = \frac{5\pi}{6} = 2.617994$.

$$\frac{1}{2} \int_{\theta_1}^{\theta_2} \left( (r(\theta))^2 - \left(\frac{1}{2}\right)^2 \right) d\theta$$

$$= 2.066769$$

The area is 2.067 (or 2.066).

Integrand including $\left(r(\theta)\right)^2$ Point 2 (P2)

Integrand Point 3 (P3)

Answer Point 4 (P4)

### Scoring Notes for Part B

- P2 is earned for a definite integral including $(r(\theta))^2$, such as $\int_a^b \left( (r(\theta))^2 - \left(\frac{1}{2}\right)^2 \right) d\theta$ or $\int_a^b (r(\theta))^2 d\theta$, with or without the differential $d\theta$.

- P3 is earned for a definite integral (or integrals) with a correct integrand, such as $\int_a^b \left( (r(\theta))^2 - \left(\frac{1}{2}\right)^2 \right) d\theta$ or $\int_a^b (r(\theta))^2 d\theta - \int_c^d \left(\frac{1}{2}\right)^2 d\theta$, with or without the differential $d\theta$.

- The limits $\theta_1 = \frac{\pi}{6} = 0.523599$ and $\theta_2 = \frac{5\pi}{6} = 2.617994$ and the factor $\frac{1}{2}$ are assessed in P4, not in P2 or P3.

- P4 is earned for the correct answer, with or without supporting work. A reported answer should be accurate to three places after the decimal point, rounded or truncated. An inappropriately rounded answer does not earn the point, unless an earlier point was not earned due to inappropriate rounding.

© 2025 College Board

<!-- Page 8 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

- Incorrect or unclear communication between the correct integral and the correct answer is treated as scratch work and is not considered in scoring. For example:

$$\circ \int_{\pi/6}^{5\pi/6} \left( (r(\theta))^2 - \left(\frac{1}{2}\right)^2 \right) d\theta = 4.133538 \text{ so the area is } 2.067.$$

Note: This response earns P2 and P3 for the integral. It also earns P4 for the correct answer.

$$\circ \int_{\pi/6}^{5\pi/6} \left( (r(\theta))^2 - \left(\frac{1}{2}\right)^2 \right) d\theta = 2.067$$

Note: This response earns P2 and P3 for the integral. It also earns P4 for the correct answer. (In this instance, incorrect linkage is not considered in scoring.)

- Special case: An indefinite integral with a correct integrand does not earn P2, earns P3, and is eligible to earn P4 with a correct answer.
- A response of $$\int_{\pi/6}^{\pi/2} \left( (r(\theta))^2 - \left(\frac{1}{2}\right)^2 \right) d\theta = 2.067$$, using the symmetry of the region, earns P2, P3, and P4.

C

It can be shown that $$\frac{dx}{d\theta} = 4\sin\theta\cos^2\theta - 2\sin^3\theta$$ for curve C. For $$0 \le \theta \le \frac{\pi}{2}$$, find the value of $$\theta$$ that corresponds to the point on curve C that is farthest from the y-axis. Justify your answer.

For $$0 \le \theta \le \frac{\pi}{2}$$, the curve C is in the first quadrant. Thus, a point on the curve will be farthest away from the y-axis when the x-coordinate attains its maximum value. This will either occur when $$\frac{dx}{d\theta} = 0$$ or at an endpoint of the interval

$$0 \le \theta \le \frac{\pi}{2}.$$

$$\frac{dx}{d\theta} = 0$$

$$\Rightarrow \theta = 0.955317$$

|  $$\theta$$ | $$x(\theta) = r(\theta)\cos\theta$$  |
| --- | --- |
|  0 | 0  |
|  0.955317 | 0.769800  |
|  $$\frac{\pi}{2}$$ | 0  |

Therefore, the value of $$\theta$$ for which the point on the curve is farthest from the y-axis is 0.955.

Considers $$\frac{dx}{d\theta} = 0$$

Point 5 (P5)

Justification

Point 6 (P6)

Answer with supporting work

Point 7 (P7)

© 2025 College Board

<!-- Page 9 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

# Scoring Notes for Part C

- P5 is earned for considering $$\frac{dx}{d\theta} = 0$$. P5 is not earned by just presenting $$\theta = 0.955317$$.

A response that discusses the sign of $$\frac{dx}{d\theta}$$ changing or uses the phrase “critical points of $$x(\theta)$$” also earns P5.

- The value $$\theta = 0.955317$$ might be presented as $$\arccos\left(\frac{1}{\sqrt{3}}\right)$$, $$\arcsin\left(\sqrt{\frac{2}{3}}\right)$$, or $$\arctan(\sqrt{2})$$.

- To earn P6 using a candidates test, a response must make a global argument by correctly evaluating $$x(\theta)$$ at $$\theta = 0$$, $$\theta = 0.955317$$, and $$\theta = \frac{\pi}{2}$$. The evaluations must be correct to the first digit after the decimal, rounded or truncated.

- Alternate justifications:

  - $$\frac{dx}{d\theta} > 0$$ for $$0 < \theta < 0.955$$, and $$\frac{dx}{d\theta} < 0$$ for $$0.955 < \theta < \frac{\pi}{2}$$. Therefore, $$\theta = 0.955$$ is the location of the absolute maximum for $$x(\theta)$$ on the interval $$0 \leq \theta \leq \frac{\pi}{2}$$.

  - Because $$\frac{dx}{d\theta}$$ changes sign from positive to negative at $$\theta = 0.955$$ (this might be presented as “$$\frac{dx}{d\theta} > 0$$ for $$\theta < 0.955$$, and $$\frac{dx}{d\theta} < 0$$ for $$\theta > 0.955$$”), it is the location of a relative maximum for $$x(\theta)$$. And because $$\theta = 0.955$$ is the only critical point of $$x(\theta)$$ in the interval $$0 \leq \theta \leq \frac{\pi}{2}$$, it is the location of the absolute maximum for $$x(\theta)$$ on the interval.

  - Because $$\left.\frac{dx}{d\theta}\right|_{\theta=0.955} = 0$$ and $$\left.\frac{d^2x}{d\theta^2}\right|_{\theta=0.955} < 0$$, $$\theta = 0.955$$ is the location of a relative maximum for $$x(\theta)$$. And because $$\theta = 0.955$$ is the only critical point of $$x(\theta)$$ in the interval $$0 \leq \theta \leq \frac{\pi}{2}$$, it is the location of the absolute maximum for $$x(\theta)$$ on the interval.

- A response that presents only a local argument (such as a First Derivative Test or a Second Derivative Test) or an incorrect global argument does not earn P6 but is eligible for P7 with the correct answer. A reported answer should be accurate to three places after the decimal point, rounded or truncated. An inappropriately rounded answer does not earn the point, unless an earlier point was not earned due to inappropriate rounding.

© 2025 College Board

<!-- Page 10 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

D

A particle travels along curve C so that $$\frac{d\theta}{dt} = 15$$ for all times t. Find the rate at which the particle's distance from the origin changes with respect to time when the particle is at the point where $$\theta = 1.3$$. Show the setup for your calculations.

$$\left. \frac{dr}{dt} \right|_{\theta=1.3} = \left( \frac{dr}{d\theta} \cdot \frac{d\theta}{dt} \right) \Bigg|_{\theta=1.3} = 1.031003 \cdot 15 = 15.465041$$

The particle's distance from the origin changes at a rate of 15.465.

$$\frac{dr}{d\theta} \cdot \frac{d\theta}{dt}$$

Point 8 (P8)

Answer

Point 9 (P9)

### Scoring Notes for Part D

- To earn P8, $$\frac{dr}{d\theta} \cdot \frac{d\theta}{dt}$$ can be presented either symbolically or numerically.
- P8 might be earned in one or more steps.
- A response of 1.031·15 or [answer from part A]·15 earns both P8 and P9.
- P9 is earned for the correct answer, with or without supporting work. A reported answer should be accurate to three places after the decimal point, rounded or truncated. An inappropriately rounded answer does not earn the point, unless an earlier point was not earned due to inappropriate rounding.

© 2025 College Board

<!-- Page 11 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

## Part B (AB or BC): Graphing calculator not allowed

### Question 3

9 points

#### General Scoring Notes

- The model solution is presented using standard mathematical notation.
- Answers (numeric or algebraic) need not be simplified. Answers given as a decimal approximation should be accurate to three places after the decimal point. Within each individual free-response question, at most one point is not earned for inappropriate rounding.

A student starts reading a book at time t = 0 minutes and continues reading for the next 10 minutes. The rate at which the student reads is modeled by the differentiable function R, where  \( R(t) \)  is measured in words per minute. Selected values of  \( R(t) \)  are given in the table shown.

|  t (minutes) | 0 | 2 | 8 | 10  |
| --- | --- | --- | --- | --- |
|  R(t) (words per minute) | 90 | 100 | 150 | 162  |

#### Model Solution

#### Scoring

A Approximate \( R'(1) \) using the average rate of change of \( R \) over the interval \( 0 \leq t \leq 2 \). Show the work that leads to your answer. Indicate units of measure.

\[
R ^ {\prime} (1) \approx \frac {R (2) - R (0)}{2 - 0}
\]

\[
= \frac {1 0 0 - 9 0}{2} = \frac {1 0}{2} = 5 \text { words   per   minute   per   minute }
\]

Answer with setup Point 1 (P1)

Units Point 2 (P2)

#### Scoring Notes for Part A

- To earn P1, a response must present the answer along with the supporting work of a difference and a quotient using values from the table.

\(\frac{100 - 90}{2 - 0}, \frac{10}{2 - 0}, \frac{100 - 90}{2}\), or \(\frac{R(2) - R(0)}{2 - 0} = 5\) is sufficient to earn P1.

\(\frac{R(2) - R(0)}{2 - 0}\) by itself is not sufficient to earn P1.

- P2 is earned for correct units, whether or not they are attached to a numerical value for the average rate of change.

- P2 is also earned for the units “words/minute\( ^{2} \).”

© 2025 College Board

<!-- Page 12 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

|  **B** | Must there be a value $c$, for $0 < c < 10$, such that $R(c) = 155$? Justify your answer.  |   |   |
| --- | --- | --- | --- |
|   | $R$ is differentiable implies $R$ is continuous. | Differentiable implies continuous | **Point 3 (P3)**  |
|   | $R(0) = 90 < 155 < R(10) = 162$ | Answer with justification | **Point 4 (P4)**  |
|   | Therefore, by the Intermediate Value Theorem, there must be a value $c$, with $0 < c < 10$, such that $R(c) = 155$.  |   |   |
|  **Scoring Notes for Part B**  |   |   |   |
|  - To earn **P3**, a response must state that $R$ is continuous because $R$ is differentiable (or equivalent). A response that simply states “$R$ is continuous” without justification does not earn **P3**. - A response does not need to earn **P3** to be eligible for **P4**. - To earn **P4**, a response must indicate that $R(0) < 155$ (or $R(2) < 155$ or $R(8) < 155$) and $R(10) > 155$, state that “$R$ is continuous,” and answer “yes” in some way. - To earn **P4**, a response need not explicitly name the Intermediate Value Theorem, but if a theorem is named, it must be correct.  |   |   |   |

© 2025 College Board

<!-- Page 13 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

C

Use a trapezoidal sum with the three subintervals indicated by the data in the table to approximate the value of $$\int_{0}^{10} R(t) \, dt$$. Show the work that leads to your answer.

$$\int_{0}^{10} R(t) \, dt$$

$$\approx \frac{R(0) + R(2)}{2}(2 - 0) + \frac{R(2) + R(8)}{2}(8 - 2) + \frac{R(8) + R(10)}{2}(10 - 8)$$

$$= \frac{90 + 100}{2}(2 - 0) + \frac{100 + 150}{2}(8 - 2) + \frac{150 + 162}{2}(10 - 8)$$

$$= \frac{190}{2}(2) + \frac{250}{2}(6) + \frac{312}{2}(2) = 190 + 750 + 312 = 1252$$

Form of trapezoidal sum

Point 5 (P5)

Answer with supporting work

Point 6 (P6)

### Scoring Notes for Part C

- Read “=” as “≈” for P5.

- The form of a trapezoidal sum includes three terms, each of which includes a product of two factors, where one of the factors incorporates the $$\frac{1}{2}$$ as part of the product. To earn P5, at least five of the six factors must be correct. If any of the six factors is incorrect, the response does not earn P6. Consider the following examples:

- $$\frac{90 + 100}{2}(2 - 0) + \frac{100 + 150}{2}(8 - 2) + \frac{150 + 162}{2}(10 - 8)$$ earns P5 and is sufficient to earn P6.
- $$\frac{190}{2}(2) + \frac{250}{2}(6) + \frac{312}{2}(2)$$ earns P5 and is sufficient to earn P6.
- $$\frac{1}{2}((R(0) + R(2))(2) + (R(2) + R(8))(6) + (R(8) + R(10))(2))$$ earns P5 and is eligible for P6.
- $$\frac{90 + 100}{2}(2) + \frac{100 + 150}{2}(2) + \frac{150 + 162}{2}(2)$$ earns P5 but is not eligible for P6.

(Note that the factor of 2 in the second term of this expression is incorrect.)

- Special case: A response of $$(90 + 100) + (100 + 150)3 + (150 + 162)$$ earns both P5 and P6.
- To be eligible for P6, a response must have earned P5.

Special case: A response of $$95 \cdot 2 + 125 \cdot 6 + 156 \cdot 2$$ earns P6 but does not earn P5.

- A response of $$\frac{90 + 100}{2}(2 - 0) + \frac{100 + 150}{2}(8 - 2) + \frac{150 + 162}{2}(10 - 8)$$ or equivalent banks P6 (i.e., subsequent errors in simplification will not be considered in scoring for P6).
- A response of $$\frac{(90 \cdot 2 + 100 \cdot 6 + 150 \cdot 2) + (100 \cdot 2 + 150 \cdot 6 + 162 \cdot 2)}{2}$$ or equivalent earns both P5 and P6. (Note that the average of the left Riemann sum and right Riemann sum is equivalent to the trapezoidal sum.)
- A completely correct left Riemann sum (e.g., $$90 \cdot 2 + 100 \cdot 6 + 150 \cdot 2 = 1080$$) or a completely correct right Riemann sum (e.g., $$100 \cdot 2 + 150 \cdot 6 + 162 \cdot 2 = 1424$$) earns P5 but does not earn P6.

© 2025 College Board

<!-- Page 14 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

D

A teacher also starts reading at time t = 0 minutes and continues reading for the next 10 minutes. The rate at which the teacher reads is modeled by the function W defined by  \( W(t) = -\frac{3}{10}t^{2} + 8t + 100 \) , where  \( W(t) \)  is measured in words per minute. Based on the model, how many words has the teacher read by the end of the 10 minutes? Show the work that leads to your answer.

\[
\int_ {0} ^ {1 0} W (t) d t = \int_ {0} ^ {1 0} \left(- \frac {3}{1 0} t ^ {2} + 8 t + 1 0 0\right) d t
\]

\[
= \left(- \frac {1}{1 0} t ^ {3} + 4 t ^ {2} + 1 0 0 t\right) \bigg | _ {0} ^ {1 0}
\]

\[
\begin{array}{l} = \left(- \frac {1}{1 0} \cdot 1 0 0 0 + 4 \cdot 1 0 0 + 1 0 0 \cdot 1 0\right) - \left(- \frac {1}{1 0} \cdot 0 + 4 \cdot 0 + 1 0 0 \cdot 0\right) \\ = 1 3 0 0 \end{array}
\]

Based on the model, the teacher has read 1300 words by the end of the 10 minutes.

Integrand

Point 7 (P7)

Antiderivative

Point 8 (P8)

Answer

Point 9 (P9)

### Scoring Notes for Part D

- P7 is earned for an indefinite or definite integral with integrand \( W(t) \), with or without the differential \( dt \).
- P8 is earned for the correct antiderivative, with or without the constant of integration.
• To be eligible for P9, a response must have earned P8.
- A response of \(\left(-\frac{1}{10} \cdot 1000 + 4 \cdot 100 + 100 \cdot 10\right) - \left(-\frac{1}{10} \cdot 0 + 4 \cdot 0 + 100 \cdot 0\right)\) or equivalent banks P9 (i.e., subsequent errors in simplification will not be considered in scoring for P9).

© 2025 College Board

<!-- Page 15 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

## Part A (AB or BC): Graphing calculator not allowed

### Question 4

9 points

#### General Scoring Notes

- The model solution is presented using standard mathematical notation.
- Answers (numeric or algebraic) need not be simplified. Answers given as a decimal approximation should be accurate to three places after the decimal point. Within each individual free-response question, at most one point is not earned for inappropriate rounding.

The continuous function \( f \) is defined on the closed interval \( -6 \leq x \leq 12 \). The graph of \( f \), consisting of two semicircles and one line segment, is shown in the figure.

![img-2.jpeg](ap25-sg-calculus-bc_assets/page-15-img-2.jpeg)

Let \( g \) be the function defined by \( g(x) = \int_{6}^{x} f(t) dt \).

© 2025 College Board

<!-- Page 16 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

|   | Model Solution | Scoring  |
| --- | --- | --- |
|  A | Find $g'(8)$. Give a reason for your answer.  |   |
|   | $g'(x) = f(x)$ | Considers $g'(x) = f(x)$ **Point 1 (P1)**  |
|   | $g'(8) = f(8) = 1$ | Answer **Point 2 (P2)**  |
|  **Scoring Notes for Part A**  |   |   |
|  - **P1** is earned for $g' = f$, $g'(x) = f(x)$, or $g'(8) = f(8)$ in part A. - A response of $g'(8) = f(8) = 1$ earns both **P1** and **P2**. - A response that does not earn **P1** can earn **P2** with an implied application of the Fundamental Theorem of Calculus (e.g., $g'(8) = 1$ or $f(8) = 1$). - A response of $g'(8) = f(8) - f(6) = 1$ earns **P2** but not **P1**.  |   |   |

© 2025 College Board

<!-- Page 17 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

B

Find all values of x in the open interval -6 < x < 12 at which the graph of g has a point of inflection. Give a reason for your answer.

The graph of g has a point of inflection where g'' = f' changes sign, which is where g' = f changes from decreasing to increasing or vice versa.

The graph of g has points of inflection at x = -3 and x = 6 because f changes from decreasing to increasing there.

The graph of g also has a point of inflection at x = 3 because f changes from increasing to decreasing there.

Answer

Point 3 (P3)

Reason

Point 4 (P4)

# Scoring Notes for Part B

- P3 is earned only for an answer of x = -3, x = 3, and x = 6. If any other/additional values of x in -6 < x < 12 are declared to be points of inflection, the response does not earn either P3 or P4. Consideration of x = -6 or of x = 12 does not impact scoring.

- To earn P4, a response must tie the reason to the given graph of f.

- A response of “g has a point of inflection at x = -3, x = 3, and x = 6 because f changes from increasing to decreasing or decreasing to increasing there” earns both P3 and P4.
- A response of “g has a point of inflection at x = -3, x = 3, and x = 6 because the slope of f changes sign there” earns both P3 and P4.
- A response of “g has a point of inflection at x = -3, x = 3, and x = 6 because f attains relative extrema there” earns both P3 and P4.
- A response of “g has a point of inflection at x = -3, x = 3, and x = 6 because g changes concavity there” earns P3 but not P4.
- A response of “g has a point of inflection at x = -3, x = 3, and x = 6 because g'' = f' changes sign there” earns P3 but not P4.
- A response that relies upon an ambiguous term such as “the function” or “the graph” does not earn P4.

- Special case: A response with two of the three correct x-values with correct reasoning and no other/additional values of x declared to be points of inflection earns P4 but not P3.

© 2025 College Board

<!-- Page 18 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

C Find g(12) and g(0). Label your answers.

$$g(12) = \int_{6}^{12} f(t) \, dt = \frac{1}{2} \cdot 6 \cdot 3 = 9$$

g(12)

Point 5 (P5)

$$g(0) = \int_{6}^{0} f(x) \, dx = -\int_{0}^{6} f(x) \, dx = -\frac{\pi}{2} 3^2 = -\frac{9\pi}{2}$$

g(0)

Point 6 (P6)

### Scoring Notes for Part C

- Unlabeled values do not earn either P5 or P6.
- P5 is earned for a response of g(12) = 9, with or without supporting work.
- P6 is earned for a response of g(0) = -9π/2, with or without supporting work.

Note: Incorrect communication between the label “g(0)” and the answer will be treated as scratch work and will not impact scoring. For example, g(0) = ∫₀⁶ f(x) dx = -9π/2 earns P6.

© 2025 College Board

<!-- Page 19 -->

AP® Calculus AB/BC 2025 Scoring Guidelines

D

Find the value of x at which g attains an absolute minimum on the closed interval -6 ≤ x ≤ 12. Justify your answer.

For -6 ≤ x ≤ 12, g attains a minimum either when g'(x) = f(x) = 0 or at an endpoint.

g'(x) = f(x) = 0

⇒ x = 0, x = 6

|  x | g(x)  |
| --- | --- |
|  -6 | 0  |
|  0 | -9π/2  |
|  6 | 0  |
|  12 | 9  |

Considers g'(x) = 0 Point 7 (P7)

Justification Point 8 (P8)

Therefore, on the closed interval -6 ≤ x ≤ 12, g attains an absolute minimum value at x = 0.

Answer Point 9 (P9)

### Scoring Notes for Part D

- P7 is earned for considering g'(x) = 0 or f(x) = 0. P7 is not earned by just presenting x = 0 and x = 6.

A response that discusses the sign of g'(x) or f(x) changing OR uses the phrase “critical points of g” also earns P7.

- To earn P8 using a candidates test, a response must make a global argument by providing evaluations or reasoning for each of g(-6), g(0), g(6), and g(12) (and no other x-values).

- Alternate justification and answer:

Because g'(x) ≤ 0 (or f(x) ≤ 0) for -6 ≤ x < 0 and g'(x) ≥ 0 (or f(x) ≥ 0) for 0 < x ≤ 12, the absolute minimum of g occurs at x = 0.

- A response that presents a local argument (such as a First Derivative Test or a Second Derivative Test) or an incorrect global argument does not earn P8 but is eligible for P9 with the correct answer of x = 0.

- For P8, values of g(0) and g(12) can be imported from part C. A response can earn P9 with an answer that is consistent with the imported values.

© 2025 College Board

<!-- Page 20 -->

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

<!-- Page 21 -->

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

<!-- Page 22 -->

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

<!-- Page 23 -->

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

<!-- Page 24 -->

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

<!-- Page 25 -->

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

<!-- Page 26 -->

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

<!-- Page 27 -->

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
