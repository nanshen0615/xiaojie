# coding=utf-8
# @time:2021/8/1 18:46
# @Author:李毅杰
# @Email:Lxiaojie0615@163.com

import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers=headers)
print(r.text)

soup = BeautifulSoup(r.text, "html.parser")

title=soup.find("h1",class_="post-title").a.text.strip()

print(title)

with open('title_test.txt',"a+") as f:
	f.write(title)
