from bs4 import BeautifulSoup
import requests
import re

def scraper(link):

    page_response = requests.get(link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    node = page_content.find('a', title='Digivolution', text=re.compile("Next forms.*"))
    next_links = []
    try:
        next_links = node.parent.parent.findNext('td').find_all('a', title=True)
    except AttributeError:
        pass
    pairs = []
    for link in next_links:
        pairs.append((link.attrs['href'], link.attrs['title']))
    return pairs

# def find_name(link):
#     page_response = requests.get(link, timeout=5)
#     page_content = BeautifulSoup(page_response.content, "html.parser")


if __name__ == "__main__":
    scraper('https://digimon.fandom.com/wiki/Greymon')