import pandas as pd
import matplotlib.pyplot as plt

# Load Excel data
file_path = 'comparisonExchange.xlsx'
sheet_name = 'Sheet1'  # Change to the name of the sheet containing your data
df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl', header=None)

#extract program names
program_names = df.iloc[0, 1:].dropna().values

# Process data
data = []
file_sizes = []
file_types = []
for i, row in df.iterrows():
    if i == 0:
        continue
    if isinstance(row[0], str):
        current_file_type = row[0]
        file_types.append(current_file_type)
    else:
        file_sizes.append(row[0])
        data.append(row[1:].dropna().str.split(', ').apply(lambda x: [int(x[0].split(': ')[1]), int(x[1].split(': ')[1])]).tolist())

# Create graphs
for file_type_idx, file_type in enumerate(file_types):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle(file_type.capitalize())
    for program_idx, program_name in enumerate(program_names):
        data_by_program = data[file_type_idx::len(file_types)][program_idx::len(program_names)]
        comparisons = [entry[0] for entry in data_by_program]
        exchanges = [entry[1] for entry in data_by_program]

        if len(file_sizes) == len(comparisons) and len(file_sizes) == len(exchanges):
            ax1.plot(file_sizes, comparisons, label=program_name)
            ax2.plot(file_sizes, exchanges, label=program_name)
        else:
            print(f"Error: file_sizes, comparisons, and exchanges lengths don't match for {program_name}")

    ax1.set_title('Comparisons')
    ax1.set_xlabel('File size')
    ax1.set_ylabel('Number of comparisons')
    ax1.legend()

    ax2.set_title('Exchanges')
    ax2.set_xlabel('File size')
    ax2.set_ylabel('Number of exchanges')
    ax2.legend()

    plt.tight_layout()
    plt.savefig(f"{file_type}_graph.png")

plt.show()
