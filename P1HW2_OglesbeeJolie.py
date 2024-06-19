# Get user input
budget = float(input("Enter your budget: $"))
destination = input("Enter your travel destination: ")
gas_expense = float(input("Enter the amount you'll spend on gas?: $"))
accommodation_expense = float(input("Enter the amount you'll spend on accommodation/hotel?: $"))
food_expense = float(input("Enter the amount you'll spend on food?: $"))

# Calculate total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Calculate remaining budget
remaining_budget = budget - total_expenses

# Display results
print(f"Your total expenses for {destination} are ${total_expenses:.2f}.")
print(f"Remaining budget: ${remaining_budget:.2f}")
