# 📦 Knapsack Problem: Brute Force vs Dynamic Programming

## 🧠 Overview

This project compares three algorithmic approaches to solving the **0-1 Knapsack Problem**:

1. 🪓 **Brute Force** (Recursive, exponential time)
2. 📚 **Top-Down Dynamic Programming** (Memoization)
3. 📊 **Bottom-Up Dynamic Programming** (Tabulation)

It measures and visualizes their runtime performance as the number of items increases.

---

## 💼 Problem Statement

Given a list of item weights and values, and a total weight capacity `W`, determine the maximum value that can be carried in the knapsack. Each item can either be included **once** or not at all.

---

## 🧪 Algorithms Used

| Method             | Time Complexity | Space Complexity | Notes |
|--------------------|-----------------|------------------|-------|
| Brute Force        | O(2ⁿ)           | O(n)             | Slow but easy to implement |
| Top-Down DP        | O(n×W)          | O(n×W)           | Recursive with memoization |
| Bottom-Up DP       | O(n×W)          | O(n×W)           | Iterative, avoids recursion |

---

## 🛠️ How It Works

- Generates **random weights and values** for up to 15 items.
- Tests each algorithm for increasing values of `n` (number of items).
- Measures execution time for each method using `time.perf_counter()`.
- Plots a line graph comparing runtimes using `matplotlib`.

---

## 📈 Visualization

The resulting graph shows how each algorithm scales as the number of items increases.

- **Brute Force** grows quickly (exponential).
- **Top-Down DP** and **Bottom-Up DP** perform much faster and scale efficiently.

---

## 📂 Files

- `knapsack_comparison.py`: Main Python script
- `README.md`: This documentation

---

## ▶️ How to Run

1. **Install dependencies**:
   ```bash
   pip install matplotlib
