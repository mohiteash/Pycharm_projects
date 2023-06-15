'''1.Check if the user input number is even or odd'''
# number=int(input('Enter a number'))
# if number%2==0:
#     print(f'{number} is even')
# else:
#     print(f'{number} is odd')

'''2.Convert uppercase to lowercase and viceversa'''
# user_input=input('Enter a character:')
# if user_input.isalpha():
#     if 'a'<= user_input <='z':
#         print(chr(ord(user_input)-32))
#     else:
#         print(chr(ord(user_input)+32))
# else:
#     print('enter valid input')

# user_input=input('Enter a character:')
# if user_input.isalpha():
#     if user_input.islower():
#         print(user_input.upper())
#     else:
#         print(user_input.lower())
# else:
#     print('enter valid input')

'''3.Palindrome'''
# string1=input('enter a string:')
# if string1==string1[::-1]:
#     print(f'{string1} is palindrome')
# else:
#     print(f'{string1} is not palindrome')

'''4.check whether the input is number or alphabet or special character'''
# character=input('Enter a character:')
# if character.isalpha():
#     print(f'{character} is a alphabet')
# elif character.isdigit():
#     print(f'{character} is number')
# else:
#     print(f'{character} is special charater')

# character=input('Enter a character:')
# if 'a'<= character <='z' or 'A'<=character<='Z':
#     print(f'{character} is an alphabet')
# elif '0'<= character <='9':
#     print(f'{character} is a number')
# else:
#     print(f'{character} is special character')

'''5.WAP to check if the string is starting with vowel or not'''
# string= input('Enter a string:')
# if string.isalpha():
#     if string[0] in 'aeiouAEIOU':
#         print(f'{string} is starting with vowel')
#     else:
#         print(f'{string} is not starting with vowel')
# else:
#     print('please enter valid string')

'''6.WAP to check if the string is ending with vowel or not'''
# string= input('Enter a string:')
# if string.isalpha():
#     if string[-1] in 'aeiouAEIOU':
#         print(f'{string} is ending with vowel')
#     else:
#         print(f'{string} is not ending with vowel')
# else:
#     print('please enter valid string')

'''7.WAP to check if the string is even length or odd length'''
# string=input('Enter a string:')
# if len(string)%2==0:
#     print(f'{string} is even length')
# else:
#     print(f'{string} is odd length')

'''8.WAP to check if the ASCII value of the userinput char is even or odd'''
# character = input('Enter a character:')
# if ord(character) %2 ==0:
#     print(f'ASCII value of {character} is even')
# else:
#     print(f'ASCII value of {character} is even')

'''9.result'''
# number=int(input('Enter a number:'))
# if 0< number <=100:
#     if 0< number <35:
#         print('fail')
#     elif 35<= number <55:
#         print('pass')
#     elif 55<= number <70:
#         print('second class')
#     elif 70<= number <85:
#         print('first class')
#     else:
#         print('distinction')
# else:
#     print('enter number between 1 to 100')

'''10.Create a dict with user input char as a key and its ASCII value as a value'''
# # d1={}
# user=input('enter a character:')
# # d1.setdefault(user,ord(user))
# # print(d1)
# #
# d2=dict.fromkeys(user,ord(user))
# print(d2)
#
# d1.update([(user,ord(user))])
# print(d1)
#
# d1[user]=ord(user)
# print(d1)

'''11.if length of the user input str is even, create a dict with 
user input as key and the same as value, else reverse the str for value'''
# user_input=input('enter the string:')
# dict_1={}
# if len(user_input)%2==0:
#     dict_1[user_input]=user_input
# else:
#     dict_1[user_input]=user_input[::-1]
# print(dict_1)

'''12.remove a random element from a set and create a dictionary with removed element 
as key and its len as value'''
# set={'python',10,'10',True,'False','java'}
# element=set.pop()
# dict={}
# if isinstance(element, str):
#     dict[element]=len(element)
# else:
#     dict[element]=element
# print(dict)

'''13.In a number, check if the first digit of number is even or odd'''
# number=int(input('Enter a number:'))
# str_=str(number)
# if int(str_[0])%2==0:
#     print(f'first number of {str_} is even')
# else:
#     print(f'first number of {str_} is odd')

'''14.In a number, check if the first digit of number is even or odd'''
# number=int(input('Enter a number:'))
# str_=str(number)
# if int(str_[-1])%2==0:
#     print(f'Last number of {str_} is even')
# else:
#     print(f'Last number of {str_} is odd')

'''15.Create a dictionary with the first char of user input as a key and user input as value'''
# string=input('Enter a string:')
# dict={}
# dict[string[0]]=string
# print(dict)

