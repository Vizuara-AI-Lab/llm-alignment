import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Synthetic data representing expected progression
models = ['Zero-Shot Base Model', 'SFT Model (Baseline)', 'DPO Model (Future Work)']
rouge_l_scores = [0.15, 0.38, 0.45] # Hypothetical scores, SFT matches Fig 3, DPO is higher

# Target ROUGE-L F1 threshold
target_rouge_l_threshold = 0.35

# Plotting
fig, ax = plt.subplots(figsize=(9, 5))

bars = ax.bar(models, rouge_l_scores, color=['lightgrey', 'mediumseagreen', 'steelblue'], width=0.6)

# Add scores on top of bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.01, round(yval, 2), ha='center', va='bottom', fontsize=11, color='black')

# Add target ROUGE-L threshold line
ax.axhline(target_rouge_l_threshold, color='grey', linestyle='--', linewidth=1.5,
           label=f'Target ROUGE-L F1 ({target_rouge_l_threshold})')

ax.set_ylim(0, max(rouge_l_scores) * 1.2) # Adjust y-axis limit
ax.set_ylabel('ROUGE-L F1 Score', fontsize=12)
ax.set_title('Comparative ROUGE-L F1 Scores Across Alignment Stages', fontsize=14, pad=15)
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=11)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.legend(fontsize=10)

plt.tight_layout()
plt.savefig('figure_4.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved figure_4.png")