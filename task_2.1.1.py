import math, time
from selenium import webdriver


link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)

input = browser.find_element_by_css_selector('#answer')
input.send_keys(y)

option = browser.find_element_by_css_selector('#robotCheckbox')
option.click()

option1 = browser.find_element_by_css_selector('#robotsRule')
option1.click()

button = browser.find_element_by_css_selector('body > div > form > button')
button.click()

time.sleep(5)

browser.quit()