# CSV dosyaları handle lamak icin
import pandas as pd 

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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
'''
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

# Grafiğin okunurluğunu kolaylaştır
plt.grid(color='green', linestyle='--', linewidth=0.5)

# Graiği göster.
plt.show() 


# Relation between price and bedrooms/stories

# Yatak odası - Fiyat İlişkisi

plt.title('Bedrooms - Price Analysis') # Grafik başlığı

plt.scatter(housing['bedrooms'], housing['price'], s=50, c='violet', alpha=0.1, edgecolors='purple') # Grafik iskeleti

# X Ekseni
plt.xlabel('Bedrooms') # X ekseninin temsili
plt.xlim(0, 7) # X ekseni aralığı
plt.xticks([1, 2, 3, 4, 5, 6]) # X eksenindeki aralıklar

# Y Ekseni
plt.ylabel('House Price') # Y ekseni temsili
plt.ylim(0, 13500000) # Y ekseni aralığı
plt.yticks([1750000, 2900000, 4100000, 5200000, 6400000, 7500000, 8700000, 9850000, 11000000, 13300000]) # Y eksenindeki aralıklar

# Grafiğin okunurluğunu kolaylaştır
plt.grid(color='blue', linestyle='--', linewidth=0.5)

# Graiği göster.
plt.show()



# Kat - Fiyat İlişkisi

plt.title('Stories - Price Analysis') # Grafik başlığı

plt.scatter(housing['stories'], housing['price'], s=50, c='yellow', alpha=0.1, edgecolors='orange') # Grafik iskeleti

# X Ekseni
plt.xlabel('Stories') # X ekseni neyi temsil ediyor?
plt.xlim(0, 5) # X Ekseni aralığı
plt.xticks([1, 2, 3, 4]) # X eksenindeki aralıklar

# Y Ekseni
plt.ylabel('House Prices') # Y ekseni neyi temsil ediyor?
plt.ylim(0, 13500000) # Y ekseni aralığı
plt.yticks([1750000, 2900000, 4100000, 5200000, 6400000, 7500000, 8700000, 9850000, 11000000, 13300000]) # Y eksenindeki aralıklar

# Grafiğin okunurluğunu kolaylaştır
plt.grid(color='brown', linestyle='--', linewidth=0.5)

# Grafiği göster.
plt.show()
'''

# Bathrooms'a göre ortalama
avgByBathrooms = housing.groupby('bathrooms')['price'].mean()

def avgPrice(numbers_bathrooms):
    return avgByBathrooms.get(numbers_bathrooms, None)
        
housing['avgPrice_toBaths'] = housing['bathrooms'].apply(avgPrice)

plt.title("Average Price Graph For Bathrooms") # Grafik başlığı

colors = ['pink', 'violet', 'yellow', 'orange']
                                                        
plt.barh(avgByBathrooms.index, avgByBathrooms.values, color = colors)# Grafik iskeleti

# X Ekseni
plt.xlabel('Ortalama')
plt.xticks([1750000, 2900000, 4100000, 5200000, 6400000, 7500000, 8700000, 9850000, 11000000, 13300000])

# Y Ekseni
plt.ylabel('Bathrooms')
plt.yticks([1, 2, 3, 4])

# Grafiğin okunurluğunu kolaylaştır
plt.grid(color='red', linestyle='--', linewidth=0.3)

# Grafiği göster
plt.show() 

print(avgByBathrooms)


'''
plt.title("Average Price Graph For Bathrooms")
plt.barh(avgByBathrooms.index, avgByBathrooms.values, color=colors)  # Banyo sayısına göre ortalama fiyat
plt.xlabel('Average Price')
plt.ylabel('Bathrooms')
plt.show()
'''
# Furnishingstatus'e göre ortalama
avgByFurnishing = housing.groupby('furnishingstatus')['price'].mean()