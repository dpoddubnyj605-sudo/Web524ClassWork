class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:

    def __init__(self):
        self.head = None
        self.ll_list_data = []

    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node

    def print_users_data_ll(self):
        ll_string = ''
        current_node = self.head
        if not current_node:
            print(None)
        while current_node:
            ll_string += f' {str(current_node.data)} ->'
            current_node = current_node.next_node

        ll_string += ' None'
        print(ll_string)

    def data_to_list(self):
        current_node = self.head
        while current_node.next_node:
            self.ll_list_data.append(current_node.data)
            current_node = current_node.next_node
        self.ll_list_data.append(current_node.data)
        return self.ll_list_data

    def get_data_by_id(self, user_id):
        current_node = self.head
        while current_node:
            try:
                if user_id == current_node.data['id']:
                    return current_node.data
            except TypeError:
                print("Данные не являются словарем или в словаре нет 'id'!")
            current_node = current_node.next_node
        return None


if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.insert_at_head({'id': 2, 'username': 'lazzy12345'})
    ll1.insert_at_tail({'id': 3, 'username': 'mik_roz'})
    ll1.insert_at_tail({'id': 4, 'username': 'mosh_s'})
    ll1.insert_at_head({'id': 1, 'username': 'serebro'})

    lst = ll1.data_to_list()
    print(lst)

    print(ll1.get_data_by_id(2))
    ll1.insert_at_tail({'iddqd'})
    ll1.print_users_data_ll()
