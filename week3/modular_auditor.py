def get_valid_input():
    """
    Prompts the user for a stock quantity.
    Returns:
        int  -> a valid, non-negative delivery quantity
        "quit" -> if the user wants to stop
        None -> if the input was invalid (caller counts this as a failed attempt)
    """
    stock = input("Enter stock quantity (or type 'quit' to exit): ")

    if stock.lower() == "quit":
        return "quit"

    if not stock.isdigit():
        print("Invalid input. Please enter a valid number.")
        return None

    return int(stock)


def process_delivery(current_total, new_value):
    """Adds a new delivery to the running total and returns the updated total."""
    return current_total + new_value


def calculate_tax(amount):
    """Returns 10% tax on a single delivery amount."""
    return amount * 0.10


def generate_report(total_units, deliveries_processed, failed_attempts):
    """Prints the final summary report."""
    print("\n--- Delivery Audit Report ---")
    print("Total Units Processed:", total_units)
    print("Total Deliveries Processed:", deliveries_processed)
    print("Number of Failed/Rejected Entries:", failed_attempts)


def main():
    inventory = 0
    deliveries_processed = 0
    failed_entries = 0

    while True:
        result = get_valid_input()

        if result == "quit":
            break

        if result is None:
            failed_entries += 1
            continue

        quantity = result
        inventory = process_delivery(inventory, quantity)
        tax = calculate_tax(quantity)
        deliveries_processed += 1

        print(f"Delivery of {quantity} units recorded. Tax for this delivery: {tax:.2f}")

        if inventory > 500:
            print("Overstock Alert! Inventory exceeds 500 units.")
            break

    generate_report(inventory, deliveries_processed, failed_entries)


if __name__ == "__main__":
    main()