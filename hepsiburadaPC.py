import requests
from bs4 import BeautifulSoup

# LinkedIn'deki iş ilanları sayfasının URL'si (örnek URL, değiştirilmesi gerekebilir)
url = "https://www.teknosa.com/gaming-laptop-c-116006001"

# HTTP isteği gönder
response = requests.get(url)
print(response)
# Sayfanın içeriğini BeautifulSoup ile parse et
soup = BeautifulSoup(response.content, 'html.parser')

# İş ilanlarını bul
job_cards = soup.find_all('h3', {'class': 'prd-title prd-title-style'}) #adı
meslek = [i.text.strip() for i in job_cards]
print(meslek)

# İş ilanlarını metin dosyasına yaz
with open('job_listings.txt', 'w', encoding='utf-8') as file:
    for title in zip(meslek):
        file.write(f"urun {title}\n")

print("Job listings have been written to job_listings.txt")