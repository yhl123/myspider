from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os

if __name__ == '__main__':
    list_urls = []
    url = "http://jandan.net/ooxx"
    PATH = r'E:\图片'
    options = webdriver.ChromeOptions()

    options.add_argument(
        'user-agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",--headless')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    html = driver.page_source
    driver.close()
    np = BeautifulSoup(html, 'lxml')
    img_list = np.find_all(name='img')
    print(img_list)
    for i in img_list:
        img_src = i.get('src')
        if 'http' in img_src:
            img_names = img_src.rsplit('/', maxsplit=1)[1]
            img_name = os.path.join(PATH, img_names)
            r2 = requests.get(url=img_src)
            with open(img_name, 'wb') as f:
                f.write(r2.content)
