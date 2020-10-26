from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

stock_name = []
stock_percentage = []
stock_price = []

filename = "EEStockPrices.csv"
f = open(filename, "w")
headers = "Stock, Percentage, Price\n"
f.write(headers)

driver = webdriver.Firefox()
driver.get("https://www.easyequities.co.za/")

login = driver.find_element_by_link_text('Login')
login.click()
username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "user-identifier-input"))
)
username.send_keys("Username here")
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "Password"))
)
password.send_keys("Password here")
password.send_keys(Keys.RETURN)
time.sleep(5)

usd = driver.find_element_by_css_selector('div.slideContent:nth-child(3)')
usd.click()

nextP = True
while nextP:
        prices = driver.find_element_by_id('showAllGraphsButton')
        prices.click()
        time.sleep(3)
        s_container = driver.find_element_by_id('stockContainer')
        stocks = WebDriverWait(s_container, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "imageRow")))
        for stock in stocks:
            name = WebDriverWait(stock, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "auto-ellipsis"))).text
            stock_name.append(name)
            percentage = WebDriverWait(stock, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "return-value"))).text
            stock_percentage.append(percentage)
            price = WebDriverWait(stock, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "last-price"))).text
            stock_price.append(price)

        try:
            driver.find_element_by_link_text('»')
            driver.find_element_by_link_text('»').click()
            time.sleep(5)
        except:
            nextP = False
driver.quit()

list_size = len(stock_name)
x = 0
while x < list_size:
    f.write(stock_name[x]+ "," + stock_percentage[x] + "," + stock_price[x] + "\n")
    x +=1

f.close()
