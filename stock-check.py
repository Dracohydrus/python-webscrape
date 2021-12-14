from selenium import webdriver as wd
import chromedriver_binary
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display

# you can change this URL for any amount of filtered results on newegg.ca and it will search through all of the items in the list and print out if one is availble.
# url = "https://www.newegg.ca/p/pl?Submit=Property&Subcategory=48&N=100007708%20601359415&IsPowerSearch=1"
# url = 'https://www.newegg.ca/p/pl?Submit=Property&Subcategory=48&N=100007708%20601359415%20601361654&IsPowerSearch=1'
url = 'https://www.newegg.ca/p/pl?Submit=Property&Subcategory=48&N=100007708%20601359415%20601361654%20601357250&IsPowerSearch=1'
wd = wd.Chrome()

def take_screenshot(url,screenshot_name):
    wd.set_window_size(1920, 1080)
    wd.get(url)
    wd.save_screenshot(screenshot_name)

def process_items(soup, all_rows = []):
    items = soup.find("div", {"class":"items-grid-view"})
    
    for item in items.find_all("div", {"class":"item-cell"}):
        item_title = item.find("a", {"class":"item-title"})
        item_promo = item.find("p", {"class":"item-promo"})
        price = item.find("li", {"class":"price-current"})

        row = []
        row.append(item_title.text)
        if item_promo != None:
            row.append(item_promo.text)
        else:
            row.append("In Stock")
        row.append(price.text)

        all_rows.append(row)
    return all_rows

take_screenshot(url,"screenshot.png")
soup = BeautifulSoup(wd.page_source, features="html.parser")
rows_processed = [] # going to use this for dataframe afterwards

pagination_label = soup.find("span", {"class":"list-tool-pagination-text"})
page_number = pagination_label.find("strong")
pages = 1
if pagination_label:
    pages = int(pagination_label.text.split('/')[1])
for page in range(1,pages+1):
    if page > 1:
        soup = BeautifulSoup(wd.page_source, features="html.parser")
        take_screenshot(f"{url}&page={page}","screenshot.png")
    rows_processed = process_items(soup,rows_processed)

df = pd.DataFrame.from_records(rows_processed, columns=["Item Title","Status","Price"])
isAvailable = 'In Stock' in df["Status"].values

if isAvailable:
    # you can put code in here to send out an email or use an API to send a WhatsApp message or even an SMS message to your mobile device
    print("Available!!")

# close the Web Driver after using you are done using it
wd.close()