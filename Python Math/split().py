# Splite at each white-space character

import re 

txt = "the rain in spain"
x = re.split("\s",txt)
print(x)