import time

def test_home(browser):
	url = "http://127.0.0.1:8081"
	browser.get(url)
	time.sleep(5)
	assert browser.title == "Dash"
	print("Teste da página inicial realizado com sucesso!")