'''16.WAP to find greatest of three numbers'''
# a=int(input('Enter value of a:'))
# b=int(input('Enter value of b:'))
# c=int(input('Enter value of c:'))
#
# if a>b and a>c:
#     print(f'{a} is greatest number')
# elif b>a and b>c:
#     print(f'{b} is greatest number')
# else:
#     print(f'{c} is greatest number')

'''17.Leap year program'''
# year=int(input('Enter a year:'))
# if year%4==0 and year%100!=0:
#     print(f'{year} is leap year')
# elif year%400==0:
#     print(f'{year} is leap year')
# else:
#     print(f'{year} is not leap year')

'''18.WAP to check whether the person is eligible for voting '''


'''19.Printing numbers from 10 - 1'''
# start=10
# while start>0:
#     print(start)
#     start-=1

'''20.Printing numbers from -10 - -1'''
# start=-10
# while start<0:
#     print(start)
#     start+=1

'''with methods'''
# string='abcdeh12345"£$%^&*'
# alpha=0
# no=0
# spe=0
# index=0
# while index < len(string):
#     if string[index].isalpha():
#         alpha += 1
#     elif string[index].isnumeric():
#         no += 1
#     else:
#         spe += 1
#     index+=1
# print(f'{alpha} are alphacount, {no} are numbercount, {spe} are specialcount')

'''with logic'''
# string='abcdeh12345"£$%^&*'
# alpha_count = 0
# num_count = 0
# spe_char_count = 0
# index = 0
# while index<len(string):
#     if 'a'<=string[index]<='z' or 'A'<=string[index]<='Z':
#         alpha_count += 1
#     elif '0'<=string[index]<='9':
#         num_count += 1
#     else:
#         spe_char_count += 1
#     index+=1
# print(f'{alpha_count} alpha_count,{num_count} num_count, {spe_char_count} spe_num_count')

'''WAP to add even and odd numbers to seperate lists from 1 to 20'''
# even_list=[]
# odd_list=[]
# start=1
# while start<=20:
#     if start%2==0:
#         even_list.append(start)
#     else:
#         odd_list.append(start)
#     start+=1
# print(even_list)
# print(odd_list)

'''WAP to find sum of first n numbers'''
# num=int(input('Enter a number: '))
# sum1=0
# start=1
# while start<=num:
#     sum1+=start
#     start+=1
# print(sum1)

'''WAP to get sum of user input number'''
# num=int(input('Enter a number: '))
# sum1=0
# str1=str(num)
# index=0
# while index<len(str1):
#       sum1+=int(str1[index])
#       index+=1
# print(sum1)

'''WAP to print even length element only'''
# list_1=['red', 'blue', 'green', 'pink', 'black', 'white', 'purple']
# index=0
# while index<len(list_1):
#     if len(list_1[index])%2==0:
#         print(list_1[index])
#     index+=1

'''Create a dictionary with the list element as keys and its length as value'''
# list_1=['red', 'blue', 'green', 'pink', ['black', 'white'], 'purple']
# d1={}
# index=0
# while index<len(list_1):
#       d1[list_1[index]]=len(list_1[index])
#       index+=1
# print(d1)
'''not running'''

'''WAP to count the total number of vowels and consonants in the string'''
# string='big bang theory'
# index=0
# vowel_count=0
# consonant_count=0
#
# while index<len(string):
#     if 'a' <= string[index] <= 'z' or 'A' <= string[index] <='Z':
#         if string[index] in 'aeiouAEIOU':
#             vowel_count+=1
#         else:
#             consonant_count+=1
#     index+=1
# print(f'there are {vowel_count} vowels and {consonant_count} consonant in a string')

'''Reverse the string if the length is even else keep as it is '''
# list_1=['apple', 'google', 'yahoo', 'oracle', 'brillio', 'facebook']
# index=0
# list_2=[]
# while index<len(list_1):
#     if len(list_1[index])%2==0:
#         list_2+=[list_1[index][::-1]]
#     else:
#         list_2+=[list_1[index]]
#     index+=1
# print(list_2)

'''WAP to print filenames ending with com'''
# filenames=['google.com', 'yahoo.com', 'gmail.com', 'apple.in', 'fb.co.in']
# index=0
# while index<len(filenames):
#     if filenames[index][-3:] == 'com':
#         print(filenames[index][:-4])
#     index+=1

# filenames=['google.com', 'yahoo.com', 'gmail.com', 'apple.in', 'fb.co.in']
# index=0
# while index<len(filenames):
#     var = filenames[index].split('.')
#     if var[-1] == 'com':
#         print(var[0])
#     index+=1

# filenames=['google.com', 'yahoo.com', 'gmail.com', 'apple.in', 'fb.co.in']
# index=0
# while index<len(filenames):
#     var=filenames[index].partition('.')
#     if var[-1]=='com':
#         print(var[0])
#     index+=1

