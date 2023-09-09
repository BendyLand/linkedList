from linked_list import *  

print("Python Program:")

list = LinkedList("Ben")
# Prints Ben
print(list.get_head_node().get_value())

list.insert_beginning("Olivia")
# Prints Olivia
print(list.get_head_node().get_value())

# Prints Olivia; Ben;
print(list.stringify_list())

li = LinkedList()
for i in range(10):
    li.insert_beginning(i)
print(li.stringify_list())
LinkedList.swap_nodes(li, 9, 5)
print(li.stringify_list())

