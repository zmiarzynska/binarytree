from node import Node


class TreeCalculations:

    def __init__(self, node):
        if isinstance(node, Node):
            self.root = node
            self.numbers = []
            self.numbers.append(node.value)
        else:
            raise TypeError("To create instance of Treecalculations, Node type required")

    def change_root(self, node):
        if isinstance(node, Node):
            self.root = node
            self.numbers = []
            self.numbers.append(node.value)
        else:
            raise TypeError("Node type required")

    def get_sum(self, node=None):
        if node is None:
            node = self.root
        if isinstance(node, Node):
            self.numbers.clear()
            amount = 0
            self.add_node_to_list(node)
            for i in range(len(self.numbers)):
                amount += self.numbers[i]
            return amount
        else:
            raise TypeError("Node type required")

    def get_mean(self, node=None):
        if node is None:
            node = self.root
        if isinstance(node, Node):
            amount = self.get_sum(node)
            return amount/len(self.numbers)
        else:
            raise TypeError("Node type required")

    def get_median(self, node=None):
        if node is None:
            node = self.root
        if isinstance(node, Node):
            self.numbers.clear()
            self.add_node_to_list(node)
            self.numbers.sort()
            if len(self.numbers) % 2 == 0:
                temp = self.numbers[len(self.numbers) // 2] + self.numbers[(len(self.numbers) // 2) - 1]
                return temp / 2
            else:
                return self.numbers[(len(self.numbers) - 1) // 2]
        else:
            raise TypeError("Node type required")

    def add_node_to_list(self, node):
        if node is not None:
            self.numbers.append(node.value), self.add_node_to_list(node.right), self.add_node_to_list(node.left)
        else:
            pass








