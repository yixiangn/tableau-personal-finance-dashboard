# Tableau Calculations

This document records the main Tableau calculated fields used in the personal finance dashboard project.

The calculations are designed for synthetic transaction data and are used to separate completed income, completed expenses, net savings, and savings rate.

---

## Income Amount

```tableau
IF [transaction_type] = "Income" AND [status] = "Completed" THEN [amount] ELSE 0 END
```

### Purpose

Calculates completed income amount only.

This excludes:

- Expenses
- Transfers
- Pending transactions
- Refunded transactions

---

## Expense Amount

```tableau
IF [transaction_type] = "Expense" AND [status] = "Completed" THEN [amount] ELSE 0 END
```

### Purpose

Calculates completed expense amount only.

This excludes:

- Income
- Transfers
- Pending transactions
- Refunded transactions

---

## Net Amount

```tableau
IF [status] = "Completed" THEN [signed_amount] ELSE 0 END
```

### Purpose

Calculates the completed signed transaction amount.

This is used for net cashflow-style calculations where:

- Income is positive
- Expense is negative
- Transfer is zero

---

## Completed Transaction Count

```tableau
IF [status] = "Completed" THEN [transaction_id] END
```

### Purpose

Returns the transaction ID only when the transaction status is completed.

This field can be counted using `COUNTD()` to get the number of completed transactions.

---

## Completed Transaction Count KPI

```tableau
COUNTD(
    IF [status] = "Completed" THEN [transaction_id] END
)
```

### Purpose

Counts the number of unique completed transactions.

---

## Savings Rate

```tableau
IF SUM([Income Amount]) = 0 THEN 0
ELSE SUM([Net Amount]) / SUM([Income Amount])
END
```

### Purpose

Calculates the percentage of income retained after expenses.

Formula:

```text
Savings Rate = Net Amount / Income Amount
```

---

# Expense-Specific Calculations

## Completed Expense Amount

```tableau
IF [transaction_type] = "Expense"
AND [status] = "Completed"
THEN [amount]
ELSE 0
END
```

### Purpose

Calculates only completed expense transactions.

Used in:

- Total expense KPI
- Monthly expense trend
- Expense by category
- Top merchants by expense
- Recurring vs non-recurring expense analysis

---

## Completed Expense Transaction ID

```tableau
IF [transaction_type] = "Expense"
AND [status] = "Completed"
THEN [transaction_id]
END
```

### Purpose

Returns transaction IDs for completed expense transactions only.

Used for counting completed expense transactions.

---

## Completed Expense Count KPI

```tableau
COUNTD([Completed Expense Transaction ID])
```

### Purpose

Counts the number of unique completed expense transactions.

---

## Average Expense Amount

```tableau
IF COUNTD([Completed Expense Transaction ID]) = 0 THEN 0
ELSE SUM([Completed Expense Amount]) / COUNTD([Completed Expense Transaction ID])
END
```

### Purpose

Calculates the average amount per completed expense transaction.

Formula:

```text
Average Expense Amount = Total Completed Expense Amount / Number of Completed Expense Transactions
```

---

# Income-Specific Calculations

## Completed Income Amount

```tableau
IF [transaction_type] = "Income"
AND [status] = "Completed"
THEN [amount]
ELSE 0
END
```

### Purpose

Calculates only completed income transactions.

Used in:

- Total income KPI
- Monthly income trend
- Income by category
- Income versus expenses analysis

---

## Completed Income Transaction ID

```tableau
IF [transaction_type] = "Income"
AND [status] = "Completed"
THEN [transaction_id]
END
```

### Purpose

Returns transaction IDs for completed income transactions only.

Used for counting completed income transactions.

---

## Completed Income Count KPI

```tableau
COUNTD([Completed Income Transaction ID])
```

### Purpose

Counts the number of unique completed income transactions.

---

## Average Income Amount

```tableau
IF COUNTD([Completed Income Transaction ID]) = 0 THEN 0
ELSE SUM([Completed Income Amount]) / COUNTD([Completed Income Transaction ID])
END
```

### Purpose

Calculates the average amount per completed income transaction.

Formula:

```text
Average Income Amount = Total Completed Income Amount / Number of Completed Income Transactions
```

---

# Savings Calculations

## Completed Net Savings

```tableau
SUM([Completed Income Amount]) - SUM([Completed Expense Amount])
```

### Purpose

Calculates total savings after completed expenses are subtracted from completed income.

Formula:

```text
Completed Net Savings = Completed Income - Completed Expenses
```

---

## Completed Savings Rate

```tableau
IF SUM([Completed Income Amount]) = 0 THEN 0
ELSE [Completed Net Savings] / SUM([Completed Income Amount])
END
```

### Purpose

Calculates the percentage of completed income retained after completed expenses.

Formula:

```text
Completed Savings Rate = Completed Net Savings / Completed Income
```

---

## Completed Signed Amount

```tableau
IF [status] = "Completed" THEN [signed_amount] ELSE 0 END
```

### Purpose

Creates a row-level completed signed amount.

Used for monthly net savings and cashflow trend analysis.

---

## Monthly Savings Rate

```tableau
IF SUM([Completed Income Amount]) = 0 THEN 0
ELSE SUM([Completed Signed Amount]) / SUM([Completed Income Amount])
END
```

### Purpose

Calculates the savings rate at the current level of detail in the view, usually by month.

When `transaction_date` is placed on Columns as Month, this field shows savings rate by month.

---

# Notes on Filter Design

The dashboards rely mostly on calculated fields instead of only dashboard filters.

This prevents common Tableau issues such as:

- Income dashboards accidentally filtering out expenses needed for comparison charts
- Expense dashboards being affected by income-only category filters
- KPI cards showing zero because dashboard filters were applied globally

Recommended approach:

- Use calculated fields to define income, expenses, and completed transactions.
- Use dashboard filters mainly for user exploration.
- Be careful when applying filters to `All Using This Data Source`.
- For comparison charts such as `Monthly Income vs Expenses`, avoid filtering to only `Income` or only `Expense`.