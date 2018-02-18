from selenium import webdriver

driver = webdriver.Chrome("/Users/igor/Downloads/chromedriver")
driver.get(url='http://google.com')
print(driver.title)
driver.maximize_window()
driver.implicitly_wait(3000)
driver.quit()
