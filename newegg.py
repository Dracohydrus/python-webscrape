from selenium import webdriver as wd
import chromedriver_binary
import keyring

wd = wd.Chrome()
wd.maximize_window()
wd.implicitly_wait(10)

def random_sleep(min=3.0, max=10.0):
    import random
    import time
    time.sleep(random.randrange(min,max))

def login(email_address, password):
    email_address_textbox = wd.find_element_by_xpath('//*[@id="labeled-input-signEmail"]')
    email_address_textbox.click()
    email_address_textbox.send_keys(email_address)

    sign_in_button = wd.find_element_by_id('signInSubmit')
    sign_in_button.click()
    random_sleep()

    password_textbox = wd.find_element_by_xpath('//*[@id="labeled-input-password"]')
    password_textbox.click()
    password_textbox.send_keys(password)

    sign_in_button = wd.find_element_by_id('signInSubmit')
    sign_in_button.click()
    random_sleep()

def checkout():
    continue_to_delivery_button = wd.find_element_by_xpath('//*[@id="shippingItemCell"]/div/div[3]/button')
    continue_to_delivery_button.click()
    random_sleep()

    # implement a way to select cheapest shipping option
    continue_to_payment_button = wd.find_element_by_xpath('//*[@id="deliveryItemCell"]/div/div[3]/button')
    continue_to_payment_button.click()
    random_sleep()

    cvv_textbox = wd.find_element_by_xpath('//*[@id="paymentItemCell"]/div/div[2]/div/div[3]/div[2]/div[2]/div[1]/div/label/div[4]/input')
    cvv_textbox.click()
    cvv_textbox.send_keys(keyring.get_password('newegg_login',"cvv"))
    random_sleep()

    review_order_button = wd.find_element_by_xpath('//*[@id="paymentItemCell"]/div/div[3]/button')
    review_order_button.click()

    # Finalize Order. Uncomment to complete payment
    # random_sleep()
    # place_order_button = wd.find_element_by_id('btnCreditCard')
    # place_order_button.click()

def add_to_cart():
    random_sleep()
    add_to_cart_button = wd.find_element_by_xpath('//*[@id="ProductBuy"]/div/div[2]/button')
    add_to_cart_button.click()
    random_sleep()

    decline_extra_warranty_button = wd.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div/div[3]/button[1]')
    decline_extra_warranty_button.click()
    random_sleep()

    proceed_to_checkout_button = wd.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[2]')
    proceed_to_checkout_button.click()

def full_buy_process(url):
    newegg_email = keyring.get_password("newegg_login","email")
    newegg_password = keyring.get_password("newegg_login","password")

    wd.get(url)

    add_to_cart()
    random_sleep()
    login(newegg_email,newegg_password)
    random_sleep()
    checkout()