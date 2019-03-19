from scraper import scraper
from Node import Node
from queue import Queue

def BFS(root_link):

    q = Queue()
    seen = set()
    explored = []

    base_link = root_link[:root_link[:root_link.rfind('/')].rfind('/')]
    root_title = root_link[root_link.rfind('/') + 1:]
    root_node = Node(title=root_title, link=root_link)
    seen.add(root_title)
    q.put(root_node)

    while not q.empty():
        curr = q.get()
        next_links = scraper(curr.link)
        for link in next_links:
            if link[1] not in seen:
                next_node = Node(link=base_link+link[0], title=link[1], parent=curr)
                curr.add_child(next_node)
                q.put(next_node)
                seen.add(next_node.title)
        explored.append(curr)
    for node in explored:
        print("{} evolves into {}".format(node.title, node.list_children()))

if __name__ == '__main__':
    BFS('https://digimon.fandom.com/wiki/Greymon')

