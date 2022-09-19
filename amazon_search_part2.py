from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='/Users/roya/Documents/automation/python-selenium-automation/chromedriver')

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('dress')

driver.find_element(By.ID, 'nav-search-submit-button').click()

expected_result = '"dress"'

actual_result= driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'

print('Test case passed')
driver.quit()