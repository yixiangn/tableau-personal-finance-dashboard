import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

OUTPUT_PATH = Path("data/transactions.csv")

accounts = [
    "Main Savings",
    "Everyday Spending",
    "Credit Card",
    "Digital Wallet"
]

payment_methods = [
    "Card",
    "Bank Transfer",
    "Cash",
    "PayNow",
    "GIRO"
]

income_categories = {
    "Salary": ["Monthly Salary", "Bonus", "Allowance"],
    "Side Income": ["Freelance", "Tutoring", "Online Sales"],
    "Investment": ["Dividend", "Interest", "Capital Gain"]
}

expense_categories = {
    "Food": ["Hawker", "Cafe", "Restaurant", "Groceries"],
    "Transport": ["MRT", "Bus", "Taxi", "Ride Hailing"],
    "Shopping": ["Clothes", "Electronics", "Household"],
    "Entertainment": ["Movies", "Games", "Subscriptions"],
    "Bills": ["Phone Bill", "Utilities", "Insurance"],
    "Health": ["Clinic", "Pharmacy", "Gym"],
    "Education": ["Books", "Courses", "Software"]
}

merchants = {
    "Food": ["FairPrice", "Koufu", "Toast Box", "McDonald's", "Don Don Donki"],
    "Transport": ["SimplyGo", "Grab", "ComfortDelGro", "Gojek"],
    "Shopping": ["Uniqlo", "Shopee", "Lazada", "Courts"],
    "Entertainment": ["Netflix", "Steam", "Golden Village", "Spotify"],
    "Bills": ["Singtel", "SP Services", "AIA", "Income Insurance"],
    "Health": ["Guardian", "Watsons", "Anytime Fitness", "Raffles Medical"],
    "Education": ["Coursera", "Udemy", "Popular", "Notion"],
    "Salary": ["Company Payroll"],
    "Side Income": ["Freelance Client", "Private Student", "Carousell Buyer"],
    "Investment": ["Brokerage Platform", "Bank Interest"]
}

statuses = ["Completed", "Completed", "Completed", "Completed", "Pending", "Refunded"]

budget_map = {
    "Food": "Essentials",
    "Transport": "Essentials",
    "Bills": "Essentials",
    "Health": "Essentials",
    "Shopping": "Lifestyle",
    "Entertainment": "Lifestyle",
    "Education": "Growth",
    "Salary": "Income",
    "Side Income": "Income",
    "Investment": "Income"
}


def random_date(start_date, end_date):
    delta = end_date - start_date
    return start_date + timedelta(days=random.randint(0, delta.days))


def generate_transaction(transaction_id, start_date, end_date):
    transaction_date = random_date(start_date, end_date)

    transaction_type = random.choices(
        ["Income", "Expense", "Transfer"],
        weights=[15, 80, 5],
        k=1
    )[0]

    account_name = random.choice(accounts)
    payment_method = random.choice(payment_methods)
    status = random.choice(statuses)

    if transaction_type == "Income":
        category = random.choice(list(income_categories.keys()))
        subcategory = random.choice(income_categories[category])

        if category == "Salary":
            amount = round(random.uniform(2500, 4500), 2)
            is_recurring = "Yes"
        elif category == "Side Income":
            amount = round(random.uniform(80, 800), 2)
            is_recurring = random.choice(["Yes", "No"])
        else:
            amount = round(random.uniform(10, 500), 2)
            is_recurring = random.choice(["Yes", "No"])

        signed_amount = amount

    elif transaction_type == "Expense":
        category = random.choice(list(expense_categories.keys()))
        subcategory = random.choice(expense_categories[category])

        if category == "Food":
            amount = round(random.uniform(4, 80), 2)
        elif category == "Transport":
            amount = round(random.uniform(1, 45), 2)
        elif category == "Shopping":
            amount = round(random.uniform(15, 400), 2)
        elif category == "Entertainment":
            amount = round(random.uniform(8, 120), 2)
        elif category == "Bills":
            amount = round(random.uniform(30, 300), 2)
        elif category == "Health":
            amount = round(random.uniform(15, 180), 2)
        else:
            amount = round(random.uniform(10, 250), 2)

        signed_amount = -amount
        is_recurring = "Yes" if category in ["Bills", "Entertainment", "Health"] and random.random() < 0.4 else "No"

    else:
        category = "Transfer"
        subcategory = "Internal Transfer"
        amount = round(random.uniform(50, 1000), 2)
        signed_amount = 0
        is_recurring = "No"

    merchant = random.choice(merchants.get(category, ["Unknown Merchant"]))

    if status == "Refunded":
        signed_amount = 0

    return {
        "transaction_id": f"TXN{transaction_id:05d}",
        "transaction_date": transaction_date.strftime("%Y-%m-%d"),
        "transaction_type": transaction_type,
        "account_name": account_name,
        "payment_method": payment_method,
        "category": category,
        "subcategory": subcategory,
        "merchant": merchant,
        "description": f"{subcategory} transaction at {merchant}",
        "amount": amount,
        "signed_amount": signed_amount,
        "currency": "SGD",
        "status": status,
        "month": transaction_date.strftime("%Y-%m"),
        "year": transaction_date.year,
        "is_recurring": is_recurring,
        "budget_category": budget_map.get(category, "Other")
    }


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 12, 31)

    rows = [
        generate_transaction(i, start_date, end_date)
        for i in range(1, 1001)
    ]

    fieldnames = [
        "transaction_id",
        "transaction_date",
        "transaction_type",
        "account_name",
        "payment_method",
        "category",
        "subcategory",
        "merchant",
        "description",
        "amount",
        "signed_amount",
        "currency",
        "status",
        "month",
        "year",
        "is_recurring",
        "budget_category"
    ]

    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Generated {len(rows)} rows at {OUTPUT_PATH}")


if __name__ == "__main__":
    main()