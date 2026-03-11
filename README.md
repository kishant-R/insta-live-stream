**Insta Live Stream Processing System**

# About the Project

This project is a simple event processing system built with Python.
It simulates how real-time applications receive and process data streams.

A Flask server is used to receive incoming requests (webhooks).
When data is received, it is passed through a small pipeline made of a **producer** and a **consumer** module.

The producer generates or forwards the incoming data, and the consumer processes it.
This structure is inspired by real streaming systems used in backend and data engineering.

**Project Structure**

# app/

-> main.py – Runs the Flask server and handles incoming webhook requests

-> producer.py – Generates or forwards event data

-> consumer.py – Processes the event data

# data/

-> raw_orders.json – Sample order data used for testing the pipeline

# kafka/

-> Placeholder folder for future Kafka integration

-> requirements.txt – Python dependencies needed to run the project

**How It Works**

-> The Flask server starts and waits for incoming requests.

-> When a webhook request arrives, the data is captured.

-> The producer module receives the event data.

-> The consumer module processes the event and prints or stores the result.

-> This setup demonstrates a simple producer–consumer workflow.

**How to Run the Project**

# Install dependencies:

pip install -r requirements.txt

# Run the server:

python app/main.py

# The server will start at:

http://localhost:5000

**Sample Data**

The data/raw_orders.json file contains example order data that can be used to test the system.

**Future Improvements**

# In the future this project could be extended by:

-> Adding Kafka for real streaming pipelines

-> Storing processed events in a database

-> Adding logging and monitoring

**System Architecture**

Incoming Event (Webhook)
        ↓
Flask Server (main.py)
        ↓
Producer Module
        ↓
Event Stream
        ↓
Consumer Module
        ↓
Processed Output
