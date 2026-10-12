# Inventory Manager

inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15,
    "Headphones": 5
}

item = input("Enter item name: ")
quantity = int(input("Enter quantity sold: "))

if item in inventory:
    if quantity <= inventory[item]:
        inventory[item] -= quantity
        print(f"Sale completed. {item} stock: {inventory[item]}")

        if inventory[item] == 0:
            print(f"WARNING: {item} is out of stock!")
    else:
        print("Not enough stock available.")
else:
    print("Item not found.")