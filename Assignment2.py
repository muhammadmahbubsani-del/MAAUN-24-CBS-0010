from Assignment2models import FuelDispenser, CarWash
def main():
    # Create different assets
    asset1 = FuelDispenser("Fuel Pump 1", 500, 2.5)
    asset2 = FuelDispenser("Fuel Pump 2", 300, 2.5)
    asset3 = CarWash("Car Wash 1", 50, 10)

    # Store in a list
    assets = [asset1, asset2, asset3]

    total_revenue = 0

    # Loop through assets and calculate total revenue
    for asset in assets:
        revenue = asset.calculate_revenue()
        print(f"{asset.name} Revenue: {revenue}")
        total_revenue += revenue

    print(f"\nTotal Station Revenue: {total_revenue}")


if __name__ == "__main__":
    main()