import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Data for the conceptual plot
epochs = np.arange(1, 6) # 5 hypothetical epochs
# Synthetic loss data, decreasing with some noise
np.random.seed(42) # for reproducibility
loss = np.array([2.5, 1.8, 1.2, 0.9, 0.7]) + np.random.normal(0, 0.05, 5)
loss = np.maximum(loss, 0.5) # Ensure loss doesn't go too low

plt.rcParams.update({'font.size': 12})
fig, ax = plt.subplots(figsize=(7, 5))

# Plot the training loss
ax.plot(epochs, loss, marker='o', linestyle='-', color='#2ca02c', linewidth=2, markersize=7, label='Training Loss')

ax.set_xlabel('Epoch', fontsize=12)
ax.set_ylabel('Loss', fontsize=12)
ax.set_title('Conceptual Supervised Fine-Tuning (SFT) Loss Curve (Illustrative)', fontsize=14)

ax.set_xticks(epochs) # Ensure ticks are at each epoch
ax.set_ylim(bottom=0) # Start y-axis from 0

# Hide the top and right spines for a cleaner look
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add a subtle grid
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.xaxis.grid(True, linestyle='--', alpha=0.7)

ax.legend(fontsize=10)

plt.tight_layout()
plt.savefig('figure_2.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved figure_2.png")