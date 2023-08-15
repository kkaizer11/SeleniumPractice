from selenium import webdriver
from selenium.webdriver import Firefox

driver = Firefox()
driver.get("https://www.youtube.com")
# search = driver.find_element_by_id("search")

driver.execute_script("window.open('https://www.google.com')")