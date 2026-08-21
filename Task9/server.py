import asyncio
import websockets
import json
import logging
from datetime import datetime

# set-up server logging
logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - SERVER - %(levelname)s - %(message)s"
)

async def handle_client(websocket):
    logging.info(f"Client connected: {websocket.remote_address}")
    try:
        # Wait and listen for messages from the connected client
        async for message in websocket:
            try:
                # parse the incoming json message
                data = json.loads(message) 
                
                # append current timestamp
                data["server_timestamp"] = datetime.now().isoformat()
                
                # send the modified JSON back to the client
                response = json.dumps(data)
                await websocket.send(response)
                
                # log successful process
                logging.info(f"Processed and replied to: {data.get('method')}")
                
            except json.JSONDecodeError:
                logging.error("Received invalid JSON data")
                await websocket.send(json.dumps({"error": "Invalid JSON format"}))
                
    except websockets.exceptions.ConnectionClosed as e:
        logging.info(f"Client disconnected: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

async def main():
    # Start the WebSocket server on localhost, port 8765
    server = await websockets.serve(handle_client, "localhost", 8765)
    print("WebSocket Server started on ws://localhost:8765")
    logging.info("WebSocket Server started")
    await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
