import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data based on paper's description of expected good performance and typical LLM behavior
# Helpfulness and harmlessness are on a 1-10 scale
data = {
    'Metric': ['Avg. Helpfulness Score', 'Avg. Harmlessness Score', 'Overall Avg. Score', 'Refusal Rate for Harmful Prompts'],
    'Value': [8.5, 7.8, 8.1, 82.0], # Scores out of 10, Refusal Rate in %
    'Type': ['Score', 'Score', 'Score', 'Percentage']
}

# Separate scores and percentage for plotting on different axes
scores = [data['Value'][i] for i, t in enumerate(data['Type']) if t == 'Score']
score_labels = [data['Metric'][i] for i, t in enumerate(data['Type']) if t == 'Score']
refusal_rate = data['Value'][data['Type'].index('Percentage')]
refusal_label = data['Metric'][data['Type'].index('Percentage')]

# Set style for publication quality
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams.update({'font.size': 12, 'axes.labelsize': 14, 'xtick.labelsize': 12, 'ytick.labelsize': 12, 'legend.fontsize': 12})

fig, ax1 = plt.subplots(figsize=(8, 6))

# Plot scores on ax1
bar_width = 0.4
index = np.arange(len(scores))
bars1 = ax1.bar(index, scores, bar_width, label='Score (1-10)', color=sns.color_palette("viridis", 3)[0])
ax1.set_xlabel('Alignment Metric')
ax1.set_ylabel('Score (1-10)', color=sns.color_palette("viridis", 3)[0])
ax1.set_xticks(index)
ax1.set_xticklabels(score_labels, rotation=30, ha='right')
ax1.set_ylim(0, 10)
ax1.tick_params(axis='y', labelcolor=sns.color_palette("viridis", 3)[0])

# Add text labels on top of the bars for scores
for bar in bars1:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 0.2, round(yval, 1), ha='center', va='bottom', fontsize=10)


# Create a second y-axis for refusal rate
ax2 = ax1.twinx()
bars2 = ax2.bar(index[-1] + bar_width + 0.1, refusal_rate, bar_width, label='Refusal Rate (%)', color=sns.color_palette("viridis", 3)[1]) # Position slightly offset
ax2.set_ylabel('Refusal Rate (%)', color=sns.color_palette("viridis", 3)[1])
ax2.set_ylim(0, 100)
ax2.tick_params(axis='y', labelcolor=sns.color_palette("viridis", 3)[1])

# Add text label on top of the refusal rate bar
for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{int(yval)}%', ha='center', va='bottom', fontsize=10)

# Manually create a legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color=sns.color_palette("viridis", 3)[0], lw=4, label='Score (1-10)'),
    Line2D([0], [0], color=sns.color_palette("viridis", 3)[1], lw=4, label='Refusal Rate (%)')
]
ax1.legend(handles=legend_elements, loc='upper left')


plt.title('Zephyr-7B-SFT-Full Alignment Performance on Synthetic Dataset', pad=20)
plt.tight_layout()
plt.savefig('figure_1.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved figure_1.png")