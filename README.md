# yes24_best_seller_crwaler

## 사용법

monthly_best_seller_top_100.py 파일에서 `year`, `month`를 바꿔 원하는 연도와 월의 베스트 셀러를 선택 할 수 있습니다.  
`size`변수는 추출 책의 개수를 정합니다.  
`category`변수는 원하는 분야의 값을 찾아서 넣으시면 됩니다


## Tag
### 출판사  
div.topColRgt > div.gd_infoTop > div.gd_titArea > h2  
### 출간일  
div.topColRgt > div.gd_infoTop > span.gd_pubArea > span.gd_date  
### 출판사
div.topColRgt > div.gd_infoTop > span.gd_pubArea >span.gd_pub  
### 저자
div.topColRgt > div.gd_infoTop > span.gd_pubArea >span.gd_auth  
### 가격
div.topColRgt > div.gd_infoBot > div.gd_infoTbArea > div.gd_infoTb > table > tbody > tr > td > span > em  
### 판매지수
div.topColRgt > div.gd_infoTop > span.gd_ratingArea > span.gd_sellNum   
