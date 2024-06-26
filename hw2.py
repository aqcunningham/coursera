def read_file(file_name):
    """ Reads in a file.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    ### WRITE SOLUTION HERE
    f = open(file_name, 'r')
    sampleText = f.read()
    print(sampleText)
    return sampleText
    raise NotImplementedError()

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    ### WRITE SOLUTION HERE
    # f_name = input(file_name)
    f = open(file_name)
    f_content = f.read()
    nn = f_content.split(" ")
    # print(nn)
    return nn
    raise NotImplementedError()

def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.
    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename
        We determine the first line to be everything in a string before the
        first newline ('\n') character.
    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ### WRITE SOLUTION HERE
    f = open(file_contents)
    ff = f.readline()  # first line of file_contents # a little one string
   
    with open(output_filename, 'w') as file:
        file.writelines(ff)
    print(ff)
    return ff
    # f = open('file_contents')
    # f_content = f.read() # first line from file_contents

    # # output = open(output_filename, 'r')
    # # out_content = output.readline() # saves the first line

    # with open(output_filename, 'w') as file:
    #     file.writelines(f_content)

    # f = open(output_filename, 'r')
    # out = f.readline()
    # return open(out)
    raise NotImplementedError()


def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    ### WRITE SOLUTION HERE
    list = []
    f = open(file_name)
    f_content = f.read()
    
    oneline = f_content.split("\n")
    # print('line:',oneline)
    for i, item in enumerate(oneline):
        if(i%2 == 0):
            list.append(item)
    # print(list)
    return list
    # nn = f_content.split("\n") # turns into a list
    # for x in nn.length:        
    # print(f_content)
    # print(len(nn))
    raise NotImplementedError()

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    ### WRITE SOLUTION HERE
    list = []
    f = open(file_name)
    f_content = f.read()

    oneline = f_content.split("\n")
    # length = len(oneline)
    for length in reversed(oneline):
        list.append(length)
        # print(length)
        # length-1
           
    # print(list)
    return list
    raise NotImplementedError()

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file("someContent.txt", "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()