# filenames=['google.com', 'yahoo.com', 'gmail.com', 'apple.in', 'fb.co.in']
# index=0
# while index<len(filenames):
#     var=filenames[index].split('.',maxsplit=1)
#     if var[-1]=='com':
#         print(var[0])
#     index+=1

'''WAP to add even length and odd length elements in seperate list'''
# list_1=['apple', 'google', 'yahoo', 'oracle', 'brillio', 'facebook']
# even_length=[]
# odd_length=[]
# index=0
# while index<len(list_1):
#     if len(list_1[index])%2==0:
#         even_length.append(list_1[index])
#     else:
#         odd_length.append(list_1[index])
#     index+=1
# print(even_length)
# print(odd_length)

'''WAP to print the factorial of a number'''
# num=int(input('Enter a number: '))
# fact=1
# factorial=1
# while fact<=num:
#     factorial *= fact
#     fact+=1
# print(factorial)

# num=int(input('Enter a number: '))
# fact=1
# while num>0:
#     fact *= num
#     num -=1
# print(fact)

'''Find the avarage of numbers in the list'''
# list_2=[10,11,1,14,87,56,42,98,58]
# sum1=0
# index=0
# while index<len(list_2):
#     sum1 += list_2[index]
#     index+=1
# print(sum1/len(list_2))

''''''
# list_1=['apple', 'google', 'yahoo', 'oracle','google','facebook', 'brillio', 'facebook']
# list_2=[]
# for element in list_1:
#     if len(element)%2==0 and element not in list_2:
#         list_2.append(element)
# print(list_2)

''''''
# list_1=['apple', 'google', 'yahoo', 'oracle','facebook', 'brillio']
# dict2={}
# for element in list_1:
#     count=0
#     for item in element:
#         if item in 'aeiouAEIOU':
#             count+=1
#     dict2[element]=count
# print(dict2)

'''WAP to reverse the string if the length is even, else keep as it is'''
# list_1=['pune', 'lonavla', 'karad', 'satara', 'khanapur', 'sangli']
# list_2=[]
# for element in list_1:
#     if len(element)%2==0:
#         list_2+=[element[::-1]]
#     else:
#         list_2+=[element]
# print(list_2)

'''WAP TO COUNT THE NO. OF VOWELS AND NO. OF CONSONANTS'''
# string='an eye for an eye a tooth for a tooth'
# vowel_count=0
# consonant_count=0
# for char in string:
#       if 'a' <= char <= 'z' or 'A' <= char <='Z':
#         if char in 'aeiouAEIOU':
#             vowel_count+=1
#         else:
#             consonant_count+=1
#
# print(vowel_count,'are vowels')
# print(consonant_count,'are consonant')

'''WAP TO PRINT FACTORIAL OF NUMBER'''
# number=int(input('enter a number: '))
# fact=1
# for factorial in range(1,number+1):
#     fact *= factorial
# print(fact)

'''WAP TO PRINT AVARAGE '''
# list_1=[23, 43, 5, 12, 21, 8, 56, 34, 15]
# total=0
# for element in list_1:
#     total += element
# avarage=(total/len(list_1))
# print(avarage)

'''WAP TO PRINT FILENAMES ENDING WITH COM'''
# filenames=['whatsapp.com','linkedin.com', 'amazon.in', 'flipkart.com', 'zoom.us', 'dailyhunt.in']
# for files in filenames:
#     var=files.split('.')
#     if var[-1]=='com':
#         print(var[0])
#
# for files in filenames:
#     var=files.partition('.')
#     if var[-1]=='com':
#         print(var[0])

# for files in filenames:
#     if files[-3:]=='com':
#         print(files[:-4])

'''WAP TO PRINT ONLY FILENAMES'''
# filenames=['whatsapp.com','linkedin.com', 'amazon.in', 'flipkart.com', 'zoom.us', 'dailyhunt.in']
# for files in filenames:
#     var=files.split('.')
#     print(var[0])

'''WAP TO PRINT ONLY extensions'''
# filenames=['whatsapp.com','linkedin.com', 'amazon.in', 'flipkart.com', 'zoom.us', 'dailyhunt.in']
# for files in filenames:
#     var=files.split('.')
#     print(var[-1])

'''FIND SUM OF NUMERICAL DATA PRESENT IN LIST'''
# list_1=[20, 34, 45.8, 'HELLO', 'SAYONARA', 100, 'AM']
# sum1=0
# for element in list_1:
#     if isinstance(element,(int,float)):
#         sum1 += element
# print(sum1)

