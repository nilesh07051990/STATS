import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats
import pandas as pd
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch
import matplotlib.patches as mpatches

# Set style for consistent look
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Create images directory if it doesn't exist
import os
os.makedirs('images', exist_ok=True)

# 1. Data Science Pipeline
def create_data_science_pipeline():
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    
    # Define stages
    stages = ['Data\nCollection', 'Data\nCleaning', 'Exploratory\nAnalysis', 
              'Statistical\nModeling', 'Interpretation', 'Decision\nMaking']
    
    # Create flowchart
    x_positions = np.linspace(1, 11, len(stages))
    y_position = 0.5
    
    for i, (stage, x) in enumerate(zip(stages, x_positions)):
        # Create rounded rectangle
        rect = FancyBboxPatch((x-0.8, y_position-0.3), 1.6, 0.6,
                            boxstyle="round,pad=0.1", 
                            facecolor='lightblue', edgecolor='navy', linewidth=2)
        ax.add_patch(rect)
        ax.text(x, y_position, stage, ha='center', va='center', fontsize=10, fontweight='bold')
        
        # Add arrow
        if i < len(stages) - 1:
            ax.arrow(x+0.8, y_position, 0.4, 0, head_width=0.1, head_length=0.1, 
                    fc='black', ec='black')
    
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 1)
    ax.set_title('Data Science Pipeline with Statistics', fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('images/data-science-pipeline.png', dpi=300, bbox_inches='tight')
    plt.close()

# 2. Mean Calculation
def create_mean_calculation():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    data = [2, 4, 6, 8, 10]
    mean_val = np.mean(data)
    
    # Create bar chart
    bars = ax.bar(range(len(data)), data, color='skyblue', edgecolor='navy', linewidth=2)
    
    # Add mean line
    ax.axhline(y=mean_val, color='red', linestyle='--', linewidth=3, label=f'Mean = {mean_val}')
    
    # Add data labels
    for i, v in enumerate(data):
        ax.text(i, v + 0.2, str(v), ha='center', va='bottom', fontweight='bold')
    
    ax.set_xlabel('Data Points', fontsize=12)
    ax.set_ylabel('Values', fontsize=12)
    ax.set_title('Mean Calculation Example', fontsize=14, fontweight='bold')
    ax.set_xticks(range(len(data)))
    ax.set_xticklabels([f'Point {i+1}' for i in range(len(data))])
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/mean-calculation.png', dpi=300, bbox_inches='tight')
    plt.close()

# 3. Median Box Plot
def create_median_boxplot():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Sample data
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    # Create box plot
    box_plot = ax.boxplot(data, patch_artist=True, labels=['Sample Data'])
    box_plot['boxes'][0].set_facecolor('lightgreen')
    
    # Add median line highlight
    median_line = box_plot['medians'][0]
    median_line.set_color('red')
    median_line.set_linewidth(3)
    
    # Add labels
    ax.set_ylabel('Values', fontsize=12)
    ax.set_title('Box Plot Showing Median and Quartiles', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # Add text annotations
    q1, median, q3 = np.percentile(data, [25, 50, 75])
    ax.text(1.1, median, f'Median = {median}', va='center', fontweight='bold', color='red')
    ax.text(1.1, q1, f'Q1 = {q1}', va='center', fontweight='bold')
    ax.text(1.1, q3, f'Q3 = {q3}', va='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('images/median-boxplot.png', dpi=300, bbox_inches='tight')
    plt.close()

# 4. Mode Histogram
def create_mode_histogram():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Sample data with mode
    data = [1, 2, 2, 3, 4, 2, 5, 2, 6, 2]
    
    # Create histogram
    n, bins, patches = ax.hist(data, bins=6, color='lightcoral', edgecolor='black', alpha=0.7)
    
    # Highlight the mode (value 2)
    mode_value = 2
    mode_bin = np.where(bins <= mode_value)[0][-1]
    if mode_bin < len(patches):
        patches[mode_bin].set_facecolor('red')
        patches[mode_bin].set_alpha(1.0)
    
    ax.set_xlabel('Values', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title('Histogram Showing Mode (Most Frequent Value)', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # Add mode annotation
    ax.annotate(f'Mode = {mode_value}', xy=(mode_value, max(n)), 
                xytext=(mode_value+1, max(n)+0.5), 
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, fontweight='bold', color='red')
    
    plt.tight_layout()
    plt.savefig('images/mode-histogram.png', dpi=300, bbox_inches='tight')
    plt.close()

# 5. Variance Scatter Plot
def create_variance_scatter():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Sample data
    data = [2, 4, 6, 8, 10]
    mean_val = np.mean(data)
    
    # Create scatter plot
    ax.scatter(range(len(data)), data, color='blue', s=100, alpha=0.7, label='Data Points')
    
    # Add mean line
    ax.axhline(y=mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean = {mean_val}')
    
    # Add deviation arrows
    for i, value in enumerate(data):
        ax.annotate('', xy=(i, mean_val), xytext=(i, value),
                   arrowprops=dict(arrowstyle='<->', color='green', lw=2))
        ax.text(i+0.1, (value + mean_val)/2, f'|{value-mean_val:.1f}|', 
                fontsize=10, color='green', fontweight='bold')
    
    ax.set_xlabel('Data Points', fontsize=12)
    ax.set_ylabel('Values', fontsize=12)
    ax.set_title('Variance Calculation: Deviations from Mean', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/variance-scatter.png', dpi=300, bbox_inches='tight')
    plt.close()

# 6. Standard Deviation Curve
def create_std_dev_curve():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Generate normal distribution
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x, 0, 1)
    
    # Plot the curve
    ax.plot(x, y, 'b-', linewidth=2, label='Normal Distribution')
    
    # Add standard deviation bands
    colors = ['lightgreen', 'yellow', 'orange']
    labels = ['±1σ (68%)', '±2σ (95%)', '±3σ (99.7%)']
    
    for i, (std, color, label) in enumerate(zip([1, 2, 3], colors, labels)):
        ax.axvspan(-std, std, alpha=0.3, color=color, label=label)
    
    ax.set_xlabel('Standard Deviations (σ)', fontsize=12)
    ax.set_ylabel('Probability Density', fontsize=12)
    ax.set_title('Normal Distribution with Standard Deviation Bands', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/std-dev-curve.png', dpi=300, bbox_inches='tight')
    plt.close()

# 7. IQR Box Plot
def create_iqr_boxplot():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Sample data with outliers
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 25, 30]  # Added outliers
    
    # Create box plot
    box_plot = ax.boxplot(data, patch_artist=True, labels=['Sample Data'])
    box_plot['boxes'][0].set_facecolor('lightblue')
    
    # Highlight IQR
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1
    
    # Add IQR annotation
    ax.annotate(f'IQR = {iqr:.1f}', xy=(1, (q1+q3)/2), 
                xytext=(1.3, (q1+q3)/2), 
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, fontweight='bold', color='red')
    
    ax.set_ylabel('Values', fontsize=12)
    ax.set_title('Box Plot with IQR and Outliers', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/iqr-boxplot.png', dpi=300, bbox_inches='tight')
    plt.close()

# 8. Five Number Summary
def create_five_number_summary():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Sample data
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    # Create box plot
    box_plot = ax.boxplot(data, patch_artist=True, labels=['Sample Data'])
    box_plot['boxes'][0].set_facecolor('lightgreen')
    
    # Get five number summary
    min_val = np.min(data)
    q1 = np.percentile(data, 25)
    median = np.median(data)
    q3 = np.percentile(data, 75)
    max_val = np.max(data)
    
    # Add labels
    ax.text(1.1, min_val, f'Min = {min_val}', va='center', fontweight='bold')
    ax.text(1.1, q1, f'Q1 = {q1}', va='center', fontweight='bold')
    ax.text(1.1, median, f'Median = {median}', va='center', fontweight='bold', color='red')
    ax.text(1.1, q3, f'Q3 = {q3}', va='center', fontweight='bold')
    ax.text(1.1, max_val, f'Max = {max_val}', va='center', fontweight='bold')
    
    ax.set_ylabel('Values', fontsize=12)
    ax.set_title('Five Number Summary', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/five-number-summary.png', dpi=300, bbox_inches='tight')
    plt.close()

# 9. Sample Space Venn Diagram
def create_sample_space_venn():
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    
    # Create a large circle for sample space
    circle = Circle((0.5, 0.5), 0.4, fill=False, edgecolor='blue', linewidth=3)
    ax.add_patch(circle)
    
    # Add sample space elements
    elements = ['1', '2', '3', '4', '5', '6']
    angles = np.linspace(0, 2*np.pi, len(elements), endpoint=False)
    
    for element, angle in zip(elements, angles):
        x = 0.5 + 0.3 * np.cos(angle)
        y = 0.5 + 0.3 * np.sin(angle)
        ax.text(x, y, element, ha='center', va='center', fontsize=14, fontweight='bold')
    
    ax.text(0.5, 0.1, 'Sample Space S = {1, 2, 3, 4, 5, 6}', 
            ha='center', fontsize=12, fontweight='bold')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('Sample Space for Rolling a Die', fontsize=14, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('images/sample-space-venn.png', dpi=300, bbox_inches='tight')
    plt.close()

# 10. Event Subset Venn Diagram
def create_event_subset_venn():
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    
    # Create sample space circle
    sample_circle = Circle((0.5, 0.5), 0.4, fill=False, edgecolor='blue', linewidth=3)
    ax.add_patch(sample_circle)
    
    # Create event circle (subset)
    event_circle = Circle((0.5, 0.5), 0.25, fill=True, facecolor='lightgreen', 
                         edgecolor='green', linewidth=2, alpha=0.7)
    ax.add_patch(event_circle)
    
    # Add labels
    ax.text(0.5, 0.5, 'E = {2, 4, 6}', ha='center', va='center', 
            fontsize=12, fontweight='bold')
    ax.text(0.5, 0.1, 'Sample Space S = {1, 2, 3, 4, 5, 6}', 
            ha='center', fontsize=10)
    ax.text(0.5, 0.05, 'Event E (Even Numbers)', 
            ha='center', fontsize=10, fontweight='bold', color='green')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('Event as Subset of Sample Space', fontsize=14, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('images/event-subset-venn.png', dpi=300, bbox_inches='tight')
    plt.close()

# 11. Overlapping Events Venn Diagram
def create_overlapping_events_venn():
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    
    # Create overlapping circles
    circle1 = Circle((0.4, 0.5), 0.3, fill=True, facecolor='lightblue', 
                    edgecolor='blue', linewidth=2, alpha=0.7)
    circle2 = Circle((0.6, 0.5), 0.3, fill=True, facecolor='lightcoral', 
                    edgecolor='red', linewidth=2, alpha=0.7)
    
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    
    # Add labels
    ax.text(0.3, 0.5, 'A', ha='center', va='center', fontsize=16, fontweight='bold')
    ax.text(0.7, 0.5, 'B', ha='center', va='center', fontsize=16, fontweight='bold')
    ax.text(0.5, 0.5, 'A∩B', ha='center', va='center', fontsize=14, fontweight='bold')
    
    # Add probability labels
    ax.text(0.2, 0.7, 'P(A)', ha='center', fontsize=12, fontweight='bold')
    ax.text(0.8, 0.7, 'P(B)', ha='center', fontsize=12, fontweight='bold')
    ax.text(0.5, 0.3, 'P(A∩B)', ha='center', fontsize=12, fontweight='bold')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('Overlapping Events with Probabilities', fontsize=14, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('images/overlapping-events-venn.png', dpi=300, bbox_inches='tight')
    plt.close()

# 12. Conditional Probability Tree
def create_conditional_probability_tree():
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    
    # Tree structure
    # Root
    ax.text(0.5, 0.9, 'Study?', ha='center', fontsize=14, fontweight='bold')
    
    # First level branches
    ax.plot([0.5, 0.3], [0.8, 0.6], 'k-', linewidth=2)
    ax.plot([0.5, 0.7], [0.8, 0.6], 'k-', linewidth=2)
    
    ax.text(0.25, 0.65, 'Yes (60%)', ha='center', fontsize=12)
    ax.text(0.75, 0.65, 'No (40%)', ha='center', fontsize=12)
    
    # Second level branches
    ax.plot([0.3, 0.2], [0.5, 0.3], 'k-', linewidth=2)
    ax.plot([0.3, 0.4], [0.5, 0.3], 'k-', linewidth=2)
    ax.plot([0.7, 0.6], [0.5, 0.3], 'k-', linewidth=2)
    ax.plot([0.7, 0.8], [0.5, 0.3], 'k-', linewidth=2)
    
    # Labels
    ax.text(0.15, 0.25, 'Pass (80%)', ha='center', fontsize=10)
    ax.text(0.35, 0.25, 'Fail (20%)', ha='center', fontsize=10)
    ax.text(0.55, 0.25, 'Pass (30%)', ha='center', fontsize=10)
    ax.text(0.85, 0.25, 'Fail (70%)', ha='center', fontsize=10)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title('Conditional Probability Tree', fontsize=16, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('images/conditional-probability-tree.png', dpi=300, bbox_inches='tight')
    plt.close()

# 13. Independent Events Trees
def create_independent_events_trees():
    fig, ax = plt.subplots(1, 2, figsize=(16, 8))
    
    # First tree - Coin flip
    ax[0].text(0.5, 0.9, 'Coin Flip', ha='center', fontsize=14, fontweight='bold')
    ax[0].plot([0.5, 0.3], [0.8, 0.6], 'k-', linewidth=2)
    ax[0].plot([0.5, 0.7], [0.8, 0.6], 'k-', linewidth=2)
    ax[0].text(0.25, 0.65, 'Heads (50%)', ha='center', fontsize=12)
    ax[0].text(0.75, 0.65, 'Tails (50%)', ha='center', fontsize=12)
    ax[0].set_title('Independent Event 1', fontsize=14, fontweight='bold')
    ax[0].axis('off')
    
    # Second tree - Die roll
    ax[1].text(0.5, 0.9, 'Die Roll', ha='center', fontsize=14, fontweight='bold')
    ax[1].plot([0.5, 0.3], [0.8, 0.6], 'k-', linewidth=2)
    ax[1].plot([0.5, 0.7], [0.8, 0.6], 'k-', linewidth=2)
    ax[1].text(0.25, 0.65, 'Even (50%)', ha='center', fontsize=12)
    ax[1].text(0.75, 0.65, 'Odd (50%)', ha='center', fontsize=12)
    ax[1].set_title('Independent Event 2', fontsize=14, fontweight='bold')
    ax[1].axis('off')
    
    plt.suptitle('Independent Events - Separate Probability Trees', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/independent-events-trees.png', dpi=300, bbox_inches='tight')
    plt.close()

# 14. Bayes Theorem Tree
def create_bayes_theorem_tree():
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    
    # Medical test example
    ax.text(0.5, 0.9, 'Medical Test Example', ha='center', fontsize=16, fontweight='bold')
    
    # Disease status
    ax.plot([0.5, 0.3], [0.8, 0.6], 'k-', linewidth=2)
    ax.plot([0.5, 0.7], [0.8, 0.6], 'k-', linewidth=2)
    ax.text(0.25, 0.65, 'Has Disease (1%)', ha='center', fontsize=12)
    ax.text(0.75, 0.65, 'No Disease (99%)', ha='center', fontsize=12)
    
    # Test results
    ax.plot([0.3, 0.2], [0.5, 0.3], 'k-', linewidth=2)
    ax.plot([0.3, 0.4], [0.5, 0.3], 'k-', linewidth=2)
    ax.plot([0.7, 0.6], [0.5, 0.3], 'k-', linewidth=2)
    ax.plot([0.7, 0.8], [0.5, 0.3], 'k-', linewidth=2)
    
    # Labels with probabilities
    ax.text(0.15, 0.25, 'Positive (95%)', ha='center', fontsize=10)
    ax.text(0.35, 0.25, 'Negative (5%)', ha='center', fontsize=10)
    ax.text(0.55, 0.25, 'Positive (10%)', ha='center', fontsize=10)
    ax.text(0.85, 0.25, 'Negative (90%)', ha='center', fontsize=10)
    
    # Bayes calculation
    ax.text(0.5, 0.1, 'P(Disease|Positive) = 0.95 × 0.01 / (0.95 × 0.01 + 0.10 × 0.99) = 0.0875', 
            ha='center', fontsize=12, fontweight='bold', 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow"))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('images/bayes-theorem-tree.png', dpi=300, bbox_inches='tight')
    plt.close()

# 15. Binomial Distribution
def create_binomial_distribution():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Binomial distribution parameters
    n, p = 10, 0.5
    x = np.arange(0, n+1)
    y = stats.binom.pmf(x, n, p)
    
    # Create histogram
    bars = ax.bar(x, y, color='skyblue', edgecolor='navy', alpha=0.7)
    
    # Highlight specific value
    bars[7].set_color('red')
    bars[7].set_alpha(1.0)
    
    ax.set_xlabel('Number of Successes', fontsize=12)
    ax.set_ylabel('Probability', fontsize=12)
    ax.set_title(f'Binomial Distribution (n={n}, p={p})', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # Add annotation
    ax.annotate(f'P(X=7) = {y[7]:.3f}', xy=(7, y[7]), 
                xytext=(7, y[7]+0.02), 
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, fontweight='bold', color='red')
    
    plt.tight_layout()
    plt.savefig('images/binomial-distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

# 16. Poisson Distribution
def create_poisson_distribution():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Poisson distribution parameters
    lambda_val = 3
    x = np.arange(0, 15)
    y = stats.poisson.pmf(x, lambda_val)
    
    # Create bar chart
    bars = ax.bar(x, y, color='lightcoral', edgecolor='darkred', alpha=0.7)
    
    # Highlight specific value
    bars[5].set_color('red')
    bars[5].set_alpha(1.0)
    
    ax.set_xlabel('Number of Events', fontsize=12)
    ax.set_ylabel('Probability', fontsize=12)
    ax.set_title(f'Poisson Distribution (λ={lambda_val})', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # Add annotation
    ax.annotate(f'P(X=5) = {y[5]:.3f}', xy=(5, y[5]), 
                xytext=(5, y[5]+0.02), 
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, fontweight='bold', color='red')
    
    plt.tight_layout()
    plt.savefig('images/poisson-distribution.png', dpi=300, bbox_inches='tight')
    plt.close()

# 17. Normal Distribution Rule
def create_normal_distribution_rule():
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    
    # Generate normal distribution
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x, 0, 1)
    
    # Plot the curve
    ax.plot(x, y, 'b-', linewidth=3, label='Normal Distribution')
    
    # Add 68-95-99.7 rule bands
    colors = ['lightgreen', 'yellow', 'orange']
    labels = ['68% within ±1σ', '95% within ±2σ', '99.7% within ±3σ']
    percentages = [68, 95, 99.7]
    
    for i, (std, color, label, pct) in enumerate(zip([1, 2, 3], colors, labels, percentages)):
        ax.axvspan(-std, std, alpha=0.3, color=color, label=f'{label} ({pct}%)')
        ax.axvline(-std, color='red', linestyle='--', alpha=0.7)
        ax.axvline(std, color='red', linestyle='--', alpha=0.7)
    
    ax.set_xlabel('Standard Deviations (σ)', fontsize=12)
    ax.set_ylabel('Probability Density', fontsize=12)
    ax.set_title('68-95-99.7 Rule for Normal Distribution', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/normal-distribution-rule.png', dpi=300, bbox_inches='tight')
    plt.close()

# 18. Z-Score Comparison
def create_z_score_comparison():
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    
    # Two normal distributions
    x = np.linspace(-4, 4, 1000)
    y1 = stats.norm.pdf(x, 0, 1)  # Standard normal
    y2 = stats.norm.pdf(x, 1, 1.5)  # Shifted and scaled
    
    # Plot both curves
    ax.plot(x, y1, 'b-', linewidth=2, label='Distribution 1 (μ=0, σ=1)')
    ax.plot(x, y2, 'r-', linewidth=2, label='Distribution 2 (μ=1, σ=1.5)')
    
    # Add z-score lines
    z_scores = [-2, -1, 0, 1, 2]
    for z in z_scores:
        ax.axvline(z, color='gray', linestyle=':', alpha=0.7)
        ax.text(z, 0.3, f'z={z}', ha='center', fontsize=10)
    
    ax.set_xlabel('Z-Scores', fontsize=12)
    ax.set_ylabel('Probability Density', fontsize=12)
    ax.set_title('Z-Score Comparison Between Distributions', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/z-score-comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

# 19. Histogram Example
def create_histogram_example():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Sample data
    data = [60, 62, 65, 67, 70, 72, 75, 78, 80, 82, 85, 88, 90, 92, 95]
    
    # Create histogram with proper binning
    n, bins, patches = ax.hist(data, bins=5, color='skyblue', edgecolor='navy', alpha=0.7)
    
    # Add frequency labels
    for i, (count, patch) in enumerate(zip(n, patches)):
        if count > 0:
            ax.text(patch.get_x() + patch.get_width()/2, count + 0.1, 
                   f'{int(count)}', ha='center', va='bottom', fontweight='bold')
    
    ax.set_xlabel('Height (inches)', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title('Histogram with Proper Binning and Frequency Labels', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/histogram-example.png', dpi=300, bbox_inches='tight')
    plt.close()

# 20. Box Plot Components
def create_boxplot_components():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Sample data
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 25, 30]
    
    # Create box plot
    box_plot = ax.boxplot(data, patch_artist=True, labels=['Sample Data'])
    box_plot['boxes'][0].set_facecolor('lightblue')
    
    # Add component labels
    ax.text(1.1, np.min(data), 'Min', ha='left', va='center', fontweight='bold')
    ax.text(1.1, np.percentile(data, 25), 'Q1', ha='left', va='center', fontweight='bold')
    ax.text(1.1, np.median(data), 'Median', ha='left', va='center', fontweight='bold', color='red')
    ax.text(1.1, np.percentile(data, 75), 'Q3', ha='left', va='center', fontweight='bold')
    ax.text(1.1, np.max(data), 'Max', ha='left', va='center', fontweight='bold')
    
    # Add whisker labels
    ax.text(0.8, np.min(data), 'Lower\nWhisker', ha='center', va='center', fontsize=10)
    ax.text(0.8, np.max(data), 'Upper\nWhisker', ha='center', va='center', fontsize=10)
    
    ax.set_ylabel('Values', fontsize=12)
    ax.set_title('Box Plot with All Components Labeled', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/boxplot-components.png', dpi=300, bbox_inches='tight')
    plt.close()

# 21. Scatter Plot Correlation
def create_scatter_plot_correlation():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Generate correlated data
    np.random.seed(42)
    x = np.random.normal(0, 1, 50)
    y = 0.8 * x + np.random.normal(0, 0.5, 50)
    
    # Create scatter plot
    ax.scatter(x, y, color='blue', alpha=0.6, s=50)
    
    # Add correlation line
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    ax.plot(x, p(x), "r--", alpha=0.8, linewidth=2)
    
    # Calculate and display R²
    correlation = np.corrcoef(x, y)[0, 1]
    r_squared = correlation ** 2
    
    ax.text(0.05, 0.95, f'R² = {r_squared:.3f}', transform=ax.transAxes, 
            fontsize=12, fontweight='bold', 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow"))
    
    ax.set_xlabel('X Variable', fontsize=12)
    ax.set_ylabel('Y Variable', fontsize=12)
    ax.set_title('Scatter Plot with Correlation Line and R² Value', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/scatter-plot-correlation.png', dpi=300, bbox_inches='tight')
    plt.close()

# 22. Bar Chart Example
def create_bar_chart_example():
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Sample data
    categories = ['Math', 'Science', 'English', 'History']
    values = [85, 92, 78, 88]
    
    # Create bar chart
    bars = ax.bar(categories, values, color=['skyblue', 'lightgreen', 'lightcoral', 'lightyellow'], 
                  edgecolor='black', linewidth=1)
    
    # Add value labels on bars
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
               str(value), ha='center', va='bottom', fontweight='bold')
    
    ax.set_ylabel('Average Grade', fontsize=12)
    ax.set_title('Bar Chart with Proper Spacing and Labels', fontsize=14, fontweight='bold')
    ax.set_ylim(0, 100)
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig('images/bar-chart-example.png', dpi=300, bbox_inches='tight')
    plt.close()

# 23. Visualization Comparison
def create_visualization_comparison():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Good visualization
    categories = ['A', 'B', 'C', 'D']
    values = [20, 35, 30, 15]
    
    bars1 = ax1.bar(categories, values, color=['lightblue', 'lightgreen', 'lightcoral', 'lightyellow'])
    ax1.set_title('Good Visualization', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Count', fontsize=12)
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Add value labels
    for bar, value in zip(bars1, values):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                str(value), ha='center', va='bottom', fontweight='bold')
    
    # Bad visualization (misleading scale)
    ax2.bar(categories, values, color=['lightblue', 'lightgreen', 'lightcoral', 'lightyellow'])
    ax2.set_title('Bad Visualization (Misleading Scale)', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Count', fontsize=12)
    ax2.set_ylim(0, 50)  # Misleading scale
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.suptitle('Good vs Bad Visualization Practices', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/visualization-comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

# Main execution
if __name__ == "__main__":
    print("Creating all images...")
    
    # Create all images
    create_data_science_pipeline()
    print("✓ Data Science Pipeline")
    
    create_mean_calculation()
    print("✓ Mean Calculation")
    
    create_median_boxplot()
    print("✓ Median Box Plot")
    
    create_mode_histogram()
    print("✓ Mode Histogram")
    
    create_variance_scatter()
    print("✓ Variance Scatter Plot")
    
    create_std_dev_curve()
    print("✓ Standard Deviation Curve")
    
    create_iqr_boxplot()
    print("✓ IQR Box Plot")
    
    create_five_number_summary()
    print("✓ Five Number Summary")
    
    create_sample_space_venn()
    print("✓ Sample Space Venn Diagram")
    
    create_event_subset_venn()
    print("✓ Event Subset Venn Diagram")
    
    create_overlapping_events_venn()
    print("✓ Overlapping Events Venn Diagram")
    
    create_conditional_probability_tree()
    print("✓ Conditional Probability Tree")
    
    create_independent_events_trees()
    print("✓ Independent Events Trees")
    
    create_bayes_theorem_tree()
    print("✓ Bayes Theorem Tree")
    
    create_binomial_distribution()
    print("✓ Binomial Distribution")
    
    create_poisson_distribution()
    print("✓ Poisson Distribution")
    
    create_normal_distribution_rule()
    print("✓ Normal Distribution Rule")
    
    create_z_score_comparison()
    print("✓ Z-Score Comparison")
    
    create_histogram_example()
    print("✓ Histogram Example")
    
    create_boxplot_components()
    print("✓ Box Plot Components")
    
    create_scatter_plot_correlation()
    print("✓ Scatter Plot Correlation")
    
    create_bar_chart_example()
    print("✓ Bar Chart Example")
    
    create_visualization_comparison()
    print("✓ Visualization Comparison")
    
    print("\n🎉 All 23 images have been created successfully!")
    print("Images saved in the 'images/' directory")
