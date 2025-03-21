from playwright.sync_api import Page
import pytest

#@pytest.mark.skip_browser("chromium")
#@pytest.mark.only_browser("chromium")
def test_title(page: Page):
    page.goto("https://www.saucedemo.com/")
    assert page.title() == "Swag Labs"


def test_inner_text(page: Page):
    page.goto("https://www.saucedemo.com/inventory.html")
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."