# Statistics Notes for Data Science Course - Session 1

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

### The Data Science Pipeline
```
Data Collection → Data Cleaning → Exploratory Analysis → Statistical Modeling → Interpretation → Decision Making
```

**📊 IMAGE SUGGESTION**: Flowchart showing the data science pipeline with statistics at each stage

---

## Descriptive Statistics

### Measures of Central Tendency

#### Mean (Average)
- **Formula**: μ = Σx / n (population) or x̄ = Σx / n (sample)
- **Use**: Best for normally distributed data
- **Sensitive to**: Outliers
- **Detailed Example**: 
  - Data: [2, 4, 6, 8, 10]
  - Step 1: Sum = 2+4+6+8+10 = 30
  - Step 2: Count = 5
  - Step 3: Mean = 30/5 = 6
  - **Real-world**: Average test score of 5 students

**📊 IMAGE SUGGESTION**: Bar chart showing the data points and the mean line

#### Median
- **Definition**: Middle value when data is ordered
- **Use**: Best for skewed distributions
- **Robust to**: Outliers
- **Detailed Examples**:
  - **Odd number of values**: [1, 3, 5, 7, 9] → Median = 5 (middle value)
  - **Even number of values**: [1, 3, 5, 7, 9, 11] → Median = (5+7)/2 = 6
  - **Real-world**: Middle income in a neighborhood

**📊 IMAGE SUGGESTION**: Box plot showing median line and quartiles

#### Mode
- **Definition**: Most frequently occurring value
- **Use**: Categorical data, identifying peaks
- **Detailed Example**:
  - Data: [1, 2, 2, 3, 4, 2, 5]
  - Frequency count: 1(1), 2(3), 3(1), 4(1), 5(1)
  - Mode = 2 (appears 3 times)
  - **Real-world**: Most common shoe size sold

**📊 IMAGE SUGGESTION**: Histogram showing frequency distribution with mode highlighted

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
- **Detailed Step-by-Step Example**:
  - Data: [2, 4, 6, 8, 10], Mean = 6
  - Step 1: Calculate deviations: (2-6), (4-6), (6-6), (8-6), (10-6)
  - Step 2: Square deviations: (-4)², (-2)², (0)², (2)², (4)²
  - Step 3: Sum squared deviations: 16 + 4 + 0 + 4 + 16 = 40
  - Step 4: Divide by n: 40/5 = 8
  - **Real-world**: How spread out are house prices in a neighborhood

**📊 IMAGE SUGGESTION**: Scatter plot with mean line and deviation arrows

#### Standard Deviation
- **Formula**: σ = √σ² (population) or s = √s² (sample)
- **Units**: Same as original data
- **Interpretation**: Average distance from mean
- **Detailed Example**:
  - From above: σ = √8 ≈ 2.83
  - **Interpretation**: On average, data points are 2.83 units away from the mean
  - **Real-world**: Average deviation of test scores from the mean

**📊 IMAGE SUGGESTION**: Normal distribution curve with standard deviation bands

#### Interquartile Range (IQR)
- **Formula**: IQR = Q3 - Q1
- **Use**: Robust measure of spread
- **Outlier Detection**: Values beyond 1.5 × IQR from Q1 or Q3
- **Detailed Example**:
  - Data: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
  - Q1 = 5 (25th percentile), Q3 = 15 (75th percentile)
  - IQR = 15 - 5 = 10
  - **Outlier boundaries**: Q1 - 1.5×IQR = 5 - 15 = -10, Q3 + 1.5×IQR = 15 + 15 = 30
  - **Real-world**: Middle 50% of salaries in a company

**📊 IMAGE SUGGESTION**: Box plot with IQR highlighted and outlier points marked

### Five-Number Summary
1. **Minimum**: Smallest value
2. **Q1 (25th percentile)**: 25% of data below this value
3. **Median (50th percentile)**: 50% of data below this value
4. **Q3 (75th percentile)**: 75% of data below this value
5. **Maximum**: Largest value

**Detailed Example**:
- Data: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
- Min = 1, Q1 = 5, Median = 10, Q3 = 15, Max = 19
- **Real-world**: Summary of student test scores (1-19 scale)

**📊 IMAGE SUGGESTION**: Box plot with all five numbers labeled

---

## Probability Fundamentals

### Basic Concepts

#### Sample Space (S)
- **Definition**: Set of all possible outcomes
- **Example**: Rolling a die → S = {1, 2, 3, 4, 5, 6}
- **Real-world**: All possible outcomes of flipping a coin → S = {Heads, Tails}

**📊 IMAGE SUGGESTION**: Venn diagram showing sample space

#### Event
- **Definition**: Subset of sample space
- **Example**: Getting an even number → E = {2, 4, 6}
- **Real-world**: Getting a grade of A or B → E = {A, B}

**📊 IMAGE SUGGESTION**: Venn diagram showing event as subset of sample space

