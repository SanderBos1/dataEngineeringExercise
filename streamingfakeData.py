import os
import uuid
import random
import json
from azure.eventhub import EventHubProducerClient, EventData
from dotenv import load_dotenv

load_dotenv() 

# This script simulates the production of events for 5 devices.
devices = []
for x in range(0, 5):
    devices.append(str(uuid.uuid4()))

# Create a producer client to produce and publish events to the event hub.
producer = EventHubProducerClient.from_connection_string(conn_str=os.getenv("EVENT_HUB_CONNECTION_STR"), eventhub_name=os.getenv("EVENT_HUB_NAMESPACE"))

for y in range(0,1):    # For each device, produce 1 event. 
    event_data_batch = producer.create_batch() # Create a batch. You will add events to the batch later. 
    for dev in devices:
        # Create a dummy reading.
        reading = {
                'message': random.randint(70, 100), 
            }
        s = json.dumps(reading) # Convert the reading into a JSON string.
        event_data_batch.add(EventData(s)) # Add event data to the batch.
    producer.send_batch(event_data_batch) # Send the batch of events to the event hub.

# Close the producer.    
producer.close()