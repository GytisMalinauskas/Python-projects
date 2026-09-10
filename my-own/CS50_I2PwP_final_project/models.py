from datetime import date
import csv
import os

CATEGORIES = {
    "Income": ["salary", "freelance", "other"],
    "Expense": ["housing", "food", "transport", "health", "entertainment", "education", "clothing", "subscriptions", "other"],
    "Investment Income": ["savings", "stocks", "etf", "crypto", "other"],
    "Investment Expense": ["savings", "stocks", "etf", "crypto", "other"],
}
EXCHANGE = 0.92

class Transaction:
    def __init__(self,
                transaction_date: date,
                transaction_type: str,
                amount: float,
                currency: str,
                category: str,
                details: str,
                ):
        self.transaction_date = transaction_date
        self.transaction_type = transaction_type
        self.amount = amount
        self.currency = currency
        self.category = category
        self.details = details

class Wallet:
    def __init__(self):
        self.transactions = list()

    @property
    def balance(self):
        total = 0
        for transaction in self.transactions:
            if transaction.transaction_type == "Income":
                if transaction.currency == "Dollar, $":
                    total += transaction.amount * EXCHANGE
                else:
                    total += transaction.amount
            if transaction.transaction_type == "Expense":
                if transaction.currency == "Dollar, $":
                    total -= transaction.amount * EXCHANGE
                else:
                    total -= transaction.amount
        return total

    @property
    def investment_balance(self):
        total = 0
        for transaction in self.transactions:
            if transaction.transaction_type == "Investment Income":
                if transaction.currency == "Dollar, $":
                    total += transaction.amount * EXCHANGE
                else:
                    total += transaction.amount
            if transaction.transaction_type == "Investment Expense":
                if transaction.currency == "Dollar, $":
                    total -= transaction.amount * EXCHANGE
                else:
                    total -= transaction.amount
        return total

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def load_transactions(self):
        if os.path.exists("transactions.csv"):
            with open("transactions.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.add_transaction(Transaction(
                        transaction_date = date.fromisoformat(row["transaction_date"]),
                        transaction_type = row["transaction_type"],
                        amount = float(row["amount"]),
                        currency = row["currency"],
                        category = row["category"],
                        details = row["details"]
                    ))


    def save_transaction(self, values: dict):
        add_header = False
        if not os.path.exists("transactions.csv"):
            add_header = True
        elif os.path.exists("transactions.csv") and os.path.getsize("transactions.csv") == 0:
            add_header = True
        with open("transactions.csv", "a") as file:
            fieldnames = ["transaction_date", "transaction_type", "amount", "currency", "category", "details"]
            writer = csv.DictWriter(file, fieldnames)
            if add_header:
                writer.writeheader()
            writer.writerow(values)
