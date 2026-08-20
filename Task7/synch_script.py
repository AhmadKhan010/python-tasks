import time
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler("synch_execution.log", mode='w'), # logs to a file
        logging.StreamHandler(sys.stdout)                  # logs to the console
    ]
)

def find_divisibles(range_limit, divisor):
    """Finds numbers divisible by the divisor in the given range."""
    
    # check that both range_limit and divisor should be int
    if not isinstance(range_limit, int) or not isinstance(divisor, int):
        logging.error(f"TypeError: Both range_limit ({range_limit}) and divisor ({divisor}) must be integers.")
        return []
    
    # check that correct range_limit is given
    if range_limit < 1:
        logging.error(f"Invalid range_limit ({range_limit}). Range must be >= 1.")
        return []

    logging.info(f"Starting synchronous task for range 1-{range_limit} by divisor {divisor}")
    divisibles = []

    try:
        for i in range(1, range_limit + 1):
            if i % divisor == 0:
                divisibles.append(i)

    except ZeroDivisionError:
        logging.error("ZeroDivisionError: Divisor cannot be 0.")
        return []
    except Exception as e:
        logging.exception(f"Unexpected error during calculation: {e}")
        return []
            
    logging.info(f"Completed synchronous task for divisor {divisor}. Found {len(divisibles)} numbers.")
    return divisibles

# main function to run the code
def main():
    pairs = [(50800000, 34113), (100052, 3210),(20000, 5), (100,0), ("pair",3)]
    
    start_time = time.time()

    with open("result_synch.txt", "w") as file:
        
        # Run synchronously
        for item in pairs:
            # Handle malformed pair tuples
            try:
                range_limit, divisor = item
            except ValueError:
                logging.error(f"Malformed pair {item}: Each entry must contain exactly (range_limit, divisor).")
                continue
                
            result = find_divisibles(range_limit, divisor)

            # Write result to the file much cleaner using f-strings
            file.write(f"Pair: {item}\n")
            file.write(f"Result: {result}\n")

    end_time = time.time()
    total_time = end_time - start_time
    logging.info(f"Total time taken (Synchronous): {total_time:.4f} seconds")

if __name__ == "__main__":
    main()