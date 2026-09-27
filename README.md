# VIT Bhopal College Canteen Management System

## Project Overview

The VIT Bhopal College Canteen Management System is a Python-based console application designed to simplify the process of selecting food items, managing a cart, calculating bills, and placing canteen orders.

The system provides a simple menu-driven interface for students to view available food items, add or remove items from their cart, view the total bill, and place an order using their student details.

## Problem Statement

Managing food orders manually in a college canteen can lead to difficulties in calculating bills, maintaining order details, and managing food selections.

This project provides a simple offline solution that allows students to manage their food orders through a structured Python application.

## Objectives

- Display the available canteen food items and prices.
- Allow students to add food items to a cart.
- Allow students to remove food items from the cart.
- Calculate the total order amount automatically.
- Collect student name and roll number.
- Confirm and display the placed order.
- Validate user inputs.
- Provide basic automated testing.

## Features

### 1. Food Menu
Displays available food items along with their prices.

### 2. Cart Management
Students can:
- Add food items.
- Specify quantities.
- View the cart.
- Remove food items.
- Calculate the total amount.

### 3. Order Placement
Students can enter:
- Student name
- Roll number

The system displays the complete order and total amount before confirmation.

### 4. Input Validation
The system checks user input and handles invalid numerical and empty inputs.

### 5. Order Confirmation
After confirmation, the system displays:
- Student details
- Ordered items
- Quantities
- Total amount
- Order date and time

### 6. Automated Testing
The project contains unit tests for important functions such as:
- Menu availability
- Cart operations
- Total calculation
- Cart clearing

## Technologies Used

- Python 3
- Python Dictionaries
- Python Functions
- Python Modules
- Python `datetime`
- Python `os`
- Python `unittest`

## Project Structure

```text
COLLEGE-CANTEEN-MANAGEMENT-SYSTEM/
│
├── main.py
├── menu.py
├── cart.py
├── order.py
├── validation.py
├── utils.py
├── test_canteen.py
├── README.md
├── statement.md
└── screenshots/