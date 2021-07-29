from selenium import webdriver
import math



link = ' http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector('body > form > div > div > button')
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector('#input_value')
x = x_element.text
y = calc(x)

input = browser.find_element_by_css_selector('#answer')
input.send_keys(y)

button1 = browser.find_element_by_css_selector('body > form > div > div > button')
button1.click()