from menu import menu
from utils import clear_screen, header, pause
from validation import get_integer, get_positive_integer

cart = {}


def add_food():

    clear_screen()

    header()

    print()
    print("FOOD MENU")
    print("-" * 60)

    print(
        f"{'No.':<6}"
        f"{'Food Item':<30}"
        f"{'Price':>10}"
    )

    print("-" * 60)

    for number, item in menu.items():

        name, price = item

        print(
            f"{number:<6}"
            f"{name:<30}"
            f"₹{price:>8}"
        )

    print("-" * 60)

    choice = get_integer(
        "\nEnter food number: "
    )

    if choice not in menu:

        print("\nInvalid food number.")

        pause()

        return

    quantity = get_positive_integer(
        "Enter quantity: "
    )

    if choice in cart:

        cart[choice] += quantity

    else:

        cart[choice] = quantity

    name, price = menu[choice]

    print(
        f"\n{quantity} x {name} added to cart."
    )

    pause()


def calculate_total():

    total = 0

    for number, quantity in cart.items():

        name, price = menu[number]

        total += price * quantity

    return total


def view_cart():

    clear_screen()

    header()

    print()
    print("YOUR CART")
    print("-" * 60)

    if not cart:

        print("Your cart is empty.")

        pause()

        return

    print(
        f"{'Food Item':<25}"
        f"{'Qty':<10}"
        f"{'Price':<10}"
        f"{'Total':>10}"
    )

    print("-" * 60)

    grand_total = 0

    for number, quantity in cart.items():

        name, price = menu[number]

        total = price * quantity

        grand_total += total

        print(
            f"{name:<25}"
            f"{quantity:<10}"
            f"₹{price:<9}"
            f"₹{total:>9}"
        )

    print("-" * 60)

    print(
        f"{'GRAND TOTAL':<45}"
        f"₹{grand_total:>9}"
    )

    print("-" * 60)

    pause()


def remove_food():

    if not cart:

        clear_screen()

        header()

        print("\nYour cart is empty.")

        pause()

        return

    clear_screen()

    header()

    print()
    print("YOUR CART")
    print("-" * 60)

    for number, quantity in cart.items():

        name, price = menu[number]

        total = price * quantity

        print(
            f"{number}. {name} "
            f"x {quantity} = ₹{total}"
        )

    print("-" * 60)

    choice = get_integer(
        "\nEnter food number to remove: "
    )

    if choice not in cart:

        print(
            "\nThat item is not in your cart."
        )

        pause()

        return

    quantity = get_positive_integer(
        "Enter quantity to remove: "
    )

    if quantity > cart[choice]:

        print(
            "\nYou cannot remove more "
            "than the quantity in your cart."
        )

        pause()

        return

    cart[choice] -= quantity

    if cart[choice] == 0:

        del cart[choice]

    print("\nCart updated.")

    pause()


def clear_cart():

    cart.clear()