'''Create a dictionary with list elements as key and number of vowels as value'''
# list_1=['grapes', 'watermlon', 'cherry', 'banana','orange']
# d1={}
# for element in list_1:
#     count=0
#     for items in element:
#         if items in 'aeiouAEIOU':
#             count+=1
#     d1[element]=count
# print(d1)

'''CREATE A LIST WITH EVEN LENGTH ELEMENTS AVOID DUPLICATE'''
# list_2=['lemon', 'grapes', 'orange', 'apple', 'lemon', 'orange']
# list_3=[]
# for element in list_2:
#     if len(element)%2==0 and element not in list_3:
#         list_3.append(element)
# print(list_3)

'''WAP FOR PRIME NUMBER'''
# num=int(input('Enter a number: '))
# for integer in range(2,num):
#     if num%integer==0:
#         print('not prime number')
#         break
# else:
#     print('prime number')

# for integer in range(2,50):
#     for number in range(2,integer):
#         if integer%number==0:
#             break
#     else:
#         print(integer)

'''enumerate()'''
'''CREATE A DICT WHERE THE ELEMENTS WILL BE THE KEY AND ITS POSITION WILL BE THE VALUE'''
# a='god bless you'
# d={}
# for index, item in enumerate(a):
#     if item not in d:
#         d[item]=[index]
#     else:
#         d[item]+=[index]
# print(d)

# a='god bless you'
# print(enumerate(a))
# for item in enumerate(a):
#     print(item)

'''Print the statement for 5 times'''
# statement='sayonara'

'''even and odd numbers to seperate list'''
# list_1=[1,2,3,4,5,6,7,8,9,12]
# even_list=[]
# odd_list=[]
# for num in list_1:
#     if num%2==0:
#         even_list.append(num)
#     else:
#         odd_list.append(num)
# print(even_list)
# print(odd_list)

# list_1=[1,2,3,4,5,6,7,8,9,12]
# even_list=[]
# odd_list=[]
# for num in list_1:
#     if num%2==0:
#         even_list += [num]
#     else:
#         odd_list += [num]
# print(even_list)
# print(odd_list)

'''extract the palindromes from the below list'''
# list_1=['radar', 'torch', 'ship', 'malyalam', 'dad', 'mom']
# list_2=[]
# for element in list_1:
#     if element==element[::-1]:
#         list_2 += [element]
# print(list_2)

'''wap to find the sum of first n numbers'''
# number=int(input('Enter a number: '))
# sum1=0
# for item in range(1,number+1):
#     sum1 += item
# print(sum1)

'''wap to find the sum of alternate numbers from 1-50'''
# sum1=0
# for item in range(1,50,2):
#     sum1 += item
# print(sum1)
#
# sum_1=0
# for item in range (1,50):
#     if item%2!=0:
#         sum_1 += item
# print(sum_1)

'''wap to find the sum of user input number'''
# num=int(input('Enter a number: '))
# str_num=str(num)
# sum_1=0
# for element in str_num:
#     sum_1 += int(element)
# print(sum_1)

'''wap to get the maximum number in the list'''
list_1=[10, 20, 30, 40, 50, 60, 56,78]
# li_num=list_1[0]
# for item in list_1:
#     if  list_1[0] < item:
#         list_1[0]=item
# print(item)

# list_1=[10, 20, 30, 40, 50, 60, 56,78]
# list_1.sort()
# print(list_1)
# print(list_1[-1])

# list_1=[10, 20, 30, 40, 50, 60, 56,78]
# print(max(list_1))


'''even numbers from 1-50'''
# for item in range(1,50):
#     if item%2==0:
#         print(item)


'''print only even length elements'''
# list_2=['lemon', 'grapes', 'orange', 'banana', 'cherry']
# for item in list_2:
#     if len(item)%2==0:
#         print(item)

# l2=[item for item in list_2 if len(item)%2==0]
# print(l2)


'''if len of element is even retain as it is, else reverse it'''
# list_2=['lemon', 'grapes', 'orange', 'banana', 'cherry']
# l2=[]
# for item in list_2:
#     if len(item)%2==0:
#         l2.append(item)
#     else:
#         l2.append(item[::-1])
# print(l2)

'''comprehension'''
# list1=[item if len(item)%2==0 else item[::-1] for item in list_2 ]
# print(list1)


'''Assignment'''
'''1. create a list with elements whose length is less than six '''
# list1 = ['apple', 'ajio', 'ola', 'myntra', 'uber', 'oppo']
# list2=[]
# for item in list1:
#     if len(item)<6:
#         list2.append(item)
# print(list2)

# list1 = ['apple', 'ajio', 'ola', 'myntra', 'uber', 'oppo']
# list2=[]
# for item in list1:
#     if len(item)<6:
#         list2 += [item]
# print(list2)

# list1 = ['apple', 'ajio', 'ola', 'myntra', 'uber', 'oppo']
# list_2=[item for item in list1 if len(item)<6]
# print(list_2)

