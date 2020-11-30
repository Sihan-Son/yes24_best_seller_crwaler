# Author: sihan
# Date: 2020-11-30

import requests
from bs4 import BeautifulSoup

url = "http://www.yes24.com/Product/Goods/91165789"

res = requests.post(url)
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

header = "제목, 출간일, 출판사, 저자, 가격, 판매지수\r\n"

for _ in range(10):
    header += f'{title}, {publishing_date}, {publish}, {author}, {price}, {selling_score} \r\n'

with open("a book_list.csv", "w") as f:
    f.write(header)


# print(str(title_a).split("\">")[1].split("</")[0])
# print(str(date).split(">")[1].split("<")[0])
# print(str(pbp).split("\">")[2].split("<")[0])
# print(str(aut).split("\">")[2].split("<")[0])
# print(str(pri).split("\">")[1].split("<")[0])
# print((str(scp).split("</em>")[1].split("<a")[0]).strip().split(" ")[1])
