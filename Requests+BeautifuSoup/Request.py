# coding:utf-8

import urllib.request
from bs4 import BeautifulSoup
import requests
import re

num = []
lianjie = []
url = "http://tool.oschina.net/"
con = requests.get(url).text
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")
top = soup.find_all("a")
lianjie = re.findall('<a href="(.*?\")', con)

url = []
for i in lianjie:
    if (i[:4] != "http"):
        url.append("http://tool.oschina.net/"+i[:-1])
    else:
        url.append(i[:-1])

i = 0
nu = []
url = url[:len(url)-6]
top = top[:len(url)]

while i < len(top):
    num.append(top[i].get_text())
    nu.append(num[i].replace("原", ""))
    i = i + 1
j = 0

strc = []
while j < len(nu):
    strc.append(nu[j])
    j = j + 1


m = 0
tops = ""
print(len(strc),len(url))
while m < len(strc):
    tops += str(strc[m]) + "\t" + str(url[m]) + "\n"
    m = m + 1

k = 0
while k < len(tops):
    with open("Requests.txt", "a+") as f:
        f.write(tops[k])
        k = k + 1
        f.close()

print("写入成功")
