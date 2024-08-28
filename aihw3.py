import pandas as pd

# Load the data
f = pd.read_csv('ed1.csv')

# Replace 'n.p.' with 0 and convert the Count column to numeric
f['Count'] = pd.to_numeric(f['Count'].replace('n.p.', 0), errors='coerce')

# Filter for NSW jurisdiction and SA4 names containing 'Sydney'
nsw_data = f[(f['Jurisdiction'] == 'NSW') & (f['SA4 name'].str.contains('Sydney', case=False))]

# Group by SA4 name and Condition group and sum the counts
grouped_nsw = nsw_data.groupby(['SA4 name', 'Condition group'])['Count'].sum().reset_index()

# Find the top 3 conditions by count for each SA4 name
top_3_conditions = grouped_nsw.groupby('SA4 name').apply(lambda x: x.nlargest(3, 'Count')).reset_index(drop=True)

# Print the top 3 conditions for each SA4 name containing 'Sydney'
print(top_3_conditions[['SA4 name', 'Condition group', 'Count']])