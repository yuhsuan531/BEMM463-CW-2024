import pandas as pd
import random
import matplotlib.pyplot as plt

# Create a DataFrame for the product profiles
products = {
    'Product Name': ['Power Pro Max', 'Eco-Cleaner Plus', 'Turbo Sweep Elite'],
    'Suction Power': [10, 8, 9],
    'Price': ['High', 'Low', 'Moderate'],
    'Weight': ['Lightweight', 'Ultra-light', 'Moderate'],
    'Function': ['Multi-surface cleaning, pet hair removal, advanced filtration',
                 'Energy-efficient, versatile attachments, suitable for small spaces',
                 'Turbo boost mode, large dustbin capacity, smart navigation technology']
}

product_df = pd.DataFrame(products)

# Generate 1000 survey takers to rank the products
survey_results = []
for _ in range(1000):
    survey_results.append(random.sample(products['Product Name'], k=3))

# Create a DataFrame for survey results
survey_df = pd.DataFrame(survey_results, columns=['1st Choice', '2nd Choice', '3rd Choice'])

# Count the number of times each product was ranked as 1st, 2nd, or 3rd
ranking_counts = {
    'Product Name': products['Product Name'],
    '1st Choice': [survey_df['1st Choice'].value_counts()[product] for product in products['Product Name']],
    '2nd Choice': [survey_df['2nd Choice'].value_counts()[product] for product in products['Product Name']],
    '3rd Choice': [survey_df['3rd Choice'].value_counts()[product] for product in products['Product Name']]
}

ranking_df = pd.DataFrame(ranking_counts)

# Calculate percentage of votes for each product in each ranking category
total_votes = len(survey_df)
ranking_df['1st Choice (%)'] = (ranking_df['1st Choice'] / total_votes) * 100
ranking_df['2nd Choice (%)'] = (ranking_df['2nd Choice'] / total_votes) * 100
ranking_df['3rd Choice (%)'] = (ranking_df['3rd Choice'] / total_votes) * 100

# Plot the survey results with percentage labels
plt.figure(figsize=(10, 6))
plt.barh(ranking_df['Product Name'], ranking_df['1st Choice'], color='lightblue', label='1st Choice')
plt.barh(ranking_df['Product Name'], ranking_df['2nd Choice'], left=ranking_df['1st Choice'], color='lightgreen', label='2nd Choice')
plt.barh(ranking_df['Product Name'], ranking_df['3rd Choice'], left=ranking_df['1st Choice']+ranking_df['2nd Choice'], color='orange', label='3rd Choice')

# Annotate bars with percentage labels at the center of each section
for index, value in enumerate(ranking_df['1st Choice']):
    plt.text(value / 2, index, f'{ranking_df["1st Choice (%)"][index]:.2f}%', ha='center', va='center', fontsize=15)
for index, value in enumerate(ranking_df['2nd Choice']):
    plt.text(value / 2 + ranking_df['1st Choice'][index], index, f'{ranking_df["2nd Choice (%)"][index]:.2f}%', ha='center', va='center', fontsize=15)
for index, value in enumerate(ranking_df['3rd Choice']):
    plt.text(value / 2 + ranking_df['1st Choice'][index] + ranking_df['2nd Choice'][index], index, f'{ranking_df["3rd Choice (%)"][index]:.2f}%', ha='center', va='center', fontsize=15)

plt.xlabel('Number of Votes', fontsize=15)
plt.ylabel('Product Name', fontsize=15)
plt.title('Survey Results', fontsize=15)
plt.xticks(fontsize=15)  # Adjust font size for x ticks
plt.yticks(fontsize=13)  # Adjust font size for y ticks
plt.legend()
plt.show()

# Display the product comparison table
print("Product Comparison Table:")
print(product_df)
