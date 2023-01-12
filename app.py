import connexion
from connexion import NoContent 
import datetime
import json
import logging
import logging.config
import pykafka
from pykafka import KafkaClient
import requests
import uuid
import yaml

# TODO - create array to store incoming JSON buy/sell objects

def process_events(event):
    # TODO
    # Use datetime and strftime to create a string representing the current 
    # date and time (see openapi.yml for format)
    #
    # Create a uuid called trace_id using the uuid.uuid4() function, 
    # and append it to the event parameter
    #
    # Create an object named 'obj' with three properties:
    # received_timestamp (value is the current date and time created above)
    # event_data (value is a string containing all values from the event parameter,
    # including your trace_id)
    #
    # if array length is less than 10, add your object (obj) to the array
    #
    # If array length equals ten, 
    # remove last object from the array and insert your new object (obj) at the beginning,
    # then write the entire array to a file named events.json 
    #
    # note: you are allowed to overwrite the contents of events.json each time you write

    # TODO - return obj
    pass

# Endpoints
def buy(body):
    # TODO - pass the body parameter to your process_events function
    return NoContent, 201

def sell(body):
    # TODO - pass the body parameter to your process_events function
    return NoContent, 201

app = connexion.FlaskApp(__name__, specification_dir='')
app.add_api("openapi.yml", strict_validation=True, validate_responses=True)

if __name__ == "__main__":
    app.run(port=8080)