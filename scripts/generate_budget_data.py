import csv
import random
from datetime import datetime
from pathlib import Path

random.seed(42)

OUTPUT_PATH = Path("data/budgets.csv")

START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 12, 31)


budget_categories = {
    "Food": {
        "budget_category": "Essentials",
        "base_budget": 650,
        "variation": 80
    },
    "Transport": {
        "budget_category": "Essentials",
        "base_budget": 220,
        "variation": 50
    },
    "Bills": {
        "budget_category": "Essentials",
        "base_budget": 450,
        "variation": 60
    },
    "Health": {
        "budget_category": "Essentials",
        "base_budget": 180,
        "variation": 60
    },
    "Shopping": {
        "budget_category": "Lifestyle",
        "base_budget": 350,
        "variation": 120
    },
    "Entertainment": {
        "budget_category": "Lifestyle",
        "base_budget": 180,
        "variation": 60
    },
    "Education": {
        "budget_category": "Growth",
        "base_budget": 160,
        "variation": 70
    }
}


def get_months(start_date, end_date):
    months = []
    current = datetime(start_date.year, start_date.month, 1)

    while current <= end_date:
        months.append(current)

        if current.month == 12:
            current = datetime(current.year + 1, 1, 1)
        else:
            current = datetime(current.year, current.month + 1, 1)

    return months


def generate_budget_rows():
    rows = []
    months = get_months(START_DATE, END_DATE)

    budget_id = 1

    for month_start in months:
        month = month_start.strftime("%Y-%m")
        year = month_start.year
        month_number = month_start.month

        for category, config in budget_categories.items():
            base_budget = config["base_budget"]
            variation = config["variation"]

            budget_amount = base_budget + random.randint(-variation, variation)

            # Add slight seasonal variation to make the dataset more realistic.
            if category == "Shopping" and month_number in [6, 11, 12]:
                budget_amount += random.randint(80, 180)

            if category == "Entertainment" and month_number in [6, 12]:
                budget_amount += random.randint(40, 100)

            if category == "Food" and month_number in [1, 12]:
                budget_amount += random.randint(50, 120)

            if category == "Education" and month_number in [1, 8]:
                budget_amount += random.randint(60, 150)

            budget_amount = max(budget_amount, 50)

            rows.append({
                "budget_id": f"BUD{budget_id:05d}",
                "month": month,
                "year": year,
                "month_number": month_number,
                "category": category,
                "budget_category": config["budget_category"],
                "budget_amount": round(budget_amount, 2)
            })

            budget_id += 1

    return rows


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    rows = generate_budget_rows()

    fieldnames = [
        "budget_id",
        "month",
        "year",
        "month_number",
        "category",
        "budget_category",
        "budget_amount"
    ]

    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    total_budget = sum(row["budget_amount"] for row in rows)

    print(f"Generated {len(rows)} rows at {OUTPUT_PATH}")
    print(f"Total annual budget: S${total_budget:,.2f}")

    print("\nBudget categories generated:")
    for category in budget_categories:
        category_total = sum(
            row["budget_amount"]
            for row in rows
            if row["category"] == category
        )
        print(f"- {category}: S${category_total:,.2f}")


if __name__ == "__main__":
    main()