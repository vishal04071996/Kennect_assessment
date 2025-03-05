# Kennect_assessment - Selenium Python Test Automation

## Project Overview
This is a Selenium-based test automation framework for testing the ScopeX Money web application: [Gor Pathology Dashboard](https://gor-pathology.web.app/dashboard).

The framework is built using **Selenium WebDriver, Pytest, and Python** and supports logging, reporting, and test data handling.

---

## Project Structure
```
Kennect_assessment/
│-- Base_Page/
│   │-- __init__.py
│   │-- AddPatient_page.py
│   │-- Login_page.py
│-- configuration/
│   │-- config.ini
│-- logs/
│-- reports/
│-- screenshots/
│-- test_cases/
│   │-- __init__.py
│   │-- conftest.py
│   │-- test_loginPage.py
│   │-- test_Patient.py
│-- test_data/
│-- utilities/
│   │-- __init__.py
│   |
│   │-- read_properties.py
│-- venv/
│-- main.py
│-- README.md
```

---

## Setup Instructions
### 1️⃣ Prerequisites
- Install **Python 3.8+**
- Install **Google Chrome**
- Install **ChromeDriver** (Ensure it matches your Chrome version)
- Install virtual environment (Optional but recommended)

### 2️⃣ Clone the Repository
```bash
git clone <repo-url>
cd Kennect_assessment
```

### 3️⃣ Create & Activate Virtual Environment (Optional)
```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Running Test Cases
### Run All Tests
```bash
pytest --html=reports/test_report.html --self-contained-html
```

### Run Specific Test
```bash
pytest test_cases/test_login.py --html=reports/test_report.html --self-contained-html
```

### Run Tests with Logging Enabled
```bash
pytest --log-cli-level=INFO --html=reports/test_report.html --self-contained-html
```

---

## Viewing the HTML Report
After running tests, open the generated **HTML report** in a browser:
```bash
open reports/test_report.html  # Mac/Linux
start reports/test_report.html  # Windows
```

---

## Configuration
- The **config.ini** file stores environment variables such as base URL, credentials, and timeout settings.
- Modify **read_properties.py** in `utilities/` to read configurations dynamically.

---

## Logging & Screenshots
- Logs are stored in the `logs/` folder.
- Failed test screenshots are saved in the `screenshots/` folder automatically.

---

## Additional Notes
- Follow POM (Page Object Model) in `base_page/`.
- Use `conftest.py` for fixture management.
- Ensure correct `test_data/` is provided before execution.



