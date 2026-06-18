import pytest
from pages.login_page import LoginPage
from utils.test_data import LOGIN_DATA

def test_login_invalido(page):  
    login_page = LoginPage(page)

    login_page.navigate("https://practicetestautomation.com/practice-test-login/"
                        )

    login_page.login("user_fake", "3445")

    error = login_page.get_error_message()

    assert "your username is invalid!" in error.lower()

def test_login_exitoso(page):
    login_page = LoginPage(page)

    login_page.navigate("https://practicetestautomation.com/practice-test-login/"
                        )

    login_page.login("student", "Password123")

    assert page.url == "https://practicetestautomation.com/logged-in-successfully/"

@pytest.mark.parametrize(
    "username, password, expected",
    [
        ("student", "Password123", True),
        ("user_fake", "3445", False),
        ("student", "wrong_pass", False),
    ]
)
def test_login(page, username, password, expected):
    login_page = LoginPage(page)

    login_page.navigate("https://practicetestautomation.com/practice-test-login/"
                        )

    login_page.login(username, password)

    if expected:
        assert page.url == "https://practicetestautomation.com/logged-in-successfully/"
    else:
        error = login_page.get_error_message()
        assert "your username is invalid!" in error.lower() or "your password is invalid!" in error.lower()

# assert False para simular un fallo en el test y verificar que se capture correctamente el error.