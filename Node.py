
class Node:
    def __init__(self, link, title, parent=None):
        self.link = link
        self.title = title
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)
    def list_children(self):
        ret = ", ".join([child.title for child in self.children])
        if len(ret) < 1:
            return "no one"
        return ret
