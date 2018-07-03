import urllib.request
from bs4 import BeautifulSoup

for a in range(3, 4):
    parsing_page = 'https://habibur.com/quran/%d' % (a + 1)

    print(parsing_page)

    html_doc = urllib.request.urlopen(parsing_page)

    soup = BeautifulSoup(html_doc, 'html.parser')

    body = soup.find_all("div", class_="container-fluid")
    b2 = soup.find_all("div", class_="row-fluid")
    b3 = soup.find_all("div", class_="span7")

    with open("test.html", "a+", encoding="utf-8") as file:
        file.write(str(b3))
