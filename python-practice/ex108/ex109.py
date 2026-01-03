'''
109 — Selenium: Navegação e interação com inputs
Tarefa: crie um script Selenium que acesse https://br.search.yahoo.com/,
localize o campo de busca, insira o texto "Python", e depois pressione Enter.
Conceitos: Selenium, envio de texto para input, interação com elementos da
página.
'''
from pathlib import Path
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CAMINHO_ROOT_PROJETO = Path(__file__).parent
CAMINHO_DRIVER_CHROME = CAMINHO_ROOT_PROJETO / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CAMINHO_DRIVER_CHROME),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


options = ()
browser = make_chrome_browser(*options)
browser.get("https://br.search.yahoo.com/")

if __name__ == '__main__':
    try:
        search_input = WebDriverWait(browser, 5).until(
            expected_conditions.presence_of_element_located(
                (By.NAME, 'p')
            )
        )

        search_input.send_keys('Python')
        search_input.send_keys(Keys.ENTER)

    except Exception as e:
        print(e)

    sleep(5)
