# SWE6301 Donation Management System

## Overview

This project was developed as part of the SWE6301 Agile Programming module.

The system represents a simple non-profit donation management application developed using Python and Behaviour-Driven Development (BDD).

## Features

- Record donor information
- Record donations
- Validate donation amounts
- Calculate total donations
- Count recorded donations

## Technologies Used

- Python 3.11
- Behave (BDD Framework)
- Git
- GitHub

## BDD Scenarios

### Successful Donation

Given the donation system is running

When a donor contributes a valid amount

Then the donation should be recorded successfully

### Multiple Donations

Given the donation system is running

When multiple donors contribute

Then the total donations should be updated correctly

### Invalid Donation

Given the donation system is running

When a donor enters an invalid amount

Then an error message should be displayed

## Project Structure

```text
SWE6301_Donation_System
│
├── Donation_System.py
├── main.py
├── requirements.txt
├── README.md
│
└── features
    ├── donation.feature
    └── steps
        └── donation_steps.py
```

## Running the Application

```bash
python main.py
```

## Running BDD Tests

```bash
behave
```

## Author

Mario Balakchiev

SWE6301 Agile Programming