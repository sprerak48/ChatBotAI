from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import requests
import sys


data = sys.argv[1].replace("+","%2B")
html = urlopen("https://calculatorpi.com/c?a="+data+"&submit=+++Calculate+++&b=#here")
bsObj = BeautifulSoup(html, "html.parser")
# link = bsObj.findAll("div", id="findet_1")
# table1 = link.find('table').find_all('tr')

table_div = bsObj.find('div' , {'class': 'd01_scientific_calculator'})
table = table_div.find_all('tr')
td = bsObj.find('td' , {'class': 'cc'})
a = td.find('a')
# print(a)
span = a.find_all('span')
# for s in span:
	# print(s.text)
data1 = td.select_one("a[onclick^=fill]")["onclick"]
# length = len(data1)
# print(length)

# print(data1[6:9])
le = len(data1)-4
# print(le)
print(data1[6:(le)])
# print(data1[len(data1)-5])
# string = data1.substring(6, len(data1)-5)
# print(string)
# for d in data1:
	# print(d)