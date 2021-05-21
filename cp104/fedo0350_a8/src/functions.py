"""
-------------------------------------------------------
[description of functions]
-------------------------------------------------------
Author:  Noah Fedosoff
ID:      200420350
Email:   fedo0350@mylaurier.ca
__updated__ = "2020-11-28"
-------------------------------------------------------
"""
#[import statements]

#[constants]

def total_nums(fh):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in s.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """
    total = 0
    numlist = []
    line = fh.readline()
    linelist = line.strip().split(" ")
    for x in linelist:
        if x.isdigit():
            numlist.append(x)
            total += int(x)
    return numlist, total

def locate_median(fh):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in s.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """
    line = fh.readline()
    numlist = []
    
    while line != "":
        linelist = line.strip().split(" ")
        for x in range(len(linelist)):
            numlist.append(int(linelist[x]))
        line = fh.readline()
    
    numlist.sort()
    first_middle = int(len(numlist)/2)-1
    second_middle = int(len(numlist)/2)
    middle = int(len(numlist)/2)
    if len(numlist)%2 == 0:
        median = (numlist[first_middle]+numlist[second_middle])/2
    else:
        median = numlist[middle]
             
    return median

def file_analysis(fh):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in s.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """
    line = fh.readline()
    whitecount = 0
    digitcount = 0
    uppercount = 0
    lowercount = 0
    while line != "":
        whitecount += line.count(" ") + line.count("\n")
        linelist = line.strip().split(" ")
        for words in linelist:
            for char in words:  # are ya winning son?
                if char.isdigit():
                    digitcount += 1
                elif char.islower():
                    lowercount += 1
                elif char.isupper():
                    uppercount += 1
                
        line = fh.readline()
    
    return uppercount, lowercount, digitcount, whitecount
    
def is_valid(linestring):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in s.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """ 
    valid = True
    if "/" not in linestring:
        valid = False
        if "-" not in linestring:
            valid = False
    
    return valid

def valid_sn_file(fh,oh1,oh2):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in s.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """ 
    line = fh.readline()
    while line != "":
        valid = is_valid(line.strip())
        if valid == True:
            oh1.write(line)
        else:
            oh2.write(line)
        line = fh.readline()
    return


          
     
        
    
        
        
    
    
    

