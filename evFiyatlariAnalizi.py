# CSV dosyaları handle lamak icin
import pandas as pd 

import matplotlib.pyplot as plt

# CSV dosyasını yükledim
housing = pd.read_csv('Housing.csv')

# Relation between price and area

expStatusByArea = [ # 0 - 9 pahalılık durumu -9'a yaklaştıkça pahalılaşıyor-
    (15000, 9),
    (13500, 8),
    (12000, 7),
    (10500, 6),
    (9000, 5),
    (7500, 4),
    (6000, 3),
    (4500, 2),
    (3000, 1),
    (1500, 0)
]

# Alan - pahalılık 
def statusByArea(area):
    for min, status in expStatusByArea:
        if area >= min:
            return status

# Alan - pahalılık durumu
housing['areaStatus'] = housing['area'].apply(statusByArea) # tabloya eklendi

plt.title('Area - Price Analysis') # Grafik başlığı
plt.scatter(housing['area'], housing['areaStatus'], s=50, c='red', alpha=0.1, edgecolors='black') # Grafik iskeleti

# X Ekseni
plt.xlabel('Area') # X ekseninin temsili
plt.xlim(0, 16500) # X ekseni aralığı
plt.xticks([1500, 3000, 4500, 6000, 7500, 9000, 10500, 12000, 13500, 15000]) # X eksenindeki aralıklar

# Y Ekseni
plt.ylabel('Expensiveness') # Y ekseni temsili
plt.ylim(0, 10) # Y ekseni aralığı
plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9]) # Y eksenindeki aralıklar

# Graiği göster.
plt.show() 


# Relation between price and bedrooms/stories

''' Kata ve oda sayısına göre ev fiyatı ortalaması
4. kattaki evlerin veya 4 odalı evlerin fiyat ortalaması gibi
bu ortalamalara göre pahalı/ucuz yorumu yapılabilir'''
'''
# Yatak odası sayısına göre ortalama
avgByBedroom = housing.groupby('bedrooms')['price'].mean() 

# Yatak odası sayısına göre ortalamanın üstü/altı yorumlaması
def statusByBedroomNum(house):
    avgPrice = avgByBedroom[house['bedrooms']]
    if house['price'] > avgPrice:
        return 'expensive'
    else:
        return 'cheap'

# Yatak odası sayısına göre pahalılık durumu
#housing['statusByBedrooms'] = housing.apply(statusByBedroomNum) # tabloya eklendi

# Kata göre ortalama
avgByStory = housing.groupby('stories')['price'].mean() 

# Kata göre ortalamanın üstü altı yorumlaması
def statusByStories(house):
    avgPrice = avgByStory[house['stories']]
    if house['price'] > avgPrice:
        return 'expensive'
    else:
        return 'cheap'

# Kata göre pahalılık durumu
#housing['statusByStories'] = housing.apply(statusByStories) # tabloya eklendi
'''