'''2. wap to return the list of elements starting with vowels'''
# list1 = ['apple', 'ajio', 'ola', 'myntra', 'uber', 'oppo']
# list2=[]
# for element in list1:
#     if element[0] in 'aeiouAEIOU':
#         list2 += [element]
# print(list2)

# list1 = ['apple', 'ajio', 'ola', 'myntra', 'uber', 'oppo']
# list2=[element for element in list1 if element[0] in 'aeiouAEIOU']
# print(list2)

'''3. wap to return the list of elements not starting with vowels'''
# list1 = ['apple', 'ajio', 'ola', 'myntra', 'uber', 'oppo']
# list2=[]
# for element in list1:
#     if element[0] not in 'aeiouAEIOU':
#         list2 += [element]
# print(list2)

# list1 = ['apple', 'ajio', 'ola', 'myntra', 'uber', 'oppo']
# list2=[element for element in list1 if element[0] not in 'aeiouAEIOU']
# print(list2)

'''4. wap to return the list of elements ending with vowels'''
# list1 = ['apple', 'ajio', 'ola', 'myntra', 'uber', 'oppo']
# list2=[]
# for element in list1:
#     if element[-1] not in 'aeiouAEIOU':
#         list2 += [element]
# print(list2)

# list1 = ['apple', 'ajio', 'ola', 'myntra', 'uber', 'oppo']
# list2=[element for element in list1 if element[-1] in 'aeiouAEIOU']
# print(list2)


'''5. wap to create a list of tuples of element and its len pair'''
# list1 = ['apple', 'ajio', 'ola', 'myntra', 'uber', 'oppo']
# list_2=[(item,len(item)) for item in list1]
# print(list_2)

# a = 'python'
# b = 'java'
# for item in zip(a, b):
#     print(item)

# states = ['Karnataka', 'AP', 'Maharashtra', 'Assam', 'Telangana']
# capitals = ['Bengaluru', 'Amaravathi', 'Mumbai', 'Dispur', 'Hyderabad']
# temperature = [24, 39, 35, 26, 32]
#
# print(zip(states, capitals))    #<zip object at 0x0000022422AEE7C0>
#
# for item in zip(states, capitals, temperature):
#     print(item)

# from itertools import zip_longest
# a = 'python'
# b = 'java'
# for item in zip_longest(a, b):
#     print(item)


# from itertools import zip_longest
# a = 'python'
# b = 'java'
# for item in zip_longest(a, b, fillvalue=1000):
#     print(item)

'''FUNCTIONS'''
# s='hello'
# def length():
#     count=0
#     for item in s:
#         count += 1
#     return count
# length()
# print(length())

'''wap to find prime numbers from range 2 to 100'''
# def prime(start, end):
#     for i in range(start,end):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)
# prime(2,100)

'''Global variable'''
'''to perform any operation on variable inside a function which is declared outside function we need to use
 initilize it inside function as global var_name'''

# num1=10
# def sample():
#     global num1
#     num1 += 5
#     print(num1)
# sample()

# num1= 10
# def sample():
#     global num1
#     num1 += 5
#     print(num1)
# print(num1)
# sample()
# print(num1)

'''nonlocal'''
'''used for variables which are neither global nor local, its used in nested functions '''
# a = 10
# def sample():
#     b = 5
#     def spam():
#         nonlocal b
#         global a
#         a += 3
#         b += 5
#         print(a)
#         print(b)
#     spam()
# sample()

'''Anonymous function'''
'''lambda - Syntax     lambda arg1, arg2, arg3 : expression'''
# square= lambda num: num ** 2
# print(square(9))
# print(square(11))

'''map- map applies a function to all the items in the iterable'''
# list1 = ['malyalam', 'radar', 'moon', 'pen', 'nitin', 'dad', 'mom']
# palindrome=map(lambda item:'palindrome' if item==item[::-1] else 'not palindrome',list1)
# print(palindrome)
# print(list(palindrome))

'''filter- this offers only elements which fuctions returns true'''
# even_odd=filter(lambda num: num%2==0,range(1,50))
# print(list(even_odd))
#
# even_odd=map(lambda num: num%2==0,range(1,50))
# print(list(even_odd))

# a='python is a programming language and programs are fun'
# dict={}
# var=a.split()
# for item in var:
#     for char in item:
#         if char not in dict:
#             dict[char]=[item]
#             break
#         else:
#             dict[char] += [item]
#             break
# print(dict)

'''generator function'''
'''write a generator function which produces even numners from 1-n'''
# def even(n):
#     for num in range(1,n):
#         if num%2==0:
#             yield num
# even(30)
# res1= even(30)
# print(list(res1))

