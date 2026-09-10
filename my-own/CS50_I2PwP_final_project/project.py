from models import Transaction, Wallet, CATEGORIES
from analysis import filter_by, export_to_excel, load_data
import sys
import os
from datetime import datetime

def main():
    clear_CLI()
    wallet = Wallet()
    wallet.load_transactions()
    error_message = ""
    t_details = "TRANSACTION DETAILS:"
    f_details = "FILTER DETAILS:"
    while True:
        try:
            clear_CLI()
            control_c()
            if error_message:
                print(error_message)
                error_message = ""
            option = input("FINANCE TRACKER MENU\n(1) Add transaction\n(2) View balance"
            "\n(3) View (un)filtered summary\n(4) Export wallet to Excel\nChoose(1-4): ").strip().lower()
            if option == "1":
                try:
                    clear_CLI()
                    print("Press Control + C to CANCEL the transaction...")
                    collected = {}
                    collected["transaction_date"] = get_valid_input("Enter transaction date. \n(YYYY MM DD): ", validate_transaction_date, collected, t_details, control_c_trans)
                    display_progress(collected, t_details, control_c_trans)
                    collected["transaction_type"] = get_valid_input("Choose transaction type (income/expense/investment(+)/investment(-)).\n(+/-/i+/i-): ", validate_transaction_type, collected, t_details, control_c_trans)
                    display_progress(collected, t_details, control_c_trans)
                    collected["amount"] = get_valid_input("Enter amount.\n(00.00): ", validate_amount, collected, t_details, control_c_trans)
                    display_progress(collected, t_details, control_c_trans)
                    collected["currency"] = get_valid_input("Choose currency (dollars/euros).\n(d/e): ", validate_currency, collected, t_details, control_c_trans)
                    display_progress(collected, t_details, control_c_trans)
                    list_of_categories_for_prompt = "/".join(CATEGORIES[collected["transaction_type"]])
                    collected["category"] = get_valid_category(f"Choose category of transaction ({list_of_categories_for_prompt}).\nCategory: ", collected, t_details, control_c_trans)
                    display_progress(collected, t_details, control_c_trans)
                    collected["details"] = input("\nEnter details.\nDetails: ")
                    display_progress(collected, t_details, control_c_trans)
                    while True:
                        try:
                            confirm_details = input("Do you want to confirm?\n(y/n): ").strip().lower()
                            if confirm_details == 'y':
                                wallet.add_transaction(Transaction(*collected.values()))
                                wallet.save_transaction(collected)
                                clear_CLI()
                                print("Transaction was added successfully :)\n")
                                enter_to_continue()
                                break
                            elif confirm_details == 'n':
                                clear_CLI()
                                print("Transaction was not added :)\n")
                                enter_to_continue()
                                break
                            else:
                                raise ValueError("\nInvalid input: please enter \'y\' for yes, \'n\' for no :(\n")

                        except ValueError as e:
                            clear_CLI()
                            control_c_trans()
                            display_progress(collected, t_details, control_c_trans)
                            print(e)
                    clear_CLI()
                except ValueError as e:
                    clear_CLI()
                    print(e)
                    continue
                except KeyboardInterrupt:
                    clear_CLI()
                    sys.exit("Exiting Program...")
            elif option == '2':
                clear_CLI()
                control_c()
                print(f"Your balance is {wallet.balance:.2f} EUR")
                print(f"Your investment balance is {wallet.investment_balance:.2f} EUR")
                enter_to_continue()
            elif option == '3':
                clear_CLI()
                control_c()
                if os.path.isfile("transactions.csv"):
                    collected = {}
                    collected["transaction_date_start"] = get_valid_input("Enter start date (or press ENTER to skip).\n(YYYY MM DD): ", validate_transaction_date, collected, f_details, control_c, skippable=True)
                    display_progress(collected, f_details, control_c)
                    collected["transaction_date_end"] = get_valid_input("Enter end date (or press ENTER to skip).\n(YYYY MM DD): ", validate_transaction_date, collected, f_details, control_c, skippable=True)
                    display_progress(collected, f_details, control_c)
                    collected["transaction_type"] = get_valid_input("Choose transaction type (or press ENTER to skip).\n(+/-/i+/i-): ", validate_transaction_type, collected, f_details, control_c, skippable=True)
                    display_progress(collected, f_details, control_c)
                    collected["amount_lower_bound"] = get_valid_input("Enter amount LOWER bound (or press ENTER to skip).\n(00.00): ", validate_amount, collected, f_details, control_c, skippable=True)
                    display_progress(collected, f_details, control_c)
                    collected["amount_upper_bound"] = get_valid_input("Enter amount UPPER bound (or press ENTER to skip).\n(00.00): ", validate_amount, collected, f_details, control_c, skippable=True)
                    display_progress(collected, f_details, control_c)
                    collected["currency"] = get_valid_input("Choose currency(or press ENTER to skip).\n(d/e): ", validate_currency, collected, f_details, control_c, skippable=True)
                    display_progress(collected, f_details, control_c)
                    collected["category"] = get_valid_category("Choose category(or press ENTER to skip).\nCategory: ", collected, f_details, control_c, skippable=True)
                    display_progress(collected, f_details, control_c)
                    df = filter_by(**collected)
                    if df is None or df.empty:
                        clear_CLI()
                        control_c()
                        print("No data to show.")
                    else:
                        clear_CLI()
                        control_c()
                        print("##################################### RESULTS #####################################\n", df.to_string(index=False), "\n##################################### RESULTS #####################################")
                else:
                    print("No data to show.")
                enter_to_continue()
            elif option == '4':
                clear_CLI()
                control_c()
                export_to_excel()
                if not os.path.isfile("transaction_analysis.xlsx"):
                    clear_CLI()
                    control_c()
                    print("No data to export")
                else:
                    clear_CLI()
                    control_c()
                    print("Exported to transaction_analysis.xlsx")
                enter_to_continue()
            else:
                raise ValueError("Invalid input: please enter (1-4)\n")
        except ValueError as e:
            error_message = str(e)
        except KeyboardInterrupt:
            clear_CLI()
            sys.exit("Exiting Program...")

