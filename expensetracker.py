import csv
import datetime

class Expense:
    """
    A class to represent an expense.

    Attributes:
    -----------
    date : str
        The date of the expense.
    category : str
        The category of the expense.
    amount : float
        The amount of the expense.
    description : str
        A brief description of the expense.

    Methods:
    --------
    to_csv_row():
        Converts the expense instance to a list suitable for writing to a CSV file.
    """

    def __init__(self, date, category, amount, description):
        """
        Constructs all the necessary attributes for the Expense object.

        Parameters:
        -----------
        date : str
            The date of the expense.
        category : str
            The category of the expense.
        amount : float
            The amount of the expense.
        description : str
            A brief description of the expense.
        """
        self.date = date
        self.category = category
        self.amount = float(amount)
        self.description = description

    def to_csv_row(self):
        """
        Converts the expense instance to a list suitable for writing to a CSV file.

        Returns:
        --------
        list
            A list containing the expense attributes.
        """
        return [self.date, self.category, self.amount, self.description]


class ExpenseTracker:
    """
    A class to manage expenses.

    Attributes:
    -----------
    file_name : str
        The name of the file to store expenses.

    Methods:
    --------
    add_expense(expense):
        Adds an expense to the CSV file.
    view_monthly_expenses(month):
        Displays all expenses for a given month.
    view_category_expenses(category):
        Displays all expenses for a given category.
    """

    def __init__(self, file_name):
        """
        Constructs all the necessary attributes for the ExpenseTracker object.

        Parameters:
        -----------
        file_name : str
            The name of the file to store expenses.
        """
        self.file_name = file_name

    def add_expense(self, expense):
        """
        Adds an expense to the CSV file.

        Parameters:
        -----------
        expense : Expense
            The expense object to be added.
        """
        with open(self.file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(expense.to_csv_row())
        print("Expense added successfully!")

    def view_monthly_expenses(self, month):
        """
        Displays all expenses for a given month.

        Parameters:
        -----------
        month : str
            The month in the format 'YYYY-MM'.
        """
        total = 0
        with open(self.file_name, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    expense_date = datetime.datetime.strptime(row[0], "%Y-%m-%d")
                    if expense_date.strftime("%Y-%m") == month:
                        print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Description: {row[3]}")
                        total += float(row[2])
        print(f"Total expenses for {month}: {total}")

    def view_category_expenses(self, category):
        """
        Displays all expenses for a given category.

        Parameters:
        -----------
        category : str
            The category to filter expenses by.
        """
        total = 0
        with open(self.file_name, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[1] == category:
                    print(f"Date: {row[0]}, Category: {row[1]}, Amount: {row[2]}, Description: {row[3]}")
                    total += float(row[2])
        print(f"Total expenses for category '{category}': {total}")


def main():
    """
    The main function to run the Expense Tracker application.
    """
    tracker = ExpenseTracker('expenses.csv')

    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. View monthly expenses")
        print("3. View expenses by category")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category (e.g., food, transportation, entertainment): ")
            amount = input("Enter the amount: ")
            description = input("Enter a brief description: ")

            expense = Expense(date, category, amount, description)
            tracker.add_expense(expense)
        elif choice == '2':
            month = input("Enter the month (YYYY-MM): ")
            tracker.view_monthly_expenses(month)
        elif choice == '3':
            category = input("Enter the category: ")
            tracker.view_category_expenses(category)
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
