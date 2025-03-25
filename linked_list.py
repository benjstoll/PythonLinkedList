class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, root: Node):
        self.root = root


    # Add to the beginning of the list
    def linked_list_prepend(self, data) -> None:
        current = self.root
        new_root = Node(data)

        self.root = new_root
        self.root.next = current


    # add to the end of the list
    def linked_list_append(self, data) -> None:
        current = self.root

        while current.next != None:
            current = current.next

        current.next = Node(data)


    # return a string of all elements in order
    def traverse_list(self) -> str:
        traversal_string = ''
        current = self.root

        while current != None:
            if current.next == None:
                traversal_string += f'{str(current.data)}'
            else:
                traversal_string += f'{str(current.data)} -> '

            current = current.next

        return traversal_string


    # Reverse the order of the list
    def reverse_list(self) -> None:
        current = self.root
        previous = None
        next = current.next

        while current != None:
            current.next = previous

            if next == None:
                self.root = current
                break

            previous = current
            current = next
            next = current.next


    # remove element from specified index
    def remove_element(self, index: int) -> None:
        current = self.root
        current_index = 0

        if index == 0:
            self.root = self.root.next
            return

        while current != None:
            if current_index + 1 == index and current.next and current.next.next:
                current.next = current.next.next
                break
            elif current_index + 1 == index and current.next and not current.next.next:
                current.next = None
                break

            current = current.next
            current_index += 1

            if current == None:
                print(f'Could not find element at index {index}.')


if __name__ == '__main__':
    my_list = LinkedList(Node(1))

    my_list.linked_list_append(2)
    my_list.linked_list_append(3)
    my_list.linked_list_append(4)
    my_list.linked_list_append(5)
    my_list.linked_list_append(6)

    my_list.linked_list_prepend(7)
    my_list.linked_list_prepend(8)
    my_list.linked_list_prepend(9)
    my_list.linked_list_prepend(10)
    my_list.linked_list_prepend(11)

    print(my_list.traverse_list())

    my_list.remove_element(2)
    my_list.remove_element(13)

    print(my_list.traverse_list())

    my_list.reverse_list()

    print(my_list.traverse_list())
            