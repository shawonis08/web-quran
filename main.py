import urllib.request
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose


quote_page = 'https://habibur.com/quran/1/'

# page = urllib.request.urlopen(quote_page)
#
# soup = BeautifulSoup(page, 'html.parser')

# name_box = soup.find_all('div', attrs={'class': 'span7'})
# name_box = soup.find_all('span7')
# name = name_box.text
# print (name)
with open("bad.html") as fp:
    data = fp.read()
diagnose(data)