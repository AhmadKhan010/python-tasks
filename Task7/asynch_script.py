import asyncio
import time
import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler("asynch_execution_async.log", mode='w'), # logs to a file
        logging.StreamHandler(sys.stdout)                      # logs to the console
    ]
)

async def find_divisibles_async(range_limit, divisor):
    """Finds numbers divisible by the divisor asynchronously with context switching."""
    
    # check that both range_limit and divisor should be int
    if not isinstance(range_limit, int) or not isinstance(divisor, int):
        logging.error(f"TypeError: Both range_limit ({range_limit}) and divisor ({divisor}) must be integers.")
        return []
    
    # check that correct range_limit is given
    if range_limit < 1:
        logging.error(f"Invalid range_limit ({range_limit}). Range must be >= 1.")
        return []

    logging.info(f"Starting asynchronous task for range 1-{range_limit} by divisor {divisor}")
    divisibles = []

    try:
        for i in range(1, range_limit + 1):
            if i % divisor == 0:
                divisibles.append(i)
                # Yield control back to the event loop to allow context switching
                await asyncio.sleep(0) 

    except ZeroDivisionError:
        logging.error("ZeroDivisionError: Divisor cannot be 0.")
        return []
    except Exception as e:
        logging.exception(f"Unexpected error during calculation: {e}")
        return []
            
    logging.info(f"Completed asynchronous task for divisor {divisor}. Found {len(divisibles)} numbers.")
    return divisibles


async def main():
    raw_pairs = [(50800000, 34113), (100052, 3210), (20000, 5), (100, 0), ("test", 2)]
    
    start_time = time.time()
    
    valid_pairs = []
    tasks = []

    # 1. Validate pairs and create tasks
    for item in raw_pairs:
        try:
            range_limit, divisor = item
            valid_pairs.append(item)

            # Create the task and add it to our list
            tasks.append(find_divisibles_async(range_limit, divisor))
        except ValueError:
            logging.error(f"Malformed pair {item}: Each entry must contain exactly (range_limit, divisor).")
            continue

    # run all tasks concurrently and wait for them to finish
    results = await asyncio.gather(*tasks)

    # write results to the file safely
    with open("result_async.txt", "w") as file:
        for item, result in zip(valid_pairs, results):
            file.write(f"Pair: {item}\n")
            file.write(f"Result: {result}\n")


    end_time = time.time()
    total_time = end_time - start_time
    logging.info(f"Total time taken (Asynchronous): {total_time:.4f} seconds")


if __name__ == "__main__":
    # Run the asyncio event loop
    asyncio.run(main())
