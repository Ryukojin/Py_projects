import os
import re
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import gc
os.chdir('C:\\Users\\Fahim\\Downloads\\scraper')

#Clear env + gc
def cleanup():
    for name in dir():
        if not name.startswith('_'):
            del globals()[name]
    gc.collect()

#Read file and soup it
def make_soup(f):
    with open(f, 'r') as f:
        f = f.read()
    return BeautifulSoup(f,'html.parser')

#                                           WORKING WITH HTML FILES
#=======================================================================================================================================
#1. Printing individual tags
soup = make_soup('page1.html')
#Make soup object and print it
print(soup.prettify())

#access some tags such as: div,p,head,body
soup.body['class']

#Print only the string content in a tag if it has one
p1 = soup.p
p1.string

#You can also replace the tag string with something else
p1.string.replace_with("Title changed!")

#2. Navigating children
soup = make_soup('page2.html')
print(soup.prettify())

#choosing tag
soup.body
soup.head

#                           METHODS to access tag contents in different ways
#===========================================================================================================================================
soup = make_soup('page2.html')
#tag.contents will return a direct child of tag
len(soup.head.contents)
print([child for child in soup.head.contents if child != '\n'])

len(soup.contents)

#tag.children will return an iterator. Preferable when working with children
soup.head.children
for child in soup.body.children:
    print(child if child is not None else '', end='\n')

#tag.descendants will return the children of a tag and its child tags as separate 
for i,j in enumerate(soup.head.descendants):
    print(i)
    print(j)

#tag.parent will return the direct parent tag of the tag
#hierarchy is as follows: soup>html>head/body. So soup has no parent.
b = soup.b
print(b.parent.name)

body = soup.body
print(body.parent.name)

html = soup.html
print(type(html.parent))

#tag.parents will all the parents and grandparents of the tag. It returns a list of all parents
p = soup.body.p
b = soup.body.b
for parent in b.parents:
    print(parent.name)

#tag.next_sibling shows the next sibling
print(b.next_sibling.next_sibling)

for sib in b.next_sibling:
    print(sib if sib != '\n' else '')

#tag.previous_sibling
print(p.previous_sibling.previous_sibling)

for sib in p.previous_sibling:
    print(sib if sib != '\n' else '')

#                                               Find methods
#==============================================================================================================================
#find_all(): finds all tags that match string
for tag in soup.find_all('a'):
    print(tag)
#    print(tag.name)


#Find more than one tag
soup.find_all(['p','b'])

# Find all tags that stars with b using regex pattern 
pattern = re.compile('^b')

for tag in soup.find_all(pattern):
    print(tag)

#Fine tuning find_all() using attributes:
attr = {'class':'sister'}
soup.find_all('a', attrs=attr, limit = 2)#limit rows by 2

#Alternatively you can directly use tag attributes as args. class has an underscore since class is a keyword in python
soup.find_all('a', class_='sister', id = 'link2')

#Find tags using a string pattern
pattern = re.compile('story')
soup.find_all(string=pattern)

#find() finds the first object
soup.find('a')

#recursive searching. Default is True. When set to FALSE it only looked for direct children tags of 'html' with name 'title' and none exists.
soup.find_all('title', recursive=False)
soup.find_all('title',recursive=True)


#                                               Working example
#==============================================================================================================================

url = 'https://www.consumerreports.org/cro/a-to-z-index/products/index.htm' 
file_name = 'cust_reports.txt'
header = {'user-agent':UserAgent().chrome}
page = requests.get(url,headers = header)

#Write html to a file and work in order to avoid pinging server
with open(file_name,'w') as f:
    f.write(page.content.decode('utf-8')) if type(page.content) == bytes else file.write(page.content)
soup = make_soup('cust_reports.txt')

all_div = soup.find_all('div', class_='crux-body-copy')

for div in all_div:
    print(div.a.string)


    print(div.a['href'])

item_link ={div.a.string:div.a['href'] for div in all_div}
print(item_link)


#                                           WORKING WITH URLS
#=====================================================================================================
#Header is needed if you wish to trick the server into thinking the request was sent from a browser
ua = UserAgent()
header = {'user-agent':ua.chrome}

#Reading the URL with a fake user
url = 'https://www.google.com'

page = requests.get(url,headers = header)

'''
Different status numbers
Response 200:
Response :
Response :
'''



