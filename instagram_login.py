from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

curent_working_account = open('/Users/ysenkiv/Code/my projects/instagram/curent_working_account.txt', 'r')
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


# <editor-fold desc="get credentials">
with open(path_to_credentials) as credentials_file:
    lines = credentials_file.readlines()
    username = lines[0].strip()
    password = lines[1].strip()
# </editor-fold>

browser = webdriver.Firefox()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')

login_field = browser.find_element_by_css_selector("input[name='username']")
login_field.send_keys(username)
login_field = browser.find_element_by_css_selector("input[name='password']")
login_field.send_keys(password)
browser.find_element_by_xpath("//button[@type='submit']").click()
click_if_exists_else_pass(remember_me_button_xpath)
click_if_exists_else_pass(notifications_not_now_button_xpath)

