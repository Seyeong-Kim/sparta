import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
titles = soup.select('.list > .info > a.title')
ranks = soup.select('.list > .number')
singers = soup.select('.list > .info > a.artist')

for rank, title, singer in zip(ranks, titles, singers):

    print(rank.text.split("\n")[0], title.text.strip(), singer.text)