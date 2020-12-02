# Author: sihan
# Date: 2020-12-02

from util import *

category = '001001003'
year = '2018'
# month = '2'
size = '100'

for month in (range(1, 13, 1)):
    book_list = best_selling_month_and_year(category, year, month, size)
    book_info = get_book_info(book_list)

    save_to_csv(book_info, year, month, size)
