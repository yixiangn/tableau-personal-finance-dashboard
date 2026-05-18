import csv
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)

OUTPUT_PATH = Path("data/transactions.csv")

START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 12, 31)

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

budget_map = {
    "Salary": "Income",
    "Side Income": "Income",
    "Investment": "Income",
    "Food": "Essentials",
    "Transport": "Essentials",
    "Bills": "Essentials",
    "Health": "Essentials",
    "Shopping": "Lifestyle",
    "Entertainment": "Lifestyle",
    "Education": "Growth",
    "Transfer": "Transfer"
}


def get_month_start_dates(start_date, end_date):
    months = []
    current = datetime(start_date.year, start_date.month, 1)

    while current <= end_date:
        months.append(current)

        if current.month == 12:
            current = datetime(current.year + 1, 1, 1)
        else:
            current = datetime(current.year, current.month + 1, 1)

    return months


def get_random_date_in_month(month_start, min_day=1, max_day=28):
    day = random.randint(min_day, max_day)
    return datetime(month_start.year, month_start.month, day)


def get_random_date_between(start_date, end_date):
    delta = end_date - start_date
    return start_date + timedelta(days=random.randint(0, delta.days))


def create_transaction(
    transaction_id,
    transaction_date,
    transaction_type,
    account_name,
    payment_method,
    category,
    subcategory,
    merchant,
    amount,
    status="Completed",
    is_recurring="No"
):
    amount = round(amount, 2)

    if transaction_type == "Income":
        signed_amount = amount
    elif transaction_type == "Expense":
        signed_amount = -amount
    else:
        signed_amount = 0

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


def generate_salary_transactions(months, starting_id):
    rows = []
    transaction_id = starting_id

    for month_start in months:
        salary_date = get_random_date_in_month(month_start, 25, 28)
        salary_amount = random.uniform(3200, 3800)

        rows.append(
            create_transaction(
                transaction_id=transaction_id,
                transaction_date=salary_date,
                transaction_type="Income",
                account_name="Main Savings",
                payment_method="Bank Transfer",
                category="Salary",
                subcategory="Monthly Salary",
                merchant="Company Payroll",
                amount=salary_amount,
                status="Completed",
                is_recurring="Yes"
            )
        )
        transaction_id += 1

    return rows, transaction_id


def generate_recurring_bills(months, starting_id):
    rows = []
    transaction_id = starting_id

    recurring_items = [
        {
            "subcategory": "Phone Bill",
            "merchant": "Singtel",
            "amount_range": (45, 75),
            "payment_method": "GIRO",
            "account_name": "Main Savings",
            "day_range": (3, 8)
        },
        {
            "subcategory": "Utilities",
            "merchant": "SP Services",
            "amount_range": (90, 180),
            "payment_method": "GIRO",
            "account_name": "Main Savings",
            "day_range": (8, 15)
        },
        {
            "subcategory": "Insurance",
            "merchant": "Income Insurance",
            "amount_range": (120, 220),
            "payment_method": "GIRO",
            "account_name": "Main Savings",
            "day_range": (10, 18)
        }
    ]

    for month_start in months:
        for item in recurring_items:
            min_day, max_day = item["day_range"]
            transaction_date = get_random_date_in_month(month_start, min_day, max_day)
            amount = random.uniform(*item["amount_range"])

            rows.append(
                create_transaction(
                    transaction_id=transaction_id,
                    transaction_date=transaction_date,
                    transaction_type="Expense",
                    account_name=item["account_name"],
                    payment_method=item["payment_method"],
                    category="Bills",
                    subcategory=item["subcategory"],
                    merchant=item["merchant"],
                    amount=amount,
                    status="Completed",
                    is_recurring="Yes"
                )
            )
            transaction_id += 1

    return rows, transaction_id


