# import os

# # List of folder names to extract data for
# # folders = ["firstItemPivotOutput", "median3Output", "MergeSortOutput", "quickSort50_output", "quickSort100Output"]
# folders = ["MergeSortOutput"]

# # Get the current directory
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # Iterate over the folders in the current directory
# for folder_name in folders:
#     # Create an empty dictionary to store data for this folder
#     folder_data = {}

#     # Iterate over the .dat files in this folder
#     for filename in os.listdir(folder_name):
#         if filename.endswith(".dat"):
#             # Extract the comparisons and exchanges data
#             with open(os.path.join(folder_name, filename)) as f:
#                 lines = f.readlines()[-10:]  # Read the last 10 lines of the file
#                 comparisons = None
#                 exchanges = None
#                 for line in lines:
#                     if "Comparisons:" in line:
#                         comparisons = int(line.split(":")[1].split(",")[0])
#                     elif "Exchanges:" in line:
#                         exchanges = int(line.split(":")[1])
#                     if comparisons is not None and exchanges is not None:
#                         break  # Stop searching if both values have been found
                
#                 if comparisons is not None and exchanges is not None:
#                     # Add data to the folder_data dictionary
#                     folder_data[filename] = {"comparisons": comparisons, "exchanges": exchanges}
    
#     # Create the output file path
#     output_file_path = os.path.join(current_dir, f"{folder_name}_output.txt")

#     # Write the extracted data for this folder to a file
#     with open(output_file_path, "w") as f:
#         for filename, data in folder_data.items():
#             f.write(f"{filename}:\n")
#             f.write(f"\tComparisons: {data['comparisons']}\n")
#             f.write(f"\tExchanges: {data['exchanges']}\n")
import os
import pandas as pd

folders = ["firstItemPivotOutput", "median3Output", "MergeSortOutput", "quickSort50_output", "quickSort100Output"]

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

folders_to_process = folders
data = []

print(f"Processing folders: {folders_to_process}")
for folder in folders_to_process:
    data.extend(process_folder(folder))

df = pd.DataFrame(data)

df = df[df["size"] != 0]

if not df.empty:
    df = df.sort_values(by="size")
    print("\nData table:\n")
    print(df.to_string(index=False))
else:
    print("No valid data found.")
