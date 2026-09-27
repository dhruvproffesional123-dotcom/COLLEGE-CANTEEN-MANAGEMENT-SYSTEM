from utils import clear_screen, header, pause

menu = {
    1: ("Samosa", 20),
    2: ("Vada Pav", 25),
    3: ("Veg Sandwich", 40),
    4: ("Masala Maggi", 50),
    5: ("Veg Noodles", 60),
    6: ("Cheese Burger", 70),
    7: ("French Fries", 60),
    8: ("Tea", 15),
    9: ("Cold Coffee", 50),
    10: ("Cold Drink", 30)
}


def show_menu():

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

    pause()