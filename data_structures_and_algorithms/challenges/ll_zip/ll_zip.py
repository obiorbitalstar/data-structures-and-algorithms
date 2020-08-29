from data_structures_and_algorithms.data_structures.linked_list.linked_list import LinkedList

def zip_lists(list1, llist2):
        first_list = list1.head
        second_list = llist2.head
        jumping_pointer = None

        if not first_list:
            return second_list
        if not second_list:
            return first_list

        if first_list and second_list:

            jumping_pointer = first_list
            first_list = jumping_pointer.next

            new_head = jumping_pointer
        while first_list and second_list:
            jumping_pointer.next = second_list
            jumping_pointer = second_list
            second_list = jumping_pointer.next
            jumping_pointer.next = first_list
            jumping_pointer = first_list
            first_list = jumping_pointer.next

        if not first_list:
            jumping_pointer.next = second_list
        if not second_list:
            jumping_pointer.next = first_list
        return new_head
