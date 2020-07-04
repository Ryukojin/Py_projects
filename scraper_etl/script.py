from bs4 import BeautifulSoup
from time import sleep
import requests
import pandas as pd

#Create a bs4 object from url
ebayUrl = 'https://www.ebay.com.au/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=face+mask&_sacat=0'
document = requests.get(ebayUrl).text
soup = BeautifulSoup(document)

names = []
prices = []
sold = []
links = []
shipping = []

#Set the index for each listing
listings = soup.find_all('div', class_="s-item__info clearfix")

for article in listings: 
    try:
        name = article.find('h3', class_="s-item__title").text        
        names.append(name)    
    except:
        name = ''
        names.append(name)

    try:
        price = article.find('span', class_="s-item__price").text.split("AU $")[1].split(' ')[0]
        #price = article.find('span', class_="s-item__price").text
        prices.append(price)
    except:
        price = ''
        prices.append(price)

    try:
        sales = article.find('span', class_="BOLD NEGATIVE").text
        sold.append(sales)
    except:
        sales = ''
        sold.append(sales)  

    try:
        link = article.find('a').get('href')
        links.append(link)
    except:
        link = ''
        links.append(link)
    
    try:
        ship = article.find('span', class_="s-item__shipping s-item__logisticsCost").text
        shipping.append(ship)
    except:
        ship = ''
        shipping.append(ship)


#Make a dataframe
dataset = pd.DataFrame({
                        "Name":names, 
                        "Prices": prices, 
                        "Sold": sold,
                        "Shipping": shipping,
                        "Links": links
                        })

#Write to csv
dataset.to_csv('item_prices.csv')
