import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Define colors for each flavor
colors = {'Vanilla': 'khaki', 'Chocolate': 'brown', 'Matcha': 'mediumseagreen'}

# Create a custom colormap
cmap = ListedColormap(list(colors.values()))

# Generate synthetic data for Q1: Preference for Flavor
choices_q1 = ['Vanilla', 'Chocolate', 'Matcha']
q1_data = pd.DataFrame(np.random.choice(choices_q1, size=100), columns=['Q1'])

# Generate synthetic data for Q2: Taste Preference
q2_data = pd.DataFrame(np.random.choice(choices_q1, size=(100, 3), replace=True), columns=['1st Choice', '2nd Choice', '3rd Choice'])

# Generate synthetic data for Q3: Degree of Preference
q3_data = pd.DataFrame(np.random.randint(1, 11, size=(100, 3)), columns=['Vanilla', 'Chocolate', 'Matcha'])

# Visualize Q1: Preference for Flavor using a bar plot
fig, ax = plt.subplots(figsize=(6, 4))
q1_data['Q1'].value_counts().plot(kind='bar', ax=ax, color='skyblue')
ax.set_xlabel('Flavour')
ax.set_ylabel('Frequency')
ax.set_title('Preference for Flavour (Q1)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Sort the dictionary keys and get the values in the sorted order
sorted_colors = {k: v for k, v in sorted(colors.items(), key=lambda item: item[0])}

# Visualize Q2: Taste Preference using a stacked bar plot with specified colors
fig, ax = plt.subplots(figsize=(6, 4))

# Count the occurrences of each flavor in the entire DataFrame
counts = q2_data.apply(pd.Series.value_counts).fillna(0)

# Plot the stacked bar chart with specified colors
counts.T.plot(kind='bar', stacked=True, ax=ax, color=[sorted_colors[i] for i in sorted_colors])

ax.set_xlabel(' ')
ax.set_ylabel('Frequency')
ax.set_title('Taste Preference (Q2)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Visualize Q3: Degree of Preference using a box plot
fig, ax = plt.subplots(figsize=(6, 4))
q3_data.plot(kind='box', ax=ax)
ax.set_xlabel(' ')
ax.set_ylabel('Degree of Preference')
ax.set_title('Degree of Preference (Q3)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()