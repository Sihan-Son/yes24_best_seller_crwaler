# Author: sihan
# Date: 2020-12-08

import requests
from bs4 import BeautifulSoup
import re

# url = "http://www.yes24.com/Product/Goods/91165789"
url = 'http://www.yes24.com/Product/Goods/24567417'

res = requests.post(url)
soup = BeautifulSoup(res.text, 'html.parser')

title_tag = '.gd_titArea > h2'
date_tag = '.gd_date'
pb = ".gd_pub"  # 출판사
au = ".gd_auth > a"  # 저자
pr = ".gd_infoTb > table > tbody > tr > td > span > em"
sc = ".gd_sellNum"
#


title_a = soup.select(title_tag) # 제목
date = soup.select(date_tag)  # 출간일
pbp = soup.select(pb)  # 출판사
aut = soup.select(au)  # 저자
pri = soup.select(pr)  # 가격
scp = soup.select(sc)  # 판매지수



title = title_a[0].get_text().replace(",", ' ')
publishing_date = date[0].get_text().replace("년 ", '-').replace("월 ", '-').replace("일", '')
publish = pbp[0].get_text()
author = aut[0].get_text()
price = pri[0].get_text().replace(",", '')
selling_score = re.findall('\d+', scp[0].get_text().replace(',', ''))[0]


#
# if price.find(','):
#     price = price.replace(",", '')
#
# if selling_score.find(','):
#     selling_score = selling_score.replace(',', "")

header = "제목, 출간일, 출판사, 저자, 가격, 판매지수\r\n"
#
# for _ in range(10):
#     header += f'{title}, {publishing_date}, {publish}, {author}, {price}, {selling_score} \r\n'
#
# with open("a book_list.csv", "w") as f:
#     f.write(header)