def generate_subscriptions(months, starting_id):
    rows = []
    transaction_id = starting_id

    subscriptions = [
        {
            "subcategory": "Subscriptions",
            "merchant": "Netflix",
            "amount": 17.98,
            "day": 5
        },
        {
            "subcategory": "Subscriptions",
            "merchant": "Spotify",
            "amount": 10.98,
            "day": 12
        },
        {
            "subcategory": "Games",
            "merchant": "Steam",
            "amount": 14.99,
            "day": 18
        }
    ]

    for month_start in months:
        for subscription in subscriptions:
            # Steam is less consistent, so only generate it for some months.
            if subscription["merchant"] == "Steam" and random.random() < 0.45:
                continue

            transaction_date = datetime(
                month_start.year,
                month_start.month,
                min(subscription["day"], 28)
            )

            rows.append(
                create_transaction(
                    transaction_id=transaction_id,
                    transaction_date=transaction_date,
                    transaction_type="Expense",
                    account_name="Credit Card",
                    payment_method="Card",
                    category="Entertainment",
                    subcategory=subscription["subcategory"],
                    merchant=subscription["merchant"],
                    amount=subscription["amount"],
                    status="Completed",
                    is_recurring="Yes"
                )
            )
            transaction_id += 1

    return rows, transaction_id


def generate_food_transactions(months, starting_id):
    rows = []
    transaction_id = starting_id

    food_options = [
        ("Hawker", "Koufu", 4.5, 9.5),
        ("Cafe", "Toast Box", 5.0, 12.0),
        ("Restaurant", "McDonald's", 8.0, 18.0),
        ("Groceries", "FairPrice", 20.0, 85.0),
        ("Cafe", "Don Don Donki", 8.0, 25.0)
    ]

    for month_start in months:
        number_of_food_transactions = random.randint(18, 28)

        for _ in range(number_of_food_transactions):
            subcategory, merchant, low, high = random.choice(food_options)
            transaction_date = get_random_date_in_month(month_start, 1, 28)
            amount = random.uniform(low, high)

            rows.append(
                create_transaction(
                    transaction_id=transaction_id,
                    transaction_date=transaction_date,
                    transaction_type="Expense",
                    account_name=random.choice(["Everyday Spending", "Credit Card", "Digital Wallet"]),
                    payment_method=random.choice(["Card", "Cash", "PayNow"]),
                    category="Food",
                    subcategory=subcategory,
                    merchant=merchant,
                    amount=amount,
                    status="Completed",
                    is_recurring="No"
                )
            )
            transaction_id += 1

    return rows, transaction_id


def generate_transport_transactions(months, starting_id):
    rows = []
    transaction_id = starting_id

    transport_options = [
        ("MRT", "SimplyGo", 1.2, 2.5),
        ("Bus", "SimplyGo", 1.0, 2.2),
        ("Ride Hailing", "Grab", 12.0, 35.0),
        ("Ride Hailing", "Gojek", 10.0, 32.0),
        ("Taxi", "ComfortDelGro", 15.0, 45.0)
    ]

    for month_start in months:
        number_of_transport_transactions = random.randint(15, 26)

        for _ in range(number_of_transport_transactions):
            subcategory, merchant, low, high = random.choice(transport_options)

            # Public transport appears more often than taxis/rides.
            if subcategory in ["Ride Hailing", "Taxi"] and random.random() < 0.45:
                continue

            transaction_date = get_random_date_in_month(month_start, 1, 28)
            amount = random.uniform(low, high)

            rows.append(
                create_transaction(
                    transaction_id=transaction_id,
                    transaction_date=transaction_date,
                    transaction_type="Expense",
                    account_name=random.choice(["Everyday Spending", "Credit Card", "Digital Wallet"]),
                    payment_method=random.choice(["Card", "PayNow"]),
                    category="Transport",
                    subcategory=subcategory,
                    merchant=merchant,
                    amount=amount,
                    status="Completed",
                    is_recurring="No"
                )
            )
            transaction_id += 1

    return rows, transaction_id


