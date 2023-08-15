from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


ge = "https://ge.globo.com/futebol/brasileirao-serie-a/"

driver = Firefox()
driver.get(ge)

#elements no plural ou singular
game = driver.find_elements(By.CLASS_NAME, "jogo__transmissao--text").send_keys(Keys.COMMAND + 't') 


# action = ActionChains(driver)
# action.click(game)
# action.perform

# for i in range(len(game)):
#     if game[i].text != "VEJA COMO FOI":
#         game[i].click()
#         break

# sleep(5)
# alerta = driver.find_elements(By.CLASS_NAME, "sc-jhGSUB eLKMpq")
# actions = ActionChains(driver)

# alerta.click()

# sleep(1)
# driver.close()


