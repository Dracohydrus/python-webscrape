from selenium import webdriver as wd
import chromedriver_binary
import keyring
import selenium

wd = wd.Chrome()
# wd.title = "GPU Checker Test"
wd.implicitly_wait(10)
wd.get("https://www.newegg.ca/asus-geforce-rtx-3080-strix-rtx3080-o10g-v2-gaming/p/N82E16814126534?Description=rtx%203080&cm_re=rtx_3080-_-14-126-534-_-Product")

def login(email_address, password):
    email_address_textbox = wd.find_element_by_xpath('//*[@id="labeled-input-signEmail"]')
    email_address_textbox.click()
    email_address_textbox.send_keys(email_address)

    sign_in_button = wd.find_element_by_id('signInSubmit')
    sign_in_button.click()

    password_textbox = wd.find_element_by_xpath('//*[@id="labeled-input-password"]')
    password_textbox.click()
    password_textbox.send_keys(password)

    sign_in_button = wd.find_element_by_id('signInSubmit')
    sign_in_button.click()


add_to_cart_button = wd.find_element_by_xpath('//*[@id="ProductBuy"]/div/div[2]/button')
add_to_cart_button.click()

decline_extra_warranty_button = wd.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div/div[3]/button[1]')
decline_extra_warranty_button.click()

proceed_to_checkout_button = wd.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[2]')
proceed_to_checkout_button.click()

newegg_email = keyring.get_password("newegg_login","email")
newegg_password = keyring.get_password("newegg_login","password")
login(newegg_email,newegg_password)