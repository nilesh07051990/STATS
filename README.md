# Statistics Notes for Data Science Course - Day 1

## Table of Contents
1. [Introduction to Statistics](#introduction-to-statistics)
2. [Descriptive Statistics](#descriptive-statistics)
3. [Probability Fundamentals](#probability-fundamentals)
4. [Common Probability Distributions](#common-probability-distributions)
5. [Data Visualization](#data-visualization)
6. [Practical Examples](#practical-examples)
7. [Key Takeaways](#key-takeaways)

---

## Introduction to Statistics

### What is Statistics?
Statistics is the science of collecting, analyzing, interpreting, and presenting data. In data science, statistics provides the foundation for:
- Understanding data patterns
- Making informed decisions
- Drawing valid conclusions
- Predicting future outcomes

### Types of Statistics
1. **Descriptive Statistics**: Summarize and describe data
2. **Inferential Statistics**: Make predictions and draw conclusions about populations from samples

---

## Descriptive Statistics

### Measures of Central Tendency

#### Mean (Average)
- **Formula**: μ = Σx / n
- **Use**: Best for normally distributed data
- **Sensitive to**: Outliers

#### Median
- **Definition**: Middle value when data is ordered
- **Use**: Best for skewed distributions
- **Robust to**: Outliers

#### Mode
- **Definition**: Most frequently occurring value
- **Use**: Categorical data, identifying peaks

### Measures of Variability

#### Range
- **Formula**: Range = Maximum - Minimum
- **Limitation**: Sensitive to outliers

#### Variance
- **Population Variance**: σ² = Σ(x - μ)² / N
- **Sample Variance**: s² = Σ(x - x̄)² / (n-1)
- **Units**: Squared units of original data

#### Standard Deviation
- **Formula**: σ = √σ² (population) or s = √s² (sample)
- **Units**: Same as original data
- **Interpretation**: Average distance from mean

#### Interquartile Range (IQR)
- **Formula**: IQR = Q3 - Q1
- **Use**: Robust measure of spread
- **Outlier Detection**: Values beyond 1.5 × IQR from Q1 or Q3

### Five-Number Summary
1. Minimum
2. Q1 (25th percentile)
3. Median (50th percentile)
4. Q3 (75th percentile)
5. Maximum

---

## Probability Fundamentals

### Basic Concepts

#### Sample Space (S)
- **Definition**: Set of all possible outcomes
- **Example**: Rolling a die → S = {1, 2, 3, 4, 5, 6}

#### Event
- **Definition**: Subset of sample space
- **Example**: Getting an even number → E = {2, 4, 6}

#### Probability Rules
1. **0 ≤ P(A) ≤ 1**
2. **P(S) = 1**
3. **P(A ∪ B) = P(A) + P(B) - P(A ∩ B)** (Addition Rule)

### Conditional Probability
- **Formula**: P(A|B) = P(A ∩ B) / P(B)
- **Interpretation**: Probability of A given B has occurred

### Independence
- **Definition**: Events A and B are independent if P(A ∩ B) = P(A) × P(B)
- **Alternative**: P(A|B) = P(A)

### Bayes' Theorem
- **Formula**: P(A|B) = P(B|A) × P(A) / P(B)
- **Use**: Updating probabilities with new information

---

## Common Probability Distributions

### Discrete Distributions

#### Binomial Distribution
- **Parameters**: n (trials), p (success probability)
- **Use**: Counting successes in n independent trials
- **Mean**: μ = np
- **Variance**: σ² = np(1-p)

#### Poisson Distribution
- **Parameter**: λ (rate)
- **Use**: Counting events in fixed time/space
- **Mean**: μ = λ
- **Variance**: σ² = λ

### Continuous Distributions

#### Normal Distribution
- **Parameters**: μ (mean), σ (standard deviation)
- **Properties**:
  - Bell-shaped curve
  - Symmetric about mean
  - 68-95-99.7 rule
- **Standard Normal**: μ = 0, σ = 1

#### Standardization
- **Z-score**: z = (x - μ) / σ
- **Use**: Comparing values from different distributions

---

## Data Visualization

### Essential Plots

#### Histogram
- **Use**: Distribution of continuous data
- **Key Elements**: Bins, frequency, shape

#### Box Plot
- **Use**: Five-number summary, outlier detection
- **Components**: Box (Q1-Q3), whiskers, outliers

#### Scatter Plot
- **Use**: Relationship between two variables
- **Patterns**: Linear, non-linear, no relationship

#### Bar Chart
- **Use**: Categorical data comparison
- **Types**: Vertical, horizontal, grouped, stacked

### Best Practices
1. **Choose appropriate plot type**
2. **Label axes clearly**
3. **Use consistent scales**
4. **Avoid misleading visualizations**
5. **Consider your audience**

---

## Practical Examples

### Example 1: Student Grades Analysis
```python
import numpy as np
import matplotlib.pyplot as plt

# Sample data
grades = [85, 92, 78, 96, 88, 91, 83, 89, 94, 87]

# Descriptive statistics
mean_grade = np.mean(grades)
median_grade = np.median(grades)
std_grade = np.std(grades, ddof=1)

print(f"Mean: {mean_grade:.2f}")
print(f"Median: {median_grade:.2f}")
print(f"Standard Deviation: {std_grade:.2f}")
```

### Example 2: Probability Calculation
```python
# Probability of rolling a 6 on a fair die
P_six = 1/6
print(f"Probability of rolling a 6: {P_six:.3f}")

# Probability of rolling an even number
P_even = 3/6  # {2, 4, 6}
print(f"Probability of rolling even: {P_even:.3f}")
```

### Example 3: Normal Distribution
```python
from scipy import stats

# Standard normal distribution
z_score = 1.5
probability = stats.norm.cdf(z_score)
print(f"P(Z ≤ 1.5) = {probability:.3f}")

# Finding percentile
percentile_95 = stats.norm.ppf(0.95)
print(f"95th percentile: {percentile_95:.3f}")
```

---

## Key Takeaways

### Day 1 Learning Objectives
1. **Understand the role of statistics in data science**
2. **Calculate and interpret descriptive statistics**
3. **Apply basic probability concepts**
4. **Recognize common probability distributions**
5. **Create effective data visualizations**

### Next Steps
- Practice with real datasets
- Explore more advanced statistical concepts
- Learn statistical testing and hypothesis testing
- Understand correlation and regression analysis

### Resources for Further Learning
- **Books**: "Statistics for Data Scientists" by Bruce & Bruce
- **Online**: Khan Academy Statistics, Coursera Data Science courses
- **Practice**: Kaggle datasets, R/Python tutorials

### Common Pitfalls to Avoid
1. **Confusing correlation with causation**
2. **Ignoring outliers without investigation**
3. **Using inappropriate visualizations**
4. **Misinterpreting p-values**
5. **Overfitting to sample data**

---

## Quick Reference

### Statistical Formulas
- **Mean**: μ = Σx / n
- **Variance**: σ² = Σ(x - μ)² / n
- **Standard Deviation**: σ = √σ²
- **Z-score**: z = (x - μ) / σ
- **Correlation**: r = Σ[(x-x̄)(y-ȳ)] / √[Σ(x-x̄)²Σ(y-ȳ)²]

### Python Libraries
- **NumPy**: Numerical computations
- **Pandas**: Data manipulation
- **Matplotlib/Seaborn**: Visualization
- **SciPy**: Statistical functions
- **Scikit-learn**: Machine learning

---

*This document serves as a foundation for your data science journey. Practice these concepts regularly and apply them to real-world problems!*
