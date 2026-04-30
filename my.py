# Store Manager

# Initial data
items = ["book", "bag", "pen", "bread", "milk"]
prices = {"book": 60, "bag": 450, "pen": 10, "bread": 35, "milk": 29}

while True:
    print("\n--- STORE MENU ---")
    print("1. Show Items")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Update Price")
    print("5. Search Item")
    print("6. Show Total Cost")
    print("7. Highest Priced Item")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nItems and Prices:")
        for item in items:
            print(item, ":", prices[item])

    elif choice == "2":
        new_item = input("Enter new item name: ")
        new_price = int(input("Enter price: "))
        items.append(new_item)
        prices[new_item] = new_price
        print("Item added successfully!")

    elif choice == "3":
        remove_item = input("Enter item to remove: ")
        if remove_item in items:
            items.remove(remove_item)
            prices.pop(remove_item)
            print("Item removed!")
        else:
            print("Item not found!")

    elif choice == "4":
        update_item = input("Enter item to update: ")
        if update_item in prices:
            new_price = int(input("Enter new price: "))
            prices[update_item] = new_price
            print("Price updated!")
        else:
            print("Item not found!")

    elif choice == "5":
        search_item = input("Enter item name: ")
        if search_item in prices:
            print(search_item, ":", prices[search_item])
        else:
            print("Item not found!")

    elif choice == "6":
        total = sum(prices.values())
        print("Total cost:", total)

    elif choice == "7":
        highest = max(prices, key=prices.get)
        print("Highest priced item:", highest)
        print("Price:", prices[highest])

    elif choice == "8":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")