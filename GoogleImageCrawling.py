from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
import time

browser = webdriver.Chrome("C:/Users/MILAB/anaconda3/envs/wonyong/chromedriver_win32/chromedriver.exe")

key_word = "원룸 인테리어"
download_image_count = 1000

main_url = f'https://www.google.com/search?q={quote_plus(key_word)}&source=source=lnms&tbm=isch&sa=X'
browser.get(main_url)
time.sleep(2)
for i in range(download_image_count):
    browser.execute_script("window.scrollBy(0,10000)")

html = browser.page_source
soup = BeautifulSoup(html)
img = soup.select('.rg_i.Q4LuWd')

imgurl = []
for i in img:
    try:
        imgurl.append(i.attrs["src"])
    except KeyError:
        imgurl.append(i.attrs["data-src"])

n=1
for i in imgurl:
    with urlopen(i) as f:
        with open("./사진/" + key_word + str(n) + ".jpg", "wb") as h:
            current_image = f.read()
            h.write(current_image)
    n += 1
    time.sleep(0.1)

browser.close()
