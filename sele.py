# https://www.freelancer.com/projects/Python/Python-expert-required-import-data/

from selenium import webdriver
import time
browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
# browser = webdriver.PhantomJS("/usr/lib/phantomjs/phantomjs")

browser.get('https://accounts.google.com/ServiceLoginAuth')

emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('parasdoshipu@gmail.com')
nextButton = browser.find_element_by_id('next')
nextButton.click()
time.sleep(2)
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('algoforme12')
signinButton = browser.find_element_by_id('signIn')
signinButton.click()

browser.get('https://www.google.com/finance/portfolio?action=view&pid=3&authuser=2&ei=sAg8WLn-MYviugSQ_4WQBA?pview=pview')
element = browser.find_element_by_class_name("gf-table")
browser.find_element_by_class_name("sorted-arrow").Click();

# data = element.get_attribute('innerHTML')
# f = open("something4.html","w")
# f.write(data.encode("utf-8").strip())
