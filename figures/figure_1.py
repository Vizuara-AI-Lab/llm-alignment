import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Set a consistent style for publication quality
plt.style.use('seaborn-v0_8-darkgrid')

# Data for illustrative loss curves
epochs = np.arange(1, 4) # 3 epochs as per plan
train_loss = np.array([1.8, 1.2, 0.9])
val_loss = np.array([1.6, 1.1, 0.95])

# Add some noise for realism, but keep the trend
np.random.seed(42)
train_loss = train_loss + np.random.normal(0, 0.05, size=len(epochs))
val_loss = val_loss + np.random.normal(0, 0.05, size=len(epochs))

# Ensure loss remains positive and generally decreasing
train_loss = np.maximum(train_loss, 0.5)
val_loss = np.maximum(val_loss, 0.5)


plt.figure(figsize=(8, 5))

plt.plot(epochs, train_loss, marker='o', linestyle='-', color='#1f77b4', label='Training Loss')
plt.plot(epochs, val_loss, marker='x', linestyle='--', color='#ff7f0e', label='Validation Loss')

plt.title('Illustrative Training and Validation Loss During LLM Supervised Fine-Tuning', fontsize=14, pad=15)
plt.xlabel('Epoch', fontsize=12)
plt.ylabel('Loss (Cross-Entropy)', fontsize=12)
plt.xticks(epochs)
plt.yticks(fontsize=10)
plt.ylim(bottom=0.5, top=2.0)
plt.legend(fontsize=10)
plt.grid(True, linestyle=':', alpha=0.7)
plt.text(0.5, -0.25, 'Note: This figure uses synthetic data to illustrate expected trends, as no actual results were obtained due to experimental failure.',
         transform=plt.gca().transAxes, fontsize=9, color='gray', ha='center', va='top')

plt.tight_layout()
plt.savefig('figure_1.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved figure_1.png")