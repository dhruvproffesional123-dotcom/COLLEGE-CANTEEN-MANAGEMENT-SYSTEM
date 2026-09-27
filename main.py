from utils import clear_screen, header, pause
from menu import show_menu
from cart import add_food, view_cart, remove_food
from order import place_order
from validation import get_integer


def main():

    while True:

        clear_screen()
        header()

        print()
        print("MAIN MENU")
        print("-" * 60)

        print("1. View Food Menu")
        print("2. Add Food to Cart")
        print("3. View Cart")
        print("4. Remove Food from Cart")
        print("5. Place Order")
        print("6. Exit")

        print("-" * 60)

        choice = get_integer(
            "Enter your choice: "
        )

        if choice == 1:

            show_menu()

        elif choice == 2:

            add_food()

        elif choice == 3:

            view_cart()

        elif choice == 4:

            remove_food()

        elif choice == 5:

            place_order()

        elif choice == 6:

            clear_screen()

            print("=" * 60)
            print("       THANK YOU FOR VISITING")
            print("          VIT BHOPAL COLLEGE CANTEEN")
            print("=" * 60)

            break

        else:

            print(
                "\nInvalid choice. "
                "Please select 1-6."
            )

            pause()


if __name__ == "__main__":
    main()