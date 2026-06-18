import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    # Detecta automáticamente si está en GitHub Actions (CI)
    is_ci = os.getenv("CI") == "true"
    
    with sync_playwright() as p:
        # Si está en CI corre en headless=True, si es local corre en headless=False
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
            # Creamos la subcarpeta 'assets' de forma segura si no existe
            os.makedirs("reports/assets", exist_ok=True)
            
            # Guardamos la captura dentro de la subcarpeta organizada
            page.screenshot(
                path=f"reports/assets/{item.name}.png"
            )