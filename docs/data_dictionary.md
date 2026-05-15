# Data Dictionary

This document describes the fields used in the synthetic personal finance dataset.

The dataset is fully synthetic and is used only for Tableau dashboard learning and portfolio practice.

## Dataset: `transactions.csv`

| Column | Data Type | Description | Example |
|---|---|---|---|
| `transaction_id` | Text | Unique identifier for each transaction. | `TXN00001` |
| `transaction_date` | Date | Date when the transaction occurred. | `2025-01-05` |
| `transaction_type` | Text | Main type of transaction. | `Income`, `Expense`, `Transfer` |
| `account_name` | Text | Account used for the transaction. | `Main Savings` |
| `payment_method` | Text | Payment method used for the transaction. | `Card`, `Bank Transfer`, `Cash`, `PayNow`, `GIRO` |
| `category` | Text | Main transaction category. | `Food`, `Salary`, `Bills` |
| `subcategory` | Text | More detailed category under the main category. | `Groceries`, `Monthly Salary`, `Phone Bill` |
| `merchant` | Text | Merchant, organisation, or source associated with the transaction. | `FairPrice`, `Company Payroll`, `Singtel` |
| `description` | Text | Short transaction description. | `Groceries transaction at FairPrice` |
| `amount` | Decimal Number | Absolute transaction amount. This value is always positive. | `45.80` |
| `signed_amount` | Decimal Number | Signed amount used for net calculations. Income is positive, expense is negative, and transfer is zero. | `-45.80` |
| `currency` | Text | Currency of the transaction. | `SGD` |
| `status` | Text | Transaction status. | `Completed`, `Pending`, `Refunded` |
| `month` | Text / Date Group | Year and month of the transaction. | `2025-01` |
| `year` | Whole Number | Year of the transaction. | `2025` |
| `is_recurring` | Text | Indicates whether the transaction is recurring. | `Yes`, `No` |
| `budget_category` | Text | Higher-level budget grouping. | `Essentials`, `Lifestyle`, `Income`, `Growth` |

## Transaction Type Definitions

| Transaction Type | Description |
|---|---|
| `Income` | Money received, such as salary, side income, or investment income. |
| `Expense` | Money spent, such as food, transport, shopping, bills, health, and education. |
| `Transfer` | Movement of money between accounts. Transfers are assigned a signed amount of zero to avoid affecting net savings. |

## Status Definitions

| Status | Description |
|---|---|
| `Completed` | Transaction is finalised and included in main dashboard calculations. |
| `Pending` | Transaction is not finalised and is excluded from main KPI calculations. |
| `Refunded` | Transaction has been refunded and is excluded from main KPI calculations. |

## Budget Category Definitions

| Budget Category | Description | Example Categories |
|---|---|---|
| `Income` | Incoming money sources. | Salary, Side Income, Investment |
| `Essentials` | Necessary spending. | Food, Transport, Bills, Health |
| `Lifestyle` | Discretionary spending. | Shopping, Entertainment |
| `Growth` | Self-improvement or learning-related spending. | Education |

## Notes

- `amount` is used when analysing absolute transaction values.
- `signed_amount` is used when calculating net savings or cashflow.
- Most Tableau dashboards focus on `Completed` transactions only.
- Pending and refunded transactions are intentionally excluded from core KPIs.