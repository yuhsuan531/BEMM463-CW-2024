import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the Excel file
file_path = r"https://github.com/yuhsuan531/BEMM463-CW-2024/raw/main/Advertising%20Placement%20Data.xlsx"  
df = pd.read_excel(file_path)

# Check the structure and content of the DataFrame
print("DataFrame information:")
print(df.info())

# Perform linear regression
X = df[['Facebook', 'Instagram']]  # Independent variables (advertising impressions)
y = df['total_weekly_sales']  # Dependent variable (total weekly product sales)

# Add constant term for intercept
X = sm.add_constant(X)

# Fit the linear regression model
model = sm.OLS(y, X).fit()

# Print the regression results
print("\nRegression results:")
print(model.summary())

import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Facebook', y='total_weekly_sales', data=df, label='Facebook')
sns.scatterplot(x='Instagram', y='total_weekly_sales', data=df, label='Instagram')

# Add labels and title
plt.xlabel('Advertising Impressions')
plt.ylabel('Total Weekly Product Sales')
plt.title('Relationship between Advertising Impressions and Sales')

# Optionally, add a regression line
sns.regplot(x='Facebook', y='total_weekly_sales', data=df, scatter=False, label='Facebook Regression Line')
sns.regplot(x='Instagram', y='total_weekly_sales', data=df, scatter=False, label='Instagram Regression Line')

# Add legend
plt.legend()

# Show plot
plt.show()