def validate_transaction_date(raw_value):
    try:
        value = datetime.strptime(raw_value.strip(), '%Y %m %d')
    except ValueError:
        raise ValueError("Invalid input: please use format YYYY MM DD.")
    if value > datetime.now():
        raise ValueError("Invalid Input: please enter date from the past/present times.")

    return value.date()

def validate_transaction_type(raw_value):
    value = str(raw_value.strip().lower())
    if value not in ["+", "-", "i+","i-"]:
        raise ValueError("\nInvalid input: please enter \'+\' for Income, \'-\' for Expense, \'i+\' for Investment(+), \'i-\' for Investment(-).")
    elif value == "+":
        value = "Income"
    elif value == "-":
        value = "Expense"
    elif value == "i+":
        value = "Investment Income"
    else:
        value = "Investment Expense"
    return value

def validate_amount(raw_value):
    try:
        value = float(raw_value.strip())
    except ValueError:
        raise ValueError("\nInvalid input: please enter a number")
    if value <= 0:
        raise ValueError("\nInvalid input: please enter amount that is more than 0.")
    return value

def validate_currency(raw_value):
    value = str(raw_value.strip().lower())
    if value not in ["d", "e"]:
        raise ValueError("\nInvalid Input: please enter \'d\' for (dollars), \'e\' for (euros).")
    elif value == "d":
        value = "Dollar, $"
    else:
        value = "Euro, €"
    return value

def validate_category(raw_value, transaction_type):
    value = raw_value.strip().lower()
    categories = CATEGORIES[transaction_type]
    if value not in categories:
        raise ValueError("Invalid Input: please enter a Category from the list.")
    else:
        return value.capitalize()

def get_valid_input(prompt, validator, collected, message, control_message, skippable=False):
    while True:
        try:
           raw = input(f"\n{prompt}")
           if skippable:
               if raw.strip() == "":
                   return None
           value = validator(raw)
           return value
        except ValueError as e:
            if collected is not None:
                display_progress(collected, message, control_message)
            print(e)

def get_valid_category(prompt, collected, message, control_message, skippable=False):
    while True:
        try:
           if collected.get("transaction_type") is None:
               return None
           raw = input(f"\n{prompt}")
           if skippable:
               if raw.strip() == "":
                   return None
           value = validate_category(raw, collected["transaction_type"])
           return value
        except ValueError as e:
            if collected is not None:
                display_progress(collected, message, control_message)
            print(e)

def display_progress(collected_fields: dict, details: str, control_message):
    clear_CLI()
    control_message()
    if len(collected_fields) > 0:
        print(details)
        for key, field in collected_fields.items():
            print(f"{str(key).capitalize().replace("_", " ")}: {str(field).capitalize()}")

def control_c():
    print("Press Control + C to exit the program...\n")

def control_c_trans():
    print("Press Control + C to CANCEL the transaction...\n")

def clear_CLI():
    os.system('cls||clear')

def enter_to_continue():
    input("Press ENTER to continue...")

if __name__== "__main__":
    main()
