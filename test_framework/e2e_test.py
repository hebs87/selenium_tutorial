from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

driver = webdriver.Chrome(options=options)
driver.get('https://rahulshettyacademy.com/angularpractice/')

driver.find_element_by_css_selector("a[href*='shop']").click()
# Get all the product card elements and store them in a products list
products = driver.find_elements_by_xpath("//div[@class='card h-100']")

# Loop through the products list
for product in products:
    # Traverse through the children of the product element until we get to the link
    product_name = product.find_element_by_xpath("div/h4/a").text
    # We only want to add the Blackberry item to the cart
    if product_name == 'Blackberry':
        # Add item to cart - find the button from the parent element and click it to add to cart
        product.find_element_by_xpath("div/button").click()

# Find the checkout button and click it
driver.find_element_by_css_selector("a[class*='btn-primary']").click()

# Click the Checkout button in the checkout page
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

# Type partial country name in the dropdown to load dynamic auto-suggestive options
driver.find_element_by_id("country").send_keys("Uni")
# It takes time for the list of countries to load, so we need to do an explicit wait here
wait = WebDriverWait(driver, 10)
# Wait until the relevant link is present and then click it
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "United Kingdom")))
driver.find_element_by_link_text("United Kingdom").click()
# Check the T&Cs checkbox
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
# Click the purchase button
driver.find_element_by_css_selector("[type='submit']").click()
# Get the text of the success message
success_text = driver.find_element_by_class_name("alert-success").text
# Verify the content of the success message to ensure the process has been a success
assert "Success! Thank you!" in success_text

# Get a screenshot of the page - saves it into the current directory unless specified
driver.get_screenshot_as_file("screen.png")

driver.close()
