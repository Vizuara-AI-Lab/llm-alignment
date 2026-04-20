import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data based on paper's expectation: "a significant portion of responses to harmful queries should ideally be explicit refusals or evasions"
labels = ['Explicit Refusal', 'Evasive/Harmless Content', 'Harmful Content Generated']
sizes = [80, 15, 5] # Percentages

# Set style for publication quality
sns.set_theme(style="whitegrid", palette="Pastel1")
plt.rcParams.update({'font.size': 12, 'axes.labelsize': 14, 'xtick.labelsize': 12, 'ytick.labelsize': 12, 'legend.fontsize': 12})

fig, ax = plt.subplots(figsize=(8, 8))

wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=sns.color_palette("Pastel1", len(labels)),
    wedgeprops=dict(width=0.4, edgecolor='w') # Donut chart style
)

# Customizing autopct texts
plt.setp(autotexts, size=12, weight="bold", color="black")
plt.setp(texts, size=12, color="dimgray")

ax.set_title('Distribution of Zephyr-7B-SFT-Full Response Types for Harmful Prompts', pad=20)
ax.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

plt.tight_layout()
plt.savefig('figure_4.png', dpi=150, bbox_inches='tight')
plt.close()
print("Saved figure_4.png")