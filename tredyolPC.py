import requests
from bs4 import BeautifulSoup

# Sayfanın URL'si (örnek URL, değiştirilmesi gerekebilir)
url = "https://www.trendyol.com/laptop-x-c103108"

# HTTP isteği gönder
response = requests.get(url)

# Sayfanın içeriğini BeautifulSoup ile parse et
soup = BeautifulSoup(response.content, 'html.parser')

# Ürün bilgilerini bul
urun_bilgileri = soup.find_all('h3', {'class': 'prdct-desc-cntnr-ttl-w two-line-text'}) #ürün bilgileri
UrunBilgi = [i.text.strip() for i in urun_bilgileri]
print(UrunBilgi)

fiyat_bilgileri = soup.find_all('div', {'class': 'prc-box-dscntd'}) # fiyat bilgileri
fiyatBilgi = [i.text.strip() for i in fiyat_bilgileri]


#  metin dosyasına yaz
with open('TrendyolPC.txt', 'w', encoding='utf-8') as file:
    for title,fiyat in zip(UrunBilgi,fiyatBilgi):
        file.write(f"Ürün_bilgileri {title},Fiyat {fiyat}\n")

print("Job listings have been written to TrendyolPC.txt")