from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# <editor-fold desc="default code">
curent_working_account = open('/Users/ysenkiv/Code/my projects/instagram automation/curent_working_account.txt', 'r')
account = curent_working_account.read()
print(account)

# <editor-fold desc="variables">
# account_credentials_file_name = 'dogarea'  # input('enter account_credentials_file_name: ')
path_to_credentials = f'/Users/ysenkiv/Code/access files/personal/instagram/{account}.txt'
remember_me_button_xpath = '//*[@class="sqdOP  L3NKy   y3zKF     "]'
notifications_not_now_button_xpath = '//*[@class="aOOlW   HoLwm "]'
# </editor-fold>


def click_if_exists_else_pass(xpath):
    try:
        browser.find_element_by_xpath(xpath).click()
    except NoSuchElementException:
        pass

def test_login_page(browser):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login("<your username>", "<your password>")

    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0


# <editor-fold desc="get credentials">
with open(path_to_credentials) as credentials_file:
    lines = credentials_file.readlines()
    username = lines[0].strip()
    password = lines[1].strip()
# </editor-fold>

browser = webdriver.Firefox()
browser.maximize_window()
browser.implicitly_wait(5)
# </editor-fold>


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        click_if_exists_else_pass(remember_me_button_xpath)
        click_if_exists_else_pass(notifications_not_now_button_xpath)
        sleep(5)


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        self.browser.find_element_by_xpath("//a[text()='Log in']").click()
        sleep(2)
        return LoginPage(self.browser)


home_page = HomePage(browser)
login_page = LoginPage(browser)
login_page.login(username, password)
