# Project Statement

## Project Title

VIT Bhopal College Canteen Management System

## Problem Statement

Managing food orders manually in a college canteen can lead to difficulties in selecting food items, calculating bills, managing quantities, and maintaining a clear order process.

This project provides a simple offline, Python-based solution that allows students to view the canteen menu, add and remove food items from a cart, calculate the total bill, and place an order using their student details.

## Project Scope

The project focuses on providing a basic command-line system for managing food orders in a college canteen.

The system includes:

- Food menu management
- Food item selection
- Cart management
- Quantity management
- Automatic bill calculation
- Student details collection
- Order confirmation
- Date and time recording
- Input validation
- Automated testing

The current version is designed as an offline console application and does not include online payments, databases, or online ordering.

## Target Users

The primary target users are:

### Students

Students can use the system to:

- View available food items
- Select food items
- Add items to their cart
- Remove items from their cart
- View their total bill
- Place an order using their name and roll number

### College Canteen

The system can provide a structured way to process student food orders and calculate bills.

## High-Level Features

### 1. Food Menu

Displays the available food items and their prices.

### 2. Cart Management

Allows users to add food items, specify quantities, view the cart, and remove items.

### 3. Bill Calculation

Automatically calculates the total cost based on the selected food items and quantities.

### 4. Order Placement

Collects the student's name and roll number and displays the complete order before confirmation.

### 5. Order Confirmation

Displays the confirmed order, student details, total amount, and order date and time.

### 6. Input Validation

Handles invalid numerical input, empty input, invalid food numbers, and incorrect quantities.

### 7. Automated Testing

Uses Python's built-in `unittest` framework to test important project functions.

## Technologies Used

- Python 3
- Python Functions
- Python Dictionaries
- Python Modules
- `datetime`
- `os`
- `unittest`

## Project Type

**Offline Command-Line Application**

## Current Limitations

- No database is used.
- Orders are not permanently stored.
- The application works through the command line.
- The food menu is predefined.
- Online ordering and digital payments are not included.

## Future Scope

Possible future improvements include:

- Database integration
- Graphical user interface
- Online ordering
- Digital payment integration
- Order history
- Admin panel
- Stock management
- Receipt generation