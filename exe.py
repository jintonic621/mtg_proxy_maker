from modules.PickUpUrl import PickUpUrlClass
from modules.SaveAsPDF import SaveAsPDFClass
import sys
sys.dont_write_bytecode = True

pick_up_url = PickUpUrlClass()
pick_up_url.read_cards()
pick_up_url.serch_cards()
pick_up_url.show_nohit_cards()

save_as_PDF = SaveAsPDFClass(pick_up_url.url_list)
save_as_PDF.make_images()
