# MY FIRST TEST CASE
# 1. open web browser(chrome/firefox/IE).
# 2. Open url https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
# 3. Provide username (Admin).
# 4. Provide password (admin123).
# 5. click on login.
# 6. capture title of the dashboard page.(actual title).
# 7. verify title of the page: orangehrm (expected)
# 8. close browser.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.ID,"password").send_keys("admin123")
driver.find_element(By.ID,"submit").click()

act_title=driver.title
exp_title='OrangeHRM'

if act_title==exp_title:
    print("Login test passed:")
else:
    print("Login test failed:")

driver.close()
