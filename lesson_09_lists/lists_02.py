example_list_str = ["Drama", "Comedy", "Fantasy"]
example_list_int = [1, 2, 3]
example_list_float = [2.5, 3.5, 4.5]
example_list_list = [["Drama", "Comedy", "Fantasy"], [1, 2, 3]]
example_list_dict = [{"key_1": "value_1"}, {1: 1050}]


class ExampleClass:
    pass


ex_obj = ExampleClass()

example_list_mix = ["Drama", 2.5, 1, ["Drama", "Comedy", "Fantasy"], {"key_1": "value_1"}, ex_obj]


example_list_str_01 = ["Drama", "Comedy", "Fantasy", "Drama", "Comedy", "Fantasy"]
print(example_list_str_01)
example_list_set = list(set(example_list_str_01))
print(example_list_set)
