import asyncio
import websockets
import json
import logging
import time

# set-up client logging
logging.basicConfig(
    filename="client.log",
    level=logging.INFO,
    format="%(asctime)s - CLIENT - %(levelname)s - %(message)s"
)

async def run_client():
    # read json data file
    try:
        with open("client_messages.json", "r") as f:
            messages = json.load(f)
        
        success_msg = f"Loaded {len(messages)} messages from data.json"
        print(success_msg)
        logging.info(success_msg)  

    except FileNotFoundError:
        error_msg = "Error: 'data.json' not found."
        print(error_msg)
        logging.error(error_msg)    
        return
    except Exception as e:
        error_msg = f"Error reading data.json: {e}"
        print(error_msg)
        logging.error(error_msg)  
        return

    # connect to the server
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            logging.info(f"Connected to server at {uri}")
            print(f"Connected to {uri}. Beginning transmission.\n")

            # open output file to store received messages
            with open("responses.json", "w") as out_file:
                
                for index, msg in enumerate(messages):
                    msg_str = json.dumps(msg)
                    
                    # Record start time
                    start_time = time.perf_counter()
                    
                    # Send message
                    await websocket.send(msg_str)
                    
                    # Wait for response
                    response_str = await websocket.recv()
                    
                    # Record end time & calculate latency
                    end_time = time.perf_counter()
                    time_taken = end_time - start_time
                    
                    # display response and time taken
#                    print(f"[{index+1}/{len(messages)}] Latency: {time_taken:.5f}s | Response: {response_str}")
                    
                    # Log to file
                    logging.info(f"Sent: {msg.get('method')} | Latency: {time_taken:.5f}s")
                    
                    # Store response in file
                    out_file.write(response_str + "\n")

            print("\nAll messages sent and responses saved to 'responses.json'")

    except ConnectionRefusedError:
        print("Error: Could not connect to the server")
        logging.error("Connection Refused. Server is likely offline.")
    except Exception as e:
        print(f"An unexpected client error occurred: {e}")
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    asyncio.run(run_client())