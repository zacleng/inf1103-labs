inventory = 0
failed_entries = 0

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
