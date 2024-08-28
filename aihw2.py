# import pandas as pd

# # Load the data
# f = pd.read_csv('ed1.csv')

# # Replace 'n.p.' with 0 and convert the Count column to numeric
# f['Count'] = pd.to_numeric(f['Count'].replace('n.p.', 0), errors='coerce')

# # Filter for NSW jurisdiction
# nsw_data = f[f['Jurisdiction'] == 'NSW']

# # Group by SA4 name and Condition group and sum the counts
# grouped_nsw = nsw_data.groupby(['SA4 name', 'Condition group'])['Count'].sum().reset_index()

# # Find the top 3 conditions by count for each SA4 name
# top_3_conditions = grouped_nsw.groupby('SA4 name').apply(lambda x: x.nlargest(3, 'Count')).reset_index(drop=True)

# # Print the top 3 conditions for each SA4 name
# print(top_3_conditions[['SA4 name', 'Condition group', 'Count']])

# # Define the file path for the output
# output_file = 'top_3_conditions.txt'

# # Write the top 3 conditions for each SA4 name to the text file
# with open(output_file, 'w') as file:
#     file.write(top_3_conditions[['SA4 name', 'Condition group', 'Count']].to_string(index=False))

# print(f"Top 3 conditions for each SA4 name have been written to {output_file}.")



import pandas as pd

# Load the data
f = pd.read_csv('ed1.csv')

# Replace 'n.p.' with 0 and convert the Count column to numeric
f['Crude rate'] = pd.to_numeric(f['Crude rate'].replace('n.p.', 0), errors='coerce')

# Filter for NSW jurisdiction
nsw_data = f[f['Jurisdiction'] == 'NSW']

# Group by SA4 name and Condition group and sum the counts
grouped_nsw = nsw_data.groupby(['SA4 name', 'Condition group'])['Crude rate'].sum().reset_index()

# Find the top 3 conditions by count for each SA4 name
top_3_conditions = grouped_nsw.groupby('SA4 name').apply(lambda x: x.nlargest(3, 'Crude rate')).reset_index(drop=True)

# Print the top 3 conditions for each SA4 name
print(top_3_conditions[['SA4 name', 'Condition group', 'Crude rate']])

# Define the file path for the output
output_file = 'top_3_conditions.txt'

# Write the top 3 conditions for each SA4 name to the text file
with open(output_file, 'w') as file:
    file.write(top_3_conditions[['SA4 name', 'Condition group', 'Crude rate']].to_string(index=False))

print(f"Top 3 conditions for each SA4 name have been written to {output_file}.")