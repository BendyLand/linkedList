from ..node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)
    
    def get_head_node(self):
        return self.head_node 
    
    def insert_beginning(self, value):
        new_node = Node(value)
        new_node.set_next_node(self.get_head_node())
        self.head_node = new_node

    def stringify_list(self):
        string = ""
        current = self.get_head_node()
        while current:
            if current.get_value() is not None:
                string += str(current.get_value()) + "; "
            current = current.get_next_node()
        return string

    @staticmethod
    def swap_nodes(input_list, val1, val2):
        print(f"Swapping {val1} with {val2}")

        node1_prev = None
        node2_prev = None
        node1 = input_list.head_node
        node2 = input_list.head_node

        if val1 == val2:
            print("Elements are the same. No swap necessary.")
            return
        
        while node1 is not None:
            if node1.get_value() == val1:
                break
            node1_prev = node1
            node1 = node1.get_next_node()
        while node2 is not None:
            if node2.get_value() == val2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()

        if node1 is None or node2 is None:
            print("Swap not possible - one or more elements not in list")
            return
        
        if node1_prev is None:
            input_list.head_node = node2
        else:
            node1_prev.set_next_node(node2)

        if node2_prev is None:
            input_list.head_node = node1
        else:
            node2_prev.set_next_node(node1)
            
        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)


