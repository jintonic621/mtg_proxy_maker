import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import json


class SaveAsPDFClass:

    def __init__(self,url_list):
        self.url_list = url_list


    def make_images(self):
        url_list_length          = len(self.url_list)
        number_of_cards_ina_page = 9

        while url_list_length != 0:
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

            if url_list_length >= number_of_cards_ina_page:
                for i in range(number_of_cards_ina_page):
                        serch_box     = driver.find_element_by_id(f"text{i}")
                        serch_img     = driver.find_element_by_id(f"image{i}")
                        serch_img.click()
                        serch_box.clear()
                        serch_box.send_keys(self.url_list[i])
                time.sleep(3)
                for i in range(number_of_cards_ina_page):
                    actions.move_to_element(driver.find_element_by_id(f"text{i}")).perform()
                    self.url_list.pop(0)
            else:
                for i in range(url_list_length):
                        serch_box     = driver.find_element_by_id(f"text{i}")
                        serch_img     = driver.find_element_by_id(f"image{i}")
                        serch_img.click()
                        serch_box.clear()
                        serch_box.send_keys(self.url_list[i])
                time.sleep(3)
                for i in range(url_list_length):
                    actions.move_to_element(driver.find_element_by_id(f"text{i}")).perform()
                    self.url_list.pop(0)



            url_list_length = len(self.url_list)
            time.sleep(5)
            driver.execute_script('return window.print()')
            driver.quit()
        print("finish!")
