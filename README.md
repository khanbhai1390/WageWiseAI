# WageWise AI

**Earnings Transparency Assistant for Gig Workers and Daily-Wage Workers**

## Problem

Gig workers and daily-wage workers may find it difficult to understand whether their payments match their agreed working terms, bonuses and deductions.

## Solution

WageWise AI helps workers calculate expected earnings, compare them with actual payments, identify potential payment discrepancies and prepare professional payment clarification messages.

## Key Features

- Calculate hourly and per-delivery earnings.
- Include expected bonuses and agreed deductions.
- Compare expected net earnings with actual payments.
- Identify potential payment shortfalls.
- Save earnings audit records using SQLite.
- View previous audits on a dashboard.
- Generate downloadable PDF reports.
- Prepare polite payment clarification messages.

## Technology Stack

- Python
- Flask
- SQLite
- HTML, CSS and JavaScript
- ReportLab
- IBM watsonx Orchestrate (separately configured assistant prototype)

## How It Works

1. Enter worker and payment details.
2. Select the payment model.
3. Enter hours or deliveries, rates, bonuses and deductions.
4. Enter the actual payment received.
5. WageWise calculates expected net earnings and compares the result.
6. Review the result and download a PDF report.

## Run Locally

Install the dependencies:

```bash
py -m pip install -r requirements.txt
```

Start the application:

```bash
py app.py
```

Open in your browser:

```text
http://127.0.0.1:5000
```

## Demo Data

The project can be demonstrated using sample worker and payment details. No real employer or payment-platform integration is required for the demonstration.

## Important Disclaimer

WageWise AI provides calculations based on information entered by the user. It does not independently verify payroll records, determine legal violations or establish that an employer has underpaid a worker.

## Project Goal

To make earnings easier to understand and help workers communicate about payment differences with greater clarity and confidence.