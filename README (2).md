# NumPy Student Marks

A beginner-friendly Python project that stores student marks in a **NumPy array** and calculates the **mean, median, maximum, minimum, and standard deviation**.

## Objective

Learn how NumPy can efficiently perform numerical analysis.

## Tools Used

- Python 3
- NumPy
- Jupyter Notebook
- Streamlit (for the live demo)

## Dataset

Manually created marks of 10 students:

| Student | Marks |
|---------|-------|
| Asha | 78 |
| Ravi | 85 |
| Meena | 62 |
| Kiran | 90 |
| Swetha | 71 |
| Harsh | 89 |
| Rupesh | 70 |
| Akhil | 65 |
| Divya | 92 |
| Teja | 55 |

## Approach

1. **Create a NumPy array** from the marks with `np.array()`.
2. **Mean** with `np.mean(marks)`.
3. **Median** with `np.median(marks)`.
4. **Maximum and minimum** with `np.max(marks)` and `np.min(marks)`.
5. **Standard deviation** with `np.std(marks)`.
6. **Display each result clearly** using formatted strings.
7. **Bonus:** find the topper and lowest scorer with `np.argmax()` and `np.argmin()`, filter marks above the mean with a boolean mask, and compare population and sample standard deviation.

## Explanation of Results

- **Mean (75.70)** is the average mark of the class.
- **Median (74.50)** is the middle mark after sorting. It is not affected much by very high or very low marks.
- **Maximum (92) and Minimum (55)** are the highest and lowest marks.
- **Standard deviation (12.35)** shows how far the marks are spread from the mean. A small value means the marks are close to the average, and a large value means they are widely spread.
- The mean and the median are close, so the marks are fairly balanced without extreme outliers.

## What is Standard Deviation?

Standard deviation measures how spread out values are around the mean. It is the square root of the variance, which is the average of the squared differences from the mean. `np.std()` uses the population formula by default (divides by n). Use `np.std(marks, ddof=1)` for the sample formula (divides by n - 1).

## Why NumPy?

- NumPy arrays are **faster and use less memory** than Python lists for numerical work.
- Operations apply to the **whole array at once** (vectorization), so no loops are needed.
- NumPy is the foundation of Pandas, scikit-learn, TensorFlow and PyTorch, so it is essential for machine learning.

## How to Run

1. Install Python, NumPy and Jupyter Notebook:
   ```
   pip install notebook numpy
   ```
2. Clone or download this repository.
3. Open a terminal in the project folder and run:
   ```
   python -m notebook
   ```
4. Open `numpy_student_marks.ipynb`.
5. Run all cells from top to bottom (`Shift + Enter`).

## Sample Output

```
Mean: 75.70
Median: 74.50
Maximum: 92
Minimum: 55
Standard deviation: 12.35
```

Extra analysis:

```
Topper: Divya - 92
Lowest: Teja - 55
Marks above mean: [78 85 90 89 92]
Students above mean: ['Asha', 'Ravi', 'Kiran', 'Harsh', 'Divya']
Population std (ddof=0): 12.35
Sample std (ddof=1): 13.01
```

## Limitations

- Marks are typed in manually.
- If two students share the highest or lowest mark, `np.argmax()` and `np.argmin()` return only the first one.

## Possible Improvements

- Read marks from a CSV file with `np.loadtxt()` or Pandas.
- Add percentiles and variance.
- Plot a histogram of the marks with Matplotlib.

## Author

SwethaPulusu
