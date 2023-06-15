'''Typecasting'''
'''converting int datatypes into other datatypes'''
# a=15
# print(float(a))
# print(complex(a))
# print(bool(a))

'''converting float datatypes into other datatypes'''
# b=5.4
# print(int(b))
# print(complex(b))
# print(bool(b))

'''converting complex datatypes into other datatypes'''
# c= 5+2j
# print(int(c))              TypeError: can't convert complex to int
# print(float(c))              TypeError: can't convert complex to float
# print(bool(c))                 True

'''default value'''
# print(bool(0))
# print(bool(int()))
#
# print(bool(0.0))
# print(bool(float(0.0)))
#
# print(bool(0j))
# print(bool(complex()))
#
# print(bool(False))
# print(bool(bool()))

'''Print: Standard function used to print output to the console
# Syntax: print(values, sep='', end=backword_slash n)'''

# print('a','b','c','d')
# print('a','b','c','d',sep='*')
#
# print('hello',end='*****')
# print('python')
#
# print('hai','hello','how','are',sep='^',end='%')
# print('you','doing',sep='*')

'''.format()'''
# print('hi {} ,I am {} years old'.format('Ram',45))
# print('hi {0},I am {1} years old'.format('Ram', 45))
# print('hi {name},I am {age} years old'.format(name='Ram', age=45))

'''f-string'''
# name='Ram'
# age=45
# print(f'hi {name},I am {age} years old')
#
# hours=24
# minutes=60
# print(f'In a day there are {hours}hours and {hours*minutes}minutes')

'''input'''
# name=input('Enter a name:')
# print(f'My name is {name}')

# num1=int(input('Enter a num1:'))
# num2=int(input('Enter a num2:'))
# print(num1+num2)

'''type()'''
# a=10
# print(type(a))     <class 'int'>

'''isinstance'''
# print(isinstance(10,int))
# print(isinstance(5.6,float))
# print(isinstance(8,int,float,complex))      TypeError: isinstance expected 2 arguments
# print(isinstance(8,(int,float,complex)))
# print(isinstance(6+0j,(int,float,complex)))

'''ord(): Gives the ASCII value'''
# print(ord('z'))
# print(ord('@'))

'''dir(): list of attributes'''
# a=10
# print(dir(a))

'''id(): gives memory address'''
# a=10
# b=20
#
# print(id(a))
# print(id(b))

'''chr(): get the character of that ASCII value '''
# print(chr(78))
# print(chr(56))
# print(chr(3))

'''STRING'''
'''len()'''
# sentence='Welcome to python world'
# print(len(sentence))

'''Indexing(): extracting single character
       Syntax: var_name[value]'''
# a='hello world kay chally'
# print(a[7])
# print(a[17])
# print(a[34])            IndexError: string index out of range    when the id is greater than its length

'''Slicing(): slice the string
   Syntrx: var_name[(start value):(end value):(step value)]
                          0         len(str)         1       '''
# a='kay world nivant'
# print(a[ : : ])
# print(a[10: :1])

'''positive slicing '''

# a='kay world nivant'

'''to slice 'kay world' '''
# print(a[0:10:1])
# print(a[-16:-7:1])
# print(a[0:-7:1])
# print(a[-16:10:1])

'''negative slicing'''
# print(a[-8: :-1])
# print(a[9: :-1])

'''String Methods'''
'''1.upper(): convert lowercase to uppercase'''
# a='NamaskaR WorlD!'
# print(a.upper())
#
# '''2.lower(): convert lowercase to uppercase'''
# print(a.lower())
#
'''3.swapcase(): convert lowercase to uppercase and viceversa'''
# print(a.swapcase())

'''4.count(): count occurance of specified element'''
# print(a.count('a'))

'''5.capitalize():'''
# b='good morning maharashtra'
# print(b.capitalize())

'''6.title():'''
# print(b.title())

'''7.startswith():'''
# print(b.startswith('g'))
# print(b.startswith('G'))

'''8.endswith():'''
# print(b.endswith('a'))
# print(b.endswith('shtra'))

'''9.strip():'''
# word='*****welcome to my world*****'
# print(word.strip('*'))
#
# word_='£^&%**welcome to my world*^@*'
# print(word_.strip('@$%^*'))

'''10.lstrip():'''
# print(word.lstrip('*'))

'''11.rstrip():'''
# print(word.rstrip('*'))

'''12.split():'''
# word_1='a tooth for a tooth and an eye for an eye'
# print(word_1.split('o'))
# print(word_1.split('o',maxsplit=3))

'''13.rsplit():'''
# print(word_1.rsplit('o'))
# print(word_1.rsplit('o',maxsplit=3))

'''14.join():'''
# word_2=['a t', '', 'th f', 'r t', '', 'th and an eye f', 'r an eye']
# print('o'.join(word_2))

