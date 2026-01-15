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
    link = page.locator("#new-page-button")
    with context.expect_page() as new_page_event:
        link.click()
    new_page = new_page_event.value
    result_text = new_page.locator("#result-text")
    expect(result_text).to_have_text("I am a new page in a new tab")
    new_page.close()
    expect(link).to_be_enabled()


def test_color_text(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    button = page.locator("#colorChange")
    expect(button).to_have_css("color", "rgb(220, 53, 69)")
    button.click()
