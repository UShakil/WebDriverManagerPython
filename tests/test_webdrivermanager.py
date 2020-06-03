from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://pypi.org/project/webdriver-manager/")
assert (driver.find_element_by_class_name("package-header__name").is_displayed())
time.sleep (2)
driver.quit()