#### Probability Rules
1. **0 ≤ P(A) ≤ 1** (Probability is between 0 and 1)
2. **P(S) = 1** (Sum of all probabilities equals 1)
3. **P(A ∪ B) = P(A) + P(B) - P(A ∩ B)** (Addition Rule)

**Detailed Examples**:
- **Rule 1**: P(rolling a 7 on a die) = 0 (impossible)
- **Rule 2**: P(rolling 1-6 on a die) = 1 (certain)
- **Rule 3**: P(rolling even OR divisible by 3) = P(even) + P(divisible by 3) - P(both)
  - P(even) = 3/6 = 0.5
  - P(divisible by 3) = 2/6 = 0.33
  - P(both) = 1/6 = 0.17
  - P(even OR divisible by 3) = 0.5 + 0.33 - 0.17 = 0.66

**📊 IMAGE SUGGESTION**: Venn diagram showing overlapping events with probabilities

### Conditional Probability
- **Formula**: P(A|B) = P(A ∩ B) / P(B)
- **Interpretation**: Probability of A given B has occurred
- **Detailed Example**:
  - A = "Student passes exam", B = "Student studied"
  - P(A|B) = "Probability of passing given that they studied"
  - **Calculation**: If 80% of students who study pass, and 60% of all students study:
    - P(B) = 0.6 (probability of studying)
    - P(A ∩ B) = 0.8 × 0.6 = 0.48 (probability of studying AND passing)
    - P(A|B) = 0.48 / 0.6 = 0.8
  - **Real-world**: P(rain|cloudy sky) = probability of rain given cloudy conditions

**📊 IMAGE SUGGESTION**: Tree diagram showing conditional probabilities

### Independence
- **Definition**: Events A and B are independent if P(A ∩ B) = P(A) × P(B)
- **Alternative**: P(A|B) = P(A)
- **Detailed Example**:
  - Rolling two dice: First die = 6, Second die = 4
  - P(First die = 6) = 1/6
  - P(Second die = 4) = 1/6
  - P(Both) = 1/6 × 1/6 = 1/36
  - These are independent events
  - **Real-world**: Flipping a coin and rolling a die are independent

**📊 IMAGE SUGGESTION**: Two separate probability trees showing independence

### Bayes' Theorem
- **Formula**: P(A|B) = P(B|A) × P(A) / P(B)
- **Use**: Updating probabilities with new information
- **Detailed Medical Example**:
  - A = "Person has disease", B = "Test is positive"
  - Given: Disease prevalence = 1%, Test sensitivity = 95%, Test specificity = 90%
  - P(A) = 0.01 (prior probability of having disease)
  - P(B|A) = 0.95 (probability of positive test given disease)
  - P(B|¬A) = 0.10 (probability of positive test given no disease)
  - P(B) = P(B|A)×P(A) + P(B|¬A)×P(¬A) = 0.95×0.01 + 0.10×0.99 = 0.1085
  - P(A|B) = 0.95 × 0.01 / 0.1085 = 0.0875
  - **Interpretation**: Only 8.75% chance of having disease despite positive test!

**📊 IMAGE SUGGESTION**: Decision tree showing Bayes' theorem calculation

---

## Common Probability Distributions

### Discrete Distributions

#### Binomial Distribution
- **Parameters**: n (trials), p (success probability)
- **Use**: Counting successes in n independent trials
- **Mean**: μ = np
- **Variance**: σ² = np(1-p)
- **Formula**: P(X = k) = C(n,k) × p^k × (1-p)^(n-k)
- **Detailed Example**:
  - n = 10 coin flips, p = 0.5 (fair coin)
  - P(exactly 7 heads) = C(10,7) × (0.5)⁷ × (0.5)³
  - C(10,7) = 10!/(7!×3!) = 120
  - P(X = 7) = 120 × 0.5^10 = 120 × 0.000977 = 0.117
  - **Real-world**: Number of successful sales calls out of 20 attempts

**📊 IMAGE SUGGESTION**: Binomial distribution histogram with n=10, p=0.5

#### Poisson Distribution
- **Parameter**: λ (rate)
- **Use**: Counting events in fixed time/space
- **Mean**: μ = λ
- **Variance**: σ² = λ
- **Formula**: P(X = k) = (λ^k × e^(-λ)) / k!
- **Detailed Example**:
  - λ = 3 customers per hour
  - P(exactly 5 customers in 1 hour) = (3⁵ × e⁻³) / 5!
  - 3⁵ = 243, e⁻³ ≈ 0.0498, 5! = 120
  - P(X = 5) = (243 × 0.0498) / 120 = 0.1008
  - **Real-world**: Number of emails received per day, accidents at an intersection

**📊 IMAGE SUGGESTION**: Poisson distribution curve with λ=3

### Continuous Distributions

#### Normal Distribution
- **Parameters**: μ (mean), σ (standard deviation)
- **Properties**:
  - Bell-shaped curve
  - Symmetric about mean
  - 68-95-99.7 rule (Empirical Rule)