'''WRITE A GENERATOR EXPRESSION AND FUNCTION TO YIELD THE TUPLE OF ELEMENT AND ITS LEN PAIR'''
# list1=['apple', 'lemon', 'grapes', 'orange', 'cherry']
# def element(list2):
#     for item in list2:
#         yield (item, len(item))
# res=element(list1)
# print(tuple(res))

'''generator expression'''
# res1=((item, len(item)) for item in list1)
# print(tuple(res1))

'''WRITE A GENERATOR FUCTION AND EXPRESSION TO YIELD THE NAMES STARTING WITH VOWELS'''
# list1=['apple', 'lemon', 'grapes', 'orange', 'cherry', 'banana']
# def vowel(list1):
#     for element in list1:
#         if element[0] in 'aeiouAEIOU':
#                 yield element
# res1=vowel(list1)
# print(list(res1))
#
# res1=(element for element in list1 if element[0] in 'aeiouAEIOU')
# print(list(res1))

'''WRITE A GENERATOR EXPRESSION AND FUNCTION TO PRINT NUM FROM 10 TO 1'''
# def number(n):
#     for num in range(n,0,-1):
#         yield num
# res1=number(10)
# print(list(res1))
#
# res2=(num for num in range (10,0,-1))
# print(list(res2))

'''file handling'''
'''without context manager'''
# file_path = r"C:\Users\Mohite's\PycharmProjects\pythonProject\python.py"
# print(file_path)
# file = open(file_path)
# print(file)
# for i in file:
#     print(i)
#
# print(file.closed)      #False
# file.close()
# print(file.closed)      #True

'''with context manager'''
# file_name = r"C:\Users\Mohite's\PycharmProjects\pythonProject\PYTHON\textfile.py"
# with open(file_name) as file:
#     print(file)
#     for line in file:
#         print(f'{line}, {len(line)}')
#         print(file.closed)
#
# print(file.closed)

'''read() : Will read the entire file '''
# f_path = r"C:\Users\Mohite's\PycharmProjects\pythonProject\PYTHON\textfile.py"
# with open(f_path) as file:
#     print(file.read())

# f_path = r"C:\Users\Mohite's\PycharmProjects\pythonProject\PYTHON\textfile.py"
# with open(f_path) as file:
#     print(file.read(3))
#     print(file.read(4))


'''readline() : Will just read one line at a time'''
# f_path = r"C:\Users\Mohite's\PycharmProjects\pythonProject\PYTHON\textfile.py"
# with open(f_path) as file:
#     print(file.readline())
#     print(file.readline())
#     print(file.readline(4))
#     print(file.readline())

'''readlines() : Reads the entire file and stores the data
in the form of a list, where each line will be the element of
a list'''
# f_path =r"C:\Users\Mohite's\PycharmProjects\pythonProject\PYTHON\textfile.py"
# with open(f_path) as file:
#     print(file.readlines())
#
# f_path =r"C:\Users\Mohite's\PycharmProjects\pythonProject\PYTHON\textfile.py"
# with open(f_path) as file:
#     print(file.readlines(3))
#     print(file.readlines(12))

'''wap to print the line along with line number'''
# f_path= r"C:\Users\Mohite's\PycharmProjects\pythonProject\PYTHON\textfile.py"
# count = 1
# with open(f_path) as file:
#     for line in file:
#         print(f'{line} - {count}')
#         count += 1

# f_path = r"C:\Users\Mohite's\PycharmProjects\pythonProject\PYTHON\textfile.py"
# with open(f_path) as file:
#     for line_no, line in enumerate(file, start=1):
#         print(line, line_no)

# '''wap to reverse the file'''
# f_path = r"C:\Users\Mohite's\PycharmProjects\pythonProject\PYTHON\textfile.py"
# with open(f_path) as file:
#      for line in reversed(list(file)):
#          print(line,end=' ')

# f_path = r"C:\Users\Mohite's\PycharmProjects\pythonProject\PYTHON\textfile.py"
# with open(f_path) as file:
#     for line in reversed(list(file)):
#         for element in reversed(line):
#             print(element, end='')

'''WAP TO PRINT THE NUMBER OF ELEMENTS IN EACH LINE'''
# f_path = r"C:\Users\Mohite's\PycharmProjects\pythonProject\PYTHON\textfile.py"
# with open(f_path) as file:
#     for line in file:
#         count = 0
#         for element in line:
#             count += 1
#         print(line, count)

