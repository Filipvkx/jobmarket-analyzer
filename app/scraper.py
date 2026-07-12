import requests
from bs4 import BeautifulSoup 

def test_scraper():
    url = "https://pythonjobs.github.io/"
    print(f"Start: {url}...")

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Bląd: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    page_title = soup.title.text
    print(f"Sukces! Tytuł stronki: {page_title}")

if __name__ == "__main__":
    test_scraper()