import pandas as pd
import matplotlib.pyplot as plt

# Example parameter summary table
parameters = {
    'Parameter': [
        'Washout Period', 'First Exposure Only', 'Prior Outcome Lookback', 'Min Days at Risk',
        'Caliper', 'Number of PS Strata', 'Outcome Model Type', 'PS Model Prior', 'Max Cohort Size'
    ],
    'Value': [
        365, True, 365, 1,
        0.2, 4, 'Cox', 'Laplace', 50000
    ],
    'Interpretation/Role': [
        'Ensures new user design',
        'Removes multiple exposures per subject',
        'Excludes subjects with prior outcome',
        'Defines risk window length',
        'PS matching threshold',
        'Number of strata for stratification',
        'Specifies time-to-event outcome model',
        'Regularization method for PS model',
        'Limits fitting to N subjects'
    ]
}
df = pd.DataFrame(parameters)

fig, ax = plt.subplots(figsize=(10, 2.5))
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(11)
table.auto_set_column_width(col=list(range(len(df.columns))))
plt.title('Parameter Summary Table', fontsize=14, pad=20)
plt.tight_layout()
plt.show()
