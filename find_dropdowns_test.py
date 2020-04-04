from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://makemytrip.com')

# Getting values of dynamic dropdowns
driver.find_element_by_id('fromCity').click()
