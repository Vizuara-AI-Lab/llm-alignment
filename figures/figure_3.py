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

# Synthetic/hypothetical data for ROUGE-L F1 scores
models = [
    'Mistral-7B (Base)',
    'Zephyr-7B-SFT (Baseline)',
    'SFT-tuned Mistral',
    'DPO-tuned Mistral'
]
# Hypothetical scores demonstrating improvement
rouge_l_scores_comparison = [0.10, 0.38, 0.42, 0.45] 
threshold_rouge_l = 0.35

# Create the bar chart
fig, ax = plt.subplots(figsize=(9, 6))

# Use a colorblind-friendly palette
colors = sns.color_palette("viridis", len(models))

bars = ax.bar(models, rouge_l_scores_comparison, color=colors)

# Add value labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f'{yval:.2f}', ha='center', va='bottom', fontsize=10, color='black')

# Add the ROUGE-L threshold line
ax.axhline(threshold_rouge_l, color='red', linestyle='--', linewidth=1.5, label=f'ROUGE-L Threshold ({threshold_rouge_l:.2f})')

# Customize the plot
ax.set_ylim(0, max(rouge_l_scores_comparison) * 1.2) # Adjust y-axis limit
ax.set_ylabel('ROUGE-L F1 Score')
ax.set_title('Comparative ROUGE-L F1 Performance Across Alignment Stages (Hypothetical)')
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(axis='x', rotation=15) # Rotate x-axis labels if they overlap
ax.legend()

plt.tight_layout()
plt.savefig('figure_3.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved figure_3.png")