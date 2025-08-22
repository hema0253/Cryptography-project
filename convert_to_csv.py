import pandas as pd

# Download file paths
data_path = "dataset\KDDTrain+.txt"
column_path = "dataset\KDDFeatureNames.txt"

# Load column names
with open(column_path) as f:
    columns = [line.strip().split(":")[0] for line in f.readlines()]
columns.append("label")  # Add the final target column

# Load data
df = pd.read_csv(data_path, names=columns)

# Save as CSV
df.to_csv("dataset/KDDTrain+.csv", index=False)
print("CSV file saved successfully.")
