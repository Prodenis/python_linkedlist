import unittest
import dynarray


class ListTest(unittest.TestCase):
    def test_insert(self):
        da = dynarray.DynArray()
        i = 0
        da.append(i)
        i = 1
        da.append(i)
        i = 2
        da.append(i)
        i = 7
        da.append(i)
        i = 3
        da.append(i)
        i = 4
        da.append(i)
        da1 = dynarray.DynArray()
        for j in range(5):
            da1.append(j)
        test = da.test_list()
        da1.insert(3, 7)
        test1 = da1.test_list()
        self.assertEqual(test, test1)

    def test_delete(self):
        da = dynarray.DynArray()
        i = 0
        da.append(i)
        i = 1
        da.append(i)
        i = 2
        da.append(i)
        i = 3
        da.append(i)
        i = 5
        da.append(i)
        da1 = dynarray.DynArray()
        for j in range(6):
            da1.append(j)
        test = da.test_list()
        da1.delete(4)
        test1 = da1.test_list()
        self.assertEqual(test, test1)