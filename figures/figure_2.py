import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Set a consistent style for publication quality
plt.style.use('seaborn-v0_8-darkgrid')

categories = ['Helpfulness', 'Harmlessness', 'Honesty']
base_model_scores = [3.5, 2.0, 3.0] # Conceptual scores for base model (lower alignment)
finetuned_model_scores = [4.5, 4.0, 4.0] # Conceptual scores for fine-tuned model (higher alignment)

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(9, 6))
rects1 = ax.bar(x - width/2, base_model_scores, width, label='Base Model (Mistral-7B-v0.1)', color='#8c564b', alpha=0.8)
rects2 = ax.bar(x + width/2, finetuned_model_scores, width, label='Fine-Tuned Model (Conceptual SFT)', color='#2ca02c', alpha=0.8)

# Add some text for labels and titles
ax.set_title('Conceptual Comparison of LLM Alignment Characteristics: Base vs. Fine-Tuned Model', fontsize=14, pad=15)
ax.set_ylabel('Alignment Score (Conceptual)', fontsize=12)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12)
ax.set_ylim(0, 5.5) # Assuming a 1-5 scale for conceptual scores
ax.legend(fontsize=10)

# Add value labels on bars for clarity
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

autolabel(rects1)
autolabel(rects2)

plt.grid(axis='y', linestyle=':', alpha=0.7)
plt.text(0.5, -0.25, 'Note: This figure uses synthetic data to illustrate expected qualitative improvements, as no actual results were obtained due to experimental failure.',
         transform=plt.gca().transAxes, fontsize=9, color='gray', ha='center', va='top')

plt.tight_layout()
plt.savefig('figure_2.png', dpi=300, bbox_inches='tight')
plt.close()
print("Saved figure_2.png")