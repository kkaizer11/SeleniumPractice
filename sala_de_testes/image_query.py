from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from sys import argv


driver = Firefox()
driver.get('https://www.google.com/')
query = driver.find_element(By.CLASS_NAME, 'Gdd5U')
query.click()
image_search = driver.find_element(By.CLASS_NAME,'cB9M7')
image_search.send_keys(argv[1])
image_search.send_keys(Keys.ENTER)