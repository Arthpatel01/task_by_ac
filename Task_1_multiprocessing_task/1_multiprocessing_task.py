import os
import zipfile
import pandas as pd

zip_folder = os.path.join(".\\Que1\\")

combined_data = pd.DataFrame()

print('------------Process Start ---->>>')
for filename in os.listdir(zip_folder):
    if filename.endswith(".zip"):
        with zipfile.ZipFile(os.path.join(zip_folder, filename), "r") as zip_file:
            csv_files = [file for file in zip_file.namelist() if
                         file.endswith(".csv") and "60d_DAM_PTPObligationBidAwards" in file]

            for csv_file in csv_files:
                print(f'processing the file: {csv_file}')
                with zip_file.open(csv_file) as file:
                    df = pd.read_csv(file)

                    combined_data = pd.concat([combined_data, df], ignore_index=True)

output_csv_file = "task_1_combined_data.csv"

combined_data.to_csv(output_csv_file, index=False)

print(f"Combined data written to {output_csv_file}")
