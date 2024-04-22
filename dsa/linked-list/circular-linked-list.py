class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(1)
node2 = Node(5)
node3 = Node(10)
node4 = Node(99)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1


start_node = node1
current_node = node1
print(current_node.data, end=" -> ")
current_node = current_node.next

while current_node != start_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next

print('...')