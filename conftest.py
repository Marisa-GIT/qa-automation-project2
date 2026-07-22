import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
 
    is_ci = os.getenv("CI") == "true"
    
    with sync_playwright() as p:
    
        browser = p.chromium.launch(headless=is_ci)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
      
            os.makedirs("reports/assets", exist_ok=True)
            
           
            page.screenshot(
                path=f"reports/assets/{item.name}.png"
            )