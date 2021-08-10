def strip(string,word):
    newstr=string.replace(word,"vaishnavi")
    return newstr.strip()

str1="mona Gupta In BSC Final year "
c = strip(str1,"mona")
print(c) 