- **Standard Normal**: μ = 0, σ = 1
- **Detailed Example**:
  - Heights of adult men: μ = 70 inches, σ = 3 inches
  - 68% of men are between 67-73 inches tall (μ ± σ)
  - 95% of men are between 64-76 inches tall (μ ± 2σ)
  - 99.7% of men are between 61-79 inches tall (μ ± 3σ)
  - **Real-world**: Test scores, heights, weights, measurement errors

**📊 IMAGE SUGGESTION**: Normal distribution curve with 68-95-99.7 rule bands

#### Standardization
- **Z-score**: z = (x - μ) / σ
- **Use**: Comparing values from different distributions
- **Detailed Example**:
  - Student A: 85 on test (μ = 80, σ = 5) → z = (85-80)/5 = 1.0
  - Student B: 90 on test (μ = 85, σ = 10) → z = (90-85)/10 = 0.5
  - Student A performed better relative to their class (higher z-score)
  - **Real-world**: Comparing SAT scores to ACT scores

**📊 IMAGE SUGGESTION**: Two normal curves with z-scores marked

---

## Data Visualization

### Essential Plots

#### Histogram
- **Use**: Distribution of continuous data
- **Key Elements**: Bins, frequency, shape
- **Detailed Example**:
  - Data: Student heights [60, 62, 65, 67, 70, 72, 75, 78, 80]
  - Bins: 60-65, 65-70, 70-75, 75-80
  - Frequencies: 2, 2, 3, 2
  - **Real-world**: Distribution of exam scores, income levels

**📊 IMAGE SUGGESTION**: Histogram with proper binning and frequency labels

#### Box Plot
- **Use**: Five-number summary, outlier detection
- **Components**: Box (Q1-Q3), whiskers, outliers
- **Detailed Example**:
  - Shows median, quartiles, and outliers clearly
  - **Real-world**: Comparing salaries across departments, test scores by grade level

**📊 IMAGE SUGGESTION**: Box plot with all components labeled

#### Scatter Plot
- **Use**: Relationship between two variables
- **Patterns**: Linear, non-linear, no relationship
- **Detailed Example**:
  - X-axis: Study hours, Y-axis: Test scores
  - Positive correlation: More study = higher scores
  - **Real-world**: Height vs weight, temperature vs ice cream sales

**📊 IMAGE SUGGESTION**: Scatter plot with correlation line and R² value

#### Bar Chart
- **Use**: Categorical data comparison
- **Types**: Vertical, horizontal, grouped, stacked
- **Detailed Example**:
  - Categories: [Math, Science, English, History]
  - Values: [85, 92, 78, 88] (average grades)
  - **Real-world**: Sales by product category, votes by political party

**📊 IMAGE SUGGESTION**: Bar chart with proper spacing and labels

### Best Practices
1. **Choose appropriate plot type**
2. **Label axes clearly**
3. **Use consistent scales**
4. **Avoid misleading visualizations**
5. **Consider your audience**

**📊 IMAGE SUGGESTION**: Side-by-side comparison of good vs bad visualizations

---

## Practical Examples

### Example 1: Student Grades Analysis
```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Sample data - 20 students' test scores
grades = [85, 92, 78, 96, 88, 91, 83, 89, 94, 87, 82, 90, 85, 93, 86, 89, 91, 84, 88, 92]

# Descriptive statistics
mean_grade = np.mean(grades)
median_grade = np.median(grades)
std_grade = np.std(grades, ddof=1)
variance_grade = np.var(grades, ddof=1)

print(f"Mean: {mean_grade:.2f}")
print(f"Median: {median_grade:.2f}")
print(f"Standard Deviation: {std_grade:.2f}")
print(f"Variance: {variance_grade:.2f}")

# Five-number summary
q1 = np.percentile(grades, 25)
q3 = np.percentile(grades, 75)
min_grade = np.min(grades)
max_grade = np.max(grades)

print(f"\nFive-Number Summary:")
print(f"Minimum: {min_grade}")
print(f"Q1: {q1:.2f}")
print(f"Median: {median_grade:.2f}")
print(f"Q3: {q3:.2f}")
print(f"Maximum: {max_grade}")

# Interpretation
print(f"\nInterpretation:")
print(f"Average score: {mean_grade:.1f}")
print(f"Middle score: {median_grade:.1f}")
print(f"Typical deviation from average: {std_grade:.1f} points")
print(f"50% of students scored between {q1:.1f} and {q3:.1f}")
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

# Conditional probability example
# P(Pass|Study) = 0.8, P(Study) = 0.6
P_study = 0.6
P_pass_given_study = 0.8
P_pass_and_study = P_pass_given_study * P_study
print(f"Probability of studying and passing: {P_pass_and_study:.3f}")
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

# Binomial distribution example
n = 20  # 20 sales calls
p = 0.3  # 30% success rate
k = 7   # exactly 7 successes
binomial_prob = stats.binom.pmf(k, n, p)
print(f"Probability of exactly 7 successes: {binomial_prob:.3f}")
```

---

## Key Takeaways

### Session 1 Learning Objectives
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
