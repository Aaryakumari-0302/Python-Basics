# import re
# text = "Python is a simple language"
# result = re.findall("^ Python",text)
# print(result)

# import re
# text = "Python is a simple language"
# result = re.findall("language$",text)
# print(result)

import re
text = "ac abc abbc abbbd"
#result = re.findall("ab+c",text)
result = re.findall("ab*c",text)
print(result)

# import re
# text = "a aa aaa aaaa"
# result = re.findall("a{2,4}",text)
# print(result)

# import re
# text = "Python is a simple language"
# #result = re.findall("[aeiou]",text)
# result = re.findall("Python | Java",text)
# print(result)

# import re
# text = "cat cant carrort correct concept"
# result = re.findall("c.....t",text)
# print(result)