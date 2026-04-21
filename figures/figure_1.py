import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Data for the conceptual plot
categories = ['SFT Model (Hypothetical)', 'Target Threshold']
values = [48, 55] # Hypothetical win rate for SFT model, and the target threshold

# Colors for better distinction (colorblind friendly)
colors = ['#1f77b4', '#ff7f0e'] # Blue for SFT model, Orange for Threshold

plt.rcParams.update({'font.size': 12})
fig, ax = plt.subplots(figsize=(7, 5))

# Create the bar chart
bars = ax.bar(categories, values, color=colors, width=0.6)

# Add value labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.1f}%', ha='center', va='bottom', fontsize=10)

# Add a dashed line for the target threshold across the graph
ax.axhline(y=55, color='red', linestyle='--', linewidth=1.5, label='Target Threshold (55%)')


ax.set_ylim(0, 70) # Set Y-axis limit for better scaling
ax.set_ylabel('AlpacaEval 2.0 Win Rate (%)', fontsize=12)
ax.set_title('Conceptual AlpacaEval 2.0 Win Rate (Illustrative)', fontsize=14)
ax.tick_params(axis='x', rotation=0) # Ensure x-axis labels are horizontal

# Hide the top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add a subtle grid
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('figure_1.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved figure_1.png")