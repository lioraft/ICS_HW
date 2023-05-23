from functools import total_ordering
import copy

class ByteNode:
    def __init__(self, byte):
        """
        A constructor for ByteNode class.
        Attributes: byte, next
        """
        if not isinstance(byte, str):
            raise TypeError("You entered a byte of wrong type")
        valid_byte = True
        for i in range(len(byte)):
            if byte[i] != "0" and byte[i] != "1":
                valid_byte = False
        if not valid_byte or len(byte) > 8:
            raise ValueError("The byte you entered is not valid")
        self.byte = byte
        self.next = None

    def get_byte(self):
        """
        :return: The string that represents the byte node
        """
        return self.byte

    def get_next(self):
        """
        :return: The next byte node.
        """
        return self.next

    def set_next(self, next):
        """
        Takes in an object of type ByteNode, and sets it as the next byte.
        """
        self.next = next

    def __repr__(self):
        """
        :return: The string representation of the ByteNode.
        """
        return "[" + self.byte + "]=>"


@total_ordering
class LinkedListBinaryNum:
    def __init__(self, num=0):
        """
        A constructor for LinkedListBinaryNum class.
        Takes in a number, and sets attributes of the binary num - an head for the
        ByteNodes linked list and the size of the linked list.
        if num is not in valid range, exception will be raised.
        """
        # Exception: The input number is not valid
        if not isinstance(num, int):
            raise TypeError("The number is not an whole number!")
        if num < 0:
            raise ValueError("The number is negative!")
        # Edge case - num is 0:
        if num == 0:
            self.head = ByteNode("00000000")
            self.size = 1
        # Calculating the binary representation and converting it to a string
        else:
            binary_str = ""
            while num != 0:
                binary_str = str(num % 2) + binary_str
                num = num // 2
            if len(binary_str) % 8 != 0:
                binary_str = "0" * (8 - (len(binary_str) % 8)) + binary_str
            # Setting all the links
            self.head = None
            while len(binary_str) > 0:
                if self.head is None:
                    self.head = ByteNode(binary_str[:8])
                    binary_str = binary_str[8:]
                    self.size = 1
                else:
                    next_byte = self.head
                    while next_byte.get_next() is not None:
                        next_byte = next_byte.get_next()
                    next_byte.set_next(ByteNode(binary_str[:8]))
                    binary_str = binary_str[8:]
                    self.size = self.size + 1

    def add_MSB(self, byte):
        """
        Takes in a string of a ByteNode, and sets it as the MSB of the current binary linked list.
        """
        temp = self.head
        self.head = ByteNode(byte)
        self.head.set_next(temp)
        self.size = self.size + 1

    def __len__(self):
        """
        :return: The length of the binary linked list.
        """
        return self.size

    def __str__(self):#end user
        """
        :return: A string representation of the binary linked list for end users.
        """
        temp = self.head
        str_of_bytes = "|"
        while temp is not None:
            str_of_bytes = str_of_bytes + temp.get_byte() + "|"
            temp = temp.get_next()
        return str_of_bytes

    def __repr__(self):#developer
        """
        :return: A string representation of the binary linked list for developers.
        """
        temp = self.head
        str_of_bytes = ""
        while temp is not None:
            str_of_bytes = str_of_bytes + repr(temp)
            temp = temp.get_next()
        if self.size == 1:
            return "LinkedListBinaryNum with 1 Byte, Bytes map: " + str_of_bytes + "None"
        else:
            return "LinkedListBinaryNum with " + str(self.size) + " Bytes, Bytes map: " + str_of_bytes + "None"

    def __getitem__(self, item):
        """
        Takes in an index and returns the object in that index.
        Args:
            item (int): The index. if not in the valid range, exception will be raised.
        Returns:
            str/Exception: if index is in the valid range, the function returns the string of the
            requested ByteNode. if not in the valid range, raises an Exception (ValueError). if not of type
            int, raises an exception (TypeError) as well.
        """
        if not isinstance(item, int):
            raise TypeError("The index you inserted is not an instance of integer")
        if item >= self.size or item <= -self.size-1:
            raise ValueError("Index is out of range!")
        cur = self.head
        if item >= 0:
            for i in range(item):
                cur = cur.get_next()
            return cur.get_byte()
        else:
            for i in range(self.size + item):
                cur = cur.get_next()
            return cur.get_byte()

    def __gt__(self, other):
        """
        Takes in another object of type LinkedListBinaryNum and returns if the current object
        is bigger than the other object or not.
        :param other: an object of type LinkedListBinaryNum.
        :return: A boolean: If the current linked list binary number is bigger than the other, returns True.
        otherwise, returns False.
        """
        # Testing the other object is a LinkedListBinaryNum
        if not isinstance(other, LinkedListBinaryNum):
            raise TypeError("The object you inserted is not an instance of LinkedListBinaryNum")
        # Calculating the decimal of the current binary
        temp = self.head
        cur_bin_str = ""
        while temp is not None:
            cur_bin_str = cur_bin_str + temp.get_byte()
            temp = temp.get_next()
        cur_bin = 0
        for i in range(len(cur_bin_str)):
            cur_bin = cur_bin * 2 + int(cur_bin_str[i])
        # Calculating the decimal of the other binary object
        temp = other.head
        compare_bin_str = ""
        while temp is not None:
            compare_bin_str = compare_bin_str + temp.get_byte()
            temp = temp.get_next()
        compare_bin = 0
        for i in range(len(compare_bin_str)):
            compare_bin = compare_bin * 2 + int(compare_bin_str[i])
        return True if cur_bin > compare_bin else False


    #Order relations:

    def __add__(self, other):
        """
        Takes in another number (as int or LinkedListBinaryNum), returns the sum of the two numbers
        :param other (int/LinkedListBinaryNum): A number that needs to be added to the current number
        :return (LinkedListBinaryNum/Exception): If the added number is not of type int or LinkedListBinaryNum,
        a TypeError will be raised. if the number is a negative number, ValueError will be raised.
        else, the function will return the addition of the numbers.
        """
        # Testing the other object is a LinkedListBinaryNum or a positive whole number
        if not isinstance(other, LinkedListBinaryNum) and not isinstance(other, int) > 0:
            raise TypeError("The object you inserted can not be added")
        if isinstance(other, int) and other < 0:
            raise ValueError("Can't add negative number")
        # String of current binary linked list
        temp = self.head
        cur_bin_str = ""
        while temp is not None:
            cur_bin_str = cur_bin_str + temp.get_byte()
            temp = temp.get_next()
        # String of other object binary linked list
        # If input is an whole number it needs to be converted to a linked list binary num
        if not isinstance(other, LinkedListBinaryNum):
            other_bin = LinkedListBinaryNum(other)
            temp = other_bin.head
        else:
            temp = other.head
        addend_bin_str = ""
        while temp is not None:
            addend_bin_str = addend_bin_str + temp.get_byte()
            temp = temp.get_next()
        # Addition of the numbers (as binary strings) with vertical addition
        carry = 0
        added_result = ""
        while len(cur_bin_str) > 0 or len(addend_bin_str) > 0:
            # Calculating sum of current digits, including carry from previous iteration
            # While considering different lengths of binary numbers
            cur_sum = carry
            if len(cur_bin_str) > 0 and len(addend_bin_str) > 0:
                cur_sum = cur_sum + int(cur_bin_str[len(cur_bin_str)-1:]) + int(addend_bin_str[len(addend_bin_str)-1:])
            if len(cur_bin_str) > 0 and len(addend_bin_str) == 0:
                cur_sum = cur_sum + int(cur_bin_str[len(cur_bin_str)-1:])
            if len(cur_bin_str) < 0 and len(addend_bin_str) == 0:
                cur_sum = cur_sum + int(addend_bin_str[len(addend_bin_str)-1:])
            # If the sum is 2 or 0, we need to add 0 to the solution. if it's 1 or 3, we add 1
            if cur_sum % 2 == 0:
                added_result = added_result + "0"
            else:
                added_result = added_result + "1"
            # If sum is bigger than 1, there will be a carry for next calculation
            if cur_sum > 1:
                carry = 1
            else:
                carry = 0
            cur_bin_str = cur_bin_str[:len(cur_bin_str) - 1]
            addend_bin_str = addend_bin_str[:len(addend_bin_str) - 1]
        # Checking if the was a carry we didn't add from the last calculation
        if carry > 0:
            added_result = added_result + "1"
        # Creating the number itself from the string by adding new msb each time
        result_num = LinkedListBinaryNum()
        while len(added_result) > 0:
            result_num.add_MSB(added_result[:8][::-1])
            added_result = added_result[8:]
        # Removing the the last node extra node (which is 0)
        temp = result_num.head
        while temp.get_next().get_next() != None:
            temp = temp.get_next()
        temp.set_next(None)
        return result_num

    def __sub__(self, other):
        """
        Takes in another number (as int or LinkedListBinaryNum), returns the subtraction of the two numbers
        :param other (int/LinkedListBinaryNum): A subtrahend. this is the number that needs to be subtracted from the
        current number.
        :return (LinkedListBinaryNum/Exception): If the subtrahend is not of type int or LinkedListBinaryNum,
        a TypeError will be raised. if the number is a negative number or bigger than the minuend,
        ValueError will be raised. else, the function will return the subtraction of the numbers.
        """
        # Testing the other object is a LinkedListBinaryNum or a positive whole number
        if not isinstance(other, LinkedListBinaryNum) and not isinstance(other, int) > 0:
            raise TypeError("The object you inserted can not be subtracted")
        if isinstance(other, int) and other < 0:
            raise ValueError("Can't subtract negative number")
        # If subtrahend is of type int we should convert it to LinkedListBinaryNum
        if isinstance(other, int):
            other = LinkedListBinaryNum(other)
        if other > self:
            raise ValueError("The value you inserted as subtrahend is bigger than the minuend and therefore can not be subtracted")
        # String of current binary linked list
        temp = self.head
        cur_bin_str = ""
        while temp is not None:
            cur_bin_str = cur_bin_str + temp.get_byte()
            temp = temp.get_next()
        # String of other object binary linked list
        temp = other.head
        sub_bin_str = ""
        while temp is not None:
            sub_bin_str = sub_bin_str + temp.get_byte()
            temp = temp.get_next()
        # Getting "rid" of all the extra 0 in the beginning of each number
        while cur_bin_str.startswith("0") == True:
            cur_bin_str = cur_bin_str[1:]
        while sub_bin_str.startswith("0") == True:
            sub_bin_str = sub_bin_str[1:]
        # Subtracting of the numbers (as binary strings) with vertical subtraction
        borrow = 0
        sub_result = ""
        while len(cur_bin_str) > 0 or len(sub_bin_str) > 0:
            # Calculating sub of current digits, including borrow from previous iteration
            # While considering different lengths of binary numbers
            if len(cur_bin_str) > 0 and len(sub_bin_str) > 0:
                cur_bin = int(cur_bin_str[len(cur_bin_str)-1:]) - int(sub_bin_str[len(sub_bin_str)-1:]) - borrow
                if cur_bin >= 0:
                    sub_result = str(cur_bin) + sub_result
                    borrow = 0
                else:
                    sub_result = "1" + sub_result
                    borrow = 1
            else:
                sub_result = str(int(cur_bin_str[len(cur_bin_str)-1:]) - borrow) + sub_result
                borrow = 0
            cur_bin_str = cur_bin_str[:len(cur_bin_str) - 1]
            sub_bin_str = sub_bin_str[:len(sub_bin_str) - 1]
        if borrow != 0:
            sub_result = "1" + sub_result
        # Adding or removing 0s from the beginning/end of the string so it matches the valid
        # length for the structure of byte node
        while sub_result.startswith("0") == True:
            sub_result = sub_result[1:]
        while len(sub_result) % 8 != 0:
            sub_result = "0" + sub_result
        # Creating the number itself from the string by adding new msb each time
        result_num = LinkedListBinaryNum()
        while len(sub_result) > 0:
            result_num.add_MSB(sub_result[len(sub_result)-8:])
            sub_result = sub_result[:len(sub_result)-8]
        # Removing the the last excessive node (which is 0)
        temp = result_num.head
        while temp.get_next().get_next() != None:
            temp = temp.get_next()
        temp.set_next(None)
        return result_num

    def __radd__(self, other):
        """
        Takes in another number (as int or LinkedListBinaryNum), and adds it from the right by using
        the add function.
        :param other (int/LinkedListBinaryNum): A number that needs to be added to the current number
        :return (LinkedListBinaryNum/Exception): If the added number is not of type int or LinkedListBinaryNum,
        a TypeError will be raised. if the number is a negative number, ValueError will be raised.
        else, the function will return the addition of the numbers.
        """
        return self + other


