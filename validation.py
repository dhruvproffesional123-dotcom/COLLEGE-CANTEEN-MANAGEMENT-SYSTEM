def get_integer(prompt):

    while True:

        try:
            return int(input(prompt))

        except ValueError:
            print("\nPlease enter a valid number.")


def get_positive_integer(prompt):

    while True:

        value = get_integer(prompt)

        if value > 0:
            return value

        print("\nThe value must be greater than 0.")


def get_non_empty_input(prompt):

    while True:

        value = input(prompt).strip()

        if value:
            return value

        print("\nThis field cannot be empty.")