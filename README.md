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
- **Simple Example**: 
  - Data: [2, 4, 6, 8, 10]
  - Mean = (2+4+6+8+10)/5 = 30/5 = 6
  - **Real-world**: Average test score of 5 students

#### Median
- **Definition**: Middle value when data is ordered
- **Use**: Best for skewed distributions
- **Robust to**: Outliers
- **Simple Example**:
  - Data: [1, 3, 5, 7, 9] → Median = 5
  - Data: [1, 3, 5, 7, 9, 11] → Median = (5+7)/2 = 6
  - **Real-world**: Middle income in a neighborhood

#### Mode
- **Definition**: Most frequently occurring value
- **Use**: Categorical data, identifying peaks
- **Simple Example**:
  - Data: [1, 2, 2, 3, 4, 2, 5] → Mode = 2
  - **Real-world**: Most common shoe size sold

### Measures of Variability

#### Range
- **Formula**: Range = Maximum - Minimum
- **Limitation**: Sensitive to outliers
- **Simple Example**:
  - Data: [10, 15, 20, 25, 30]
  - Range = 30 - 10 = 20
  - **Real-world**: Temperature range in a day (10°C to 30°C)

#### Variance
- **Population Variance**: σ² = Σ(x - μ)² / N
- **Sample Variance**: s² = Σ(x - x̄)² / (n-1)
- **Units**: Squared units of original data
- **Simple Example**:
  - Data: [2, 4, 6, 8, 10], Mean = 6
  - Variance = [(2-6)² + (4-6)² + (6-6)² + (8-6)² + (10-6)²]/5
  - Variance = [16 + 4 + 0 + 4 + 16]/5 = 40/5 = 8
  - **Real-world**: How spread out are house prices in a neighborhood

#### Standard Deviation
- **Formula**: σ = √σ² (population) or s = √s² (sample)
- **Units**: Same as original data
- **Interpretation**: Average distance from mean
- **Simple Example**:
  - From above: σ = √8 ≈ 2.83
  - **Real-world**: Average deviation of test scores from the mean

#### Interquartile Range (IQR)
- **Formula**: IQR = Q3 - Q1
- **Use**: Robust measure of spread
- **Outlier Detection**: Values beyond 1.5 × IQR from Q1 or Q3
- **Simple Example**:
  - Data: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
  - Q1 = 5, Q3 = 15, IQR = 15 - 5 = 10
  - **Real-world**: Middle 50% of salaries in a company

### Five-Number Summary
1. Minimum
2. Q1 (25th percentile)
3. Median (50th percentile)
4. Q3 (75th percentile)
5. Maximum

**Simple Example**:
- Data: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
- Min = 1, Q1 = 5, Median = 10, Q3 = 15, Max = 19
- **Real-world**: Summary of student test scores (1-19 scale)

---

## Probability Fundamentals

### Basic Concepts

#### Sample Space (S)
- **Definition**: Set of all possible outcomes
- **Example**: Rolling a die → S = {1, 2, 3, 4, 5, 6}
- **Real-world**: All possible outcomes of flipping a coin → S = {Heads, Tails}

#### Event
- **Definition**: Subset of sample space
- **Example**: Getting an even number → E = {2, 4, 6}
- **Real-world**: Getting a grade of A or B → E = {A, B}

#### Probability Rules
1. **0 ≤ P(A) ≤ 1**
2. **P(S) = 1**
3. **P(A ∪ B) = P(A) + P(B) - P(A ∩ B)** (Addition Rule)

**Simple Examples**:
- **Rule 1**: P(rolling a 7 on a die) = 0 (impossible)
- **Rule 2**: P(rolling 1-6 on a die) = 1 (certain)
- **Rule 3**: P(rolling even OR divisible by 3) = P(even) + P(divisible by 3) - P(both)

### Conditional Probability
- **Formula**: P(A|B) = P(A ∩ B) / P(B)
- **Interpretation**: Probability of A given B has occurred
- **Simple Example**:
  - A = "Student passes exam", B = "Student studied"
  - P(A|B) = "Probability of passing given that they studied"
  - **Real-world**: P(rain|cloudy sky) = probability of rain given cloudy conditions

### Independence
- **Definition**: Events A and B are independent if P(A ∩ B) = P(A) × P(B)
- **Alternative**: P(A|B) = P(A)
- **Simple Example**:
  - Rolling two dice: First die = 6, Second die = 4
  - These are independent events
  - **Real-world**: Flipping a coin and rolling a die are independent

### Bayes' Theorem
- **Formula**: P(A|B) = P(B|A) × P(A) / P(B)
- **Use**: Updating probabilities with new information
- **Simple Example**:
  - A = "Person has disease", B = "Test is positive"
  - P(A|B) = P(B|A) × P(A) / P(B)
  - **Real-world**: Medical diagnosis - probability of having a disease given a positive test

