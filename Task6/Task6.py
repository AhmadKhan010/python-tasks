import calculations
import matplotlib.pyplot as plt
import sys

file_name = "data.txt"

# create and write to file safely
try:
    with open(file_name, 'w') as file:
        file.write("1,2,3,4,5,6,7,8,9,10")
except IOError as e:
    print(f"File writing error: Cannot write to {file_name}. Details: {e}")
    sys.exit(1)  # exit script safely


# read file and parse data 
try:
    with open(file_name, 'r') as file:
        text = file.read()
    
    # convert string type to int
    numbers = [int(num) for num in text.split(',')]

except FileNotFoundError:
    print(f"Error: The file {file_name} was not found.")
    sys.exit(1)
except ValueError as e:
    print(f"Data parsing error: The file contains non-integer values. Details: {e}")
    sys.exit(1)
except IOError as e:
    print(f"File reading error: Details: {e}")
    sys.exit(1)

# perform calculations
squares = calculations.get_squares(numbers)
cubes = calculations.get_cubes(numbers)

# we proceed to plot only if both lists successfully populated
if squares and cubes:
    try:
        plt.figure(figsize=(8, 5))
        plt.plot(squares, cubes, marker='o', color='purple', linestyle='-', linewidth=2)

        plt.title("Relationship Between Squares and Cubes")
        plt.xlabel("Squares (x-axis)")
        plt.ylabel("Cubes (y-axis)")
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"An unexpected error occurred during plotting: {e}")
else:
    print("Plotting skipped due to calculation errors.")