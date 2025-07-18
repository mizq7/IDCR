from graphviz import Digraph

# Create a directed graph
dot = Digraph(comment='Cohort Construction Logic', format='png')

# Nodes
dot.node('A', 'All patients in database')
dot.node('B', 'Observation window:\n2010-01-01 to 2024-12-31')
dot.node('C', '≥365 days prior observation')
dot.node('D', 'First qualifying\ndiagnosis of cognitive\ncondition (code set)')
dot.node('E', 'Collapse to first event/era\n(optional)')
dot.node('F', 'Final analytic cohort')

# Edges
dot.edge('A', 'B', label='Step 1')
dot.edge('B', 'C', label='Step 2')
dot.edge('C', 'D', label='Step 3')
dot.edge('D', 'E', label='Step 4')
dot.edge('E', 'F', label='Step 5')

# For a simple flow (if collapse step is always included)
# If collapse is optional, you could add a direct edge from D to F as well:
# dot.edge('D', 'F', label='If not collapsing events')

# Render the diagram to file and display it in the notebook (optional)
dot.render('cohort_construction_flow', view=True)

# Display as SVG in Jupyter Notebook (optional)
# from IPython.display import display, SVG
# display(SVG(dot.pipe(format='svg')))
