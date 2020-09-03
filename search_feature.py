def read_magazine_names(filename):
    """
    This function takes in the file and extract its content to a list
    :param filename: file
    :return: list
    """
    magazine_names = []
    with open(filename) as magazine_file:
        for magazine in magazine_file:
            magazine_names.append(magazine.strip())
        return magazine_names


def search_function(magazine_list, user_input):
    """
    This function takes in the list of magazines and the user search criteria and returns a sorted list
    :param magazine_list: list
    :param user_input: string
    :return: list
    """
    filtered_list = []
    magazines = sorted(magazine_list)

    for magazine in magazines:
        if magazine.lower()[0:len(user_input)].startswith(user_input.lower()) and len(filtered_list)<3:
            filtered_list.append(magazine)

    return filtered_list


def main():
    """
    This is the entry point of the Application and where user interaction occurs
    :return: string(s)
    """
    magazines = read_magazine_names('liste_magazine.txt')
    search_input = input('Hello Esteemed Customer, \nKindly enter your search criteria: ')
    result = search_function(magazines, search_input)
    for item in result:
        print(item)


if __name__ == '__main__':
    main()





