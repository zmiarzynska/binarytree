from calculations import TreeCalculations
from node import Node
import unittest
from statistics import median
from statistics import mean

# creating first tree
root=Node(5)
root.left=Node(3)
root.right=Node(7)
root.left.left=Node(2)
root.left.right=Node(5)
root.right.left=Node(1)
root.right.right=Node(0)
root.right.right.left=Node(2)
root.right.right.right=Node(8)
root.right.right.right.right=Node(5)
firsttree=TreeCalculations(root)

# creating second tree
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(10)
node5 = Node(15)
node6 = Node(11)
node7 = Node(1)
node1.left = node2
node1.right = node3
node2.left = node4
node4.left = node5
node3.right = node6
node3.left=node7
secondtree = TreeCalculations(node1)

# Kod testujący moduł.


class TestTreeCalculations(unittest.TestCase):

    def test_not_int(self):
        with self.assertRaises(ValueError):
            Node("ala")

    def test_not_int2(self):
        with self.assertRaises(ValueError):
            Node("1")

    def test_sum_first_from_root(self):
        self.assertEqual(firsttree.get_sum(None), 38)

    def test_sum_firsttree(self):
        firsttree.add_node_to_list(root.left)
        array = firsttree.numbers
        self.assertEqual(firsttree.get_sum(root.left), sum(array))
        self.assertEqual(firsttree.get_sum(root.left), sum(firsttree.numbers))
        self.assertEqual(firsttree.get_sum(root.right), sum(firsttree.numbers))
        self.assertEqual(firsttree.get_sum(root.left.left), sum(firsttree.numbers))
        self.assertEqual(firsttree.get_sum(root.left.right), sum(firsttree.numbers))
        self.assertEqual(firsttree.get_sum(root.right.left), sum(firsttree.numbers))
        self.assertEqual(firsttree.get_sum(root.right.right), sum(firsttree.numbers))
        self.assertEqual(firsttree.get_sum(root.right.right.right), sum(firsttree.numbers))
        self.assertEqual(firsttree.get_sum(root.right.right.left), sum(firsttree.numbers))
        self.assertEqual(firsttree.get_sum(root.right.right.right.right), sum(firsttree.numbers))

    def test_sum_firsttree_root_right_right_right_right(self):
        self.assertEqual(firsttree.get_sum(root.right.right.right.right), 5)

    def test_sum_secondtree(self):
        secondtree.add_node_to_list(node2)
        array = secondtree.numbers
        self.assertEqual(secondtree.get_sum(node2), sum(array))
        self.assertEqual(secondtree.get_sum(node2), sum(secondtree.numbers))
        self.assertEqual(secondtree.get_sum(node2), sum([node2.value,node4.value,node5.value]))
        self.assertEqual(secondtree.get_sum(), sum(secondtree.numbers))
        self.assertEqual(secondtree.get_sum(node3), sum(secondtree.numbers))
        self.assertEqual(secondtree.get_sum(node4), sum(secondtree.numbers))
        self.assertEqual(secondtree.get_sum(node5), sum(secondtree.numbers))
        self.assertEqual(secondtree.get_sum(node6), sum(secondtree.numbers))
        self.assertEqual(secondtree.get_sum(node7), sum(secondtree.numbers))

    def test_mean_firsttree_root(self):
        self.assertEqual(firsttree.get_mean(), 3.8)


    def test_mean_firsttree(self):
        firsttree.add_node_to_list(root.left)
        array = firsttree.numbers
        self.assertEqual(firsttree.get_mean(root.left), mean(array))
        self.assertEqual(firsttree.get_mean(root.left), mean(firsttree.numbers))
        self.assertEqual(firsttree.get_mean(root.right), mean(firsttree.numbers))
        self.assertEqual(firsttree.get_mean(root.left.left), mean(firsttree.numbers))
        self.assertEqual(firsttree.get_mean(root.left.right), mean(firsttree.numbers))
        self.assertEqual(firsttree.get_mean(root.right.left), mean(firsttree.numbers))
        self.assertEqual(firsttree.get_mean(root.right.right), mean(firsttree.numbers))
        self.assertEqual(firsttree.get_mean(root.right.right.right), mean(firsttree.numbers))
        self.assertEqual(firsttree.get_mean(root.right.right.left), mean(firsttree.numbers))
        self.assertEqual(firsttree.get_mean(root.right.right.right.right), mean(firsttree.numbers))

    def test_mean_firsttree_root_right_right_right_right(self):
        self.assertEqual(firsttree.get_mean(root.right.right.right.right), 5)

    def test_mean_secondtree(self):
        secondtree.add_node_to_list(node2)
        array = secondtree.numbers
        self.assertEqual(secondtree.get_mean(node2), mean(array))
        self.assertEqual(secondtree.get_mean(), mean(secondtree.numbers))
        self.assertEqual(secondtree.get_mean(node3), mean(secondtree.numbers))
        self.assertEqual(secondtree.get_mean(node4), mean(secondtree.numbers))
        self.assertEqual(secondtree.get_mean(node5), mean(secondtree.numbers))
        self.assertEqual(secondtree.get_mean(node6), mean(secondtree.numbers))
        self.assertEqual(secondtree.get_mean(node7), mean(secondtree.numbers))


    def test_median_firsttree_root(self):
        self.assertEqual(firsttree.get_median(), 4)

    def test_median_firsttree(self):
        firsttree.add_node_to_list(root.left)
        array = firsttree.numbers
        self.assertEqual(firsttree.get_median(root.left), median(array))
        self.assertEqual(firsttree.get_median(root.left), median(firsttree.numbers))
        self.assertEqual(firsttree.get_median(root.right), median(firsttree.numbers))
        self.assertEqual(firsttree.get_median(root.left.left), median(firsttree.numbers))
        self.assertEqual(firsttree.get_median(root.left.right), median(firsttree.numbers))
        self.assertEqual(firsttree.get_median(root.right.left), median(firsttree.numbers))
        self.assertEqual(firsttree.get_median(root.right.right), median(firsttree.numbers))
        self.assertEqual(firsttree.get_median(root.right.right.right), median(firsttree.numbers))
        self.assertEqual(firsttree.get_median(root.right.right.left), median(firsttree.numbers))
        self.assertEqual(firsttree.get_median(root.right.right.right.right), median(firsttree.numbers))


    def test_median_firsttree_root_right_right_right_right(self):
        self.assertEqual(firsttree.get_median(root.right.right.right.right), 5)

    def test_median_secondtree(self):
        secondtree.add_node_to_list(node2)
        array = secondtree.numbers
        self.assertEqual(secondtree.get_median(node2), median(array))
        self.assertEqual(secondtree.get_median(), median(secondtree.numbers))
        self.assertEqual(secondtree.get_median(node3), median(secondtree.numbers))
        self.assertEqual(secondtree.get_median(node4), median(secondtree.numbers))
        self.assertEqual(secondtree.get_median(node5), median(secondtree.numbers))
        self.assertEqual(secondtree.get_median(node6), median(secondtree.numbers))
        self.assertEqual(secondtree.get_median(node7), median(secondtree.numbers))

if __name__ == "__main__":  # run all tests
    unittest.main()