def generate_occasional_expenses(months, starting_id):
    rows = []
    transaction_id = starting_id

    expense_options = [
        ("Shopping", "Clothes", "Uniqlo", 25, 160),
        ("Shopping", "Electronics", "Shopee", 20, 350),
        ("Shopping", "Household", "Lazada", 15, 180),
        ("Health", "Pharmacy", "Guardian", 12, 75),
        ("Health", "Clinic", "Raffles Medical", 40, 150),
        ("Health", "Gym", "Anytime Fitness", 80, 110),
        ("Education", "Books", "Popular", 12, 60),
        ("Education", "Courses", "Udemy", 15, 120),
        ("Education", "Software", "Notion", 8, 20),
        ("Entertainment", "Movies", "Golden Village", 12, 35)
    ]

    for month_start in months:
        number_of_occasional_expenses = random.randint(6, 14)

        for _ in range(number_of_occasional_expenses):
            category, subcategory, merchant, low, high = random.choice(expense_options)
            transaction_date = get_random_date_in_month(month_start, 1, 28)
            amount = random.uniform(low, high)

            is_recurring = "Yes" if merchant in ["Anytime Fitness", "Notion"] else "No"

            rows.append(
                create_transaction(
                    transaction_id=transaction_id,
                    transaction_date=transaction_date,
                    transaction_type="Expense",
                    account_name=random.choice(["Everyday Spending", "Credit Card", "Digital Wallet"]),
                    payment_method=random.choice(["Card", "Bank Transfer", "PayNow", "Cash"]),
                    category=category,
                    subcategory=subcategory,
                    merchant=merchant,
                    amount=amount,
                    status="Completed",
                    is_recurring=is_recurring
                )
            )
            transaction_id += 1

    return rows, transaction_id


def generate_side_income(months, starting_id):
    rows = []
    transaction_id = starting_id

    side_income_options = [
        ("Freelance", "Freelance Client", 150, 900),
        ("Tutoring", "Private Student", 80, 450),
        ("Online Sales", "Carousell Buyer", 20, 250)
    ]

    for month_start in months:
        number_of_side_income = random.choices(
            [0, 1, 2, 3],
            weights=[25, 40, 25, 10],
            k=1
        )[0]

        for _ in range(number_of_side_income):
            subcategory, merchant, low, high = random.choice(side_income_options)
            transaction_date = get_random_date_in_month(month_start, 1, 28)
            amount = random.uniform(low, high)

            rows.append(
                create_transaction(
                    transaction_id=transaction_id,
                    transaction_date=transaction_date,
                    transaction_type="Income",
                    account_name="Main Savings",
                    payment_method=random.choice(["Bank Transfer", "PayNow"]),
                    category="Side Income",
                    subcategory=subcategory,
                    merchant=merchant,
                    amount=amount,
                    status="Completed",
                    is_recurring="No"
                )
            )
            transaction_id += 1

    return rows, transaction_id


def generate_investment_income(months, starting_id):
    rows = []
    transaction_id = starting_id

    for month_start in months:
        # Investment income appears in only some months.
        if random.random() < 0.45:
            continue

        subcategory = random.choice(["Dividend", "Interest", "Capital Gain"])
        merchant = random.choice(["Brokerage Platform", "Bank Interest"])
        transaction_date = get_random_date_in_month(month_start, 1, 28)
        amount = random.uniform(10, 350)

        rows.append(
            create_transaction(
                transaction_id=transaction_id,
                transaction_date=transaction_date,
                transaction_type="Income",
                account_name="Main Savings",
                payment_method="Bank Transfer",
                category="Investment",
                subcategory=subcategory,
                merchant=merchant,
                amount=amount,
                status="Completed",
                is_recurring="No"
            )
        )
        transaction_id += 1

    return rows, transaction_id


