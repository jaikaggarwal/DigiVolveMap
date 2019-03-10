from scraper import scraper
from Node import Node
from queue import Queue

def BFS(root_link):

    q = Queue()
    seen = set()

    base_link = root_link[:root_link[:root_link.rfind('/')].rfind('/')]
    root_title = root_link[:root_link.rfind('/')]
    root_node = Node(title=root_title, link=root_link)
    seen.add(root_title)
    q.put(root_node)

    while not q.empty():
        curr = q.get()
        print(curr.title)
        next_links = scraper(curr.link)
        for link in next_links:
            next_node = Node(link=base_link+link[0], title=link[1], parent=curr)
            if next_node.title not in seen:
                q.put(next_node)
                seen.add(next_node.title)

if __name__ == '__main__':
    BFS('https://digimon.fandom.com/wiki/Agumon')

