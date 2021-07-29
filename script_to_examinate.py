from selenium import webdriver
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

link = 'https://weekend.trivago.co.uk/'
browser = webdriver.Chrome()
browser.get(link)

# choosing regions
lev1 = browser.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[1]/header/div[5]/div/div/div/div[2]/div/div[1]/div/div')
lev1.click()

region = browser.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[1]/header/div[5]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/input')
region.clear()
region.send_keys('Edinburgh')
# region.send_keys(Keys.RETURN)
# region.send_keys(Keys.ENTER)
time.sleep(1)

# # choosing radius
new_lev1 = browser.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[1]/header/div[5]/div/div/div/div[2]/div/div[2]/div/div[1]')
new_lev1.click()
new_lev1.send_keys(Keys.RETURN)

# choosing date-range
date = browser.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[1]/header/div[5]/div/div/div/div[2]/div/div[3]/div')
date.click()
start = browser.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[1]/header/div[5]/div/div/div/div[2]/div/div[4]/div[2]/div/div/div/div[2]/div[3]/button[10]')
start.click()
end = browser.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[1]/header/div[5]/div/div/div/div[2]/div/div[4]/div[2]/div/div/div/div[2]/div[3]/button[11]')
end.click()
time.sleep(3)

# confirming the deal
button = browser.find_elements_by_css_selector("#__next > main > div.Inspiration_container__11ZhC > ul > li:nth-child(1) > div.fresnel-container.fresnel-greaterThanOrEqual-md > section > div.DealTilesDesktopWithContent_accommodations__37jzZ > div > div:nth-child(2) > div > div > div > ul > li:nth-child(1) > div > div.AccommodationCard_footer__2UVVz > div > div.Footer_dealArea__1PCaW > div.Footer_deal__3IGk7 > button")
button1 = button[0]

button1.click()

time.sleep(5)
browser.quit()