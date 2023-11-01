import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


def test_link_about():
    s = Service('C:\\Users\\igore\\PycharmProjects\\resource\\geckodriver.exe')
    driver = webdriver.Firefox(service=s)

    print("Start Test")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()

    print("Finish test")
    time.sleep(10)
    driver.quit()









    # enter_shoping_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "// div[ @ id = 'shopping_cart_container']")))
    # enter_shoping_cart.click()
    # print("Click Enter Shoping Cart")