def generate_transfers(months, starting_id):
    rows = []
    transaction_id = starting_id

    for month_start in months:
        number_of_transfers = random.randint(1, 3)

        for _ in range(number_of_transfers):
            transaction_date = get_random_date_in_month(month_start, 1, 28)
            amount = random.uniform(100, 1000)

            rows.append(
                create_transaction(
                    transaction_id=transaction_id,
                    transaction_date=transaction_date,
                    transaction_type="Transfer",
                    account_name=random.choice(["Main Savings", "Everyday Spending"]),
                    payment_method="Bank Transfer",
                    category="Transfer",
                    subcategory="Internal Transfer",
                    merchant="Internal Account Transfer",
                    amount=amount,
                    status="Completed",
                    is_recurring="No"
                )
            )
            transaction_id += 1

    return rows, transaction_id


def generate_pending_and_refunded_transactions(starting_id):
    rows = []
    transaction_id = starting_id

    pending_count = 12
    refunded_count = 10

    pending_options = [
        ("Expense", "Food", "Restaurant", "McDonald's", 8, 20),
        ("Expense", "Shopping", "Electronics", "Shopee", 20, 200),
        ("Expense", "Transport", "Ride Hailing", "Grab", 12, 35),
    ]

    refund_options = [
        ("Expense", "Shopping", "Clothes", "Uniqlo", 25, 160),
        ("Expense", "Entertainment", "Movies", "Golden Village", 12, 35),
        ("Expense", "Food", "Groceries", "FairPrice", 20, 85),
    ]

    for _ in range(pending_count):
        transaction_type, category, subcategory, merchant, low, high = random.choice(pending_options)
        transaction_date = get_random_date_between(START_DATE, END_DATE)
        amount = random.uniform(low, high)

        rows.append(
            create_transaction(
                transaction_id=transaction_id,
                transaction_date=transaction_date,
                transaction_type=transaction_type,
                account_name=random.choice(accounts),
                payment_method=random.choice(payment_methods),
                category=category,
                subcategory=subcategory,
                merchant=merchant,
                amount=amount,
                status="Pending",
                is_recurring="No"
            )
        )
        transaction_id += 1

    for _ in range(refunded_count):
        transaction_type, category, subcategory, merchant, low, high = random.choice(refund_options)
        transaction_date = get_random_date_between(START_DATE, END_DATE)
        amount = random.uniform(low, high)

        rows.append(
            create_transaction(
                transaction_id=transaction_id,
                transaction_date=transaction_date,
                transaction_type=transaction_type,
                account_name=random.choice(accounts),
                payment_method=random.choice(payment_methods),
                category=category,
                subcategory=subcategory,
                merchant=merchant,
                amount=amount,
                status="Refunded",
                is_recurring="No"
            )
        )
        transaction_id += 1

    return rows, transaction_id


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    months = get_month_start_dates(START_DATE, END_DATE)

    rows = []
    transaction_id = 1

    generators = [
        generate_salary_transactions,
        generate_recurring_bills,
        generate_subscriptions,
        generate_food_transactions,
        generate_transport_transactions,
        generate_occasional_expenses,
        generate_side_income,
        generate_investment_income,
        generate_transfers
    ]

    for generator in generators:
        new_rows, transaction_id = generator(months, transaction_id)
        rows.extend(new_rows)

    new_rows, transaction_id = generate_pending_and_refunded_transactions(transaction_id)
    rows.extend(new_rows)

    rows.sort(key=lambda row: (row["transaction_date"], row["transaction_id"]))

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

    completed_income = sum(
        row["amount"]
        for row in rows
        if row["transaction_type"] == "Income" and row["status"] == "Completed"
    )

    completed_expenses = sum(
        row["amount"]
        for row in rows
        if row["transaction_type"] == "Expense" and row["status"] == "Completed"
    )

    net_savings = completed_income - completed_expenses
    savings_rate = net_savings / completed_income if completed_income else 0

    print(f"Completed income:  S${completed_income:,.2f}")
    print(f"Completed expenses: S${completed_expenses:,.2f}")
    print(f"Net savings:        S${net_savings:,.2f}")
    print(f"Savings rate:       {savings_rate:.1%}")


if __name__ == "__main__":
    main()