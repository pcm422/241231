from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

header_user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36" # user-agent 설정
base_url = 'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query=' # 네이버 블로그 검색 url
keyword = input('검색어를 입력하세요: ') # 검색어 입력
url = base_url + keyword # 검색어와 함께 url 생성

options_ = Options() # 옵션 설정
options_.add_argument(f'user-agent={header_user}') # user-agent 설정
options_.add_experimental_option('detach', True) # 브라우저 자동으로 종료되지 않게 스크립트 실행
options_.add_experimental_option('excludeSwitches', ['enable-logging']) # 로그 끄기

driver = webdriver.Chrome(options=options_) # 드라이버 설정
driver.get(url) # url 열기
time.sleep(2) # 페이지 로딩 대기

for i in range(5): # 5번 스크롤 내리기
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') # 스크롤 내리기
    time.sleep(1) # 스크롤 후 잠시 대기
    
html = driver.page_source # 페이지 소스 가져오기
soup = BeautifulSoup(html, 'html.parser') # 파싱
results = soup.select('.view_wrap') 

for i in results: # 검색 결과 출력
    result = i.select_one('.title_link').text # 제목
    link = i.select_one('.title_link')['href'] # 링크
    writer = i.select_one('.name').text # 작성자
    dsc = i.select_one('.dsc_link').text # 요약
    print(f"제목 : {result}")
    print(f"링크 : {link}")
    print(f"작성자 : {writer}")
    print(f"요약 : {dsc}")
    print('---------------------------------')
    
driver.quit() # 브라우저 종료