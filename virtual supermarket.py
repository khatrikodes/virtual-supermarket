print("Welcome to the Virtual Supermarket!\n")

inventory = {
    "apple": {"price": 150, "quantity": 10},
    "banana": {"price": 40, "quantity": 20},  
    "orange": {"price": 60, "quantity": 15},
    "milk": {"price": 100, "quantity": 5},
    "bread": {"price": 50, "quantity": 8},
    "rice": {"price": 80, "quantity": 30},
    "flour": {"price": 70, "quantity": 25},
    "eggs": {"price": 10, "quantity": 50},
    "butter": {"price": 200, "quantity": 12},
    "cheese": {"price": 250, "quantity": 7},
    "chicken": {"price": 350, "quantity": 8},
    "potato": {"price": 25, "quantity": 40},
    "onion": {"price": 35, "quantity": 18},
    "carrot": {"price": 45, "quantity": 22},
    "tomato": {"price": 30, "quantity": 30}
}
def shopping_cart():
    cart = {}
    total = 0

    while True:
        print("\nCurrent Inventory:")
        for item, details in inventory.items():
            print(f"{item.capitalize()} - Rs.{details['price']} per item, {details['quantity']} available")
        
        item = input("Enter item name (apple, banana, orange, milk, bread,rice, flour,eggs, butter,cheese,chicken,potato,onoin,carrot tomato) or 'done' to finish: ").lower()

        if item == "done":
            break

        if item not in inventory:

            print("Sorry, that item is not available. Please choose another item.")
            continue

        quantity = int(input(f"How many {item}s would you like to buy? "))

        if quantity > inventory[item]["quantity"]:
            print(f"Sorry, we only have {inventory[item]['quantity']} {item}s available.")
            continue

        if item not in cart:
            cart[item] = {"price": inventory[item]["price"], "quantity": quantity}
        else:
            cart[item]["quantity"] += quantity

        inventory[item]["quantity"] -= quantity

        total += inventory[item]["price"] * quantity

    print("\nReceipt:")
    for item, details in cart.items():
        print(f"{item.capitalize()} - {details['quantity']} @ Rs.{details['price']} = Rs.{details['quantity'] * details['price']}")
    print(f"Total: Rs.{total}")

def supermarket():
    while True:
        shopping_cart()

        another_customer = input("Would another customer like to shop? (yes/no): ").lower()
        if another_customer != "yes":
            print("Thank you for shopping with us!")
            break

supermarket()


