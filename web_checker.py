import time
import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"  
KEYWORD = "Ukraine" 

def check_website():
    try:
        response = requests.get(URL)
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, "html.parser")

        if KEYWORD.lower() in soup.get_text().lower():
            print(f"[+] Anahtar kelime bulundu: '{KEYWORD}'!")
        else:
            print(f"[-] '{KEYWORD}' henüz sayfada yok.")

    except requests.exceptions.RequestException as e:
        print(f"[!] Hata oluştu: {e}")

while True:
    check_website()
    print("Tekrar kontrol etmek için 60 saniye bekleniyor...\n")
    time.sleep(60)  