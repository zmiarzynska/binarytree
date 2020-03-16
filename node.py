class Node:
    ''' Klasa node jest odpowiedzialna za strukturę węzła oraz za przyporządkowanie
    potomkow '''

    def __init__(self, data):
        if isinstance(data, int):
            self.left = None
            self.right = None
            self.value = data
        else:
            raise ValueError("Value of a node should be an Integer")



