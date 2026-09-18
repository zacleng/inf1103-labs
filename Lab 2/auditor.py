inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter a stock quantity (or 'quit' to exit): ")

    if user_input.lower() == "quit":
        print(f"Total Units Processed: {inventory}")
        print(f"Number of Failed/Rejected Entries: {failed_entries}")
        break

    if not user_input.isdigit():
        print("Error: Please enter a valid integer.")
        failed_entries += 1
        continue

    quantity = int(user_input)

    if quantity < 0:
        print("Error: Negative values are not allowed.")
        failed_entries += 1
        continue

    inventory += quantity

    if inventory > 500:
        print("Alert: Overstock detected! Inventory exceeds 500 units.")
        break
