from datetime import datetime

from menu import menu
from cart import cart, calculate_total, clear_cart
from utils import clear_screen, header, pause
from validation import get_non_empty_input


def place_order():

    clear_screen()

    header()

    if not cart:

        print("\nYour cart is empty.")

        pause()

        return

    print("\nORDER DETAILS")
    print("-" * 60)

    student_name = get_non_empty_input(
        "Enter student name: "
    )

    roll_number = get_non_empty_input(
        "Enter roll number: "
    )

    print("\nYour Order")
    print("-" * 60)

    grand_total = calculate_total()

    for number, quantity in cart.items():

        name, price = menu[number]

        total = price * quantity

        print(
            f"{name} "
            f"x {quantity} "
            f"= ₹{total}"
        )

    print("-" * 60)

    print(
        f"TOTAL AMOUNT: ₹{grand_total}"
    )

    print("-" * 60)

    confirm = input(
        "\nConfirm order? (y/n): "
    ).strip().lower()

    if confirm != "y":

        print("\nOrder cancelled.")

        pause()

        return

    order_time = datetime.now().strftime(
        "%d-%m-%Y %I:%M %p"
    )

    clear_screen()

    print("=" * 60)
    print("              ORDER CONFIRMED")
    print("=" * 60)

    print(f"Student : {student_name}")
    print(f"Roll No : {roll_number}")
    print(f"Time    : {order_time}")

    print("-" * 60)

    for number, quantity in cart.items():

        name, price = menu[number]

        total = price * quantity

        print(
            f"{name} x {quantity} = ₹{total}"
        )

    print("-" * 60)

    print(
        f"TOTAL: ₹{grand_total}"
    )

    print("=" * 60)

    print(
        "\nPlease collect your order from"
    )

    print(
        "the college canteen counter."
    )

    print("\nThank you for ordering!")

    clear_cart()

    pause()