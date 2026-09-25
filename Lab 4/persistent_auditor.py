def load_inventory():
    orders = []

    try:
        file = open("inventory.txt", "r")

        for line in file:
            line = line.strip()

            if line != "":
                parts = line.split(",")

                order_id = int(parts[0])
                product_name = parts[1].strip()
                quantity = int(parts[2])

                orders.append([order_id, product_name, quantity])

        file.close()

    except FileNotFoundError:
        pass

    return orders


def save_inventory(orders):
    file = open("inventory.txt", "w")

    for order in orders:
        file.write(
            str(order[0]) + "," +
            order[1] + "," +
            str(order[2]) + "\n"
        )

    file.close()


orders = load_inventory()


print("Current Orders:")
print()

for order in orders:
    print(str(order[0]) + ", " + order[1] + ", " + str(order[2]))


product_name = input("\nEnter Product Name: ")


while True:
    try:
        quantity = int(input("Enter Quantity: "))

        if quantity < 0:
            print("Quantity cannot be negative.")
            continue

        break

    except ValueError:
        print("Please enter an integer only.")


if len(orders) == 0:
    new_order_id = 1001
else:
    new_order_id = orders[-1][0] + 1


new_order = [new_order_id, product_name, quantity]

orders.append(new_order)


print("\nNew Order Added:")
print(
    str(new_order[0]) + "," +
    new_order[1] + "," +
    str(new_order[2])
)


save_inventory(orders)

print("\nOrder successfully saved to inventory.txt")