import time
import matplotlib.pyplot as plt
import random

# Recursive (Brute Force) Approach
def knapsackRec(W, val, wt, n):
    if n == 0 or W == 0:
        return 0
    pick = 0
    if wt[n - 1] <= W:
        pick = val[n - 1] + knapsackRec(W - wt[n - 1], val, wt, n - 1)
    notPick = knapsackRec(W, val, wt, n - 1)
    return max(pick, notPick)

def knapsack_brute_force(W, val, wt):
    n = len(val)
    return knapsackRec(W, val, wt, n)

# Dynamic Programming (Top-Down with Memoization)
def knapsackRec_memo(W, val, wt, n, memo):
    if n == 0 or W == 0:
        return 0
    if memo[n][W] != -1:
        return memo[n][W]
    pick = 0
    if wt[n - 1] <= W:
        pick = val[n - 1] + knapsackRec_memo(W - wt[n - 1], val, wt, n - 1, memo)
    notPick = knapsackRec_memo(W, val, wt, n - 1, memo)
    memo[n][W] = max(pick, notPick)
    return memo[n][W]

def knapsack_top_down(W, val, wt):
    n = len(val)
    memo = [[-1] * (W + 1) for _ in range(n + 1)]
    return knapsackRec_memo(W, val, wt, n, memo)

# Dynamic Programming (Bottom-Up with Space Optimization)
def knapsack_bottom_up(W, val, wt):
    n = len(wt)
    dp = [0] * (W + 1)  # 1D array
    for i in range(n):
        # Iterate in reverse to avoid overwriting needed values
        for j in range(W, wt[i] - 1, -1):
            dp[j] = max(dp[j], val[i] + dp[j - wt[i]])
    return dp[W]

# Main Program
if __name__ == "__main__":
    random.seed(42)  # For reproducibility
    W = 500  # Increased knapsack capacity
    max_n = 50  # Increased to observe scaling
    wt = [random.randint(1, 250) for _ in range(max_n)]  
    val = [random.randint(1, 500) for _ in range(max_n)]  

    ns = list(range(10, max_n + 1, 10))  # [10, 20, 30, 40, 50]
    num_trials = 5  # Number of trials to average out noise
    brute_times = []
    top_down_times = []
    bottom_up_times = []

    for n in ns:
        wt_n = wt[:n]
        val_n = val[:n]
        
        # Brute force timing (skip for large n to save time)
        brute_total = 0
        if n <= 20:  # Limit brute force to smaller n
            for _ in range(num_trials):
                start = time.perf_counter()
                knapsack_brute_force(W, val_n, wt_n)
                brute_total += time.perf_counter() - start
            brute_avg = brute_total / num_trials
        else:
            brute_avg = float('inf')  # Placeholder for large n
        brute_times.append(brute_avg)
        
        # Top-down timing
        top_down_total = 0
        for _ in range(num_trials):
            start = time.perf_counter()
            knapsack_top_down(W, val_n, wt_n)
            top_down_total += time.perf_counter() - start
        top_down_avg = top_down_total / num_trials
        top_down_times.append(top_down_avg)
        
        # Bottom-up timing
        bottom_up_total = 0
        for _ in range(num_trials):
            start = time.perf_counter()
            knapsack_bottom_up(W, val_n, wt_n)
            bottom_up_total += time.perf_counter() - start
        bottom_up_avg = bottom_up_total / num_trials
        bottom_up_times.append(bottom_up_avg)

        # Print times for this n
        print(f"\nNumber of items (n={n}):")
        print(f"  Brute Force: {brute_avg:.6f} seconds" if n <= 20 else "  Brute Force: Skipped (too slow)")
        print(f"  Top-Down DP: {top_down_avg:.6f} seconds")
        print(f"  Bottom-Up DP: {bottom_up_avg:.6f} seconds")

    # Plotting the results
    plt.plot(ns, top_down_times, label='DP Top-Down', marker='s')
    plt.plot(ns, bottom_up_times, label='DP Bottom-Up', marker='^')
    if any(t != float('inf') for t in brute_times):
        plt.plot([n for n, t in zip(ns, brute_times) if t != float('inf')], 
                 [t for t in brute_times if t != float('inf')], 
                 label='Brute Force', marker='o')
    plt.xlabel('Number of Items (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity Comparison for 0-1 Knapsack (W=500)')
    plt.legend()
    plt.grid(True)
    plt.show()