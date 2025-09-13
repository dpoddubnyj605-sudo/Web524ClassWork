def get_data_dict_from_file(filename, divider):
    managers_dict = {}
    with open(filename, encoding='utf-8') as managers_data:
        for manager_data in managers_data:
            clean_data = manager_data.strip().split(divider)
            # manager = clean_data[0]
            # company = clean_data[1]
            # head_company = clean_data[2]
            manager, company, head_company = clean_data
            managers_dict[(company, head_company)] = manager
    return managers_dict


if __name__ == '__main__':
    managers_data_dict = get_data_dict_from_file(r'data_files\managers_data_own_format.txt', ':')
    print(managers_data_dict)
    for companies_, manager_ in managers_data_dict.items():
        print(f'{manager_} работает в компании {companies_[0]} которая принадлежит {companies_[1]}')
