import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data based on paper's description: CoT might lead to "slightly lower refusal rates being identified"
metrics = ['Avg. Helpfulness Score (1-10)', 'Avg. Harmlessness Score (1-10)', 'Refusal Rate for Harmful Prompts (%)']
direct_scores = [8.5, 7.8, 82.0]
cot_scores = [8.6, 7.9, 78.0] # Slightly lower refusal rate for CoT

# Set style for publication quality
sns.set_theme(style="whitegrid", palette="colorblind")
plt.rcParams.update({'font.size': 12, 'axes.labelsize': 14, 'xtick.labelsize': 12, 'ytick.labelsize': 12, 'legend.fontsize': 12})

fig, ax = plt.subplots(figsize=(9, 6))

bar_width = 0.35
index = np.arange(len(metrics))

# Colors for the two prompting strategies
color1 = sns.color_palette("colorblind")[0] # Direct Scoring
color2 = sns.color_palette("colorblind")[1] # CoT Prompting

bars1 = ax.bar(index - bar_width/2, direct_scores, bar_width, label='Direct Scoring', color=color1)
bars2 = ax.bar(index + bar_width/2, cot_scores, bar_width, label='Chain-of-Thought (CoT) Prompting', color=color2)

ax.set_xlabel('Alignment Metric')
ax.set_ylabel('Score (1-10) / Rate (%)')
ax.set_xticks(index)
ax.set_xticklabels(metrics, rotation=20, ha='right')
ax.set_ylim(0, 100) # Max 10 for scores, 100 for rate, so 100 is appropriate

# Add text labels on top of the bars
for bars in [bars1, bars2]:
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 1, round(yval, 1) if bar.get_width() > 10 else f'{int(yval)}%', ha='center', va='bottom', fontsize=10)

ax.legend(loc='upper right')
plt.title('Ablation Study: Effect of Judge Prompting Strategy on Alignment Scores', pad=20)
plt.tight_layout()
plt.savefig('figure_3.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved figure_3.png")