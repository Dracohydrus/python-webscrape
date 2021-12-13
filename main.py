from random import random
from selenium import webdriver as wd
import newegg

# newegg urls
newegg_3080_strix_url = "https://www.newegg.ca/asus-geforce-rtx-3080-strix-rtx3080-o10g-v2-gaming/p/N82E16814126534?Description=rtx%203080&cm_re=rtx_3080-_-14-126-534-_-Product"
newegg_3060ti_url = "https://www.newegg.ca/asus-geforce-rtx-3060-ti-dual-rtx3060ti-o8g-v2/p/1FT-000Y-00697?Description=3060%20ti&cm_re=3060_ti-_-9SIAGYBGK01935-_-Product"

newegg.full_buy_process(newegg_3080_strix_url)