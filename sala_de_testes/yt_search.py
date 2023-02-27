from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
# import sys

youtube = 'https://www.youtube.com/'

driver = Firefox()
driver.get(youtube)

search = driver.find_element(By.ID, 'search-container')
# search.send_keys("cachorro magro")