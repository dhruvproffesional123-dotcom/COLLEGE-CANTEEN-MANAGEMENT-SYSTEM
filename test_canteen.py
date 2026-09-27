import unittest

from menu import menu
from cart import cart, calculate_total, clear_cart


class TestCanteenSystem(unittest.TestCase):

    def setUp(self):

        clear_cart()

    def test_menu_contains_food_items(self):

        self.assertGreaterEqual(
            len(menu),
            10
        )

    def test_add_item_to_cart(self):

        cart[1] = 2

        self.assertEqual(
            cart[1],
            2
        )

    def test_calculate_total(self):

        cart[1] = 2
        cart[8] = 1

        total = calculate_total()

        self.assertEqual(
            total,
            55
        )

    def test_remove_item_from_cart(self):

        cart[1] = 3

        cart[1] -= 1

        self.assertEqual(
            cart[1],
            2
        )

    def test_clear_cart(self):

        cart[1] = 2
        cart[2] = 1

        clear_cart()

        self.assertEqual(
            len(cart),
            0
        )


if __name__ == "__main__":
    unittest.main()