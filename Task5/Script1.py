import os
import subprocess

file_path = "dummy_file.txt"

# check if the file exists. if not, create it and add text.
if not os.path.exists(file_path):
    with open(file_path, "w") as file:
        file.write("Hello world! This is the initial text in the dummy file.\n")
    print("1: File created and initial text added.\n")
else:
    print("1: File already exists.\n")

# run the bash command to strip all permissions from the file
print("2: Removing file permissions with chmod a=- commands.\n")
subprocess.run(["chmod", "a=-", file_path])

# try to read the file and identify the issue
print("3: Attempting to read the file. \n")
try:
    with open(file_path, "r") as file:
        print(file.read())

except PermissionError as e:
    print(f"ISSUE: The OS blocked Python from opening the file.")
    print(f"Exact Python Error: {e}")