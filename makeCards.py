import requests
from bs4 import BeautifulSoup
import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import json


url_list    = []
no_card     = []

t = open('cards.txt',encoding="utf-8_sig")

cards       = t.readlines()

for card in cards:
    result  = requests.get('https://www.hareruyamtg.com/ja/products/search?product={}'.format(card))
    soup    = BeautifulSoup(result.text, 'lxml')

    if soup.find(class_= "lazy"):
        img_url = soup.find(class_= "lazy").get("data-original")
        url_list.append(img_url)
    else:
        no_card.append(card)
print(f"検索結果なし:{no_card}")

t.close()




length = len(url_list)
while length != 0:

    options       = webdriver.ChromeOptions()
    appState = {
        "recentDestinations": [
            {
                "id": "Save as PDF",
                "origin": "local",
                "account":""
            }
        ],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }
    prefs = {'printing.print_preview_sticky_settings.appState':
    json.dumps(appState)}
    options.add_experimental_option('prefs', prefs)
    options.add_argument("--kiosk-printing")
    driver        = webdriver.Chrome(options=options)
    driver.get('https://プロキシカード.xyz/proxy2.html')
    actions = ActionChains(driver)
    if length >= 9:
        for i in range(9):
                serch_box     = driver.find_element_by_id(f"text{i}")
                serch_img     = driver.find_element_by_id(f"image{i}")
                serch_img.click()
                serch_box.clear()
                serch_box.send_keys(url_list[i])
        time.sleep(3)
        for i in range(9):
            actions.move_to_element(driver.find_element_by_id(f"text{i}")).perform()
            url_list.pop(0)
    else:
        for i in range(length):
                serch_box     = driver.find_element_by_id(f"text{i}")
                serch_img     = driver.find_element_by_id(f"image{i}")
                serch_img.click()
                serch_box.clear()
                serch_box.send_keys(url_list[i])
        time.sleep(3)
        for i in range(length):
            actions.move_to_element(driver.find_element_by_id(f"text{i}")).perform()
            url_list.pop(0)

    length = len(url_list)
    time.sleep(5)
    driver.execute_script('return window.print()')
    driver.quit()
print("finish!")
