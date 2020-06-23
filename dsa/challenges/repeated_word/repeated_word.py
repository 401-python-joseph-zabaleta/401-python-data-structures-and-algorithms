import re

def repeated_word(book):
    """ Takes in a long string (book) and returns the first repeated word to occur.
    """
    # Ouput variable
    output = ''

    # regex to substitute special characters with a space
    regex = '[^A-Za-z0-9]+'
    book = re.sub(regex, ' ', book)

    # split the book into a list of lower case words
    words = [word.lower() for word in book.split()]

    # Create a dictionary with keys from words list with default value of 0
    my_dict = dict.fromkeys(words, 0)

    # Loop through word list, and increased the value to each key based on word.
    for word in words:

        if my_dict[word]:
            my_dict[word] += 1
            if my_dict[word] == 2:
                output = word
                break
        else:
            my_dict[word] = 1

    # Finally return the word that occurs the most
    return output

def word_most_often(book):
    """ Takes in a long string (book) and will return the word that occurs the most often.
    """

    # what the maximum number count, and word
    maximum = [1, None]

    # regex to substitute special characters with a space
    regex = '[^A-Za-z0-9]+'
    book = re.sub(regex, ' ', book)

    # split the book into a list of words
    words = book.split()

    # Create a dictionary with keys from words list with default value of 0
    my_dict = dict.fromkeys(words, 0)

    # Loop through word list, and increased the value to each key based on word.
    # Also checks that word's value in dictionary compared to maximum value, if value is greater, change maximum
    for word in words:

        if my_dict[word]:
            my_dict[word] += 1
            if my_dict[word] > maximum[0]:
                maximum = [my_dict[word], word]
        else:
            my_dict[word] = 1

    # Finally return the word that occurs the most
    return maximum[1]
