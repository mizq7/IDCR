import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 13))
ax.set_xlim(0, 12)
ax.set_ylim(0, 16)
ax.axis('off')

box_width = 4.0
box_height = 1.7
x_left = 1.0
x_right = 6.5  # Shift right box a bit farther for longer arrows

main_boxes = [
    "Exposed:\nTarget: n = 6900\nComparator: n = 450628",
    "First exp. only & 365 days of\nobs. prior",
    "No prior outcome",
    "Have at least 1 days at risk",
    "Study population:\nTarget: n = 6274\nComparator: n = 379975"
]
right_boxes = [
    "Target: n = 0\nComparator: n = 0",
    "Target: n = 227\nComparator: n = 4421",
    "Target: n = 399\nComparator: n = 66232"
]

main_y = [13.5, 10.5, 7.5, 4.5, 1.5]
right_y = [10.5, 7.5, 4.5]

# Draw left (main) boxes
for i, (text, y) in enumerate(zip(main_boxes, main_y)):
    rect = patches.FancyBboxPatch((x_left, y), box_width, box_height,
                                  boxstyle="round,pad=0.04", linewidth=2,
                                  edgecolor='black', facecolor='white', zorder=2)
    ax.add_patch(rect)
    ax.text(x_left + box_width/2, y + box_height/2, text, ha='center', va='center',
            fontsize=14, color='black', zorder=3)

# Draw right-side boxes
for i, (text, y) in enumerate(zip(right_boxes, right_y)):
    rect = patches.FancyBboxPatch((x_right, y), box_width, box_height,
                                  boxstyle="round,pad=0.04", linewidth=2,
                                  edgecolor='black', facecolor='white', zorder=2)
    ax.add_patch(rect)
    ax.text(x_right + box_width/2, y + box_height/2, text, ha='center', va='center',
            fontsize=14, color='black', zorder=3)

# Vertical arrows and "Y" immediately next to arrow, in italic
for i in range(len(main_y)-1):
    x_arrow = x_left + box_width/2
    y_start = main_y[i]
    y_end = main_y[i+1] + box_height
    ax.annotate('', xy=(x_arrow, y_end), xytext=(x_arrow, y_start),
                arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=2), zorder=3)
    # Place 'Y' in italic, close to the arrow tip
    ax.text(x_arrow + 0.22, (y_start + y_end) / 2, 'Y', fontsize=16, fontweight='bold',
            fontstyle='italic', va='center', ha='left', zorder=4)

# Longer horizontal arrows and "N" in italic below the arrow
for i in range(3):
    y_level = right_y[i] + box_height/2
    x_start = x_left + box_width
    x_end = x_right
    # Longer arrow (adjust x_end farther to the right if needed)
    ax.annotate('', xy=(x_end, y_level), xytext=(x_start, y_level),
                arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=2), zorder=3)
    # 'N' italic below the middle of the horizontal arrow
    ax.text((x_start + x_end) / 2, y_level - 0.48, 'N', fontsize=16, fontweight='bold',
            fontstyle='italic', ha='center', va='top', zorder=4)

plt.tight_layout()
plt.show()