'''15.index():'''
# word_1='a tooth for a tooth and an eye for an eye'
# print(word_1.index('t'))
# print(word_1.index('f',6,10))

'''16.rindex():'''
# print(word_1.rindex('h'))
# # print(word_1.rindex('x'))             ValueError: substring not found

'''17.find()'''
# word_1='a tooth for a tooth and an eye for an eye'
# print(word_1.find('e'))
# print(word_1.index('h',6,10))

'''18.rfind():'''
# print(word_1.rfind('h'))
# print(word_1.rfind('x'))              -1

'''19.partition():'''
# word='Rollercoster'
# print(word.partition('e'))
# print(word.partition('c'))

'''20.rpartiton():'''
# print(word.rpartition('e'))
# print(word.rpartition('i'))
# print(word.rpartition('s'))

'''21.isupper():'''
# word='python'
# print(word.isupper())
# word_1='PYTHON'
# print(word_1.isupper())
# word_2='Java'
# print(word_2.isupper())

'''22.islower():'''
# print(word.islower())
# print(word_1.islower())
# print(word_2.islower())

'''23.isalpha():'''
# print(word.isalpha())
# print(word_1.isalpha())
# print(word_2.isalpha())

'''24.replace():'''
# string='Tomorrow is holiday'
# print(string.replace('o','@',3))

'''25.isnumeric()/isdigit():'''
# string_1='123456678'
# print(string_1.isnumeric())
# string_2='123456   678'
# print(string_2.isnumeric())

'''26.isalnum():'''
# string='abc123'
# print(string.isalnum())

'''27.istitle():'''
# sentence='eat one apple daily to stay healty'
# print(sentence.istitle())

'''LIST'''
'''1.append(): add element to the list'''
# list=['hi','hello',34,678,'python']
# print(list.append('bye'))
# print(list)
# list.append([12,20])
# print(list)

'''2.extend(): add more than one element to the list'''
# list=['hi','hello',34,678,'python']
# list.extend(['java','automation'])
# print(list)                              ['hi', 'hello', 34, 678, 'python', 'java', 'automation']


'''3.pop(): used to delete a specified element. returns the deleted element, if parameter not specified
          delete end element of list'''
# list=['hi', 'hello', 34, 678, 'python', 'java', 'automation']
# print(list.pop(4))               python
# print(list)                      ['hi', 'hello', 34, 678, 'java', 'automation']

'''4.insert(): used to insert element at a specified position'''
# list_1=['hi', 'hello', 34, 678, 'java', 'automation']
# print(list_1.insert(4,'python'))         None
# print(list_1)                            ['hi', 'hello', 34, 678, 'python', 'java', 'automation']

'''5.remove(): to remove a particular element'''
# list_2=['vita','khanapur','karad','sangli','pune']
# print(list_2.remove('pune'))
# print(list_2)

'''6.count(): count occurance of particular element'''
# a=[10,40,30,20,10,20,20,10,40]
# print(a.count(10))
# print(a.count(50))
# print(a.count(20))

'''7.index(): give index of first occurance of specified number'''
# a=[10,40,30,20,10,20,20,10,40]
# print(a.index(40))
# print(a.index(20))

'''8.reverse(): will reverse the original list'''
# list_2=['vita','khanapur','karad','sangli','pune']
# list_2.reverse()
# print(list_2)

'''9.sort(): will sort the list
             Syntax- var_name.sort(key=(len))'''
# list_2=['vita','khanapur','karad','sangli','pune']
# list_2.sort()
# print(list_2)
# list_2.sort(reverse=True)
# print(list_2)
# list_2.sort(key=len)
# print(list_2)
# list_2.sort(key=len, reverse=True)
# print(list_2)

'''TUPLE'''
'''1.count():'''
# A=(1,2,3,2,2,3,3,4,4,4,5,)
# print(A.count(4))

'''2.index():'''
# print(A.index(4))

'''SET'''
'''1.add(): will add an element to set, element will be at any random position'''
# set_1={'hi', 'hello', 34, 678, 'java', 'automation'}
# print(set_1.add('selenium'))
# print(set_1)

'''2.pop(): will remove any random element'''
# set_1={'hi', 'hello', 34, 678, 'java', 'automation'}
# print(set_1.pop())
# print(set_1)

'''3.remove(): will remove specified element, if the element is not present in set it will display KeyError'''
# set_1={'hi', 'hello', 34, 678, 'java', 'automation'}
# set_1.remove('automation')
# print(set_1)
# set_1.remove('bye')
# print(set_1)                     KeyError: 'bye'

'''4.discard(): works same as remove, if element is not in set it will display the set'''
# set_1={'hi', 'hello', 34, 678, 'java', 'automation'}
# set_1.discard('hi')
# print(set_1)
# set_1.discard('bye')
# print(set_1)

