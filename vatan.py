import requests
from bs4 import BeautifulSoup

# LinkedIn'deki iş ilanları sayfasının URL'si (örnek URL, değiştirilmesi gerekebilir)
url = "https://www.vatanbilgisayar.com/"

# HTTP isteği gönder
response = requests.get(url)
print(response)
# Sayfanın içeriğini BeautifulSoup ile parse et
soup = BeautifulSoup(response.content, 'html.parser')

# İş ilanlarını bul
job_cards = soup.find_all('div', {'class': 'product-list__product-name'}) #adı
meslek = [i.text.strip() for i in job_cards]

def clean_text(text):
    return text.replace(',', '').replace("'", '').replace('"', '')

# İş ilanlarını metin dosyasına yaz
with open('vatan.csv', 'w', encoding='utf-8') as file:
    for title in zip(meslek):
        title = clean_text(title)
        file.write(f"{title}\n")


print("Job listings have been written to vatan.csv")