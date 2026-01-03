''' main_legacy_2 '''

# ignora o arquivo inteiro
# type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser_2(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 5

    # Example
    # sem abrir o navegador o navegador
    # options = '--headless', '--disable-gpu',
    options = ("--incognito")
    browser = make_chrome_browser_2(*options)

    # Como antes
    browser.get('https://www.google.com')

    # espere para encontrar o input
    try:
        search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
            expected_conditions.presence_of_element_located(
                (By.NAME, 'q')
            )
        )
        search_input.send_keys('Hello World!')
        search_input.send_keys(Keys.ENTER)
    except Exception as e:
        print(e)
    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)

''' main_legacy '''

import time 
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

# config basica do selenium
chrome_options = webdriver.ChromeOptions() # depois da pra dar add_argument
chrome_service = Service(executable_path=str(CHROMEDRIVER_EXEC))
chrome_browser = webdriver.Chrome(
    service=chrome_service,
    options=chrome_options,  # dangling comma
)
chrome_browser.get('https://www.google.com.br/')
# time.sleep(30)

''' main '''

# ignora o arquivo inteiro
# type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 5

    # Example
    # sem abrir o navegador o navegador
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get("https://br.search.yahoo.com/")

    # espere para encontrar o input
    try:
        search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
            expected_conditions.presence_of_element_located(
                (By.NAME, 'p')
            )
        )
        search_input.send_keys('Hello World!')
        search_input.send_keys(Keys.ENTER)

        results = browser.find_element(By.ID, 'results')
        # print(results)
        links = results.find_elements(By.TAG_NAME, 'a')
        links[0].click()

    except Exception as e:
        print(e)
    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)