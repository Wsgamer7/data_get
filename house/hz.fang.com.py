from selenium import webdriver
from selenium.webdriver.common.by import By

# web browser setting
web_options = webdriver.ChromeOptions()
web_options.add_argument("--headless")
web = webdriver.Chrome(options=web_options)


def get_detail_a_house(url_house, web=web):
    web.get(url_house)
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
    return (house_name, house_price, house_price_metric)


def get_url_house_1page_in_searching(url_searching, web=web):
    web.get(url_searching)

    house_list_block = web.find_element(
        By.XPATH, '//*[@id="newhouse_loupan_list"]/ul'
    ).find_elements(By.TAG_NAME, "li")
    house_list = [
        li.find_element(By.TAG_NAME, "a").get_attribute("href")
        for li in house_list_block
    ]
    return house_list


def crawling(url_searching, page_num=5, web=web):
    data = []
    for i in range(page_num):
        print(url_searching)
        url_house_1page = get_url_house_1page_in_searching(url_searching, web)
        for url_house in url_house_1page:
            data.append(get_detail_a_house(url_house, web))
        web.get(url_searching)

        url_searching = (
            web.find_element(By.XPATH, '//*[@id="sjina_C01_47"]')
            .find_elements(By.CLASS_NAME, "next")[-1]
            .get_attribute("href")
        )

        print("finish {0}th page".format(i + 1))

    print(data)


search_url = "https://hz.newhouse.fang.com/house/s/"
crawling(search_url, page_num=5)

web.close()