'''write()'''
f_path = r"C:\Users\Mohite's\PycharmProjects\pythonProject\PYTHON\textfield2.py"
# with open(f_path, 'w') as file:
#     print(file.write('bengaluru\n'))
#     print(file.write('mysuru\n'))
#     print(file.write('shimoga\n'))
#     print(file.write('hubli\n'))
#
#
# f_path= r"C:\Users\Mohite's\PycharmProjects\pythonProject\PYTHON\textfield2.py"
# with open(f_path, 'w') as file:
#     print(file.write('vita\n'))
#     print(file.write('satara\n'))
#     print(file.write('khanapur\n'))
#     print(file.write('sangli\n'))
#
# '''writelines()'''
#
# f_path = r"C:\Users\Mohite's\PycharmProjects\pythonProject\PYTHON\textfield2.py"
# with open(f_path, 'a') as file:
#     print(file.writelines(['karad\n','pune\n','mumbai\n']))

'''Exception handling'''
'''Default except block'''
# num1=10
# num2=0
# try:
#     print(num1/num2)
# except:
#     print('except block executing')

'''Specific except block'''
# num1 = int(input('Enter a number1: '))
# num2 = int(input('Enter a number2: '))
# try:
#     print(num1/num2)
# except ZeroDivisionError:
#     print('number can not divided by zero')

# try:
#     print(x)
# except NameError:
#     print('variable is not defined')
#


'''Multiple except block'''
# num1 = int(input('Enter a number1: '))
# num2 = int(input('Enter a number2: '))
# try:
#     print(num1/num2)
# except ZeroDivisionError:
#     print('number can not divided by zero')
# except NameError:
#     print('name is not defined')
# except:
#     print('something went wrong')

# try:
#     print(x)
# except:
#     print('something went wrong')
# else:
#     print('nothing went wrong')


# try:
#     print(x)
# except:
#     print('something went wrong')
# else:
#     print('noting went wrong')
# finally:
#     print('finally done')

'''Generic except block'''
# num1 = 10
# num2 = 0
# try:
#     print(num1/num2)
# except BaseException as error_msg:
#     print('except block executing')
#     print(error_msg)

# try:
#     print(x)
# except BaseException as error_msg:
#     print('exception block is executing')
#     print(error_msg)

# a = []
# try:
#     a.append(10)
# except:
#     print('hello world')
# else:
#     print(a)
# finally:
#     print('finally executed')

'''raise'''
# num = int(input('Enter the number: '))
# if num < 0:
#     raise UnicodeError
# else:
#     print('number greater than zero')


'''wap to handle ZeroDivisionError, if no error, print the
result, also print all the numbers'''
# num = [(1, 0), (3, 5), (8, 6), (9, 0), (7, 5), (4, 0)]
# for item in num:
#     try:
#         result= item[0]/item[1]
#     except ZeroDivisionError:
#         print('except block executing')
#     else:
#         print(result)
#     finally:
#         print(f'the numbers are {item[0]} and {item[1]}')
#     print('**********************************************')

'''custom exception'''
# class OurOwnError(BaseException):
#     pass
#
# num = int(input('Enter the number: '))
# if num < 0:
#     raise OurOwnError
# else:
#     print('number greater than zero')

'''class'''
# class Calculator:
#
#     def __init__(self, val1, val2):
#         self.val1 = val1
#         self.val2 = val2
#
#     def add(self):
#         print(self.val1 + self.val2)
#
#     def sub(self):
#         print(self.val1 - self.val2)
#
#     def mul(self):
#         print(self.val1 * self.val2)
#
#     def div(self):
#         print(self.val1/self.val2)
#
# cal1 = Calculator(8, 4)
# # cal1.add(2, 4)
# # cal1.sub(2, 4)
# cal1.add()
# cal1.sub()
# cal1.mul()
# cal1.div()

# class Sample:
#     x = 10
#
#     def display(self):
#         print('Display method executing')
#
#     def spam(self):
#         print('spam method executing')
#
# sample_obj_1 = Sample()
# sample_obj_2 = Sample()
# sample_obj_1.display()
# sample_obj_1.spam()
# Sample.display(sample_obj_1)

# print(sample_obj_1.x)
# print(sample_obj_2.x)
# sample_obj_1.x = 100
# print(sample_obj_1.x)
# print(Sample.x)
# print(sample_obj_2.x)
# sample_obj_2.x = 300
# print(sample_obj_2.x)
# Sample.x = 200
# print(Sample.x)
# print(sample_obj_2.x)
# print(sample_obj_1.x)

# class Employee:
#
#     def __init__(self, fname, lname, eid):
#         self.fname = fname
#         self.lname = lname
#         self.eid = eid
#
#     def display(self):
#         print(f'Hello {self.fname} {self.lname}, Welcome to CapGemini')
#         print(f'Your employee ID is {self.eid}')
#
#     def email(self):
#         print(f'{self.fname}_{self.lname}_{self.eid}@capgemini.com')
#
# emp1 = Employee('Ashwini', 'Mohite', 101)
# emp1.display()
# emp1.email()

