import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Publication-quality settings
plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 16,
    'grid.alpha': 0.6,
    'axes.edgecolor': '0.3',
    'axes.labelcolor': '0.3',
    'xtick.color': '0.3',
    'ytick.color': '0.3',
})

# Synthetic data for ROUGE-L F1 scores (200 samples)
# Mean around 0.38, with some normal distribution.
np.random.seed(42) # for reproducibility
mean_rouge_l = 0.38
std_rouge_l = 0.10
num_samples = 200
rouge_l_scores_dist = np.random.normal(loc=mean_rouge_l, scale=std_rouge_l, size=num_samples)
# Clip scores to be within a sensible range [0, 1]
rouge_l_scores_dist = np.clip(rouge_l_scores_dist, 0, 1)

# Create the histogram/KDE plot
fig, ax = plt.subplots(figsize=(8, 5))

sns.histplot(rouge_l_scores_dist, bins=20, kde=True, color=sns.color_palette("viridis")[0], ax=ax, edgecolor='black')

# Add mean and median lines
ax.axvline(np.mean(rouge_l_scores_dist), color='red', linestyle='--', label=f'Mean ROUGE-L F1 ({np.mean(rouge_l_scores_dist):.2f})')
ax.axvline(np.median(rouge_l_scores_dist), color='darkorange', linestyle=':', label=f'Median ROUGE-L F1 ({np.median(rouge_l_scores_dist):.2f})')

# Customize the plot
ax.set_xlabel('ROUGE-L F1 Score')
ax.set_ylabel('Number of Samples')
ax.set_title('Distribution of ROUGE-L F1 Scores per Sample')
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend()

plt.tight_layout()
plt.savefig('figure_2.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved figure_2.png")