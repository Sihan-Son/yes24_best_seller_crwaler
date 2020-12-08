# Author: sihan
# Date: 2020-12-02

import util_refact as ur
from util import *
import time

category = '001001003'
year = '2018'
# month = '2'
size = '100'

# Origin
#########################################################################

past = time.time()
for month in (range(1, 2, 1)):
    book_list = best_selling_month_and_year(category, year, month, size)
    book_info = get_book_info(book_list)

    save_to_csv(book_info, year, month, size)
print(time.time() - past)

# Refactoring
#########################################################################

past = time.time()
for month in (range(1, 2, 1)):
    book_list = ur.best_selling_month_and_year(category, year, month, size)
    book_info = ur.get_book_info(book_list)

    ur.save_to_csv(book_info, year, month, size)
print(time.time() - past)
