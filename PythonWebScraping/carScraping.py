# Library
import pandas as pd
import csv
from carScrapingClass import Scrape

# CONSTANT VAR
LISTSPEC = []
SKIPLINK = []

# Read data link
with open("linkForEachCar.csv", "r") as file:
    URL =  [row[0] for row in csv.reader(file)]

print("Total URL in data: ", len(URL[1:]))

for link in URL[1:]:
    try:
        scrape = Scrape(link = link)
        carSpec = scrape.scrapeDetail()
        LISTSPEC.append(carSpec)
    except (AttributeError, IndexError) as e:
        SKIPLINK.append(link)
        print("Skip scrape for: ", link)
        continue 
    
    print("Done scrape for: ", link)

# Save Data
carData = pd.DataFrame(LISTSPEC)
carData.to_csv("UsedCarFromMobilBekas.csv")

# Link that can't to be scraped:
print("Total link that can't to be scraped: ", len(SKIPLINK))
skipLink = pd.DataFrame(SKIPLINK)
skipLink.to_csv("SkipLink.csv")



    