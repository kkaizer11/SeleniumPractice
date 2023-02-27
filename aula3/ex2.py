from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

navegador = Firefox()
navegador.get(url)
p1 = navegador.find_element(By.XPATH, '/html/body/p[2]')
num = p1.text[-1]

clic = navegador.find_element(By.ID, 'ancora')


while True:
    clic.click()
    var = navegador.find_elements(By.TAG_NAME, 'p')
    num1 = var[-1].text[-1]
    if num1 == num:
        break

sleep(5)
navegador.close()