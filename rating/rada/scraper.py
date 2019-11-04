from selenium import webdriver 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import platform
import sys
import os


def laws_by_deputy(id_):
    """Return number of law projects for deputy by his/her id"""
    deputy_html = parse_js_page(laws_url_by_id(id_))
    soup = BeautifulSoup(deputy_html, 'html.parser')
    table = soup.find('table')
    total_laws = len(table.find_all('tr')) - 1

    return total_laws


def parse_js_page(url, sleep_time=5):
    """Scrape webpage even if it uses JavaScript to load elements.
    Return HTML string or None if connection timed out.
    """
    browser = set_browser()
    browser.set_page_load_timeout(10)

    try:
        browser.get(url)
        html = browser.page_source
        return html
    except TimeoutException:
        return None


def set_browser():
    """Return browser instance to work with. No GUI for CLI usage."""
    options = Options()
    options.add_argument('--headless') # disable chrome GUI for CLI
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage') 

    return webdriver.Chrome(choose_driver(), chrome_options=options)


def choose_driver():
    script_dir = os.path.dirname(__file__) 
    system = platform.system()

    if system.lower() == 'linux':
        return os.path.join(script_dir, 'data', 'chromedriver_linux')
    elif system.lower() == 'darwin':
        return os.path.join(script_dir, 'data', 'chromedriver_mac')
    elif system.lower() == 'windows':
        return os.path.join(script_dir, 'data', 'chromedriver_win.exe')
    else:
        print('Chromedriver not found!.\n Aborting...')
        sys.exit(0)


def deputy_url_by_id(id_):
    deputy_url = 'https://itd.rada.gov.ua/mps/info/page/'
    return deputy_url + id_


def laws_url_by_id(id_):
    return f'http://w1.c1.rada.gov.ua/pls/pt2/reports.dep2?PERSON={id_}&SKL=10'
