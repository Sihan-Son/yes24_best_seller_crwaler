# Author: sihan
# Date: 2020-11-30

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

url_header = 'http://www.yes24.com/'

year = '2022'
month = '2'
category = '001001003'
size = '100'

url = f'http://www.yes24.com/24/category/bestseller?CategoryNumber={category}&sumgb=09&year={year}&month={month}&PageNumber=1&FetchSize={size}'

res = requests.post(url)
soup = BeautifulSoup(res.text, 'html.parser')

book_list_tag = '#category_layout > tr > td.goodsTxtInfo > p:nth-child(1) > a:nth-child(1)'

books = soup.select(book_list_tag)

book_list = []

for i in tqdm(range(int(size))):
    book_list.append(str(books[i]).split("\"")[1])

header = "제목, 출간일, 출판사, 저자, 가격, 판매지수\r"

for book in tqdm(book_list, desc="Get Book Info"):
    book_url = url_header + book
    res = requests.post(book_url)
    soup = BeautifulSoup(res.text, 'html.parser')

    title_tag = 'div.topColRgt > div.gd_infoTop > div.gd_titArea > h2'  # 제목
    date_tag = 'div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_date'  # 출간일
    pb = "div.topColRgt > div.gd_infoTop > span.gd_pubArea >span.gd_pub"  # 출판사
    au = "div.topColRgt > div.gd_infoTop > span.gd_pubArea >span.gd_auth"  # 저자
    pr = "div.topColRgt > div.gd_infoBot > div.gd_infoTbArea > input > div.gd_infoTb> table > tbody > tr > td > span > em.yes_m" # 가격
    sc = "div.topColRgt > div.gd_infoTop > span.gd_ratingArea > span.gd_sellNum "  # 판매지수

    title_a = soup.select(title_tag)
    date = soup.select(date_tag)  # 출간일
    pbp = soup.select(pb)  # 출판사
    aut = soup.select(au)  # 저자
    pri = soup.select(pr)  # 가격
    scp = soup.select(sc)  # 판매지수

    title = str(title_a).split("\">")[1].split("</")[0].replace(",", ' ')
    publishing_date = str(date).split(">")[1].split("<")[0].replace("년 ", '-').replace("월 ", '-').replace("일", '')
    publish = str(pbp).split("\">")[2].split("<")[0]

    try:
        author = str(aut).split("\">")[2].split("<")[0]
    except:
        author = str(aut).split(">")[2].split("<")[0]

    price = str(pri).split("\">")[1].split("<")[0]
    selling_score = (str(scp).split("</em>")[1].split("<a")[0]).strip().split(" ")[1]

    if price.find(','):
        price = price.replace(",", '')

    if selling_score.find(','):
        selling_score = selling_score.replace(',', "")

    header += f'{title}, {publishing_date}, {publish}, {author}, {price}, {selling_score} \r'

with open(f"{year}-{month} top {size} book.csv", "w") as f:
    f.write(header)
