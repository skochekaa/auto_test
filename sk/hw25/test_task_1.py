from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_cart(driver):
    driver.implicitly_wait(3)
    driver.get("https://www.demoblaze.com/index.html")
    link = driver.find_element(By.LINK_TEXT, "Samsung galaxy s6")
    ActionChains(driver).key_down(Keys.COMMAND).click(link).key_up(Keys.COMMAND).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_cart = driver.find_element(By.LINK_TEXT, "Add to cart")
    add_to_cart.click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    cart = driver.find_element(By.LINK_TEXT, "Cart")
    cart.click()
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//tbody[@id='tbodyid']//td[text()='Samsung galaxy s6']")
        )
    )
    products = driver.find_element(By.XPATH, "//tbody[@id='tbodyid']//td[text()='Samsung galaxy s6']")
    assert products.text == "Samsung galaxy s6"


def test_add_to_compares(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    cards = driver.find_elements(By.CLASS_NAME, "product-item-info")
    add_to_compare = cards[0].find_element(By.CSS_SELECTOR, "[title='Add to Compare']")
    actions = ActionChains(driver)
    actions.move_to_element(cards[0]).click(add_to_compare).perform()
    wait = WebDriverWait(driver, 5)
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='compare-items']//a[text()='Push It Messenger Bag']")
        )
    )
    compare_products = driver.find_element(By.XPATH, "//*[@id='compare-items']//a[text()='Push It Messenger Bag']")
    assert compare_products.text == "Push It Messenger Bag"
