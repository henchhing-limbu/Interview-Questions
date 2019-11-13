class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = Node()
    
    def insert(self, data):
        new_node = Node(data)
        cur = self.head
        while (cur.next != None):
            cur = cur.next
        cur.next = new_node

    def size(self):
        if (self.head == None):
            return 0
        temp = self.head
        count = 0
        while (temp.next != None):
            count += 1
            temp = temp.next
        return count

def remDup(linkedList):
    print("Entered the method")
    seen = set()
    ptr = linkedList.head
    # print(ptr.next.data)
    while (ptr.next != None):
        curr = ptr.next
        seen.add(curr.data)
        print(seen)
        while (curr != None and curr.data in seen):
            curr = curr.next
        ptr.next = curr
    print(linkedList.size())
    return linkedList

linked_list = LinkedList()
# print(linked_list.size())
linked_list.insert(5)
# print(linked_list.size())
linked_list.insert(2)
linked_list.insert(6)
linked_list.insert(2)
linked_list.insert(3)
# print(linked_list.size())
# print(linked_list.head.next.data)
new_linked_list = remDup(linked_list)
print(new_linked_list.size()) 
