# Inventory Management System REST API

## Project Overview

The Inventory Management System is a Flask-based REST API developed to help a small retail business manage its inventory. The application allows administrators to create, view, update, and delete inventory items while also integrating with the OpenFoodFacts API to retrieve real-time product information using a barcode.

A command-line interface (CLI) is included to enable users to interact with the API, and unit tests are provided to verify that the application's features work correctly.



## Features

* RESTful API built with Flask
* Create, Read, Update, and Delete (CRUD) inventory items
* Retrieve all inventory items
* Retrieve a single inventory item by ID
* Fetch product information from the OpenFoodFacts API using a barcode
* Command Line Interface (CLI) for interacting with the API
* Unit testing using Python's unittest framework



## Technologies Used

* Python 3
* Flask
* Requests
* unittest
* Git & GitHub



## Project Structure


InventoryManagementSystem/
│
├── app.py
├── inventory.py
├── cli.py
├── requirements.txt
├── README.md
├── tests/
│   └── test_app.py
└── .gitignore


## Installation

1. Clone the repository:
2. Navigate into the project directory:
3. Create a virtual environment:
   python -m venv venv

4. Install the required packages:

bash
pip install -r requirements.txt


## Running the Application

Start the Flask server:

bash
python app.py


The API will run locally at:
http://127.0.0.1:5000



## Running the CLI

Start the Flask server first, then run:

bash
python cli.py


The CLI allows you to:

* View inventory
* Add inventory items
* Update inventory items
* Delete inventory items
* Search products using a barcode



## Running Tests

Run all tests using:

bash
python -m unittest discover tests



