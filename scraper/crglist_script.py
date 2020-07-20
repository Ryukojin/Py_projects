import requests
from bs4 import BeautifulSoup

url = 'https://boston.craigslist.org/search/sof?lang=en&cc=gb' 
file_name = 'craigslist.txt'
page = requests.get(url)

with open(file_name, "w", encoding="utf-8") as f:
        f.write(page.text) 

with open(file_name, 'r') as f:
    f = f.read()
soup = BeautifulSoup(f,'html.parser')
print(soup.prettify())

all_li = soup.find_all('li', class_='result-row')

for li in all_li:
    print('Job: ',li.p.a.string)
    print('URL: ',li.p.a['href'],'\n')

#Save as dict
listings = {li.p.a.string : li.p.a['href'] for li in all_li}



