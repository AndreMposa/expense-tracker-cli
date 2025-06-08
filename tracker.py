import csv
from datetime import datetime


FILENAME = 'expense.csv'


def add_expense():
    amount = float(input("Enter amount spent: MWK "))
    category = input("Enter category (e.g. Food, Transport): ")
    note = input("Optional note: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])


    print("\n✅ Expense added and saved to CSV!\n")


def show_expense():
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                date, amount, category, note = row
                print(f"[{date}] MWK{amount} - {category} - {note}")
    except FileNotFoundError:
        print("No expenses recorded yet.")


while True:
    print("\n---- Expense Tracker ----")
    print("1. Add Expense")
    print("2. Show Expense")
    print("3. Exit")


    choice = input("Choose an option (1-3): ")


    if choice == '1':
        add_expense()
    elif choice == '2':
        show_expense()
    elif choice == '3':
        print("Goodbye")
        break
    else:
        print("Invalid choice. Try again.")