import json

try:
    # read the data from the given json file
    with open('input.json', 'r') as file:
        input_data=json.load(file)

    # an empty dictionary to store updated grouped data
    grouped_data = {}

    # iterate through each person in the list 
    for person in input_data:
        job = person["occupation"]
        
        # if current job is not in grouped data, than create it's empty list
        if job not in grouped_data:
            grouped_data[job] = []

        grouped_data[job].append(person)

    # write grouped data to the output file
    with open("output.json", "w") as file:
        json.dump(grouped_data, file, indent=3)

    print("Data has been grouped and saved successfully.")

# If something goes wrong above, exception will cought it
except FileNotFoundError:
    print("Error: Could not find 'input.json'. Please make sure the file exists.")
    
except json.JSONDecodeError:
    print("Error: 'input.json' contains invalid JSON data.")
    
except Exception as e:
    print(f"An unexpected error occurred: {e}")  # This catches any other unexpected errors
