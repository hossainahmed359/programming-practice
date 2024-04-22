class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(1)
node2 = Node(5)
node3 = Node(10)
node4 = Node(99)

node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3

# =============== FORWARD ===============
print("\nTraversing forward:")

current_node = node1
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next

print('null')


# =============== BACKWARD ===============
print("\nTraversing backward:")
current_node = node4

while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.prev

print('null')