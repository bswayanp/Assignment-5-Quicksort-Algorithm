
---

## ⚙️ Implementation Details

### 1️⃣ Deterministic Quicksort
- Uses the last element as pivot.
- Performs in-place partitioning.
- Efficient for random input.
- Can degrade to **O(n²)** for sorted/reverse inputs.

### 2️⃣ Randomized Quicksort
- Selects pivot randomly.
- Reduces likelihood of worst-case performance.
- Expected runtime: **O(n log n)**.
- More robust across input distributions.

---

## 🧠 Algorithm Analysis

### Time Complexity

| Case        | Deterministic | Randomized |
|------------|--------------|------------|
| Best Case  | O(n log n)   | O(n log n) |
| Average    | O(n log n)   | O(n log n) |
| Worst Case | O(n²)        | O(n²) (rare) |

### Space Complexity

- Average: O(log n) (recursion stack)
- Worst: O(n) (unbalanced recursion)

Quicksort is an **in-place sorting algorithm**, requiring no additional arrays.

---

## 📊 Empirical Testing

The program compares performance across:

### Input Sizes
- 1,000
- 5,000
- 10,000

### Input Distributions
- Random
- Sorted
- Reverse-sorted

### Observed Results

- Deterministic Quicksort slows significantly for sorted/reverse data.
- Randomized Quicksort performs consistently across all distributions.
- Experimental results confirm theoretical time complexity analysis.

---

## 🚀 How to Run the Program

### Requirements

- Python 3.x

### Execution

```bash
python quicksort_analysis.py
