import urllib.request
from bs4 import BeautifulSoup


parsing_page = 'https://habibur.com/quran/1/'

html_doc = urllib.request.urlopen(parsing_page)

soup = BeautifulSoup(html_doc, 'html.parser')

title = soup.find('title')
t = title.text
print(t)
# with open("output.html", "w",encoding="utf-8") as file:
#     file.write(str(soup.prettify()))