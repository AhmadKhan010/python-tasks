import subprocess
import sys
import logging

# Configure basic logging to both file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("log_file.log", 'w'),
        logging.StreamHandler(sys.stdout)
    ]
)

def get_system_parameters():
    logging.info("Starting system parameter retrieval.")
    
    # Initialize a dictionary with default "Not Available" values
    info = {
        "Byte order": sys.byteorder,
        "Core": "N/A",
        "Model name": "N/A",
        "CPU max Frequency": "N/A",
        "CPU min frequency": "N/A",
        "Virtualization": "N/A",
        "L1i cache size": "N/A",
        "L1d cache size": "N/A",
        "L2 cache size": "N/A",
        "L3 cache size": "N/A",
        "Thread(s) per core": "N/A",
        "Distributor ID": "N/A",
        "Distributor Description": "N/A",
        "Distributor codename": "N/A"
    }

    # fetch CPU details using lscpu command
    try:
        logging.info("Running 'lscpu' command to fetch CPU details.")
        # Run lscpu command and capture output
        lscpu_output = subprocess.check_output(['lscpu'], universal_newlines=True)
        
        # Parse output line by line into a temporary dictionary
        lscpu_data = {}
        for line in lscpu_output.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                lscpu_data[key.strip()] = value.strip()
        
        # Map the specific fields required
        info["Core"] = lscpu_data.get("Core(s) per socket", "N/A")
        info["Model name"] = lscpu_data.get("Model name", "N/A")
        info["CPU max Frequency"] = lscpu_data.get("CPU max MHz", "N/A")
        info["CPU min frequency"] = lscpu_data.get("CPU min MHz", "N/A")
        info["Virtualization"] = lscpu_data.get("Virtualization", "N/A")
        info["L1i cache size"] = lscpu_data.get("L1i cache", "N/A")
        info["L1d cache size"] = lscpu_data.get("L1d cache", "N/A")
        info["L2 cache size"] = lscpu_data.get("L2 cache", "N/A")
        info["L3 cache size"] = lscpu_data.get("L3 cache", "N/A")
        info["Thread(s) per core"] = lscpu_data.get("Thread(s) per core", "N/A")
        logging.info("Successfully parsed CPU details.")

    except FileNotFoundError:
        logging.error("'lscpu' command not found. This script requires a Linux environment for CPU stats.")
    except Exception as e:
        logging.error(f"Error fetching CPU information: {e}")

    # fetch OS/Distributor details using lsb_release command
    try:
        logging.info("Running 'lsb_release -a' command to fetch OS details.")
        # Run lsb_release -a command and capture output
        lsb_output = subprocess.check_output(['lsb_release', '-a'], stderr=subprocess.DEVNULL, universal_newlines=True)
        
        lsb_data = {}
        for line in lsb_output.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                lsb_data[key.strip()] = value.strip()

        # Map the specific fields required
        info["Distributor ID"] = lsb_data.get("Distributor ID", "N/A")
        info["Distributor Description"] = lsb_data.get("Description", "N/A")
        info["Distributor codename"] = lsb_data.get("Codename", "N/A")
        logging.info("Successfully parsed OS details.")

    except FileNotFoundError:
        logging.error("'lsb_release' command not found. Operating System details may not populate on this machine.")
    except Exception as e:
        logging.error(f"Error fetching Distributor information: {e}")

    # 3. Display the final results cleanly
    logging.info("Writing output to output.txt and displaying results.")
    print("\nSystem Parameters ")
    try:
        with open("output.txt", "w") as file:
            file.write("System Parameters\n")
            for key, value in info.items():
                print(f"{key}: {value}")
                file.write(f"{key}: {value}\n")
        logging.info("Successfully wrote output to output.txt.")
    except Exception as e:
        logging.error(f"Failed to write to output.txt: {e}")
        
    logging.info("System parameter retrieval script finished.")

if __name__ == "__main__":
    get_system_parameters()
