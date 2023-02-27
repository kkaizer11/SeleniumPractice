from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'

navegador = Firefox()
navegador.get(url)
heading = navegador.find_element(By.TAG_NAME, 'h1')
p1 = navegador.find_element(By.XPATH, '/html/body/p[1]')
p2 = navegador.find_element(By.XPATH, '/html/body/p[2]')
p3 = navegador.find_element(By.XPATH, '/html/body/p[3]')
dic = {'H1':
{
    'texto1' : p1.text,
    'texto2': p2.text,
    'texto3': p3.text
}}
print(dic)
navegador.close()