'''5.issubset(): check if the one set is subset of other set, return output is boolean'''
# a={5,6,7,8,9}
# b={1,2,3,4,5,6,7,8,9}
# print(a.issuperset(b))
# print(b.issuperset(a))

'''6.issuperset(): check if one set is superset of other set, output boolean'''
# print(a.issuperset(b))
# print(b.issuperset(a))

'''7.isdisjoint(): check if there is no common element two sets'''
# a={5,6,7,8,9}
# b={1,2,3,4,5,6,7,8,9}
# print(a.isdisjoint(b))
#
# c={23,3,2,4}
# d={56,8,9,7}
# print(c.isdisjoint(d))

'''DICTIONARY'''
'''different ways of creating a dictionary'''
# dict_1={'city':'vita','tal':'khanapur','dist':'sangli'}
# print(dict_1)
#
# dict_2=dict([('city','vita'),('tal','khanapur'),('dist','sangli')])
# print(dict_2)
#
# dict_3=dict((('city','vita'),('tal','khanapur'),('dist','sangli')))
# print(dict_3)

# dict_3['pincode']=123456
# print(dict_3)

# dict_1['pincode']=123456
# print(dict_1)

'''1.get(): returns the value of specified key'''
# dict_1={'city': 'vita', 'tal': 'khanapur', 'dist': 'sangli', 'pincode': 123456}
# print(dict_1.get('city'))

'''2.setdefalt():       Syntax- var_name.setdefault(key,[value=None])'''
# dict_1={'city': 'vita', 'tal': 'khanapur', 'dist': 'sangli', 'pincode': 123456}
# print(dict_1.setdefault('city'))        vita
# print(dict_1.setdefault('state'))       None
# print(dict_1)                   {'city': 'vita', 'tal': 'khanapur', 'dist': 'sangli', 'pincode': 123456, 'state': None}
# print(dict_1.setdefault('state','maharashtra'))            maharashtra
# print(dict_1)                      {'city': 'vita', 'tal': 'khanapur', 'dist': 'sangli', 'pincode': 123456, 'state': 'maharashtra'}

'''3.keys(): returns the list of keys'''
# dict_1={'city': 'vita', 'tal': 'khanapur', 'dist': 'sangli', 'pincode': 123456, 'state': 'maharashtra'}
# print(dict_1.keys())

'''4.values(): returns the list of values'''
# print(dict_1.values())

'''5.items(): returns the list of tuples'''
# print(dict_1.items())

'''6.update(): '''
# d={'asahi':1,'nishinoya':2,'hinata':3,'sugawara':4}
# d.update([('kageyama',5),('kenma',6),('dasai',7)])
# print(d)

'''7.pop(): removes key-value pair from list'''
# print(d.pop('dasai'))
# print(d)

'''8.popitems(): will remove last update'''
# print(d.popitem())                ('kenma', 6)

'''9.fromkeys(): '''
# a='selenium'
# print(dict.fromkeys(a))
#
# b=[('iliya'),('judith'),('airen')]
# print(dict.fromkeys(b))
#
# print(dict.fromkeys(b,'hi'))

'''merging two dictionaries'''
# d1={'airen':5,'iliya':4.5,'judith':4.3,'brete':4.4}
# d2={'ruru':6,'orak':4}
# d3={**d2, **d1}
# print(d3)
# d4={**d1, **d2}
# print(d4)

'''Conditional Statements'''
'''if statement'''

# a=int(input('Enter a number:'))
# if(a>20):
#     print(f'{a} is valid number')

'''if else statement'''
# b=int(input('Enter a number:'))
# if (20<= b <=100):
#     print(f'{b} is in range of 20-100')
# else:
#     print(f'{b} is in not range of 20-100')

'''elif statement'''
# a=int(input('Enter a number:'))
# if (a>=18):
#     print(f'your age is {a}')
#     print('you are eligible to vote')
# elif(14<=a<=17):
#     print(f'your age is {a}')
#     print('wait for some years')
# else:
#     print(f'your age is {a}')
#     print('you are a child go home and study')

'''Nested if'''
# a=int(input('Enter a number:'))
# if(0<a<=100):
#     if (a>40):
#         print('congratulations!!!!')
#         print('you are pass')
#     else:
#         print('congratulations??????')
#         print('you are fail')
# else:
#     print('enter valid number')


# num = int(input("Enter a number:"))
#
# def fibinosi():
#     a = 0
#     b = 1
#
#     for i in range(1,num):
#
#
#         c = a + b
#         yield (a)
#         a = b
#         b = c
#
# fibinosi()
# print(list(fibinosi()))
# print(list(fibinosi()))
# print(list(fibinosi()))








# f = open(r"C:\Users\Mohite's\PycharmProjects\pythonProject\PYTHON\textfile.py","r")
# print(f.read(5))













# num = int ( input("Enter a number: "))
# sum = str(num)
# abc = 0
# for i in sum:
#     abc += int(i)
#
# print(abc)



