menu = {
    "Pizza": 5,
    "Sushi": 7,
    "Chicken": 3,
    "Beef": 4,
    "Rabbit": 5,
    "Hamburger": 7.5,
    "Coconut": 4,
    "Pineapple": 3,
}
shopping_cart = []
total_cost = 0
paid = False

print("Welcome to my Grocery Store!")

while True:
    print(
        "Choose one option from the list: \n"
        "1. View menu\n"
        "2. View shopping cart\n"
        "3. View total cost\n"
        "4. Pay\n"
        "5. Leave store\n"
    )
    try:
        user_input = int(input("> "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue

    if user_input == 1:
        print("-------Menu-------")
        for food, price in menu.items():
            print(f"{food} - {price:.2f}€")
        print("------------------")

        while True:
            items_purchased = input("Choose an item from the menu! (Type q to finish): ").strip().title()
            if items_purchased == "Q":
                print("Thank you!")
                break
            elif items_purchased in menu:
                shopping_cart.append(items_purchased)
                total_cost += menu[items_purchased]
                print(f"{items_purchased} added to your cart!")
            else:
                print(f"{items_purchased} is not valid or within menu. Please try again!")

    elif user_input == 2:
        if shopping_cart:
            print("Your shopping cart contains:")
            for item in shopping_cart:
                print(f"- {item}")
        else:
            print("Your shopping cart is empty.")

    elif user_input == 3:
        print(f"Total cost: {total_cost:.2f}€")

    elif user_input == 4:
        if paid:
            print("Items are already paid!")
        else:
            print(f"The total amount will be {total_cost:.2f}€")
            print("Thank you for your payment!")
            paid = True
            shopping_cart.clear()
            total_cost = 0

    elif user_input == 5:
        if not shopping_cart:
            print("Thank you! Hope to see you back soon!")
            break
        elif paid:
            print("Thank you! Hope to see you back soon!")
            break
        else:
            thief = input("Are you leaving without paying? (Y/N): ").strip().lower()
            if thief == "y":
                print("Police arrested you for stealing, and now you are in prison and banned from the store.")
                break
            elif thief == "n":
                print("Let me know when you are finished shopping!")
            else:
                print("Invalid response.")

    else:
        print(f"{user_input} is not a valid input. Please choose an option from 1-5.")




