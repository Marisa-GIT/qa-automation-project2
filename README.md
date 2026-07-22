# Second-Project-Automation-Framework


A professional web automation testing framework built with **Python**, **Playwright**, and **Pytest**, following the **Page Object Model (POM)** design pattern and QA automation best practices.

This project was developed as part of my QA Automation portfolio to strengthen my skills in automated testing, framework architecture, and software quality engineering.

---

## 🚀 Features

- Automated web UI testing with Playwright
- Page Object Model (POM) architecture
- Pytest fixtures and parametrized tests
- Positive and negative login scenarios
- Data-driven testing
- HTML test reports
- Automatic screenshots on test failures
- Ready for Continuous Integration (CI)

---

## 🛠️ Technologies

- Python 3
- Playwright
- Pytest
- Pytest HTML
- Git & GitHub
- Visual Studio Code

---

## 📁 Project Structure

```text
qa-automation-project2/
│
├── pages/
│   ├── base_page.py
│   └── login_page.py
│
├── tests/
│   └── test_login.py
│
├── utils/
│   └── test_data.py
│
├── reports/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

### Architecture Overview

The framework follows the **Page Object Model (POM)** design pattern to improve readability, scalability, and maintainability.

- **pages/** → Contains page classes and reusable UI actions.
- **tests/** → Stores test cases only.
- **utils/** → Test data and helper utilities.
- **conftest.py** → Shared fixtures and test configuration.
- **reports/** → Generated execution reports and screenshots.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Marisa-GIT/Second-Project-Automation-Framework.git
```

Navigate to the project folder:

```bash
cd Second-Project-Automation-Framework
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

## ▶️ Running the Tests

Run all tests:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Generate an HTML report:

```bash
pytest --html=reports/report.html
```

---

## 📊 Test Reports

The framework supports HTML reporting through **pytest-html**.

After execution, reports are generated inside the **reports/** folder.

Example:

```text
reports/
├── report.html
├── test_login_invalid.png
└── test_login_valid.png
```

Screenshots are automatically captured whenever a test fails, making debugging easier.

---

## ✅ Current Test Coverage

### Login

- Successful login
- Invalid username
- Invalid password
- Data-driven login testing

---

## 🎯 Next Steps

The framework will continue evolving with:

- GitHub Actions CI/CD pipeline
- Allure Reports
- API Automation
- Database validation
- Cross-browser testing
- Environment configuration
- Logging system
- Code quality improvements
- Test tagging and execution filters

---

## 📚 Learning Goals

This project is part of my QA Automation learning journey, focused on developing industry-standard testing frameworks and best practices.

The objective is to build a scalable automation framework similar to those used by professional QA Automation Engineers.

---

## 👩‍💻 Author

**Isabel Vides**

QA Automation Engineer in Training

- GitHub: https://github.com/Marisa-GIT
- LinkedIn: www.linkedin.com/in/maria-isabel-vides-021531232