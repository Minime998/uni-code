"""
-------------------------------------------------------
[description of functions]
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
__updated__ = "2020-11-26"
-------------------------------------------------------
"""
# [import statements]

# [constants]


def customer_by_id(fh, id_number):
    """
    -------------------------------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fh, id_number)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    result = []
    line = fh.readline()

    while line != "" and result == []:
        line = line.strip().split(",")
        check = line[0]
        if id_number == check:
            result = line
        line = fh.readline()
    return result


def customer_append(fh, fields):
    """
    -------------------------------------------------------
    Appends a customer record to a comma-delimited sequential file.
    Use: customer_append(fh, fields)
    -------------------------------------------------------
    Parameters:
        fh - file to add to (file handle - already open for appending)
        fields - a list of the field data to append to the file (list)
    Returns:
       None
    -------------------------------------------------------
    """
    strfields = ','.join(fields)
    fh.write(strfields)
    fh.write("\n")

    return


def number_stats(fh):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """
    line = fh.readline()
    total = 0
    count = 0
    smallest = int(line[0])
    largest = int(line[0])
    while line != "":
        data = int(line.strip())
        count += 1
        total += data
        if smallest > data:
            smallest = data
        if largest < data:
            largest = data
        line = fh.readline()

    average = total/count

    return smallest, largest, total, average


def find_longest(fh):
    """
    -------------------------------------------------------
    Finds the last word with longest length in fh.
    Assumes file is not empty.
    Use: word = find_longest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the last word with the longest length in fh (str)
    ------------------------------------------------------
    """
    line = fh.readline()
    longest = 0
    while line != "":
        line = line.strip()
        if longest <= len(line):
            longest = len(line)
            word = line
        line = fh.readline()

    return word


def file_copy(fh_1, fh_2):
    """
    -------------------------------------------------------
    Copies the contents of fh_1 to fh_2.
    Any contents of fh_2 are overwritten.
    Use: file_copy(fh_1, fh_2)
    -------------------------------------------------------
    Parameters:
        fh_1 - source file (file handle - already open for reading)
        fh_2 - target file (file handle - already open for writing)
    Returns:
        None
    ------------------------------------------------------
    """
    for line in fh_1:
        fh_2.write(line)

    return
