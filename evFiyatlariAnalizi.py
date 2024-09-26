# csv dosyaları handle lamak icin
import pandas as pd 

import matplotlib.pyplot as plt

# CSV dosyasını yükledim
housing = pd.read_csv('Housing.csv')

# Relation between price and area
housing['sMeter prices'] = housing['price'] / housing['area'] # 1m² ne kadar?

# m² fiyatına göre
perSmeterStatus = [
    
]

# m² başına pahalılık 
def statusByArea(squareMeter):
    for alt_sinir, durum in perSmeterStatus:
        if squareMeter >= alt_sinir:
            return durum

# m² başına pahalılık durumu
housing['statusByArea'] = housing['sMeter prices'].apply(statusByArea) # tabloya eklendi

# Relation between price and bedrooms/stories

''' Kata ve oda sayısına göre ev fiyatı ortalaması
4. kattaki evlerin veya 4 odali evlerin fiyat ortalaması gibi
bu ortalamalara göre pahalı ucuz yorumu yapılabilir'''

# Yatak odası sayısına göre ortalama
avgByBedroom = housing.groupby('bedrooms')['price'].mean() 

# Yatak odası sayısına göre ortalamanın üstü/altı yorumlaması
def statusByBedroomNums(house):
    avgPrice = avgByBedroom[house['bedrooms']]
    if house['price'] > avgPrice:
        return 'expensive'
    else:
        return 'cheap'

# Yatak odası sayısına göre pahalılık durumu
housing['statusByBedroomNums'] = housing.apply(statusByBedroomNums) # tabloya eklendi

# Kata göre ortalama
avgByStory = housing.groupby('stories')['price'].mean() 

# Kata göre ortalamanın üstü altı yorumlaması
def statusByStories(house):
    avgPrice = avgByStory[house['stories']]
    if house['price'] > avgPrice:
        return 'expensive'
    else:
        return 'cheap'

# Kara göre pahalılık durumu
housing['statusByStories'] = housing.apply(statusByBedroomNums) # tabloya eklendi
