import pickle


class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head.prev_node = new_node
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            # return self.insert_at_head(data)
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.prev_node = self.tail
        self.tail = new_node

    def print_ll_from_head(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        print(f'Список выведен с головы')

    def print_ll_from_tail(self):
        current_node = self.tail
        while current_node:
            print(current_node.data)
            current_node = current_node.prev_node
        print(f'Список выведен с хвоста')


if __name__ == '__main__':
    my_ll = DoubleLinkedList()
    my_ll.insert_at_head("Барсик_1")
    my_ll.insert_at_head("Снежок_0")
    my_ll.insert_at_tail("Персик_2")
    print(my_ll)

    my_ll = pickle.dumps(my_ll)
    print(my_ll)
    my_ll = pickle.loads(my_ll)
    print(my_ll)
    my_ll.print_ll_from_head()
    print()

    with open('pickled_data.cats', 'wb') as file:
        pickle.dump(my_ll, file)

    try:
        with open('pickled_data.cats', 'rb') as file:
            my_ll_from_file = pickle.load(file)
    except FileNotFoundError:
        print('Файл не найден!')

    print(my_ll_from_file)
    my_ll_from_file.print_ll_from_tail()
