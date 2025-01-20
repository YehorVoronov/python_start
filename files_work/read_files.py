# 8:42:00

import json
import csv
import os

file_path = "files_work/file_detection.txt"
file_path_json = "files_work/file_detection.json"
file_path_csv = "files_work/file_detection.csv"

# txt
# if os.path.exists(file_path):
#     with open(file_path, mode="r") as file:
        
#         print(f"Content: {file.read()}")
# else:
#     print("File does not exists") 

# json
# with open(file_path_json, "r") as file:
#     content = json.load(file)
#     print(f"json: {content}")
    
#     print(f"name: {content['age']}")

# csv
with open(file_path_csv, "r") as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        print(f"{line}")