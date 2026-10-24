# Project 3: Estimating $\pi$ and Curve Areas with Random Points

## 1. Introduction and Theoretical Background
This project focuses on estimating ($\pi$) and calculating the area under the curve ($y = x^k$) for x from 0 to 1. In this project, random points are generated and tested to estimate values that can also be calculated mathematically. For example, random points are selected from a unit square, and their locations are checked to determine whether they fall inside a quarter circle or below a given curve. The project also investigates how changing random points affects the accuracy and reliability of the estimates.

The project is implemented in Python using the built-in random module.

### 1.1 Objectives
The main objectives of this project are:
1. To estimate ($\pi$) using random points.
2. To estimate the area under the curve ($y = x^k$).
3. To compare the estimates with exact mathematical values.
4. To calculate the absolute error.
5. To investigate how the number of random points affects accuracy.

### 1.2 Estimating ($\pi$)
We can analyze the first quadrant: a quarter circle of radius 1 is placed inside a unit square. The square has area 1, while the quarter circle has area ($\frac{pi}{4}$).

Random points (x, y) are generated inside the square. A point is inside the quarter circle when:
$x^2 + y^2 <= 1$

The quarter circle has area ($\frac{pi}{4}$). The square has area 1.

### 1.3 Estimating Area Under $y = x^k$
For ($y = x^k$), random points are generated in the unit square. A point is considered "under the curve" if $y <= x^k$.

---

## 2. Example Run Results

### Task 2: $\pi$ Estimation Table (Standard Outputs)

Our 3 runs (estimate / error):

**Run 1**

| n | estimate | error |
| ---: | ---: | ---: |
| 10 | 3.20000 | 0.05841 |
| 100 | 3.12000 | 0.02159 |
| 1000 | 3.16400 | 0.02241 |
| 10000 | 3.15680 | 0.01521 |
| 100000 | 3.13968 | 0.00191 |


**Run 2**

| n | estimate | error |
| ---: | ---: | ---: |
| 10 | 3.44000 | 0.29841 |
| 100 | 3.44000 | 0.29841 |
| 1000 | 3.20800 | 0.06641 |
| 10000 | 3.16040 | 0.01881 |
| 100000 | 3.14788 | 0.00629 |


**Run 3**

| n | estimate | error |
| ---: | ---: | ---: |
| 10 | 2.80000 | 0.34159 |
| 100 | 2.68000 | 0.46159 |
| 1000 | 3.02800 | 0.11359 |
| 10000 | 3.10640 | 0.03519 |
| 100000 | 3.14000 | 0.00159 |


### Task 3: Area Under $y = x^k$ (n = 100,000)

| Curve | Estimate | Analytical Exact Value |
| :--- | :---: | :---: |
| y = x^2 | 0.33430 | 0.33333 |
| y = x^3 | 0.25200 | 0.25000 |
| y = x^4 | 0.20000 | 0.20000 |

---

## 3. Think and Explain

### Q: What happens when n gets bigger? 
The estimates were generally close to the expected values, although differences occurred because the points were generated randomly. Increasing the sample size generally improved accuracy with the typical error decreasing approximately as; 
       $\frac{1}{\sqrt(n)}$.
 **Is a bigger n always better?**
  Yes.Because the estimates usually become more reliable, so using bigger($n$) is generally better when greater accuracy is needed. However, the improvement becomes smaller as n increases, and bigger samples require more computation time and memory. A larger sample size reduces variance and bounds the standard error, making the estimates progressively more reliable.
  * **In individual instances**: Bigger n does not guarantee a smaller error in every individual run because the results are random.

## 4. Challenges

For the estimation of the minimum n such that  an error is smaller than 0.005, we  tested  different values of n from 100 to 1000000. With each value of n, we estimated the value of pi and computed the error. By counting the number of trials so that the error is less than 0.005, we identified the value of 1000000. For this value, the error is less than 0.005 for all 20 attempts. The choice of 20 trials is an arbitrary value and can be equal to 30, 50 or more. This logic is the same for the n values which are arbitrary chosen for the need of the task. 
