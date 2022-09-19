from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='/Users/roya/Documents/automation/python-selenium-automation/chromedriver')

#amazon logo
driver.find_element((BY.XPATH, "//i[@class='a-icon a-icon-logo']"))

#email
driver.find_element(By.XPATH, "//input[@class='a-input-text a-span12 auth-autofocus auth-required-field']")

#continue button
driver.find_element(By.ID,'continue')



#need help
driver.find_element(BY.XPATH, "//span[@class='a-expander-prompt']")

#forgot password
driver.find_element(BY.XPATH, "//a[@id='auth-fpp-link-bottom']")

#sign in
driver.find_element(BY.ID, 'ap-other-signin-issues-link')

#create your account
driver.find_element(BY.XPATH, "//a[@class='a-button-text']")

#condition of use link
driver.find_element(BY.XPATH, "//a[@class='a-link-normal' and contains(text(), 'Conditions')]")


#Privacy linl
driver.find_element(BY.XPATH, "//a[@class='a-link-normal' and contains(text(), 'Privacy')]" )


