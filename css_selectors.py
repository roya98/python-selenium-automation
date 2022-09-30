from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/roya/Documents/automation/python-selenium-automation/chromedriver")

driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")

driver.find_element(By.CSS_SELECTOR, ".a-box-inner .a-spacing-small")

#$$("input[type='text']")
driver.find_element((By.CSS_SELECTOR, "input[type='text']"))

#$$("input[type='email']")
driver.find_element(By.CSS_SELECTOR, "input[type='email']")



#$$("input#ap_password")
driver.find_element(By.CSS_SELECTOR,"input#ap_password" )

# $$("#ap_password_check")
driver.find_element((By.CSS_SELECTOR, "#ap_password_check"))

#$$("input#continue")
driver.find_element(By.CSS_SELECTOR, "input#continue")


# $$("a[href*='ion_condition_of_use?ie=UTF8&nodeId=508088']")
driver.find_element(By.CSS_SELECTOR, "a[href*='ion_condition_of_use?ie=UTF8&nodeId=508088']")


# $$("a[href*='on_privacy_notice?ie=UTF8&nodeId=468496']")
driver.find_element(By.CSS_SELECTOR, "a[href*='on_privacy_notice?ie=UTF8&nodeId=468496']")

# $$("a[href*='ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0']")
driver.find_element(By.CSS_SELECTOR, "a[href*='ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0']")

