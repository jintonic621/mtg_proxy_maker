from modules.PickUpUrl import PickUpUrlClass
from modules.SaveAsPDF import SaveAsPDFClass
import sys
sys.dont_write_bytecode = True
try:
    pick_up_url = PickUpUrlClass()
    pick_up_url.read_cards()
    pick_up_url.serch_cards()
    pick_up_url.show_nohit_cards()
except:
    print("URLを読み込む過程でエラーが発生し、すべてのカードが検索できませんでした。")
    print("最後に検索したカード：" + pick_up_url.url_list[-1])


try:
    save_as_PDF = SaveAsPDFClass(pick_up_url.url_list)
    save_as_PDF.make_images()
except:
    print("ブラウザを動かせませんでした")
    print("取得したurl:")
    print(pick_up_url.url_list)
