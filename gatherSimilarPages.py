from selenium import webdriver

path_to_webdriver = '/Users/ysenkiv/Code/access files/chromedriver'
path_to_credentials = '/Users/ysenkiv/Code/access files/personal/instagram/personalProfile.txt'
allow_cookies_button_xpath = '//*[@class="aOOlW  bIiDR  "]'
login_fields = '//*[@class="_2hvTZ pexuQ zyHYP"]'

webdriver = webdriver.Chrome(executable_path=path_to_webdriver)
webdriver.maximize_window()


with open(path_to_credentials) as credentials_file:
    lines = credentials_file.readlines()
    username = lines[0].strip()
    password = lines[1].strip()

webdriver.get('https://www.instagram.com/')
webdriver.find_element_by_xpath(allow_cookies_button_xpath).click()
login_form = webdriver.find_element_by_xpath(login_fields)
login_form[0].sendkeys(username)
login_form = webdriver.find_element_by_xpath(login_fields)
login_form[1].sendkeys(password)

