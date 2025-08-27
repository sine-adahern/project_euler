"""
define two lists 
enter the key
remove key from list_1
append key to start of list
enter word
find the index of each letter
print

"""

list_1 = [ "A", "B", "C", "D", "E", "F", "G", "H", "I","J","K", "L", "M", "N", "O","P","Q","R", "S","T","U","V","W", "X", "Y", "Z"]

alphabet = [ "A", "B", "C", "D", "E", "F", "G", "H", "I","J","K", "L", "M", "N", "O","P","Q","R", "S","T","U","V","W", "X", "Y", "Z"]


user_in = input("enter key:")
user_in = user_in.upper()

for i in user_in:
    if i in list_1:
        list_1.remove(i)




list_2 = []
for i in user_in:
    list_2.append(i)

list_1 = list_2 + list_1
print(list_1)

word = input("enter uncoded pass:")
word = word.upper()

password_num = ""
password_lt = ""

for i in word:
    if i in list_1:
        pos = list_1.index(i) +1 
        pos_lt = str(pos)
        password_num = password_num+pos_lt
        password_lt = password_lt + alphabet[pos]

        password_num = password_num+ " "



print(password_num)
print(password_lt)
