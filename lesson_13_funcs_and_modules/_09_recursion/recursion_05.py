def max_depth(structure: list) -> int:
    if not isinstance(structure, list):
        return 0
    if not structure:
        return 1
    return 1 + max(max_depth(item) for item in structure)


if __name__ == '__main__':
    simple_structure = [1, 5]
    structure = ['path_01', ['path_02', ['path_03', ['path_04']]], 'path_05']
    print(max_depth(simple_structure))
    print(max_depth(structure))
