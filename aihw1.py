# import pandas as pd

# # Load the data
# f = pd.read_csv('ed2.csv')

# # Replace 'n.p.' with 0 and convert the Count column to numeric
# f['Count'] = pd.to_numeric(f['Count'].replace('n.p.', 0), errors='coerce')

# # Group by Jurisdiction and Condition group and sum the counts
# grouped = f.groupby(['Jurisdiction', 'Condition group'])['Count'].sum().reset_index()

# # Find the condition with the maximum count for each Jurisdiction
# max_conditions = grouped.loc[grouped.groupby('Jurisdiction')['Count'].idxmax()]

# # Find the condition with the least count for each Jurisdiction
# min_conditions = grouped.loc[grouped.groupby('Jurisdiction')['Count'].idxmin()]

# # Combine both results
# result = pd.concat([max_conditions, min_conditions], keys=['Max', 'Min']).reset_index(level=0).rename(columns={'level_0': 'Type'})

# # Print the results
# print(result[['Jurisdiction', 'Type', 'Condition group', 'Count']])

# import pandas as pd

# # Load the data
# f = pd.read_csv('ed2.csv')

# # Replace 'n.p.' with 0 and convert the Count column to numeric
# f['Count'] = pd.to_numeric(f['Count'].replace('n.p.', 0), errors='coerce')

# # Group by Jurisdiction and Condition group and sum the counts
# grouped = f.groupby(['Jurisdiction', 'Condition group'])['Count'].sum().reset_index()

# # Sort by Jurisdiction and Count, then find the top 3 conditions per jurisdiction
# top_conditions = grouped.sort_values(['Jurisdiction', 'Count'], ascending=[True, False]).groupby('Jurisdiction').head(3)

# # Identify the top condition across all jurisdictions
# top_condition = top_conditions.groupby('Jurisdiction').first().reset_index()

# # Find the 3 jurisdictions with the highest counts for this top condition
# top_jurisdictions = top_condition.sort_values('Count', ascending=False).head(3)

# # Print the results
# print("Top 3 conditions per jurisdiction:")
# print(top_conditions[['Jurisdiction', 'Condition group', 'Count']])

# print("\nTop 3 jurisdictions with the highest count for the top condition:")
# print(top_jurisdictions[['Jurisdiction', 'Condition group', 'Count']])

# import pandas as pd

# # Load the data
# f = pd.read_csv('ed1.csv')

# # Replace 'n.p.' with 0 and convert the Count column to numeric
# f['Count'] = pd.to_numeric(f['Count'].replace('n.p.', 0), errors='coerce')

# # Group by Condition group and sum the counts across all jurisdictions
# condition_totals = f.groupby('Condition group')['Count'].sum().reset_index()

# # Find the top 3 conditions with the highest counts
# top_3_conditions = condition_totals.sort_values('Count', ascending=False).head(3)

# # Print the top 3 conditions
# print("Top 3 conditions overall:")
# print(top_3_conditions)

# # Now find the SA4 areas with the highest counts for the top condition
# top_condition = top_3_conditions.iloc[0]['Condition group']

# # Filter the original data for the top condition and group by SA4 area
# sa4_totals = f[f['Condition group'] == top_condition].groupby('SA4 name')['Count'].sum().reset_index()

# # Find the top 6 SA4 areas with the highest counts for the top condition
# top_6_sa4_areas = sa4_totals.sort_values('Count', ascending=False).head(6)

# # Print the top 6 SA4 areas
# print(f"\nTop 6 SA4 areas for the top condition '{top_condition}':")
# print(top_6_sa4_areas)

import pandas as pd

# Load the data
f = pd.read_csv('ed1.csv')

# Replace 'n.p.' with 0 and convert the Count column to numeric
f['Count'] = pd.to_numeric(f['Count'].replace('n.p.', 0), errors='coerce')

# Group by Condition group and sum the counts across all jurisdictions
condition_totals = f.groupby('Condition group')['Count'].sum().reset_index()

# Find the top 3 conditions with the highest counts
top_3_conditions = condition_totals.sort_values('Count', ascending=False).head(3)

# Now find the SA4 areas with the highest counts for the top condition
top_condition = top_3_conditions.iloc[0]['Condition group']

# Filter the original data for the top condition and group by SA4 area
sa4_totals = f[f['Condition group'] == top_condition].groupby('SA4 name')['Count'].sum().reset_index()

# Find the top 6 SA4 areas with the highest counts for the top condition
top_6_sa4_areas = sa4_totals.sort_values('Count', ascending=False).head(6)

# Print the results to a text file
with open('results.txt', 'w') as file:
    # Top 3 conditions overall
    file.write("Top 3 conditions overall:\n")
    file.write(top_3_conditions.to_string(index=False))
    file.write("\n\n")

    # Top 6 SA4 areas for the top condition
    file.write(f"Top 6 SA4 areas for the top condition '{top_condition}':\n")
    file.write(top_6_sa4_areas.to_string(index=False))
    file.write("\n")

print("Results have been written to 'results.txt'")
