# Karolina Szafran-Belzowska, 2019-03-19
# secondstring.py / This program will print every second word
# this page helped me to solve the problem https://stackoverflow.com/questions/22767509/python-get-the-x-first-words-in-a-string/22767557


words = "The quick brown fox jumps over the lazy dog."


splitted = words.split()

first = splitted[1]
second = splitted[3]
third = splitted[5]
fourth = splitted[7]

print(first,second,third,fourth)
