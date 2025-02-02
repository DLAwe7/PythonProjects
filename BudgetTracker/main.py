
print("Welcome to your Budget Tracker!")
options = ["1. Add Income/Expense", "2. View Balance", "3. View All Transactions", "4. Exit"]

current_balance = 0
transactions = []

while True:

    for option in options:
        print(option)
    user_input = input("> ")


    if user_input == "1":
        while True:
            transaction_type = input("Is this an income or expense? (type 'income' or 'expense'): ")
            if transaction_type.lower() == "income" or transaction_type.lower() == "expense":
                break
            else:
                print(f"'{transaction_type}'is an invalid input. Please type 'income' or 'expense'")
        while True:
            amount = input("Enter the amount: ")
            try:
                amount = float(amount)
                if transaction_type == "income":
                    current_balance += amount
                elif transaction_type == "expense":
                    current_balance -= amount
                break
            except ValueError:
                print(f"'{amount}' is not a valid number. Please enter a valid numeric amount.")

        description = input("Enter a description: ")

        transaction = {
            "type": transaction_type,
            "amount": amount,
            "description": description}

        transactions.append(transaction)

        print("Transaction added successfully!")

    elif user_input == "2":
        print(current_balance)
    elif user_input == "3":
        for transaction in transactions:
            print(transaction)
    elif user_input == "4":
        print("Goodbye!")
        break
    else:
        print(f"{user_input} is not a valid input. Please insert a number from 1-4")

