import pandas as pd
import os

def load_data():
    if os.path.isfile("transactions.csv"):
        df = pd.read_csv("transactions.csv")
        if df.empty:
            return None
        df['transaction_date'] = pd.to_datetime(df['transaction_date'])
        return df
    else:
        return None

def filter_by(transaction_date_start = None, transaction_date_end = None, transaction_type = None, amount_lower_bound = None, amount_upper_bound = None, currency = None, category = None):
    df = load_data()
    if df is not None:
        if transaction_date_start is not None and transaction_date_end is None:
            df = df[df['transaction_date'] >= pd.Timestamp(transaction_date_start)]
        elif transaction_date_end is not None and transaction_date_start is None:
            df = df[df['transaction_date'] <= pd.Timestamp(transaction_date_end)]
        elif transaction_date_start is not None and transaction_date_end is not None:
            df = df[(df['transaction_date'] >= pd.Timestamp(transaction_date_start)) &
                    (df['transaction_date'] <=  pd.Timestamp(transaction_date_end))]
        if transaction_type:
            df = df[df['transaction_type'] == transaction_type]
        if amount_lower_bound is not None and amount_upper_bound is None:
            df = df[df['amount'] >= amount_lower_bound]
        elif amount_lower_bound is None and amount_upper_bound is not None:
            df = df[df['amount'] <= amount_upper_bound]
        elif amount_lower_bound is not None and amount_upper_bound is not None:
            df = df[(df['amount'] >= amount_lower_bound) & (df['amount'] <= amount_upper_bound)]
        if currency:
            df = df[df['currency'] == currency]
        if category:
            df = df[df['category'] == category]
        return df
    else:
        return None


def export_to_excel():
    df = load_data()
    if df is not None:
        df.to_excel(excel_writer="transaction_analysis.xlsx")
    else:
        return None