'''INHERITANCE'''

'''Single level Inheritance'''
# class Parent:
#     villa='Aanadsagar'
#     def display(self):
#         print(f'The villa name is {self.villa}')
#
# class Child(Parent):
#     car ='swift'
#     def display(self):
#          print(f'The car name is {self.car} and the villa name is {self.villa}')
#
# a=Child()
# b=Parent()
# a.display()
# b.display()


'''Multilevel'''
# class Grandpa:
#     land = 2
#     def display(self):
#         print(f'the land is {self.land} akr')
#
# class Parent(Grandpa):
#     villa='Aanadsagar'
#     def display(self):
#         print(f'The villa name is {self.villa} and land {self.land} akr')
#
# class Child(Parent):
#     car ='swift'
#     def display(self):
#          print(f'The car name is {self.car} and the villa name is {self.villa} and land {self.land} akr')
#
# a1=Grandpa()
# a2=Parent()
# a3=Child()
# a1.display()
# a2.display()
# a3.display()




'''classmethod'''

# class PrimeMinister:
#     current_pm = 'Narendra Modi'
#
#     def display(self):
#         print(f'The current PrimeMinister is {self.current_pm}')
#
#     @classmethod
#     def replacement(self, votes):
#         if votes > 100:
#             self.current_pm = 'Yogi Adithyanath'
#
# bjp = PrimeMinister()
# opposition = PrimeMinister()
# common_people = PrimeMinister()
# bjp.display()
# opposition.display()
# common_people.display()
# bjp.replacement(110)
# bjp.display()
# opposition.display()
# common_people.display()

#############################################
'''static method'''
# class Calculator:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         print(self.a + self.b)
#
#     @staticmethod
#     def display(x, y):
#         print('display executing')
#         print(x * y)
#
# cal1 = Calculator(1, 2)
# cal1.display(6,7)
# cal1.add()

'''constructor chaining'''
# class sample:
#     def __init__(self, val1, val2):
#         self.val1 = val1
#         self.val2 = val2
#
#     def display(self):
#         print(f'The values are {self.val1} and {self.val2}')
#
# class Example(sample):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#         super().__init__(a, b)
#
#     def spam(self):
#         print(f'The values are {self.a} and {self.b} and {self.c}')
#
# example_obj_1 = sample(7,9)
# example_obj = Example(2, 5, 4)
# example_obj.display()
# example_obj.spam()
# example_obj_1.display()

# class sample:
#     def __init__(self, val1, val2, val3):
#         self.val1 = val1
#         self.val2 = val2
#         self.val3 = val3
#
#     def display(self):
#         print(f'The values are {self.val1} and {self.val2} and {self.val3}')
#
# class Example(sample):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         super().__init__(a, b)
#
#     def spam(self):
#         print(f'The values are {self.a} and {self.b}')
#
# example_obj_1 = sample(7,9,6)
# example_obj = Example(2, 5)
# example_obj.display()
# example_obj.spam()
# example_obj_1.display()
###### if the no of argument are 3 in first class init method and 2 in second class init method it will
###### it will throw error but if there are less no of arguments in first init class and more no of arguments
###### in second init class then it will not throw any error



'''Custom Iterator'''
'''create a class to print numbers from 1 to 10'''
# class Number:
#     def __init__(self,start,end):
#         self.start=start
#         self.end=end
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start < self.end:
#             print(self.start)
#             self.start += 1
#         else:
#             raise StopIteration
# obj=Number(1,11)
# for item in obj:
#     if item !=None:
#         print(item)

'''create a class to print numbers from 10 to 1'''
# class Number:
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start > self.end :
#             self.start -= 1
#             return self.start
#         else:
#             raise StopIteration
#
# obj1=Number(11,1)
# for item in obj1:
#     print(item)

'''Create a class to print square of the numbers from 1 to 10'''
# class Square:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < self.end:
#             print(self.start * self.start)
#             self.start += 1
#
# square_obj = Square(1,11)
# for item in square_obj:
#     if item != None:
#         print(item)


# class Sample:
#     def display(self, a):#overridden method
#         self.a=a
#         print(f'value of a is {a}')
#         print('Sample class display method executing')
#     def spam(self):     #independent method
#         print('Sample class spam method executing')
#
# class Example(Sample):
#
#     def display(self, a):
#         print(f'value of a is {a}')
#         print('Example class display method executing')
#
#     def spam1(self):
#         print('Example class spam1 method executing')
#
# example_obj = Example()
# example_obj.display(3) #Example class display method executing
# example_obj.spam1() #Example class spam1 method executing
# example_obj.spam()  #Sample class spam method executing
# sample_obj = Sample()
# sample_obj.display(4)




















