class DoublyLinkedNode:
    def __init__(self, data):
        """
        A constructor for DoublyLinkedNode class.
        Attributes: data, next, prev
        """
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        """
        :return: The data of the node.
        """
        return self.data

    def set_next(self, next):
        """
        Takes in another DoublyLinkedNode, and sets it as the next node.
        """
        self.next = next

    def get_next(self):
        """
        :return: The next DoublyLinkedNode of the current node.
        """
        return self.next

    def get_prev(self):
        """
        :return: The previous DoublyLinkedNode of the current node.
        """
        return self.prev

    def set_prev(self, prev):
        """
        Takes in another DoublyLinkedNode, and sets it as the previous node.
        """
        self.prev = prev

    def __repr__(self):
        """
        :return: A string that represents the node by presenting it's data.
        """
        return "=>[" + str(self.data) + "]<="


class DoublyLinkedList:
    def __init__(self):
        """
        A constructor for DoublyLinkedList class.
        Attributes: head, tail, size
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        """
        :return: the length of the DoublyLinkedList object.
        """
        return self.size

    def is_empty(self):
        """
        :return: True/False (A boolean): If the DoublyLinkedList object is empty, returns True.
        if not empty, returns False.
        """
        return True if self.size == 0 else False

    def add_at_start(self, data):
        """
        Takes in data (of any type), and adds it as a node to the beginning of the list
        :param data: An object that can be of any type.
        """
        new_node = DoublyLinkedNode(data)
        # If there are no nodes in the list we need to set the attributes
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size = 1
        # If the list is not empty, we add the node
        else:
            old_node = self.head
            new_node.set_next(old_node)
            old_node.set_prev(new_node)
            self.head = new_node
            # Increase the size of the list by 1
            self.size = self.size + 1

    def remove_from_end(self):
        """
        Removes the tail node from the list and returns it
        :return: Exception/Object: If the list is empty, function raises StopIteration. else,
        the function will return the data in the tail.
        """
        # If the list is empty, exception will be raised
        if self.is_empty():
            raise StopIteration("This Doubly Linked List is empty!")
        data = self.tail.get_data()
        # Edge case: only one node in the list
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return data
        self.tail = self.tail.get_prev()
        self.tail.set_next(None)
        self.size = self.size - 1
        return data

    def get_tail(self):
        """
        :return: The tail of the DoublyLinkedList object.
        """
        return self.tail

    def get_head(self):
        """
        :return: The head of the DoublyLinkedList object.
        """
        return self.head

    def __repr__(self):
        """
        :return: The string representation of DoublyLinkedList object.
        """
        # If list is empty
        if self.is_empty():
            return "Head==><==Tail"
        # If there are nodes in the list
        temp = self.head
        str_of_nodes = ""
        while temp != None:
            str_of_nodes = str_of_nodes + str(temp)
            temp = temp.get_next()
        return "Head=" + str_of_nodes + "=Tail"


class DoublyLinkedListQueue:
    def __init__(self):
        """
        A constructor for DoublyLinkedListQueue class.
        Attributes: data
        """
        self.data = DoublyLinkedList()

    def enqueue(self, val):
        """
        Takes in an object and adds it to the start of the queue.
        """
        self.data.add_at_start(val)

    def dequeue(self):
        """
        Takes out the first object in the queue and returns it.
        """
        return self.data.remove_from_end()

    def __len__(self):
        """
        :return: The length of the queue.
        """
        return len(self.data)

    def is_empty(self):
        """
        :return: True/False (A boolean): If the queue is empty, returns True. if not empty, returns False.
        """
        return self.data.is_empty()

    def __iter__(self):
        """
        :return: An iterator that iterates through the queue.
        """
        self.iterator = copy.deepcopy(self.data)
        return self

    def __next__(self):
        """
        :return (object/Exception): A function that returns the next data in the queue.
        if the queue is empty, raises StopIteration.
        """
        return self.iterator.remove_from_end()

    def __repr__(self):
        """
        :return: The string representation of the queue.
        """
        str_of_queue = ""
        for item in iter(self):
            str_of_queue = str(item) + "," + str_of_queue
        return "Newest=>[" + str_of_queue[:len(str_of_queue)-1] + "]<=Oldest"


from hw8_lib import Stack
from hw8_lib import BinarySearchTree


class NumsManagment:
    def __init__(self, file_name):
        """
        A constructor for NumsManagment.
        Attributes: file_name.
        """
        self.file_name = file_name

    def is_line_pos_int(self, st):
        """
        Takes in a line from the file, returns if the line represents an whole positive number.
        :param st (str): A string. represents a line from the file.
        :return True/False (boolean): If the line is an whole positive number, returns True. otherwise, False.
        """
        st = st.strip("\n")
        return True if st.isdigit() and int(st) > 0 else False

    def read_file_gen(self):
        """
        :return: generator/Exception: if file is found, the function returns a generator that can be used to iterate
        over the positive integers in the file. in each iteration the generator returns the next number in its binary
        form. if file not found, the function will raise an "FileNotFoundError".
        """
        with open(self.file_name, 'r') as f:
            for line in f:
                if self.is_line_pos_int(line):
                    binary_num = LinkedListBinaryNum(int(line.strip("\n")))
                    yield binary_num

    def stack_from_file(self):
        """
        :return stack_of_nums (Stack(LinkedListBinaryNum)): A stack that contains the LinkedListBinaryNum representation of
        the positive whole numbers in the file.
        """
        gen_of_file = self.read_file_gen()
        stack_of_nums = Stack()
        for num in gen_of_file:
            stack_of_nums.push(num)
        return stack_of_nums

    def sort_stack_descending(self, s):
        """
        Takes in a stack that has binary numbers in it, and returns the stack in descending order.
        :param s (Stack(LinkedListBinaryNum)): A stack that contains numbers as linked list binary numbers.
        :return: sorting_stack (Stack(LinkedListBinaryNum)): A stack that contains the values of the input stack
        in descending order.
        """
        sorting_stack = Stack()
        temp_stack = Stack()
        while not s.is_empty():
            # Edge case: first item to be sorted
            if sorting_stack.is_empty():
                sorting_stack.push(s.pop())
            else:
                # If top item in unsorted stack is greater than item in sorted stack
                if s.top() >= sorting_stack.top():
                    sorting_stack.push(s.pop())
                else:
                    # If top item in sorted stack is greater than top item in unsorted stack
                    temp_stack.push(s.pop())
                    while not sorting_stack.is_empty() and temp_stack.top() < sorting_stack.top():
                        s.push(sorting_stack.pop())
                    sorting_stack.push(temp_stack.pop())
        return sorting_stack

    def queue_from_file(self):
        """
        :return queue_of_nums (DoublyLinkedListQueue(LinkedListBinaryNum)): A queue that contains the LinkedListBinaryNum
        representation of the positive whole numbers in the file.
        """
        gen_of_file = self.read_file_gen()
        queue_of_nums = DoublyLinkedListQueue()
        for num in gen_of_file:
            queue_of_nums.enqueue(num)
        return queue_of_nums

    def set_of_bytes(self, q_of_nums):
        """
        Takes in a queue of objects of type LinkedListBinaryNum, returns a set of all the ByteNodes.
        :param q_of_nums (DoublyLinkedListQueue(LinkedListBinaryNum)): A queue that contains objects of LinkedListBinaryNum.
        :return: s (set): A set of all the ByteNodes in the queue.
        """
        s = set()
        temp_queue = copy.deepcopy(q_of_nums)
        while not temp_queue.is_empty():
            new_queue = copy.deepcopy(temp_queue)
            for i in range(len(temp_queue.dequeue())):
                another_queue = copy.deepcopy(new_queue)
                s.add(another_queue.dequeue()[i])
        return s

    def nums_bst(self):
        """
        :return tree(BinarySearchTree(int, LinkedListBinaryNum)): An object of type BinarySearchTree that contains all
        the positive whole number in the file. the keys of the tree are the numbers in their decimal form (int objects),
        and the values are the numbers in their binary form (LinkedListBinaryNum objects).
        """
        gen_of_file = self.read_file_gen()
        tree = BinarySearchTree()
        for num in gen_of_file:
            # Creating a string that represents the current binary
            cur_bin_str = str(num).replace("|", "")
            # Converting to integer
            cur_bin = 0
            for i in range(len(cur_bin_str)):
                cur_bin = cur_bin * 2 + int(cur_bin_str[i])
            # Adding to the tree
            tree.insert(cur_bin, num)
        return tree

    def bst_closest_gen(self, bst):
        """
        Takes in a tree, and returns a generator that returns nodes of all the values between the minimal distance nodes
        of the tree.
        :param bst (BinarySearchTree(int, LinkedListBinaryNum)): A tree that contains nodes with int keys and
        LinkedListBinaryNum values.
        :return: The function calculates the minimum distance between two nodes in the tree and returns all the possible
        nodes whose values are between the two nodes whose distance is minimal.
        """
        # Iterating the tree and inserting all the values into a queue
        bst_iter = iter(bst)
        tree_queue = DoublyLinkedListQueue()
        for tree_node in bst_iter:
            tree_queue.enqueue(tree_node)
        # Finding the minimum distance and saving it and the relevant nodes
        first_min_node = tree_queue.dequeue()
        second_min_node = tree_queue.dequeue()
        # Values of minimal distance start node and the distance
        min_fir_node = first_min_node[0]
        cur_min_dist = second_min_node[0] - first_min_node[0]
        while not tree_queue.is_empty():
            next_min_node = tree_queue.dequeue()
            new_min_dist = next_min_node[0] - second_min_node[0]
            if new_min_dist < cur_min_dist:
                cur_min_dist = new_min_dist
                min_fir_node = second_min_node[0]
            second_min_node = next_min_node
        # Creating a tree in the range
        new_bst_tree = BinarySearchTree()
        for i in range(cur_min_dist+1):
            new_binary_node = LinkedListBinaryNum(min_fir_node + i)
            new_bst_tree.insert(min_fir_node + i, new_binary_node)
        # Returning a generator for the new tree
        new_iter = iter(new_bst_tree)
        for i in range(cur_min_dist+1):
            yield next(new_iter)
