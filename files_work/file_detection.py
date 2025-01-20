#os module provide pyrhon opportunity to comunicate with operating system
import os
import json
import csv

file_path = "file_detection.txt"
file_path_json = "file_detection.json"
file_path_csv = "file_detection.csv"
txt_data = "I don't like milkshake"

# if os.path.exists(file_path):
#     try:
#     # 'with' will open the file and close it by itself 
#     # | "w"-write if the file already exist, 
#     # | "x" - will create a file and write,if the file already exist we will receive an error
#     # | "a" - append a file(add data to the file)
#     # | "r" - read a file 
#         with open(file=file_path, mode="a") as file:
#             file.write(txt_data+" new info")
#             print(f"text_data: {txt_data} written to file {file_path}")
#     except FileExistsError:
#         print("My Error: file already exists ")
# else:
#     print(" I don't see the file")    

# if os.path.isdir(file_path):
# if os.path.isfile(file_path):


# employees = ["Tom", "John", "Kris", "Cate"]

# try:
#     with open(file=file_path, mode="a") as file:
#         for index, employee in enumerate(employees):
#             file.write(f"employe {index}: {employee} \n")
#             print(f"employe {index}: {employee}")
# except Exception:
#     print("it is Error")
    
# employee = {
#     "name": "Bill",
#     "email": "bill@example.com",
#     "age":24
# }

# with open(file=file_path_json, mode="w") as file:
#     # json to string
#     json.dump(employee, file, indent=4)

#     # file.write(employee)
#     print("json was creted")


# .csv- comma separated values

employee = [["Name", "Age", "Job"], 
            ["Roman", 22, "CEO"], 
            ["John", 28, "CTO"],
            ["Ted", 25, "Manager"],
            ["Ran", 52, "Founder"],
            ["Bob", 42, "PR manager"]]

with open(file=file_path_csv, mode="w", newline="") as file:
    # creating csv file
    writer = csv.writer(file)
    for line in employee:
        writer.writerow(line)
