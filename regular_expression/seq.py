import re
text = "my name is swati, my age is 26, 800002, Patna"
result = re.findall("Patna\\Z",text)
print(result)