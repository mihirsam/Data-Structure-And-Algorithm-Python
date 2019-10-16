#!/usr/bin/python

import unittest
import random
from redBlack import *
from linkedList import *
import time
from BST import *
class TestInsert(unittest.TestCase):
    def test_total_num_of_items(self):
        test_tree = RedBlackTree()
        for num in[1,2,3,4,5]:
            test_tree.add(num)
        self.assertEqual(len([1, 2, 3,4,5]), test_tree.size, "There should be 5 elements in this tree")
        self.assertEqual(test_tree.root.red, False, "The trees root should be false")

    def benchmark_against_linked_list_search_100000(self):
        """
        This should fine the last possible element in the list THe Linked lIst should be slower than the RBT due to
         linear structure vs a logarithmic structure
        :return:
        """
        test_tree = RedBlackTree()
        test_linked_list = LinkedList()
        test_list =[random.randint(1, 100) for _ in range(100000)]
        last_item_in_list = test_list[len(test_list)-1]

        # ----- Benchmark section for LL vs RBT -----#

        # ----- LinkList Benchmarks -----#


        for num in test_list:
            test_linked_list.append(num)


        # -----  RBT Benchmarks ----- #


        for num in test_list:
            test_tree.add(num)

        LL_start_time = time.time()
        test_linked_list.find(last_item_in_list)
        LL_end_time = time.time()

        LL_running_time = LL_end_time - LL_start_time


        RBT_start_time = time.time()
        test_tree.contains(last_item_in_list)
        RBT_end_time = time.time()

        RBT_running_time = RBT_end_time - RBT_start_time

        print("LL ran in {}. RBT ran in {}".format(LL_running_time,RBT_running_time))

        self.assertGreater(LL_running_time,RBT_running_time,"RBT running time should be shorter")

    def test_against_regular_BST(self):
        test_list_random = [random.randint(1, 100) for _ in range(100)]
        test_list_linear = [i for i in range(10000)]

        test_BST = BinarySearchTree()
        test_tree = RedBlackTree()




if __name__ == '__main__':
    unittest.main()