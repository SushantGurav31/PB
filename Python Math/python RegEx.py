# Search the string to see if starts with "The" and end with "Spain"

import re 

txt = "the rain in spain"
x = re.search("^the.*spain$",txt)
if x:
    print("yes! we have a match!")

else:
    print("no match")