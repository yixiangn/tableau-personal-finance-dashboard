# Tableau Personal Finance Dashboard

This project is a Tableau dashboard built using synthetic personal finance transaction data.

The goal of the project is to practise data visualisation, dashboard design, calculated fields, filters, KPI cards, and financial trend analysis using a safe, generic dataset.

## Project Overview

The dashboard analyses income, expenses, savings, recurring spending, merchant activity, and transaction-level details.

The dataset is fully synthetic and does not contain any real personal, company, client, donor, or financial information.

## Tools Used

- Tableau Public / Tableau Desktop
- Python
- CSV
- GitHub

## Database

The dataset is generated using `scripts/generate_synthetic_data.py`.

Output file:
- data/transactions.csv

## Repository Structure
tableau-personal-finance-dashboard
- data
    - transactions.csv
- docs
    - data_dictionary.md
    - project_notes.md
    - tableau_calculations.md
- scripts
  - generate_synthetic_data.py
- tableau
    - personal_finance_dashboard.twbx
- README.md
- .gitignore

## Dataset
The dataset contains synthetic personal finance transactions with fields such as:

- transaction ID
- transaction date
- transaction type
- account name
- payment method
- category
- subcategory
- merchant
- amount
- signed amount
- status
- recurring flag
- budget category

## Dashboards Built
#### Financial Overview
Provides a high-level summary of income, expenses, net savings, savings rate, and transaction volume.

Main features:

- Total income KPI
- Total expenses KPI
- Net savings KPI
- Savings rate KPI
- Transaction count KPI
- Monthly net cashflow trend
- Expenses by category

#### Expense Analysis
Shows completed expenses by month, category, merchant, and recurring status.

Main features:
- Total completed expenses
- Number of completed expense transactions
- Average expense amount
- Monthly expense trend
- Expense breakdown by category
- Top merchants by expense
- Recurring vs non-recurring expenses

#### Expense Transaction Details

Provides a row-level view of completed expense transactions.
Main features:

- Transaction date
- Merchant
- Category
- Subcategory
- Payment method
- Amount
- Filters for detailed exploration

#### Income & Savings Analysis

Analyses completed income, monthly savings, income versus expenses, and savings rate trends.

Main features:

- Total completed income
- Income transaction count
- Net savings
- Savings rate
- Monthly income trend
- Income by category
- Monthly income versus expenses
- Monthly net savings
- Monthly savings rate

## Key Tableau Skills Practised

This project was used to practise:

- Connecting Tableau to CSV data
- Creating calculated fields
- Building KPI cards
- Creating line charts
- Creating bar charts
- Creating text tables
- Using filters across worksheets and dashboards
- Applying filters to selected worksheets
- Formatting financial values and percentages
- Structuring a dashboard for business-style analysis
- Key Design Decisions

#### Summary and Detail Dashboards Are Separated

The project separates high-level dashboard views from row-level transaction details. This avoids cluttering summary dashboards with overly granular data.

#### Only Completed Transactions Were Used

Pending and Refunded transactions were excluded from this practice to avoid confusion and were put in place in case of further development.

####  Income and Expense Logic Uses Calculated Fields

Instead of relying only on dashboard filters, income and expense logic is handled through Tableau calculated fields. This makes the dashboard more stable and reduces accidental filter conflicts.

#### How to Use This Project
- Clone the repository.
- Open the Tableau workbook in the tableau/ folder.
- Review the dashboard pages.
- Use the filters to explore the synthetic transaction data.
- Regenerate the dataset using the Python script if needed.

## Status
Initial dashboard build completed.

Future improvements may include:
- More realistic synthetic data generation
- Monthly salary patterns
- Recurring bills
- Budget tracking dashboard
- Better dashboard styling