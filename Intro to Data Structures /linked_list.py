class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node.
    """
    data= None
    next_node= None

def __init__(self,data):
        self.data= data

def __repr__(self):
    return "<Node data: %s>" % self.data

class LinkedList:

    def __init__(self):
        self.head = None