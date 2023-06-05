#  A lambda function that takes two arguments, x and y, and returns their sum

x, y = map(int, input().split())
print((lambda x, y: x + y)(x, y))

# A lambda function that takes a list as input and returns a new list with each element squared.

from random import randint

n = int(input("lists size: "))

list_num = [randint(0, 10) for i in range(n)]

print(list_num)
print((lambda list_num: [i * i for i in list_num])(list_num))

# A lambda function that takes a list of strings as input and returns a new list with the length of each string.

from random import randint

n = int(input("lists size: "))

list_num = [input("Input string: ") for i in range(n)]

print(list_num)
print((lambda list_num: [len(i) for i in list_num])(list_num))

# A lambda function that takes a list of numbers as input and returns their average.

from random import randint

n = int(input("lists size: "))

list_num = [randint(0, 100) for i in range(n)]

print(list_num)
print((lambda list_num: sum(list_num) / len(list_num))(list_num))

# A lambda function that takes a string as input and returns its reverse.

n = input(("Input string: "))
print(n)
print((lambda string: string[::-1])(n))

# A lambda function that takes a list of strings as input and returns a new list with each string capitalized.

from random import randint

n = int(input("lists size: "))

list_num = [input("Input string: ") for i in range(n)]

print(list_num)
print((lambda list_num: [i[0].upper() + i[1:] for i in list_num])(list_num))

# A lambda function that takes a list of numbers as input and returns a new list with only the even numbers.

from random import randint

n = int(input("lists size: "))

list_num = [randint(0, 100) for i in range(n)]

print(list_num)
print((lambda list_num: [i for i in list_num if i % 2 == 0])(list_num))

#  A lambda function that takes a dictionary as input and returns a list of its keys.

from random import randint

n = int(input("lists size: "))

dict = {}

for i in range(n):
    dict[i] = input("Input dict value for {0} key: ".format(i))

print(dict)
print((lambda dict: dict.keys())(dict))

# A lambda function that takes a list of strings as input and returns a new list with only the strings containing vowels (a, e, i, o, u).

-

