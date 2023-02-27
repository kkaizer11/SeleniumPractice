from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
gg =  'https://www.google.com/'

driver = Firefox()
driver.get(gg)

query = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")

button = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")

query.send_keys("selenium")

button.click()