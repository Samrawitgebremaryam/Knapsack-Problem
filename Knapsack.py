import time
import matplotlib.pyplot as plt
import random

# Brute Force Approach (Recursive)
def brute_force_knapsack(W, wt, val, n):
    def recurse(i, w):
        if i == n or w == 0:
            return 0
        if wt[i] > w:
            return recurse(i + 1, w)
        else:
            return max(val[i] + recurse(i + 1, w - wt[i]), recurse(i + 1, w))
    return recurse(0, W)

# Dynamic Programming (Top-Down with Memoization)
def dp_top_down_knapsack(W, wt, val, n):
    dp = [[-1] * (W + 1) for _ in range(n + 1)]
    def recurse(i, w):
        if w == 0 or i == n:
            return 0
        if dp[i][w] != -1:
            return dp[i][w]
        if wt[i] > w:
            dp[i][w] = recurse(i + 1, w)
        else:
            dp[i][w] = max(val[i] + recurse(i + 1, w - wt[i]), recurse(i + 1, w))
        return dp[i][w]
    return recurse(0, W)

# Dynamic Programming (Bottom-Up with Tabulation)
def dp_bottom_up_knapsack(W, wt, val, n):
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] > w:
                K[i][w] = K[i - 1][w]
            else:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
    return K[n][W]

# Main Program
if __name__ == "__main__":
    random.seed(42)  
    W = 100  # Knapsack capacity
    max_n = 15  # Maximum number of items
    wt = [random.randint(1, 50) for _ in range(max_n)]  
    val = [random.randint(1, 100) for _ in range(max_n)]  

    ns = list(range(5, 16, 2))  # [5, 7, 9, 11, 13, 15]
    brute_times = []
    top_down_times = []
    bottom_up_times = []

    for n in ns:
        wt_n = wt[:n]
        val_n = val[:n]
        
        start = time.perf_counter()
        brute_force_knapsack(W, wt_n, val_n, n)
        brute_times.append(time.perf_counter() - start)
        
        start = time.perf_counter()
        dp_top_down_knapsack(W, wt_n, val_n, n)
        top_down_times.append(time.perf_counter() - start)
        
        start = time.perf_counter()
        dp_bottom_up_knapsack(W, wt_n, val_n, n)
        bottom_up_times.append(time.perf_counter() - start)

    plt.plot(ns, brute_times, label='Brute Force', marker='o')
    plt.plot(ns, top_down_times, label='DP Top-Down', marker='s')
    plt.plot(ns, bottom_up_times, label='DP Bottom-Up', marker='^')
    plt.xlabel('Number of items (n)')
    plt.ylabel('Time (s)')
    plt.title('Time Complexity Comparison for 0-1 Knapsack')
    plt.legend()
    plt.grid(True)
    plt.show()