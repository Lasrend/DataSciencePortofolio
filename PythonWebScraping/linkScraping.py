#Library
from os import link
import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

#Headers for users
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

# Constant Variable
CHROME_WEBDRIVER = "D:\My Project\Keys\Webdriver\chromedriver.exe"
URL = "https://www.mobilbekas.co.id/search/iPage-"
START_PAGE = 1
END_PAGE = 1314


#Driver
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = webdriver.Chrome(CHROME_WEBDRIVER, options=options)

# Access URL
urlCar = []
for i in range(START_PAGE, END_PAGE+1):
    page = str(i)
    URLPage = URL + page
    driver.implicitly_wait(5)
    driver.get(URLPage)

    page = requests.get(URLPage, headers=headers).text

    #Create a BeautifulSoup Object
    soup = BeautifulSoup(page, "html.parser")

    #Find all link product
    links = soup.select(".listing-block a")

    for j in links:
        urlCar.append(j['href'])

# Change URL list to be dataframe
dfURL = pd.DataFrame(urlCar)
dfURL.to_csv("linkForEachCar.csv", index=False)
