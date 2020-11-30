# Author: sihan
# Date: 2020-11-30

import requests
from bs4 import BeautifulSoup


url_header = 'http://www.yes24.com/'

year = '2020'
month = '11'
category = '001001003'
size = '100'

url = f'http://www.yes24.com/24/category/bestseller?CategoryNumber={category}&sumgb=09&year={year}&month={month}&PageNumber=1&FetchSize={size}'

res = requests.post(url)
soup = BeautifulSoup(res.text, 'html.parser')

book_list_tag = '#category_layout > tr > td.goodsTxtInfo > p:nth-child(1) > a:nth-child(1)'

books = soup.select(book_list_tag)

book_list = []

for i in range(int(size)):
    book_list.append(str(books[i]).split("\"")[1])

header = "제목, 출간일, 출판사, 저자, 가격, 판매지수\r\n"

for book in book_list:
    book_url = url_header + book
    res = requests.post(book_url)
    soup = BeautifulSoup(res.text, 'html.parser')

    title_tag = 'div.topColRgt > div.gd_infoTop > div.gd_titArea > h2'
    date_tag = 'div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_date'
    pb = "div.topColRgt > div.gd_infoTop > span.gd_pubArea >span.gd_pub"  # 출판사
    au = "div.topColRgt > div.gd_infoTop > span.gd_pubArea >span.gd_auth"  # 저자
    pr = "div.topColRgt > div.gd_infoBot > div.gd_infoTbArea > div.gd_infoTb > table > tbody > tr > td > span > em"
    sc = "div.topColRgt > div.gd_infoTop > span.gd_ratingArea > span.gd_sellNum "

    title_a = soup.select(title_tag)
    date = soup.select(date_tag)  # 출간일
    pbp = soup.select(pb)  # 출판사
    aut = soup.select(au)  # 저자
    pri = soup.select(pr)  # 가격
    scp = soup.select(sc)  # 판매지수

    title = str(title_a).split("\">")[1].split("</")[0]
    publishing_date = str(date).split(">")[1].split("<")[0]
    publish = str(pbp).split("\">")[2].split("<")[0]
    author = str(aut).split("\">")[2].split("<")[0]
    price = str(pri).split("\">")[1].split("<")[0]
    selling_score = (str(scp).split("</em>")[1].split("<a")[0]).strip().split(" ")[1]

    if price.find(','):
        price = price.replace(",", '')

    if selling_score.find(','):
        selling_score = selling_score.replace(',', "")

    header += f'{title}, {publishing_date}, {publish}, {author}, {price}, {selling_score} \r\n'

with open("100 book_list.csv", "w") as f:
    f.write(header)
