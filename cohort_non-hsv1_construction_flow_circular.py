import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch

# Step text from your logic, matching JSON/ATLAS logic for non-hsv1 cohort
steps = [
    "All patients in database",
    "Step 1\nObservation window:\n2010-01-01 to 2024-12-31",
    "Step 2\n≥365 days prior observation",
    "Step 3\nExclude: Any HIV diagnosis\n(prior 1 year)",
    "Step 4\nExclude: Any other infection\n(prior 1 year)",
    "Step 5\nExclude: Any transplant status\n(prior 90 days)",
    "Step 6\nFirst qualifying HSV-1 diagnosis\n(code set)",
    "Step 7\nCollapse to first event/era\n(optional)",
    "Final analytic cohort"
]

# Positioning for vertical flow
n = len(steps)
fig, ax = plt.subplots(figsize=(5, 10))
ax.set_xlim(-2, 2)
ax.set_ylim(-1, n * 2)
ax.axis('off')

ellipse_width = 2.6
ellipse_height = 0.9
y_positions = list(reversed(range(n)))

# Draw ellipses and text
for i, (text, y) in enumerate(zip(steps, y_positions)):
    ellipse = Ellipse((0, y * 2), width=ellipse_width, height=ellipse_height,
                      edgecolor='black', facecolor='white', lw=2)
    ax.add_patch(ellipse)
    ax.text(0, y * 2, text, ha='center', va='center', fontsize=10, fontweight='bold' if i == 0 or i == n-1 else 'normal')
    # Draw arrow except after last ellipse
    if i < n - 1:
        arrow = FancyArrowPatch((0, y * 2 - ellipse_height / 2 + 0.05), (0, (y - 1) * 2 + ellipse_height / 2 - 0.05),
                                arrowstyle='->', mutation_scale=18, lw=2, color='black')
        ax.add_patch(arrow)

plt.tight_layout()
plt.show()
