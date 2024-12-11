# Inventory Tracking System

This project is an inventory tracking system for a small store. It is implemented as a RESTful API using Flask and follows SOLID principles for clean, maintainable code.

## Features
- **CRUD Operations:**
  - Create a new product in the inventory.
  - Read (fetch) all products in the inventory.
  - Update an existing product's price and quantity.
  - Delete a product from the inventory.

- **JSON-Based Storage:** The inventory is stored in a `JSON` file (`data/inventory.json`).
- **SOLID Principles:** Code is modular and adheres to software design principles for maintainability and scalability.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd inventory_tracking
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
## Testing
- Use the provided `data/inventory.json` file as a mock database.
- After performing operations, check the changes by fetching all products (`GET /inventory/`).
