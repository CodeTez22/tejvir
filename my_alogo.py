import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the log data
log_file_path = 'HealthApp/HealthApp_2k.log_structured.csv'
log_df = pd.read_csv(log_file_path)

# Read the event templates
templates_file_path = 'HealthApp/HealthApp_2k.log_templates.csv'
templates_df = pd.read_csv(templates_file_path)

# Merge the log data with the event templates based on EventId
merged_df = pd.merge(log_df, templates_df, on='EventId', how='left')

# Convert 'Time' column to datetime format
merged_df['Time'] = pd.to_datetime(merged_df['Time'], format='%Y%m%d-%H:%M:%S:%f')

# Display the DataFrame
print(merged_df)

# Visualize events over time
plt.figure(figsize=(14, 8))
sns.scatterplot(x='Time', y='EventId', hue='Component', palette='viridis', data=merged_df, markers=True, s=100)
plt.title('Events Over Time Categorized by Component and EventId with EventTemplate')
plt.xlabel('Time')
plt.ylabel('EventId')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