---

## Common Probability Distributions

### Discrete Distributions

#### Binomial Distribution
- **Parameters**: n (trials), p (success probability)
- **Use**: Counting successes in n independent trials
- **Mean**: μ = np
- **Variance**: σ² = np(1-p)
- **Simple Example**:
  - n = 10 coin flips, p = 0.5 (fair coin)
  - P(exactly 7 heads) = C(10,7) × (0.5)⁷ × (0.5)³
  - **Real-world**: Number of successful sales calls out of 20 attempts

#### Poisson Distribution
- **Parameter**: λ (rate)
- **Use**: Counting events in fixed time/space
- **Mean**: μ = λ
- **Variance**: σ² = λ
- **Simple Example**:
  - λ = 3 customers per hour
  - P(exactly 5 customers in 1 hour) = (3⁵ × e⁻³) / 5!
  - **Real-world**: Number of emails received per day, accidents at an intersection

### Continuous Distributions

#### Normal Distribution
- **Parameters**: μ (mean), σ (standard deviation)
- **Properties**:
  - Bell-shaped curve
  - Symmetric about mean
  - 68-95-99.7 rule
- **Standard Normal**: μ = 0, σ = 1
- **Simple Example**:
  - Heights of adult men: μ = 70 inches, σ = 3 inches
  - 68% of men are between 67-73 inches tall
  - **Real-world**: Test scores, heights, weights, measurement errors

#### Standardization
- **Z-score**: z = (x - μ) / σ
- **Use**: Comparing values from different distributions
- **Simple Example**:
  - Student A: 85 on test (μ = 80, σ = 5) → z = (85-80)/5 = 1.0
  - Student B: 90 on test (μ = 85, σ = 10) → z = (90-85)/10 = 0.5
  - Student A performed better relative to their class
  - **Real-world**: Comparing SAT scores to ACT scores

---

## Data Visualization

### Essential Plots

#### Histogram
- **Use**: Distribution of continuous data
- **Key Elements**: Bins, frequency, shape
- **Simple Example**:
  - Data: Student heights [60, 62, 65, 67, 70, 72, 75, 78, 80]
  - Bins: 60-65, 65-70, 70-75, 75-80
  - **Real-world**: Distribution of exam scores, income levels

#### Box Plot
- **Use**: Five-number summary, outlier detection
- **Components**: Box (Q1-Q3), whiskers, outliers
- **Simple Example**:
  - Shows median, quartiles, and outliers clearly
  - **Real-world**: Comparing salaries across departments, test scores by grade level

#### Scatter Plot
- **Use**: Relationship between two variables
- **Patterns**: Linear, non-linear, no relationship
- **Simple Example**:
  - X-axis: Study hours, Y-axis: Test scores
  - Positive correlation: More study = higher scores
  - **Real-world**: Height vs weight, temperature vs ice cream sales

#### Bar Chart
- **Use**: Categorical data comparison
- **Types**: Vertical, horizontal, grouped, stacked
- **Simple Example**:
  - Categories: [Math, Science, English, History]
  - Values: [85, 92, 78, 88] (average grades)
  - **Real-world**: Sales by product category, votes by political party

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

# Sample data - 10 students' test scores
grades = [85, 92, 78, 96, 88, 91, 83, 89, 94, 87]

# Descriptive statistics
mean_grade = np.mean(grades)
median_grade = np.median(grades)
std_grade = np.std(grades, ddof=1)

print(f"Mean: {mean_grade:.2f}")
print(f"Median: {median_grade:.2f}")
print(f"Standard Deviation: {std_grade:.2f}")

# Simple interpretation
print(f"Average score: {mean_grade:.1f}")
print(f"Middle score: {median_grade:.1f}")
print(f"Typical deviation from average: {std_grade:.1f} points")
```

### Example 2: Probability Calculation
```python
# Probability of rolling a 6 on a fair die
P_six = 1/6
print(f"Probability of rolling a 6: {P_six:.3f}")

# Probability of rolling an even number
P_even = 3/6  # {2, 4, 6}
print(f"Probability of rolling even: {P_even:.3f}")

# Real-world example: Weather probability
sunny_days = 200
total_days = 365
P_sunny = sunny_days / total_days
print(f"Probability of sunny day: {P_sunny:.3f}")
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

# Real-world example: Test scores
mean_score = 80
std_score = 10
student_score = 90
z_score = (student_score - mean_score) / std_score
percentile = stats.norm.cdf(z_score) * 100
print(f"Student scored better than {percentile:.1f}% of students")
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
