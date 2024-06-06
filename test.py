import requests
from bs4 import BeautifulSoup

# Vatan Bilgisayar'daki ürün listesi sayfasının URL'si (örnek URL, değiştirilmesi gerekebilir)
url = "https://www.vatanbilgisayar.com/"

# HTTP isteği gönder
try:
    response = requests.get(url)
    response.raise_for_status()  # HTTP hataları kontrolü
    print("HTTP isteği başarılı.")
except requests.exceptions.RequestException as e:
    print(f"HTTP isteği başarısız: {e}")
    exit(1)

# Sayfanın içeriğini BeautifulSoup ile parse et
try:
    soup = BeautifulSoup(response.content, 'html.parser')
    print("Sayfa parse işlemi başarılı.")
except Exception as e:
    print(f"Sayfa parse işlemi başarısız: {e}")
    exit(1)

# Ürün adlarını bul
try:
    product_names = soup.find_all('div', {'class': 'product-list__product-name'})
    products = [product.text.strip() for product in product_names]
    if not products:
        print("Hiç ürün bulunamadı.")
    else:
        print(f"{len(products)} ürün bulundu.")
except Exception as e:
    print(f"Ürün adları alınırken bir hata oluştu: {e}")
    exit(1)

# Karakter temizleme fonksiyonu
def clean_text(text):
    return text.replace(',', '').replace("'", '').replace('"', '')

# Temizlenmiş ürün adlarını metin dosyasına yaz
try:
    with open('vatan.csv', 'w', encoding='utf-8') as file:
        for product in products:
            clean_product = clean_text(product)
            file.write(f"'{clean_product}'\n")
    print("Veriler 'vatan.csv' dosyasına başarıyla kaydedildi.")
except Exception as e:
    print(f"Dosya yazılırken bir hata oluştu: {e}")
    exit(1)
