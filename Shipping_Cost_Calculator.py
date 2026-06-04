"""Shipping cost calculator."""


def calculate_shipping_cost(weight, rate):
    """Return the shipping cost for a given weight and rate."""
    return weight * rate


def main():
    """Run the shipping calculator CLI."""
    weight = float(input("Enter the package weight in kilograms: "))
    rate = float(input("Enter the shipping rate per kilogram: "))
    shipping_cost = calculate_shipping_cost(weight, rate)
    print(f"Shipping Cost: {shipping_cost} USD")


if __name__ == "__main__":
    main()
