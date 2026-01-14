from playwright.sync_api import Page, expect, Dialog, BrowserContext
from time import sleep


def test_alert(page: Page):
    page.on("dialog", lambda alert: alert.accept())
    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.get_by_role("link", name="Click").click()
    text = page.locator("#result-text")
    expect(text).to_have_text("Ok")


def test_tabs(page: Page, context: BrowserContext):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
