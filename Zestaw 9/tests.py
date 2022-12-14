import pytest
from single_list import SingleList
from single_list import Node

class TestSingleList:

    @pytest.fixture(scope="class")
    def SingleListA(self):
        list = SingleList()
        list.insert_tail(Node(1, None))
        list.insert_tail(Node(1, None))
        list.insert_tail(Node(1, None))
        list.insert_tail(Node(1, None))
        list.insert_tail(Node(9, None))
        return list

    @pytest.fixture(scope="class")
    def SingleListB(self):
        list = SingleList()
        list.insert_tail(Node(7, None))
        list.insert_tail(Node(6, None))
        list.insert_tail(Node(5, None))
        list.insert_tail(Node(4, None))
        list.insert_tail(Node(2, None))
        return list

    def testRemoveTail(self, SingleListA, SingleListB):
        assert str(SingleListA.tail) == "9"
        assert str(SingleListA.remove_tail()) == "9"
        assert str(SingleListA.tail) != "9"

        SingleListA.insert_tail(Node(5))
        assert str(SingleListA.tail) == "5"

        assert str(SingleListB.tail) == "2"
        assert str(SingleListB.remove_tail()) == "2"
        assert str(SingleListB.tail) == "4"
        SingleListB.insert_tail(Node(7))

    def testJoin(self, SingleListA, SingleListB):
        SingleListA.join(SingleListB)
        assert str(SingleListA.head) == "1"
        assert str(SingleListA.tail) == "7"

        assert SingleListB.is_empty() == True

        SingleListB.join(SingleListA)

        assert SingleListA.is_empty() == True

        assert str(SingleListB.head) == "1"
        assert str(SingleListB.tail) == "7"

    def testClear(self, SingleListA, SingleListB):
        assert SingleListA.is_empty() == True
        
        SingleListB.clear()

        assert SingleListB.is_empty() == True