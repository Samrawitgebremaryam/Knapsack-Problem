
# 📦 0-1 Knapsack Problem: Brute Force vs Dynamic Programming

## 🧠 Overview

This project compares three algorithmic approaches to solving the classic **0-1 Knapsack Problem**:

1. 🪓 **Brute Force** (Recursive, exponential time)
2. 📚 **Top-Down Dynamic Programming** (Memoization)
3. 📊 **Bottom-Up Dynamic Programming** (Tabulation)

It measures and visualizes their runtime performance as the number of items increases.

---

## 💼 Problem Statement

You are given `n` items where each item has a **weight** and a **profit**. You are also given a bag with a weight capacity `W`.

**Goal:** Select a subset of the items to include in the bag such that:
- The total weight does **not exceed `W`**
- The total profit is **maximized**
- Items **cannot be broken** — either take the whole item or leave it

### ✅ Example 1:
```python
W = 4
profit = [1, 2, 3]
weight = [4, 5, 1]
```
**Output:** `3`

➡️ Best choice is item 3 (weight = 1, profit = 3)

### ✅ Example 2:
```python
W = 3
profit = [1, 2, 3]
weight = [4, 5, 6]
```
**Output:** `0`

➡️ No items can fit into the bag.

---

## 🧪 Algorithms Compared

| Method             | Time Complexity | Space Complexity | Notes |
|--------------------|-----------------|------------------|-------|
| Brute Force        | O(2ⁿ)           | O(n)             | Very slow for large `n` |
| Top-Down DP        | O(n×W)          | O(n×W)           | Efficient with recursion |
| Bottom-Up DP       | O(n×W)          | O(n×W)           | Efficient and iterative |

---

## 🛠️ How It Works

- Random weights and profits are generated for up to 15 items.
- Each of the three methods is tested on increasing values of `n`.
- Execution time is measured and compared using `matplotlib`.

---

## 📈 Visualization

A line graph is plotted:

- **X-axis:** Number of items
- **Y-axis:** Time taken (seconds)

This demonstrates how each algorithm scales with input size.

---

## 📂 Files

- `knapsack_comparison.py`: Main Python script
- `README.md`: This documentation

---

## ▶️ How to Run

1. **Install dependencies**:
   ```bash
   pip install matplotlib
   ```

2. **Run the script**:
   ```bash
   python Knapsack.py
   ```

3. **See the graph**: Matplotlib will display a runtime comparison chart.

