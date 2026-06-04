import unittest

from Shipping_Cost_Calculator import calculate_shipping_cost


class ShippingCostCalculatorTests(unittest.TestCase):
    def test_calculate_shipping_cost(self):
        self.assertEqual(calculate_shipping_cost(2.5, 4), 10.0)


if __name__ == "__main__":
    unittest.main()
