from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://market.yandex.by/"
def test_open_market():
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()
    button = browser.find_element(By.XPATH, '//div[@data-apiary-widget-name="@MarketNode/HeaderNav"]//a')
    button.click()


    window_before = browser.window_handles[0]
    window_after = browser.window_handles[1]
    browser.switch_to_window(window_after)
    button_1 = browser.find_element_by_id('passp-field-login')
    button_1.send_keys("USER")
    button_2 = browser.find_element(By.XPATH, '//div[@class="passp-button passp-sign-in-button v5"]//button')
    button_2.click()
    button_3 = browser.find_element(By.ID, 'passp-field-passwd')
    button_3.send_keys("Password")
    button_4 = browser.find_element(By.XPATH, '//div[@class="passp-button passp-sign-in-button v5"]//button')
    button_4.click()
    browser.switch_to_window(window_before)

def test_categories(browser):
    top_categories = browser.find_element_by_class_name("SyJTASPsrT _3mU1ofltUh _1fKg8X_Xiz")
    return top_categories

def test_open_category(browser):
    window_main = browser.window_handles[0]
    window_category = browser.window_handles[1]
    button_category= browser.find_element_by_link_text("/catalog--tovary-so-skidkoi/61522")
    button_category.click()
    browser.switch_to_window(window_category)
    browser.switch_to_window(window_main)

def test_logout(browser):
    button_logout = browser.find_element_by_class_name("_2fIRnyy84I")
    button_logout.click()
    button_logout_1 = browser.find_element_by_link_text("//passport.yandex.by/passport?mode=logout&yu=8168804731599045394&retpath=https://market.yandex.by/?clid=703")
    button_logout_1.click()
    browser.quit()
