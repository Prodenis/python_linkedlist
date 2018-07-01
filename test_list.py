import unittest
import list

n1 = list.Node(12)
n2 = list.Node(55)
n1.next = n2


s_list = list.LinkedList()
s_list.add_in_tail(n1)
s_list.add_in_tail(n2)
s_list2 = list.LinkedList()


s_list_clear = list.LinkedList()
s_list_clear.add_in_tail(n1)
s_list_clear.add_in_tail(n2)



class ListTest(unittest.TestCase):
    def test_count(self):
        self.assertEqual(list.LinkedList.length_list(s_list), 2)

    def test_count_empty(self):
        self.assertEqual(list.LinkedList.length_list(s_list2), 0)

    def test_clear(self):
        self.assertEqual(list.LinkedList.clear(s_list_clear), None)

    def test_insert(self):
        s_list_insert = list.LinkedList()
        s_list_insert.add_in_tail(n1)
        s_list_insert.add_in_tail(n2)
        s_list_insert.add_in_tail(list.Node(20))
        test = s_list_insert.list_test()
        test1 = s_list.list_test()
        self.assertEqual(test, test1)

    def test_remove_first(self):
        s_list_remove = list.LinkedList()
        s_list_remove.add_in_tail(n1)
        s_list_remove.add_in_tail(n2)
        s_list_remove.remove(12)
        test = s_list_remove.list_test()
        s_list_remove_end = list.LinkedList()
        s_list_remove_end.add_in_tail(n2)
        test1 = s_list_remove_end.list_test()
        self.assertEqual(test, test1)

    def test_remove_middle(self):
        s_list_remove = list.LinkedList()
        s_list_remove.add_in_tail(n1)
        s_list_remove.add_in_tail(n2)
        s_list_remove.add_in_tail(list.Node(60))
        s_list_remove.remove(15)
        test = s_list_remove.list_test()
        s_list_remove_end = list.LinkedList()
        s_list_remove_end.add_in_tail(n1)
        s_list_remove_end.add_in_tail(list.Node(60))
        test1 = s_list_remove_end.list_test()
        self.assertEqual(test, test1)

    def test_remove_end(self):
        s_list_remove = list.LinkedList()
        s_list_remove.add_in_tail(n1)
        s_list_remove.add_in_tail(n2)
        s_list_remove.add_in_tail(list.Node(60))
        s_list_remove.remove(60)
        test = s_list_remove.list_test()
        s_list_remove_end = list.LinkedList()
        s_list_remove_end.add_in_tail(n1)
        s_list_remove_end.add_in_tail(n2)
        test1 = s_list_remove_end.list_test()
        self.assertEqual(test, test1)

    def test_remove_all(self):
        s_list_remove = list.LinkedList()
        s_list_remove.add_in_tail(n1)
        s_list_remove.add_in_tail(n2)
        s_list_remove.add_in_tail(list.Node(60))
        s_list_remove.add_in_tail(list.Node(60))
        s_list_remove.add_in_tail(list.Node(60))
        s_list_remove.remove_all(60)
        test = s_list_remove.list_test()
        s_list_remove_end = list.LinkedList()
        s_list_remove_end.add_in_tail(n1)
        s_list_remove_end.add_in_tail(n2)
        test1 = s_list_remove_end.list_test()
        self.assertEqual(test, test1)

    def test_compare(self):
        s_list_compare = list.LinkedList()
        s_list_compare.add_in_tail(n1)
        s_list_compare.add_in_tail(n2)
        s_list_compare.add_in_tail(list.Node(60))
        s_list_compare_end = list.LinkedList()
        s_list_compare_end.add_in_tail(list.Node(24))
        s_list_compare_end.add_in_tail(list.Node(110))
        s_list_compare_end.add_in_tail(list.Node(120))
        test2 = s_list_compare_end.list_test()
        test1 = list.compare(s_list_compare, s_list_compare)
        self.assertEqual(test1, test2)

    def test_search(self):
        s_list_search = list.LinkedList()
        s_list_search.add_in_tail(n1)
        s_list_search.add_in_tail(n2)
        s_list_search.add_in_tail(list.Node(60))
        s_list_search.add_in_tail(list.Node(60))
        test = s_list_search.search(60)
        test1 = []
        test1.append(list.Node(60))
        test1.append(list.Node(60))
        self.assertEqual(test, test1)


if __name__ == "__main__":
    unittest.main()