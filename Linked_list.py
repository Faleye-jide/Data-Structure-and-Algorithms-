class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self, head):
        self.head = None


    # implementing some functions
    # prepending to a list
    # appending to a list

    def prepend(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node


        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            return None

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
#
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.append(data_list)




    def remove(self, index):
        if index < 0:
            return
        if index >= self.get_length():
            return
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        cur_node = self.head
        while cur_node:
            if count == index - 1:
                cur_node.next = cur_node.next.next
                break

            cur_node = cur_node.next
            count += 1



llist = linked_list()
llist.insert_values(["jide","alex","ayo"])
print("length:", llist.get_length())
llist.append("A")
llist.prepend("B")
llist.prepend("C")
llist.print_list()

