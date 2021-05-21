'''
Marks check to see if they pass
Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2020-10-02"

'''
mid_mark = float(input("Midterm mark (%): "))
final_mark = float(input("Final exam mark (%): "))

exam_portion = ((0.2*(mid_mark/100))+(0.4*(final_mark/100)))/(0.2+0.4)

print("""Your weighted exam average is: {:.1%}. The passing mark of the weighted exam 
average is 50%""".format(exam_portion))