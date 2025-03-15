# Expense Splitter

## Overview
This project is a **Flask-based web application** that helps users fairly split expenses among a group of people. It calculates how much each participant owes and generates transactions to settle balances efficiently.

## Features
- Accepts contributions from multiple people.
- Calculates each participant's fair share of the total expense.
- Determines who needs to pay whom and by how much.
- Provides a simple API for frontend integration.

## Technologies Used
- **Flask** (Python web framework)
- **HTML, CSS, JavaScript** (for frontend rendering, if applicable)
- **JSON** (data exchange format for API communication)

## Project Workflow
1. **User Input**
   - Users input their contributions and the total expense.
   - The backend receives and processes this data.

2. **Expense Calculation**
   - The system calculates each person’s fair share.
   - Determines balances for each participant (who needs to pay and who should receive money).
   - Generates a list of transactions to settle debts.

3. **Result Display**
   - The final transactions are returned as a JSON response.
   - These transactions can be displayed in a frontend interface or used in another application.

## How to Use
1. **Run the Flask Application**
   ```sh
   python app.py
   ```
   This will start a local server on `http://127.0.0.1:5000/`.

2. **Send a POST Request to `/calculate`**
   - Example JSON request:
     ```json
     {
       "total_amount": 100,
       "contributors": [
         {"name": "Alice", "amount": 40},
         {"name": "Bob", "amount": 30},
         {"name": "Charlie", "amount": 30}
       ]
     }
     ```
   - Example JSON response:
     ```json
     {
       "transactions": [
         "Bob pays 3.33 to Alice",
         "Charlie pays 3.33 to Alice"
       ]
     }
     ```

## Acknowledgments
This project was built to simplify group expense management and ensure fair settlements among participants.

