import random


def estimate_pi(n):
    # counter: how many points land inside the quarter circle
    count = 0

    # throw n points, one per loop turn
    for _ in range(n):
        # a random point in the square: x and y between 0 and 1
        x = random.random()
        y = random.random()

        # the point is inside the quarter circle if its distance from (0, 0) is at most 1
        if x * x + y * y <= 1:
            count += 1

    # the quarter circle is pi/4 of the square, so we multiply the share by 4
    return 4 * count / n


def estimate_area(n, k):
    # counter: how many points land under the curve y = x**k
    count = 0

    for _ in range(n):
        x = random.random()
        y = random.random()

        # the curve has height x**k at this spot: if y is lower, the point is under it
        if y <= x ** k:
            count += 1

    # the square has area 1, so the share of points under the curve is the area
    return count / n


# Task 2: table of pi estimates for bigger and bigger n
# (:>8 and :>10 only align the columns)
print(f"{'n':>8} {'estimate':>10} {'error':>10}")
for n in [10, 100, 1000, 10000, 100000]:
    est = estimate_pi(n)
    # error = the gap between our estimate and the real value of pi
    print(f"{n:>8} {est:>10.5f} {abs(est - 3.14159):>10.5f}")

# Task 3: compare the estimated area with the exact value 1 / (k + 1)
print()
for k in [2, 3, 4]:
    est = estimate_area(100000, k)
    print(f"k={k}: estimate {est:.4f}, exact {1 / (k + 1):.4f}")

# Try your code
print()
print(f"{estimate_pi(100000):.2f}") # expected: about 3.14
print(f"{estimate_area(100000, 2):.3f}") # expected: about 0.333
print(f"{estimate_area(100000, 1):.1f}") # expected: about 0.5
print(f"{estimate_area(1000, 0):.1f}") # expected: 1.0


# Extra: from which n is the error almost always below 0.005?
print()
for n in [100, 1000, 10000, 100000, 1000000]:
    # number of successful runs for this n
    successful = 0
    # repeat the estimate 20 times to see if it works every time
    for _ in range(20):
        if abs(estimate_pi(n) - 3.14159) < 0.005:
            successful += 1
    print(f"n={n}: {successful}/20 runs with error < 0.005")