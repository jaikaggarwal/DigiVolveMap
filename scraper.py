from bs4 import BeautifulSoup, Tag, NavigableString
import requests
import re

def scraper(link):

    page_response = requests.get(link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    node = page_content.find('a', title='Digivolution', text=re.compile("Next forms.*"))
    next_links = []
    try:
        temp = node.parent.parent.findNext('td')
        to_remove_groups = re.findall(r"\(w/(.*)\)", temp.text)
        to_remove = []
        for group in to_remove_groups:
            to_remove.extend(re.findall(r"\b\w*mon.?\b", group))
        to_remove = [text.strip() for text in to_remove]
        next_links = temp.find_all('a', title=True)
        next_links = [next_link for next_link in next_links if next_link['title'] not in to_remove]
    except AttributeError:
        pass
    pairs = []
    for link in next_links:
        pairs.append((link.attrs['href'], link.attrs['title']))
    return pairs

if __name__ == "__main__":
    scraper('https://digimon.fandom.com/wiki/Omnimon')