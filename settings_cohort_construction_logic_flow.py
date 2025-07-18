import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

# Steps and coordinates for a circular layout
steps = [
    "Source Population",
    "Washout (365 days)",
    "First Exposure",
    "Covariate Extraction",
    "Propensity Score Estimation",
    "Stratification",
    "Outcome Model",
    "Effect Estimation"
]
theta = np.linspace(0, 2 * np.pi, len(steps), endpoint=False)
r = 3  # Radius
coords = [(r * np.cos(t), r * np.sin(t)) for t in theta]

fig, ax = plt.subplots(figsize=(8,8))
for (label, (x, y)) in zip(steps, coords):
    e = Ellipse((x, y), width=2.6, height=1.3, edgecolor='black', facecolor='none', lw=2)
    ax.add_patch(e)
    ax.text(x, y, label, ha='center', va='center', fontsize=11)

# Draw arrows
for i in range(len(coords)):
    start = coords[i]
    end = coords[(i + 1) % len(coords)]
    ax.annotate("", xy=end, xytext=start, arrowprops=dict(arrowstyle="->", lw=2))

ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.axis('off')
plt.title("Cohort Construction Logic Flow", fontsize=14)
plt.tight_layout()
plt.show()
