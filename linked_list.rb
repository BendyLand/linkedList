require './node.rb'

class LinkedList
    attr_accessor :head_node
    def initialize(value = nil)
        @head_node = Node.new(value)
    end

    def insert_beginning(value)
        new_node = Node.new(value)
        new_node.next_node = @head_node
        @head_node = new_node
    end

    def stringify_list
        string = ""
        current = @head_node
        until current.nil? 
            if current.value != nil
                string += (current.value).to_s + "; "
            end
            current = current.next_node
        end
        return string
    end

    def self.swap_nodes(input_list, val1, val2)
        puts "Swapping #{val1} with #{val2}"

        node1_prev = nil
        node2_prev = nil
        node1 = input_list.head_node
        node2 = input_list.head_node

        if val1 == val2
            puts "Elements are the same. No swap required"
            return
        end

        until node1.nil? || node1.value == val1 
            node1_prev = node1
            node1 = node1.next_node
        end

        until node2.nil? || node2.value == val2
            node2_prev = node2
            node2 = node2.next_node
        end

        if node1.nil? or node2.nil?
            puts "Swap not possible - one or more elements not in list"
            return
        end

        if node1_prev.nil?
            input_list.head_node = node2
        else
            node1_prev.next_node = node2
        end

        if node2_prev.nil?
            input_list.head_node = node1
        else
            node2_prev.next_node = node1
        end

        node1.next_node, node2.next_node = node2.next_node, node1.next_node
    end
end


