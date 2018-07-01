import unittest
import bidirectional_list

n1 = bidirectional_list.Node2(12)
n2 = bidirectional_list.Node2(55)
n1.next = n2


class ListTest(unittest.TestCase):
    def test_remove_first(self):
        s_list = bidirectional_list.LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(bidirectional_list.Node2(20))
        s_list_remove_first = bidirectional_list.LinkedList2()
        s_list_remove_first.add_in_tail(bidirectional_list.Node2(55))
        s_list_remove_first.add_in_tail(bidirectional_list.Node2(20))
        s_list.remove(12)
        test = s_list.test_list()
        test1 = s_list_remove_first.test_list()
        self.assertEqual(test, test1)

    def test_remove_middle(self):
        s_list = bidirectional_list.LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(bidirectional_list.Node2(20))
        s_list_remove_middle = bidirectional_list.LinkedList2()
        s_list_remove_middle.add_in_tail(bidirectional_list.Node2(12))
        s_list_remove_middle.add_in_tail(bidirectional_list.Node2(20))
        s_list.remove(55)
        test = s_list.test_list()
        test1 = s_list_remove_middle.test_list()
        self.assertEqual(test, test1)

    def test_remove_end(self):
        s_list = bidirectional_list.LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(bidirectional_list.Node2(20))
        s_list_remove_end = bidirectional_list.LinkedList2()
        s_list_remove_end.add_in_tail(bidirectional_list.Node2(12))
        s_list_remove_end.add_in_tail(bidirectional_list.Node2(55))
        s_list.remove(20)
        test = s_list.test_list()
        test1 = s_list_remove_end.test_list()
        self.assertEqual(test, test1)

    def test_add_in_head(self):
        s_list = bidirectional_list.LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(bidirectional_list.Node2(20))
        s_list_add = bidirectional_list.LinkedList2()
        s_list_add.add_in_tail(bidirectional_list.Node2(1))
        s_list_add.add_in_tail(bidirectional_list.Node2(12))
        s_list_add.add_in_tail(bidirectional_list.Node2(55))
        s_list_add.add_in_tail(bidirectional_list.Node2(20))
        s_list.add_in_head(bidirectional_list.Node2(1))
        test = s_list.test_list()
        test1 = s_list_add.test_list()
        self.assertEqual(test, test1)

    def test_insert(self):
        s_list = bidirectional_list.LinkedList2()
        s_list.add_in_tail(n1)
        s_list.add_in_tail(n2)
        s_list.add_in_tail(bidirectional_list.Node2(20))
        s_list_insert = bidirectional_list.LinkedList2()
        s_list_insert.add_in_tail(bidirectional_list.Node2(12))
        s_list_insert.add_in_tail(bidirectional_list.Node2(13))
        s_list_insert.add_in_tail(bidirectional_list.Node2(55))
        s_list_insert.add_in_tail(bidirectional_list.Node2(20))
        s_list.insert(bidirectional_list.Node2(13), bidirectional_list.Node2(12))
        test = s_list.test_list()
        test1 = s_list_insert.test_list()
        self.assertEqual(test, test1)


if __name__ == "__main__":
    unittest.main()