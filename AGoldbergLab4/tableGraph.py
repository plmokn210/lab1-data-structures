import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

input_folder = "quickSort50_output/"

def process_file(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()

        if len(lines) != 2:
            print(f"Skipping file {os.path.basename(filepath)} due to incorrect format.")
            return None

        comparisons_line = lines[0].strip()
        exchanges_line = lines[1].strip()

        if not (comparisons_line.startswith("Comparisons:") and exchanges_line.startswith("Exchanges:")):
            print(f"Skipping file {os.path.basename(filepath)} due to incorrect format.")
            return None

        comparisons = int(comparisons_line.split(":")[1].strip())
        exchanges = int(exchanges_line.split(":")[1].strip())

        size = int(filepath.split("Output")[-1].split(".")[0][3:])

        return {"size": size, "comparisons": comparisons, "exchanges": exchanges}

def process_folder(folder_path):
    data = []

    print(f"Processing folder: {folder_path}")
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)

        if os.path.isfile(filepath):
            print(f"Processing file: {filename}")
            file_data = process_file(filepath)
            if file_data is not None:
                data.append(file_data)

    return data

folders_to_process = [input_folder]
data = []

print(f"Processing folders: {folders_to_process}")
for folder in folders_to_process:
    data.extend(process_folder(folder))

df = pd.DataFrame(data)

df = df[df["size"] != 0]

if not df.empty:
    plt.figure()
    sns.scatterplot(data=df, x="size", y="comparisons", label="Comparisons")
    sns.scatterplot(data=df, x="size", y="exchanges", label="Exchanges")
    plt.legend()
    plt.show()
else:
    print("No valid data found.")
