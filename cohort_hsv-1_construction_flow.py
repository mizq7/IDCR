import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.patches import FancyArrowPatch

def draw_node(ax, xy, text, width=2.8, height=0.55):
    x, y = xy
    # Ellipse box for each node
    box = FancyBboxPatch((x - width/2, y - height/2), width, height,
                         boxstyle="round,pad=0.12", linewidth=2, edgecolor="black", facecolor="white")
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=11, wrap=True)

def draw_arrow(ax, xy_start, xy_end):
    ax.annotate('', xy=xy_end, xytext=xy_start,
                arrowprops=dict(arrowstyle='->', lw=2, color='black'))

# Set up the figure
fig, ax = plt.subplots(figsize=(4, 8))
ax.set_xlim(0, 4)
ax.set_ylim(0, 10)
ax.axis('off')

# Node positions (vertical flow)
nodes = [
    (2, 9, "All patients in database"),
    (2, 8, "Step 1\nObservation window:\n2010-01-01 to 2024-12-31"),
    (2, 7, "Step 2\n≥365 days prior observation"),
    (2, 6, "Step 3\nExclude: Any HIV diagnosis\n(prior 1 year)"),
    (2, 5, "Step 4\nExclude: Any other infection\n(prior 1 year)"),
    (2, 4, "Step 5\nExclude: Any transplant status\n(prior 90 days)"),
    (2, 3, "Step 6\nFirst qualifying HSV-1 diagnosis\n(code set)"),
    (2, 2, "Step 7\nCollapse to first event/era\n(optional)"),
    (2, 1, "Final analytic cohort")
]

# Draw nodes
for x, y, text in nodes:
    draw_node(ax, (x, y), text)

# Draw arrows
for i in range(len(nodes)-1):
    draw_arrow(ax, (nodes[i][0], nodes[i][1] - 0.3), (nodes[i+1][0], nodes[i+1][1] + 0.3))

plt.tight_layout()
plt.show()
