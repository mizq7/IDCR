import matplotlib.pyplot as plt
import networkx as nx

# Define the steps and the flow
steps = [
    "Cohort Selection",
    "Covariate Extraction",
    "Propensity Score Modeling",
    "Stratification / Matching / Trimming",
    "Outcome Modeling"
]

# Create a directed graph
G = nx.DiGraph()
for i in range(len(steps) - 1):
    G.add_edge(steps[i], steps[i+1])

pos = nx.spring_layout(G, seed=42)  # Fixed for reproducibility
plt.figure(figsize=(10, 3))
nx.draw(
    G, pos, with_labels=True,
    node_size=6000, node_color='white',
    font_size=12, edge_color='black', linewidths=2
)
plt.title("Analytic Workflow Diagram", fontsize=14)
plt.axis('off')
plt.tight_layout()
plt.show()
