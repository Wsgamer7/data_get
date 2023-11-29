from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# web browser setting
web_options = webdriver.ChromeOptions()
web_options.add_argument("--headless")
web = webdriver.Chrome(options=web_options)


url_house = "https://hz.newhouse.fang.com/loupan/2010187106.htm"

web.get(url_house)
soup = BeautifulSoup(web.page_source, "html.parser")
print(soup)
web.quit()
