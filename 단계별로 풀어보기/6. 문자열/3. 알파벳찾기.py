import string

word = str(input())
for i in string.ascii_lowercase:
    print(word.find("{0}".format(i)))