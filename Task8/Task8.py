import argparse
import numpy as np

def calculate_statistics(file_path):
    """ it reads a text file containing numbers and calculates various statistical 
    parameters using NumPy.
    """
    try:
        # open and read the file
        with open(file_path, 'r') as file:
            data=[]
            for line in file:
                if line and not line.isspace():
                    data.append(float(line))
        
        if not data:
            print("Error: The file is empty or contains no valid numbers.")
            return

        # convert list to NumPy array
        data_array = np.array(data)

        # calculate parameters
        mean_val = np.mean(data_array)
        median_val = np.median(data_array)
        max_val = np.max(data_array)
        min_val = np.min(data_array)
        std_dev = np.std(data_array)
        
        p99 = np.percentile(data_array, 99)
        p99_9 = np.percentile(data_array, 99.9)
        p99_99 = np.percentile(data_array, 99.99)
        p99_999 = np.percentile(data_array, 99.999)

        # 4. Print and write results
        output_string = (
            f"\nStatistics for {file_path}\n\n"
            f"Mean:         {mean_val:.4f}\n"
            f"Median:       {median_val:.4f}\n"
            f"Max:          {max_val:.4f}\n"
            f"Min:          {min_val:.4f}\n"
            f"Standard Deviation:  {std_dev:.4f}\n"
            f"99th Percentile:     {p99:.4f}\n"
            f"99.9th Percentile:   {p99_9:.4f}\n"
            f"99.99th Percentile:  {p99_99:.4f}\n"
            f"99.999th Percentile: {p99_999:.4f}\n"
        )
        
        # Print to terminal
        print(output_string)
        
        # Write to file
        with open("output.txt", "w") as file:
            file.write(output_string)

    # 5. Error Handling
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please check the path.")
    except ValueError:
        print("Error: The file contains invalid (non-numeric) data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":

    #initialize argumentParser object with description
    parser = argparse.ArgumentParser(description="This script calculcates statistical parameters of the text file of numbers.")

    # add argument rules
    parser.add_argument("file_path", type=str, help="path to the input text file containing numbers")

    # parse the arguments from terminal
    arguments = parser.parse_args()

    calculate_statistics(arguments.file_path)