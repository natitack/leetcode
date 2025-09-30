import unittest
from solution import Solution, ListNode

class TestSolution(unittest.TestCase):
    """
    Tests generated from prompt examples

    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. \
    Add the two numbers and return the sum as a linked list.
    """
    def list_to_listnode(self, lst):
        dummy = ListNode()
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def listnode_to_list(self, node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    def test_example_1(self):
        """
        Input: l1 = [2,4,3], l2 = [5,6,4] Output: [7,0,8] Explanation: 342 + 465 = 807.
        """
        l1 = self.list_to_listnode([2,4,3])
        l2 = self.list_to_listnode([5,6,4])
        Output = [7,0,8]
        s = Solution()
        result = s.addTwoNumbers(l1, l2)
        self.assertEqual(self.listnode_to_list(result), Output)

    def test_example_2(self):
        """
        l1 = [0], l2 = [0] Output: [0]
        """
        l1 = self.list_to_listnode([0])
        l2 = self.list_to_listnode([0])
        Output = [0]
        s = Solution()
        result = s.addTwoNumbers(l1, l2)
        self.assertEqual(self.listnode_to_list(result), Output)

    def test_example_3(self):
        """
        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] Output: [8,9,9,9,0,0,0,1]       
        """
        l1 = self.list_to_listnode([9,9,9,9,9,9,9])
        l2 = self.list_to_listnode([9,9,9,9])
        Output = [8,9,9,9,0,0,0,1]
        s = Solution()
        result = s.addTwoNumbers(l1, l2)
        self.assertEqual(self.listnode_to_list(result), Output)

        


if __name__ == '__main__':
    unittest.main()
