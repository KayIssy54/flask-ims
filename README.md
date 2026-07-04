# Inventory Management System

## Project Overview

The Inventory Management System is a full-stack web application developed to help small retail businesses efficiently manage their inventory. The application consists of a Flask REST API backend and a React frontend that provide an intuitive interface for managing products.

The system allows users to:

- View all inventory items
- Add new products
- Update existing products
- Delete products
- Search products using the OpenFoodFacts API by barcode
- Manage inventory through both a web interface and a Command Line Interface (CLI)

The project demonstrates full-stack development using React for the frontend and Flask for the backend while implementing RESTful API principles.



## Features

### Backend

- Flask REST API
- CRUD operations for inventory items
- JSON-based data storage
- OpenFoodFacts API integration
- Command Line Interface (CLI)
- Unit testing

### Frontend

- React + Vite user interface
- View inventory
- Add products
- Update products
- Delete products
- Search products using OpenFoodFacts
- Responsive inventory cards
- Axios for API communication



## Technologies Used

### Backend

- Python 3
- Flask
- Flask-CORS
- Requests
- unittest

### Frontend

- React
- Vite
- Axios
- JavaScript
- HTML5
- CSS3

### Version Control

- Git
- GitHub

## Installation

### 1. Clone the Repository
### 2. Create a Virtual Environment

bash:
python3 -m venv venv


Activate it:
bash
venv\Scripts\activate

### 3. Install Backend Dependencies

bash:
pip install -r requirements.txt



### 4. Install Frontend Dependencies

bash
cd frontend
npm install



## Running the Application

### Backend

From the project root:

bash
python3 app.py


The Flask API runs on:

http://127.0.0.1:5000



### Frontend

Open another terminal.

Navigate to the frontend folder:

bash
cd frontend


Start the React application:

bash
npm run dev


The application runs on:
http://localhost:5173



## REST API Endpoints

Method  Endpoint        Description 
GET     inventory      Get all inventory items 
GET     inventory<id> Get one inventory item 
POST    inventory      Create a new inventory item 
PATCH   inventory<id> Update an inventory item 
DELETE  inventory<id> Delete an inventory item 
GET     product<barcode> Retrieve product details from OpenFoodFacts 



## CLI

The application also includes a Command Line Interface.

Run:

bash
python3 cli.py

Available operations include:

- View inventory
- Add products
- Update products
- Delete products
- Search products by barcode



## Running Tests

Run all tests with:

bash
python -m unittest discover tests




## OpenFoodFacts Integration

The application integrates with the OpenFoodFacts API, allowing users to search for product information using a barcode.

Returned information includes:

- Product name
- Brand
- Ingredients
- Quantity
- Categories

Users can then add the retrieved product to the local inventory.



## Future Improvements

- User authentication
- SQLite or PostgreSQL database
- Product image uploads
- Dashboard with charts
- Barcode scanner integration
- Inventory reports
- Low-stock notifications
- Product categories
- Search and filtering

