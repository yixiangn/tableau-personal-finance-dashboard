# Validation Checks

This document records validation checks used to confirm that the Tableau dashboard calculations match the generated synthetic CSV dataset.

## Validation Purpose

The goal of validation is to ensure that the Tableau dashboards display accurate totals based on the underlying `transactions.csv` file.

The dashboard should not only look correct visually, but also match the expected calculation logic.

## Source of Truth

The Python data generation script prints summary totals after generating the dataset, whilst summary totals on Tableau are evaluated through the formulas below:


##### Completed Income

**Python logic**

![Completed Income Python](Images/CompletedIncome_python.png)

**Tableau logic**

![Completed Income Tableau](Images/CompletedIncome_tableau.png)

---

##### Completed Expenses

**Python logic**

![Completed Expense Python](Images/CompletedExpense_python.png)

**Tableau logic**

![Completed Expense Tableau](Images/CompletedExpense_tableau.png)

---

##### Net Savings

**Python logic**

![Net Savings Python](Images/NetSavings_python.png)

**Tableau logic**

![Net Savings Tableau](Images/NetSavings_tableau.png)

---

##### Savings Rate

**Python logic**

![Savings Rate Python](Images/SavingsRate_python.png)

**Tableau logic**

![Savings Rate Tableau](Images/SavingsRate_tableau.png)


#### Validation Results
| Metric | Python Output | Tableau Output | Status |
|---|---:|---:|---|
| Completed Income | S$48,651.67 | S$48,652 | Pass |
| Completed Expenses | S$22,789.77 | S$22,790 | Pass |
| Net Savings | S$25,861.90 | S$25,862 | Pass |
| Savings Rate | 53.2%| 53.2% | Pass |