from selenium import webdriver
from time import sleep
import creds

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
searchbar = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchbar.send_keys('anikka albrite')
search_btn = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
imagebutton = driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a').click()
tools = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[2]/div[2]/div/div').click()
size = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/c-wiz[1]/div/div/div[2]/div/div[1]/div/div[1]').click()
large= driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/c-wiz/div[2]/c-wiz[1]/div/div/div[3]/div/a[1]/div/span').click()

class tinderbot():
    def _init_(self):
        self.driver = webdriver.Chrome()


sleep(3)
driver.close()