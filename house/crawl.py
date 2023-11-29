from selenium import webdriver
from selenium.webdriver.common.by import By

query = "Selenium的使用"
url = "https://www.bing.com/search?q={0}".format(query)
url_house = "https://hz.newhouse.fang.com/loupan/2010187106.htm"

web_options = webdriver.ChromeOptions()
web_options.add_argument("--headless")
web = webdriver.Chrome(options=web_options)
page = web.get(url_house)
house_name = web.find_element(
    By.CSS_SELECTOR,
    "body > div.main_1200.tf > div.firstbox > div.firstright.fr > div.information > div.inf_left1 > div > h1 > strong",
).text
house_price = web.find_element(
    By.CSS_SELECTOR,
    "body > div.main_1200.tf > div.firstbox > div.firstright.fr > div.information > div.information_li.mb5 > div.price_line.clearfix > p > span",
).text
house_price_metric = web.find_element(
    By.XPATH, "/html/body/div[5]/div[3]/div[2]/div[1]/div[5]/div[1]/p"
).text[-8:-4]
print(house_name, house_price, house_price_metric)
