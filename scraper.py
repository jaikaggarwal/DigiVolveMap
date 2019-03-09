from bs4 import BeautifulSoup
import requests
import re

def scraper(link):

    page_response = requests.get(link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    node = page_content.find('a', title='Digivolution', text=re.compile("Next forms.*"))
    next_links = node.parent.parent.findNext('td').find_all('a', title=True)
    print(next_links)
    pairs = []
    for link in next_links:
        pairs.append((link.attrs['href'], link.attrs['title']))
    print(pairs)



if __name__ == "__main__":
    scraper('https://digimon.fandom.com/wiki/Greymon')