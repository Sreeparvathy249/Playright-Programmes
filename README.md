# Python Playwright Automation Testing

## Project Overview
This project contains web automation test scripts developed using **Python, Playwright, and Pytest**.

The purpose is to practise browser automation, web application testing, test validation, and HTML test reporting.

## Technologies Used
- Python
- Playwright
- Pytest
- Pytest-HTML
- VS Code

## Project Structure

```text
Playright-Programmes/
│
├── Test/
│   ├── test_login.py
│   ├── test_google.py
│   ├── test_complete_automation.py
│   ├── test_playwright_home.py
│   └── test_otp_login.py
│
├── Report/
│   ├── python_report.html
│   ├── all_tests_report.html
│   └── otp_report.html
│
├── venv/
│
└── README.md
```

## Installation

Install the required packages:

```bash
pip install pytest
pip install playwright
pip install pytest-playwright
pip install pytest-html
```

Install Playwright browsers:

```bash
playwright install
```

## Run Tests

Run all test files:

```bash
pytest Test/ --headed -v
```

Run an individual test:

```bash
pytest Test/test_login.py --headed -v
```

## Generate HTML Reports

Generate a report for all test files:

```bash
pytest Test/ --headed -v --html=Report/all_tests_report.html --self-contained-html
```

Generate an individual test report:

```bash
pytest Test/test_login.py --html=Report/python_report.html --self-contained-html
```

Generate an OTP test report:

```bash
pytest Test/test_otp_login.py --html=Report/otp_report.html --self-contained-html
```

## View HTML Reports

Start the local server:

```bash
python -m http.server 8000
```

Open the reports in your browser:

- All tests: `http://localhost:8000/Report/all_tests_report.html`
- Login: `http://localhost:8000/Report/python_report.html`
- OTP: `http://localhost:8000/Report/otp_report.html`

## Test Results

Pytest provides the following test results:

- **Passed:** Test executed successfully.
- **Failed:** Test did not meet the expected result.
- **Skipped:** Test was not executed.

HTML reports provide detailed test execution results and failure information.

## Project Goal

To develop practical skills in Python-based web automation testing using Playwright and Pytest, including test execution, assertions, debugging, and HTML reporting.
