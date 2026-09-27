import os

def clear_screen():

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def header():

    print("=" * 60)
    print("              VIT BHOPAL COLLEGE CANTEEN")
    print("=" * 60)
    print("          Fresh Food • Affordable Prices")
    print("=" * 60)


def pause():
    
    input("\nPress Enter to continue...")