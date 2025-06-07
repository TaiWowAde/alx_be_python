# File: create_fns_and_dsa_files.py
# Run this from the root of your project (e.g., alx_be_python)

import os

# Define the directory and file names
directory = "fns_and_dsa"
task_files = [
    "arithmetic_operations.py",
    "shopping_list_manager.py",
    "explore_datetime.py",
    "temp_conversion_tool.py"
]

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"Created directory: {directory}")
else:
    print(f"Directory already exists: {directory}")

# Create each file inside the directory
for file_name in task_files:
    file_path = os.path.join(directory, file_name)
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("# Auto-generated file for Functions, Data Structures and Modules project\n")
        print(f"Created file: {file_path}")
    else:
        print(f"File already exists: {file_path}")
