import subprocess

file_path = "dummy_file.txt"

print("1: Resolving permissions using chmod u+rw  command. \n")
# give permission of read write to user
subprocess.run(["chmod", "u+rw", file_path])

print("2: Attempting to write and read again.  \n")
try:
    # try to append text in file
    with open(file_path, "a") as file:
        file.write("Successfully restored the permissions of the file and now writing to the file again.\n")

    print("3. Succesfully wrote to the file.\n")
    # Read the whole file text 
    with open(file_path, "r") as file:
        print("Current File Contents:\n")
        print(file.read())
        print()
    
    print("4. Succesfully read from the file.\n")
except Exception as e:
    print(f"Something went wrong: {e}")