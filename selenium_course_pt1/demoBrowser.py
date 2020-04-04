from selenium import webdriver
# Browser exposes an executable file
# Through Selenium test we need to invoke the executable file which will then invoke actual browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")  # get method to hit url on browser

print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
