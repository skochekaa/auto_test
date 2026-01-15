from playwright.sync_api import Page


def test_login_fom(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Form Authentication").click()
    page.get_by_role("textbox", name="username").fill("username")
    page.get_by_role("textbox", name="password").fill("password")
    page.get_by_role("button").click()


def test_fill_form(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")
    page.locator("[id='firstName']").fill("Alex")
    page.locator("[id='lastName']").fill("Sk")
    page.locator("[id='userEmail']").fill("test@test.com")
    page.locator("//label[@for='gender-radio-1']").click()
    page.locator("[id='userNumber']").fill("1234567890")
    b_date = page.locator("[id='dateOfBirthInput']")
    b_date.press("Control+a")
    b_date.press("Backspace")
    b_date.fill("28 Dec 2020")
    page.locator("[id='subjectsContainer']").fill("Subject my text")
    page.locator("[id='hobbies-checkbox-1']").click()
    page.locator("[id='currentAddress']").fill("My current address")
    page.locator("//*[@id='state']/div[1]").click()
    page.locator("//div[text()='NCR']").click()
    page.locator("#submit").click()
