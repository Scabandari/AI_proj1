
def list_to_string(list_):
    list_as_string = ""
    list_as_string += "["
    for i in list_:
        list_as_string += str(i)
        list_as_string += ", "
    list_as_string = list_as_string[:-2]
    list_as_string += "]"
    return list_as_string


def output_text_file(tuples, file_name):
    """This takes a list of tuples ('a', Node) like so
        and outputs the results into a .txt file """
    file_name = file_name + ".txt"
    with open(file_name, 'w') as txt_file:
        for tuple_ in tuples:
            txt_file.write(str(tuple_[0]) + " " + list_to_string(tuple_[1].board.state) + "\n")




