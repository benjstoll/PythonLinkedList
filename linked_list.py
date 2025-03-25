class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, root: Node):
        self.root = root


    def linked_list_append(self, data) -> None:
        current = self.root

        while current.next != None:
            current = current.next

        current.next = Node(data)


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


    def reverse_list(self):
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


if __name__ == '__main__':
    my_list = LinkedList(Node(1))

    my_list.linked_list_append(2)
    my_list.linked_list_append(3)
    my_list.linked_list_append(4)
    my_list.linked_list_append(5)
    my_list.linked_list_append(6)

    print(my_list.traverse_list())

    my_list.reverse_list()

    print(my_list.traverse_list())
            