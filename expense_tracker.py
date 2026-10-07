from expense import Expense
import calendar
import datetime

def main():
    print("Running Expense Tracker")

    expense_file_path = "expenses.csv"
    budget = 2000

    expense = get_user_expense()

    save_user_expense_to_file(expense, expense_file_path)

    summarize_expense(expense_file_path, budget)


def get_user_expense():
    print("Getting user expense")

    expense_name = input("Enter expense name:")
    expense_amount = float(input("Enter expense amount:"))

    expense_categories = [
        "🍕food",
        "🏠home",
        "💻work",
        "🥳fun",
        "✨Misc",
    ]

    while True:
        print("Select a category:")

        for i, category_name in enumerate(expense_categories):
            print(f" {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"

        selected_index = int(
            input(f"Enter a category number {value_range}: ")
        ) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]

            new_expense = Expense(
                name=expense_name,
                category=selected_category,
                amount=expense_amount
            )

            return new_expense

        else:
            print("Invalid category. Please try again!")


def save_user_expense_to_file(expense, expense_file_path):
    print(f"Saving expense: {expense} to {expense_file_path}")

    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expense(expense_file_path, budget):
    print("Summarizing user expense")

    expenses: list[Expense] = []

    # Read expenses from the CSV file
    with open(expense_file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(",")

            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category
            )

            expenses.append(line_expense)

    # Calculate expenses by category
    amount_by_category = {}

    for expense in expenses:
        key = expense.category

        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses By Category")

    for key, amount in amount_by_category.items():
        print(f" {key}: ₹{amount:.2f}")

    # Calculate total spending
    total_spent = sum([expense.amount for expense in expenses])

    print(f"You have spent ₹{total_spent:.2f} this month!")

    # Calculate remaining budget
    remaining_budget = budget - total_spent

    if remaining_budget >= 0:
        print(f"Budget Remaining: ₹{remaining_budget:.2f} this month!")
    else:
        print(f"You have exceeded your budget by ₹{abs(remaining_budget):.2f}!")
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    print("Reamining days in the current month:", remaining_days)



if __name__ == "__main__":
    main()

