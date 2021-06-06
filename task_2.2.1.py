from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)

num1_text = browser.find_element_by_css_selector('#num1')
num1 = num1_text.text

num2_text = browser.find_element_by_css_selector('#num2')
num2 = num2_text.text
summ = str(int(num1) + int(num2))

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(summ)
button = browser.find_element_by_css_selector("body > div > form > button")
button.click()

browser.quit()