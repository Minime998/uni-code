'''
cipher

Author: Noah Fedosoff
ID: 200420350
Email: fedo0350@mylaurier.ca
__updated__ = "2021-01-21"

'''
from functions import substitute
ciphertext = "DAVIBROWNZCEFGHJKLMPQSTUXY"
string = """It appears that Ontario's Point Pelee National Park has lost its point. The southernmost 
tip of Canada is in the park, near the town of Leamington. There have always been several 
hundred metres of sand jutting out from the mainland. But park officials say recent high 
winds have washed away the sand point and all that remains is a platform. The park advertises 
itself as the southernmost tip of Canada's mainland, at the same latitude as northern 
California, and attracts more than 400,000 visitors per year. A park official says a no 
swimming sign that used to mark the southernmost point washed up on a beach in Madison, Ohio, 
about 100 kilometres across Lake Erie. Officials say the sand patterns at the point change 
frequently, but this is the first time the point has disappeared completely."""

estring = substitute(string, ciphertext)
print(estring)
