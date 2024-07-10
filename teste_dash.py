import pytest
import time
from selenium import webdriver

chrome_path = "/home/fanadevops/scripting/dash/chrome-linux64/chrome"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path
driver = webdriver.Chrome(options=chrome_options)

url = "http://127.0.0.1:8080"

#teste da pagina inicial
driver.get(url)
time.sleep(10)
assert "Dash" in driver.title
assert "pagina inicial" in driver.page_source
print ("Teste da página inicial realizado com sucesso!")

#teste da pagina do formulario
driver.get(url + "/formulario")
time.sleep(10)
assert "Dashboard - Formulario" in driver.title
assert "Formulario" in driver.page_source
print("Teste da página formulário realizado com sucesso!")

#teste da pagina de graficos
driver.get(url +"/graficos")
time.sleep(10)
assert "Dashboard - Graficos" in driver.title
assert "Graficos" in driver.page_source
print("Teste da página de gráficos realizado com sucesso!")

driver.quit()
