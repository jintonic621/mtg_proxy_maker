import requests
from bs4 import BeautifulSoup



class PickUpUrlClass:
    def __init__(self):
        self.cards    = []
        self.url_list = []
        self.no_cards = []

    def read_cards(self):
        t = open('cards.txt',encoding="utf-8_sig")
        cards       = t.readlines()
        self.cards = cards
        t.close()

    def serch_cards(self):
        for card in self.cards:
            result  = requests.get('https://www.hareruyamtg.com/ja/products/search?product={}'.format(card))
            soup    = BeautifulSoup(result.text, 'lxml')

            if soup.find(class_= "lazy"):
                img_url = soup.find(class_= "lazy").get("data-original")
                self.url_list.append(img_url)
            else:
                self.no_cards.append(card)

    def show_nohit_cards(self):
        print(self.no_cards)
