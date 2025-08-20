from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_input_text(driver):
    input_data = "qwerty"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    input_text = driver.find_element(By.ID, "id_text_string")
    input_text.send_keys(input_data)
    input_text.submit()
    result_input = driver.find_element(By.ID, "result-text")
    print(result_input.text)
    assert result_input.text == input_data


def test_fill_form(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("Alex")
    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("AQA Sraka")
    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("test@test.com")
    gender = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
    gender.click()
    tel_number = driver.find_element(By.ID, "userNumber")
    tel_number.send_keys("89111111111")
    birth_date = driver.find_element(By.ID, "dateOfBirthInput")
    birth_date.clear()
    birth_date.send_keys("10 Dec 1991")
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("qwerty")
    hobbies = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")
    hobbies.click()
    current_address = driver.find_element(By.ID, "currentAddress")
    current_address.send_keys("My address")
    input_state = driver.find_element(By.XPATH, "//div[text()='Select State']")
    input_state.click()
    select_state_nrc = driver.find_element(By.ID, "react-select-3-option-0")
    select_state_nrc.click()
    input_city = driver.find_element(By.XPATH, "//div[text()='Select City']")
    input_city.click()
    select_city_gurgaon = driver.find_element(By.ID, "react-select-4-option-1")
    select_city_gurgaon.click()
    button_submit = driver.find_element(By.ID, "submit")
    button_submit.click()

    # Печатаем данные
    student_name = driver.find_element(By.XPATH, "//td[text()='Student Name']/following-sibling::td")
    student_email = driver.find_element(By.XPATH, "//td[text()='Student Email']/following-sibling::td")
    gender_output = driver.find_element(By.XPATH, "//td[text()='Gender']/following-sibling::td")
    tel_output = driver.find_element(By.XPATH, "//td[text()='Mobile']/following-sibling::td")
    date_output = driver.find_element(By.XPATH, "//td[text()='Date of Birth']/following-sibling::td")
    subjects_output = driver.find_element(By.XPATH, "//td[text()='Subjects']/following-sibling::td")
    hobbies_output = driver.find_element(By.XPATH, "//td[text()='Hobbies']/following-sibling::td")
    address_output = driver.find_element(By.XPATH, "//td[text()='Address']/following-sibling::td")
    state_and_city = driver.find_element(By.XPATH, "//td[text()='State and City']/following-sibling::td")
    print(student_name.text, "\n", student_email.text, gender_output.text, "\n", tel_output.text, date_output.text,
          subjects_output.text, hobbies_output.text, "\n", address_output.text, state_and_city.text)


def test_select_language(driver):
    input_language = "Python"
    driver.get("https://www.qa-practice.com/elements/select/single_select")
    dropdown = driver.find_element(By.ID, "id_choose_language")
    select_language = Select(dropdown)
    select_language.select_by_visible_text(input_language)
    button = driver.find_element(By.ID, "submit-id-submit")
    button.click()
    output = driver.find_element(By.XPATH, "//p[text()='You selected']/following-sibling::p")
    assert input_language == output.text
