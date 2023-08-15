from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

yt = "https://www.youtube.com/"

driver = Firefox()
driver.get(yt)

music = driver.find_elements(By.ID, "text")
for i in range(len(music)):
    if music[i].text == "Music":
        music[i].click()
        break

# sleep(5)
# driver.close()