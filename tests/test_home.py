import time

def test_home_page(browser):
	browser.get('https://127.0.0.1:8081')
	time.sleep(5)
	assert browser.title == "Dash"
	print("Teste da página inicial realizado com sucesso!")
