# CSV dosyaları handle lamak icin
import pandas as pd 

import matplotlib.pyplot as plt

# CSV dosyasını yükledim
housing = pd.read_csv('Housing.csv')

# Pahalılık durumu
expStatus = [ # 0 - 9 pahalılık durumu -9'a yaklaştıkça pahalılaşıyor-
    (13300000, 9),
    (11000000, 8),
    (9850000, 7),
    (8700000, 6),
    (7500000, 5),
    (6400000, 4),
    (5200000, 3),
    (4100000, 2),
    (2900000, 1),
    (1750000, 0)
]

# Relation between price and area

# Pahalılık 
def status(price):
    for min, status in expStatus:
        if price >= min:
            return status

# Alan - pahalılık durumu
housing['status'] = housing['price'].apply(status) # tabloya eklendi

plt.title('Relationship between Area - Expensiveness') # Grafik başlığı
plt.scatter(housing['area'], housing['status'], s=50, c='red', alpha=0.1, edgecolors='black') # Grafik iskeleti

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
expStatusByBedroomNum = [ # 0 - 9 pahalılık durumu -9'a yaklaştıkça pahalılaşıyor-
    (1300000, 9),
    (1100000, 8),
    (9850000, 7),
    (8700000, 6),
    (7500000, 5),
    (6400000, 4),
    (5200000, 3),
    (4100000, 2),
    (2900000, 1),
    (1750000, 0)
]

# Yatak odası sayısına göre ortalamanın üstü/altı yorumlaması
avgByBedrooms = housing.groupby('bedrooms')['price'].mean() 

def statusByBedroomNum(housePrice):
    for min, status in expStatusByBedroomNum:
        if area >= min:
            return status

# Yatak odası sayısına göre pahalılık durumu
housing['bedroomsStatus'] = housing.apply(statusByBedroomNum, axis=1) # tabloya eklendi

print(housing['bedroomsStatus'])
print(max(housing['price']))
print(min(housing['price']))
'''
'''
plt.title('Bedrooms - Price Analysis') # Grafik başlığı
#plt.scatter(housing['bedrooms'], housing['bedroomsStatus'], s=50, c='violet', alpha=0.1, edgecolors='purple') # Grafik iskeleti

# X Ekseni
plt.xlabel('Bedrooms') # X ekseninin temsili
plt.xlim(0, 7) # X ekseni aralığı
plt.xticks([1, 2, 3, 4, 5, 6]) # X eksenindeki aralıklar

# Y Ekseni
plt.ylabel('House Price') # Y ekseni temsili
plt.ylim(0, 10) # Y ekseni aralığı
plt.yticks(['cheap', 'expensive']) # Y eksenindeki aralıklar


# Kata göre ortalama
avgByStory = housing.groupby('stories')['price'].mean() 

# Kata göre ortalamanın üstü altı yorumlaması
def statusByStories(house):
    avgPrice = avgByStory[house['stories']]
    if house['price'] > avgPrice:
        return 'expensive'
    else:
        return 'cheap'
'''
# Kata göre pahalılık durumu
#housing['storiesStatus'] = housing.apply(statusByStories) # tabloya eklendi

