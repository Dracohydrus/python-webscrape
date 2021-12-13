from selenium import webdriver as wd
import chromedriver_binary
from bs4 import BeautifulSoup

url = "https://www.newegg.ca/p/pl?Submit=Property&Subcategory=48&N=100007708%20601359415&IsPowerSearch=1"
wd = wd.Chrome()
wd.get(url)
wd.set_window_size(1929, 1080)
wd.save_screenshot("screenshot.png")

soup = BeautifulSoup(wd.page_source, features="html.parser")
items = soup.find("div", {"class":"items-grid-view"})



for item in items.find_all("div", {"class":"item-cell"}):
    temp = item.find("a", {"class":"item-title"})
    text = temp.get_text()
    if 'lhr' not in text.lower():
        print(text)

wd.close()