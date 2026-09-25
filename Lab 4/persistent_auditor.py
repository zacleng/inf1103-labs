def load_inventory():
    try:
        file = open("inventory.txt", "r")
        data = file.read()
        file.close()

        if data == "":
            return 0

        return int(data)

    except FileNotFoundError:
        return 0

inventory = load_inventory()
log = 0

def get_valid_input():
    global log
    while True:
        try:
            value = input("Enter the inventory count (must be a non-negative integer): ").strip()
            if value.lower() == 'quit':
                return None
            return int(value)
        except ValueError:
            print("Please enter an integer only.")
            log += 1

def process_delivery(current_total, new_value):
    if new_value < 0:
        print("Inventory count cannot be negative.")
        return current_total, 1
    new_total = current_total + new_value
    if new_total > 500:
        print('Inventory count is over limit.')
        return current_total, 1
    return new_total, 0

def calculate_tax(amount):
    return round(amount * 0.10, 2)

def generate_report(total_units, failed_attempts):
    print("Total Deliveries Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)
    print("Exiting the program.")

while True:
    value = get_valid_input()
    if value is None:
        generate_report(inventory, log)
        break

    inventory, errors = process_delivery(inventory, value)
    log += errors
    if errors:
        if value < 0:
            continue
        generate_report(inventory, log)
        break

    print("Updated Inventory Count:", inventory)
    tax = calculate_tax(inventory)
    print("Tax Calculated:", tax)
    