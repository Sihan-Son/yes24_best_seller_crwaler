# Author: sihan
# Date: 2020-12-08

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import re

year = '2020'
month = '11'
category = '001001003'
size = '100'


def best_selling_month_and_year(category, year, month, size=100):
    url = f'http://www.yes24.com/24/category/bestseller?CategoryNumber={category}&sumgb=09&year={year}&month={month}&PageNumber=1&FetchSize={size}'

    res = requests.post(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    book_list_tag = '.goodsTxtInfo > p:nth-child(1) > a:nth-child(1)'

    books = soup.select(book_list_tag)

    book_list = []

    for i in range(int(size)):
        book_list.append(str(books[i]).split("\"")[1])

    return book_list


def get_book_info(book_list):
    header = "제목, 저자, 출판사, 출간일, 가격, 판매지수\r"
    url_header = 'http://www.yes24.com/'

    for book in tqdm(book_list, desc="Get Book Info"):
        book_url = url_header + book
        res = requests.post(book_url)
        soup = BeautifulSoup(res.text, 'html.parser')

        title_tag = '.gd_titArea > h2'  # 제목
        date_tag = '.gd_date'  # 출간일
        pb = ".gd_pub"  # 출판사
        au = ".gd_auth > a"  # 저자
        pr = ".gd_infoTb > table > tbody > tr > td > span > em"  # 가격
        sc = ".gd_sellNum"  # 판매지수

        title = soup.select(title_tag)  # 제목
        date = soup.select(date_tag)  # 출간일
        pbp = soup.select(pb)  # 출판사
        aut = soup.select(au)  # 저자
        pri = soup.select(pr)  # 가격
        scp = soup.select(sc)  # 판매지수

        title = title[0].get_text().replace(",", ' ')
        publishing_date = date[0].get_text().replace("년 ", '-').replace("월 ", '-').replace("일", '')
        publish = pbp[0].get_text()
        author = aut[0].get_text()
        price = pri[0].get_text().replace(",", '')

        try:
            selling_score = re.findall('\d+', scp[0].get_text().replace(',', ''))[0]
        except:
            selling_score = "개정판 출간"

        header += f'{title}, {author}, {publish}, {publishing_date}, {price}, {selling_score} \r'

    return header


def save_to_csv(book_detail, year, month, size):
    with open(f"{year}-{month} top {size} book.csv", "w") as f:
        f.write(book_detail)
