# Project Notes

## Purpose

This project is a personal Tableau learning project.

It uses fully synthetic personal finance data and is not connected to any real company, organisation, client, donor, financial institution, or personal bank account.

The goal is to practise building business-style dashboards using safe and generic data.

## Learning Goals

- Learn Tableau from scratch
- Connect Tableau to CSV data
- Understand dimensions and measures
- Create calculated fields
- Build KPI cards
- Build line charts and bar charts
- Create text tables
- Use dashboard filters
- Separate summary dashboards from detailed transaction views
- Practise dashboard storytelling
- Document a dashboard project clearly

## Dashboard Questions

The dashboards are designed to answer:

1. How much income was received?
2. How much was spent?
3. What is the net savings amount?
4. What is the savings rate?
5. Which categories have the highest expenses?
6. Which merchants have the highest spending?
7. Which months had the highest spending?
8. Which income categories contributed the most?
9. How do income and expenses compare over time?
10. Which transactions make up the detailed expense records?

## Dashboard Pages

### Financial Overview

A high-level dashboard showing overall income, expenses, net savings, savings rate, and transaction volume.

### Expense Analysis

A summary dashboard focused on completed expenses by month, category, merchant, and recurring status.

### Expense Transaction Details

A detailed table-style dashboard showing row-level completed expense transactions.

### Income & Savings Analysis

A dashboard focused on completed income, net savings, income versus expenses, and savings rate trends.

## Design Notes

### Summary Dashboards

Summary dashboards should focus on KPIs and charts. They should not contain too many row-level details because that can make the dashboard cluttered.

### Detail Dashboards

Transaction-level data is placed in a separate dashboard to give the table enough space and allow users to filter specific records.

### Filters

Filters should be used carefully.

For example, applying a category filter globally can cause expense sheets or income sheets to show zero if only the wrong category values are selected.

### Calculated Fields

Calculated fields are used to separate completed income, completed expenses, and completed savings. This makes the dashboard more stable and easier to understand.

## Future Improvements

Possible future improvements:

- Improve synthetic data realism
- Add a budget analysis dashboard
- Add monthly salary patterns
- Add realistic recurring bills
- Add dashboard screenshots to README
- Publish the workbook to Tableau Public
- Add a project write-up explaining key insights