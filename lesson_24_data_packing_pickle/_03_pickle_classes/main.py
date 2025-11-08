from _03_pickle_classes import Pickler, UnPickler
from lesson_24_data_packing_pickle._02_pickle_advance._02_pickle_difficult import DoubleLinkedList

if __name__ == '__main__':
    pickler_5 = Pickler(protocol=5)
    pickler_default = Pickler()

    my_ll = DoubleLinkedList()
    my_ll.insert_at_head("Барсик_1")
    my_ll.insert_at_head("Снежок_0")
    my_ll.insert_at_tail("Персик_2")

    my_ll = pickler_5.pickle_data(my_ll)
    print(my_ll)
    my_ll = UnPickler.unpickle_data(my_ll)
    my_ll.print_ll_from_head()
    print()

    pickler_default.pickle_data_to_file('ll_pickle.cats', my_ll)
    my_ll_ff = UnPickler.unpickle_file('ll_pickle.cats')
    my_ll_ff.print_ll_from_tail()


