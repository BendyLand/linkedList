require './linked_list.rb'

ll = LinkedList.new(1)
ll.insert_beginning(2)
ll.insert_beginning(3)
ll.insert_beginning(4)
ll.insert_beginning(5)

puts ll.stringify_list

LinkedList.swap_nodes(ll, 2, 5)

puts ll.stringify_list