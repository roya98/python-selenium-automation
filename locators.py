from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='/Users/roya/Documents/automation/python-selenium-automation/chromedriver')

driver.get('https://www.amazon.com/')


# By XPATH
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")

