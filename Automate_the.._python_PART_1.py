# # # # # # # # CHAPTER_1 # # # # # # # # 

# print(2+3)
# print(2+3-1) # HERE PRECIDENCE IS FROM LEFT TO RIGHT
# print(21*2/3//2%2+6-2)  # HERE PRECEDENCE IS FROM LEFT TO RIGHT
# print(3232323*23234332727277)
# print(2**100)
# print(2**(22/7))
# print((5-1)*((7+1)/(3-1))) # 4 * (8/2) --> 4 * 4 = 16

# print("HELLO WORLD\n"*5)

# spam = 40
# spam_1 = 41
# print(spam + spam_1)

# var1 = 2
# var1 = 2+4
# print(var1)

# print("Hello World !")
# print("WHAT IS YOUR NAME : ")
# name = input()
# print("HELLO, "+name+" NICE TO TALK WITH YOU")
# print("THE LENGTH OF YOUR NAME IS : ")
# print(len(name))
# print("WHAT's YOUR AGE : ")
# age = int(input())
# print("YOU WILL BE "+str(age+1)+" IN A YEAR")

# a = 19
# print(str(a))
# print("YOUR AGE IS "+ str(a))
# b = 45
# c = int(45)
# print(b,c)
# d = 22.3
# print(int(d))

# print('42'==42)
# print(42.0==42)
# print(42==000042.00000)

# a = 344.233113311244
# print(round(a))
# print(round(a,2))
# print(round(a,100))

# # # # # # # # CHAPTER_2 # # # # # # # # 

# spam = True
# print(spam)

# print(42==42)
# print(91!=19)
# print(33<22)
# print(32>100)
# print(33>=33)
# print(11<=22)
# print("class1"=="class1")
# print(19.0==19.0)
# print(19==19.0)
# print(19=='19')
# print("dog"!="cat") # WHILE CODING AND MENTIONING THIS TYPE OF DATA WE CAN JUST WRITE:If TRUE.

# print(True & True)
# print(True and True)
# print(True and False)
# print(False and False)


# print(True | True)
# print(True or True)
# print(True or False)
# print(False or False)

# print((not True) | True) # print(False | True)
# # ALSO:
# print(False | True)
# print((not True) or True)
# print((not True) or False)
# print((not False) or False)

# print((1==2)|(1==1))

# print((1==2) or (1>2) and (2*2==4))

# print((1==2) and not(1*2==4) or (5-1==4)) # print(False and not False or True)-->print(False and True or True)-->print(False or True)-->print(True)-->OUTPUT: True

# name_1 = input("ENTER YOUR NAME : ").title()
# Password_1 = "12345690"
# if name_1 == "Anurag":
#     print("Hello, "+name_1+"\nTYPE THE PASSWORD : ")
#     Password_2 = int(input())
#     if Password_2 == 12345690:
#         print("ACCESS GRANTED")
#     else:
#         print("ACCESS DENIED")
# else:
#     print("ACCESS DENIED")

# name_1 = "Anurag"
# if name_1 == "Anurag":
#     print("Hello, "+name_1)
# # ALSO:
# name_1 = "Anurag"
# if True:
#     print("Hello, "+name_1)
# # BUT: 
# name_1 = "Anurag"
# if False:
#     print("Hello, "+name_1)

# name_1 = input("ENTER YOUR NAME : ").upper()
# age_1 = int(input("ENTER YOUR AGE, "+name_1+" :"))
# if name_1 == "ANURAG": # IF THIS IS FALSE THAN NEXT ELIF WILL RUN
#     print("Hello, "+name_1)
# elif name_1 == "KRSNA":   # # IF THIS IS FALSE THAN NEXT ELIF WILL RUN
#     print("Hello, "+name_1)
# elif age_1 > 200:   # IT WILL BE PRINTED IF NAME IS OTHER THAN "ANURAG" & "KRSNA" AND IF THIS IS FALSE THAN NEXT ELIF WILL RUN
#     print("YOU ARE NOT A HUMAN")
# elif age_1 < 18:   # IF THIS FALSE THEN ELSE WILL RUN 
#     print("Ok !")
# else:
#     print("HELLO STRANGER NAMED : "+name_1)

# spam = 0
# if spam < 5:
#     print("HELLO WORLD")
#     spam = spam + 1

# spam = 0
# while spam < 5:
#     print("HELLO WORLD")
#     spam = spam + 1

# name = ''
# while name != 'your name':
#     name = input("ENTER YOUR NAME : ")
# print("THANKS!")

# while True:
#     name = input("ENTER YOUR NAME : ")
#     if name == "YOUR NAME":
#         break
# print("THANK YOU")

# while True:
#     name = input("ENTER YOUR NAME : ")
#     name_1 = name.upper()
#     if name_1 != "KRSNA":
#         continue
#     print("HELLO" + name_1 + ", RADHE RADHE")
#     password = input("ENTER YOUR PASSWORD?(ITS A SONG) : ")
#     password_1 = password.upper()
#     if password_1 == "GITA":
#         break
# print("ACCESS GRANTED")

# name = ''
# while not name: # ALSO : not name != '' ---> not False(False as name = '') ---> True
#     name = input("ENTER YOUR NAME : ")
# print("HOW MANY GUEST WILL YOU HAVE ? : ")
# guest_no = int(input())
# if guest_no:
#     print("BE SURE YOU HAVE ENOUGH ROOMS FOR THE GUEST!")
# print("NO PROBLEM")

# var1 = "Hello World"
# for i in range(1,6):
#     print(f"{var1}:{i}")
# # ALSO:
# var1 = "Hello World"
# i = 1
# while i < 6:
#     print(f"{var1}:{i}")
#     i = i + 1


# total = 0
# for i in range(101):
#     total = total + i 
#     # print(total)
# print(total)
# # ALSO:
# i = 1
# total = 0
# while i<101:
#     total = total + i # 0+1+2+3...+100 = 5050
#     i = i + 1
# print(total)

# for i in range(11):
#     print(i)

# for i in range(1,11):
#     print(i)

# for i in range(1,11,2):
#     print(i)

# for i in range(10,-1,-1):
#     print(i)

# import random
# for i in range(5):
#     print(random.randint(1,5))
#     # print(random.randrange(1,5,2))
#     # print(random.random())
# # # ALSO:
# from random import random
# for i in range(5):
#     print(random())

# import sys
# while True:
#     print("TYPE 'EXIT' TO EXIT")
#     input_1 = input()
#     input_2 = input_1.upper()
#     if input_2 == "EXIT":
#         sys.exit()
#     print("YOU TYPED "+input_2)

# name = "ANURAG"
# age = 20
# print("Hello, %s. You are %s"%(name,age))

# spam = " "
# while spam != 0 : # PROGRAM WILL EXIT IF SPAM == 0 ELSE RUN FOREVER
#     spam = int(input("ENTER THE NUMBER : "))
#     if spam == 1:
#         print("HELLO")
#     elif spam == 2:
#         print("HOWDY")
#     else:
#         print("GRETTINGS !")

# for i in range(1,11):
#     print(i,end=" ")

# i = 1
# while i<=10:
#     print(i,end=" ")
#     i += 1

# # # # # # # # CHAPTER_3 # # # # # # # # #

# def hello():
#     print("Howdy!")
#     print("Howdy!!")
#     print("OK")
# hello()

# def hello(name):
#     print("Hello, "+name)
# hello("Krsna")

# import random
# def alphabets(spam):
#     if spam == 1:
#         return("a")
#     elif spam == 2:
#         return("b")
#     elif spam == 3:
#         return("c")
#     elif spam == 4:
#         return("d")
#     elif spam == 5:
#         return("e")
# n = random.randint(1,5)
# a = alphabets(n)          # WE CAN DO LIKE THIS ALSO : print(alphabets(random.randint(1,5)))
# print(a)                 ̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌

# spam = print("HELLO")
# print(spam)  # AS IN THIS VARIABLE THERE IS NO VALUE INSIDE

# def say(type_1):
#     return   # I DID NOT RETURN ANYTHING
# print(say("anurag")) # AS NOTHING IS RETURNED SO WE GET 'None'

# print("Hello")
# print("World")
# print("Hello",end=" ")
# print("World")
# print("Hello World")
# print("Hello","World",sep=',')

# def a():
#     print('a() starts')
#     b()
#     c()
#     print('a() returns')
# def b():
#     print('b() starts')           # CALLED "CALL STACK"
#     c()
#     d()
#     print('b() ends')
# def c():
#     print('c() starts')
#     print('c() ends')
# def d():
#     print('d() starts')
#     print('d() ends')
# a()                           ̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌̌

# def spam():
#     name = 50
#     return(name)
# print(spam())
# print(name)

# def spam():
#     a = 10
#     bacon()  # BACON RETURNS NONE
#     print(a)
#     b = 20
#     print(b)
# def bacon():
#     a = 50
# print(spam())

# def spam():
#     print(eggs)
# eggs = 10
# spam()
# print(eggs)

# def spam():    
#     eggs = "spam local"
#     print(eggs) # PRINTS 'SPAM LOCAL'
# def bacon():
#     eggs = 'bacon local'
#     print(eggs)  # PRINTS 'BACON LOCAL'
#     spam()   # PRINTS 'SPAM LOCAL'
#     print(eggs) # PRINTS "BACON LOCAL"
# eggs = "global"
# bacon() 
# print(eggs) # PRINTS "GLOBAL"


# # eggs = 20     # <----    
# def spam():
#     global eggs # -----̌̌̌̌̌̌̌̌̌̌̌ IT MEANS
#     eggs = 20
#     print(eggs)  # PRINTS 20
# eggs = "global"
# spam()  
# print(eggs) # PRINTS 20 AS NOW WE MODIFIED THE GLOBAL VARIABLE TO EGGS = 20

# def spam():
#     global eggs
#     eggs = "spam" # GLOBAL VARIABLE
# def bacon():
#     eggs = "bacon" # LOCAL VARIABLE
# def hams():
#     print(eggs) # GLOBAL VARIABLE
# eggs = 42 # GLOBAL VARIABLE
# spam() 
# print(eggs)

# def spam():
#     print(eggs) # PRINT GLOBAL IN PRESENCE OF LOCAL VARIABLES AS PRINT STATEMENT IS ABOVE THE LOCAL VARIABLE ASSIGNMENT HENCE ERROR COMES
#     eggs = 'spam local'
# eggs = 'global'
# spam()

# def spam(enter):
#     try:
#         return(42/enter)
#     except ZeroDivisionError:
#         return("Error:ZeroDivisionError")
# print(spam(21))
# print(spam(0))
# print(spam(2))
# print(spam(3))

# IF WE WANT TO ENTER OUR WORDS WHILE ERROR COMES AND DON'T WANT ANYTHING TO PRINT AFTER ERROR
# def spam(enter):
#     return(42/enter)
# try:
#     print(spam(21))
#     print(spam(0))
#     print(spam(2))
#     print(spam(3))
# except ZeroDivisionError:
#     print("ERROR:ZeroDivisionError")

# # # # # # # # CHAPTER_4 # # # # # # # # #

# animals = ['cat','rat','dog']
# print("Many peoples like "+animals[2]+" as their pet.")

# animals = ['cat','rat','dog',['a','b','c']]
# print(animals[3])
# print(animals[3][0])
# print(animals[3][1])

# animals = ['cat','rat','dog',['a','b','c']]
# print(len(animals))
# animals[0]=animals[1]
# print(animals)

# list_1 = ['a','b','c']
# list_2 = [1,2,3]
# final_list = list_1 + list_2
# final_list_1 = list_1 * 2
# print(final_list)
# print(final_list_1)

# var1 = "a"
# print(var1)
# del(var1)
# print(var1)

# list_1 = ['a','b','c']
# del(list_1[0])
# print(list_1)

# user_data = []
# while True:
#     try:
#         input_1 = input("ENTER THE DATA/NAME : ")
#         user_data.append(input_1)
#     except KeyboardInterrupt:
#         print("->ERROR : KEYBOARD INTERRUPTED")
#         break
# print(f"YOUR LIST ARE : {user_data}")


# user_data = []
# while True:
#     try:
#         input_1 = input("ENTER THE DATA/NAME : ")
#         user_data.append(input_1)
#     except KeyboardInterrupt:
#         print("->ERROR : KEYBOARD INTERRUPTED")
#         break
# if user_data:
#     for j in range(1,len(user_data)):
#         print("YOUR ITEMS ARE :")
#         for i in user_data:
#             print(f"{j}:{i.title()}")
#             j = j + 1
# else:
#     print("YOUR LIST IS EMPTY")

# list_1 = ['a','b','c']
# print("a" in list_1)
# print("b" not in list_1)
# print("d" not in list_1)

# cat = ['fat','grey','loud']
# size,color,deposition = cat
# print(size)
# print(color)
# print(deposition)

# list_1 = ['a','b','c','d','e']
# for index,list in enumerate(list_1):
#     print(f"{index}:{list}")

# import random
# list_1 = ['a','b','c','d','e']
# print(random.choice(list_1))  # IT WILL CHOOSE RANDOM ITEMS FROM THE LIST

# import random
# list_1 = ['a','b','c','d','e']
# random.shuffle(list_1) # IT WILL SHUFFLE THE LIST 
# print(list_1) 

# list_1 = ['a','b','c','d','e']
# print(list_1.index("a"))
# print(list_1.index("e"))
# print(list_1.index("c"))

# list_1 = ['a','b','c','d','e']
# list_1.reverse()  # AGAR NONE AARAHA HAIN ISKA MATLAB JIS VARIABLE ME LIST_1.REVERSE STORE HAIN WO KHALI HAIN
# print(list_1)

# import random
# list_1 = ["YOU ARE A GOOD PERSON",
#           "YOU ARE SO HANDSOME",
#           "YOU ARE BEAUTIFUL",
#           "WHAT ARE YOU DOING",
#           "WELL SAID",
#           "OK WELL"
# ]
# print(list_1[random.randint(0,len(list_1)-1)])

# name = "anurag"
# print(name[2])
# print(name[2:])
# print("k" in name)
# print("a" in name)

# name = "anurag"
# for i in name:
#     print("*****"+i+"*****")

# var1 = ('anurag')
# var2 = ('anurag',)
# print(type(var1),type(var2))

# list_1 = ['a','b','c','d']
# print(list_1)
# print(tuple(list_1))
# tuple_1 = ("a","b","c","d","e")
# print(tuple_1)
# print(list(tuple_1))

# name = "Anurag"
# name_1 = str()        # WHEN WE RUN THIS CODE WE WILL SEE THAT REFERENCE ID OF NAME AND NAME_1 MEANS HERE IF WE MAKE CHANGE TO ANYONE BOTH WILL CHANGED
# name = name_1      
# print(id(name_1))
# print(id(name))

# import copy
# name = 'anurag'
# name_1 = copy.copy(name)
# print(name_1)
# name_1 += "k"
# print(name_1)
# print(name)

# # # # # # # # CHAPTER_5 # # # # # # # # #

# my_cat = {'size':'fat','color':'grey','disposition':'loud'}
# print(my_cat['size'])
# print(my_cat['color'])
# print(my_cat['disposition'])

# spam = {12345:'Hello',1:'Ok'}
# print(spam[12345])
# print(spam[1])

# birth_day = {'anurag':'16 april','bob':'9 december'}
# while True:
#     name_1 = input("ENTER YOUR NAME : ")
#     if name_1 == " ":
#         break
#     if name_1 in birth_day:
#         print(f"{name_1.upper()} YOUR BIRTHDAY IS ON {birth_day[name_1].upper()}")
#     else:
#         print(f"{name_1.upper()}, I DON'T KNOW YOUR BIRTHDATE ? COULD YOU HELP ME WITH IT !!")
#         birth_date_1 = input("ENTER YOUR BIRTHDATE : ")
#         birth_day[name_1]=birth_date_1
#         print("YOUR BIRTHDATE HAVE BEEN UPDATED \U0001F929 i.e ",end=" ")
#         print(birth_day)

# birth_day = {'anurag':'16 april','bob':'9 december'}
# # for i in birth_day:
# #     print(i)
# # for i in birth_day.keys():
# #     print(i)    
# # for i in birth_day.values():
# #     print(i)
# # for i in birth_day.items():
# #     print(i)
# #     print(type(i))
# #     print(list(i))
# for i,j in birth_day.items():
#     print(f"KEY:{i}\nVALUE:{j}")

# birth_day = {'anurag':'16 april','bob':'9 december'}
# print('anurag' in birth_day.keys())
# print('anurag' in birth_day)
# print('bob' in birth_day.keys())
# print('bob' in birth_day)
# print('16 april' in birth_day.values())
# print('9 december' in birth_day.values())
# print("manoj"in birth_day)

# birth_day = {'anurag':'16 april','bob':'9 december'}
# print(birth_day.get("anurag",17))
# print(birth_day.get("krsna","17 august"))
# print(f"MY NAME IS KRSNA AND BIRTHDATE IS {birth_day.get('krsna','17 august').upper()}")
# birth_day.get('krsna','17 august')
# print(birth_day)

# birth_day = {'anurag':'16 april','bob':'9 december'}
# if 'krsna' not in birth_day:
#     birth_day["krsna"]= '17 august'
#     print(birth_day["krsna"])
#     print(birth_day)
# # ALSO:
# birth_day = {'anurag':'16 april','bob':'9 december'}
# birth_day.setdefault('krsna','17 august')
# print(birth_day["krsna"])
# print(birth_day)

# import pprint
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count_char = {}
# for character in message:
#     count_char.setdefault(character,0)
#     count_char[character] = count_char[character] + 1
# print(count_char)
# pprint.pprint(count_char)
# # LINE 598 AND 600 MEANS SAME 
# print(pprint.pformat(count_char))

# #            # GUEST:  # KEYS:
# #                      # i: # j: 
# all_guest = {'manoj':{'apple':4,'banana':10},
#             'pinku':{'mango':7,'kiwi':9},
#             'anurag':{'alphonso':12,'kiwi':12}}
# def total_boughts(guest,keys):
#     num_bought = 
#     for i,j in guest.items():
#         num_bought = num_bought + j.get(keys,0)
#         # print(f"{i}:{j}")
#     return num_bought
# print(total_boughts(all_guest,"kiwi"))

# stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
# def display_inventory(inventory):
#     for i,j in inventory.items():
#         print(f"TOTAL NUMBER OF '{i.upper()}' IS : {j}")
# display_inventory(stuff)

# # # # # # # # CHAPTER_6 # # # # # # # # #

# # print('Hello, What's going!')
# print('Hello, What"s going!')
# # print("Hello, What"s going!")
# print("Hello, What's going!")
# print("Hello, What\"s going!")
# print('Hello, What\'s going!')

# print(r"Hello, What\"s going!")
# print(r'Hello, What\'s going!')
# print('''
#         Hello, How's there!
#         I think all fine...
#                             ''')

# '''HEY THERE's IT's JUST A COMMENT'''
# print('ARE YOU FINE !!')

# spam = "HELLO WORLD"
# fizz = spam[0:5]
# print(fizz)
# print(spam)

# print("hello" in "hello world")
# print("hello" not in "hello world")
# print("hell" in "hello world")
# print(" " in "hello world")

# print("HOW ARE YOU ? : ")
# input_1 = input().upper()
# if input_1 == "GREAT":
#     print("GOOD !!")
# else:
#     print("HOPE! YOU HAVE A GREAT  DAY")

# var_1 = "Hello World"
# var_2 = "HELLO WORLD"
# var_3 = "hello world"
# print(var_1.isupper())
# print(var_1.islower())
# print(var_2.isupper())
# print(var_2.islower())
# print(var_3.isupper())
# print(var_3.islower())
# print(var_1.upper().isupper())
# print(var_1.lower().islower())

# print("hello".isalnum())
# print("Hello123".isalnum())
# print("123".isalnum())
# print(" ".isalnum())
# print("123".isalpha())
# print("123Pareek".isalpha())
# print("Pareek".isalpha())
# print("123Pareek".isdecimal())
# print("123".isdecimal())
# print("123Pareek".isspace())
# print("123Pareek".isspace())
# print("".isspace())
# print(" pareek".isspace())
# print(" ".isspace())
# print("\n".isspace())
# print("\t".isspace())
# print("Anurag".istitle())
# print("Anurag123".istitle())
# print("anurag".istitle())

# while True:
#     user_name = input("ENTER YOUR USER NAME : ")
#     age = input("ENTER YOUR AGE : ")
#     if user_name.isalnum() and age.isdecimal():
#         break
#     else:
#         continue

# print("Hello_World".startswith("H"))
# print("Hello_World".startswith("e"))
# print("Hello_World".endswith("l"))
# print("Hello_World".endswith("d"))

# print(" ".join(["My","name","is","Semon."]))
# print("ABC".join(["My","name","is","Semon."])) # JOIN KE ANDAR JO BHI DALENGE USS SE LIST JOIN JO JAEGI
# print(("My name is Semon").split())
# print(("My name is Semon").split("m"))  # SPLIT KE ANDAR JO BHI DALENGE WHA SE WO SPLIT HO JAEGA

# spam = '''Dear Alice,
# How have you been? I am fine.
# There is a container in the fridge
# that is labeled "Milk Experiment."
# Please do not drink it.
# Sincerely,
# Bob'''
# print(spam)
# print(spam.split("\n"))

# print("hello_WORLD".partition("W"))
# print("hello_WORLD".partition("_"))

# print("HELLO WORLD".rjust(10))
# print("HELLO WORLD".rjust(20))
# print("HELLO WORLD".ljust(20))
# print("HELLO WORLD".center(100))

# print("HELLO WORLD".rjust(20,"*"))
# print("HELLO WORLD".ljust(20,"-"))
# print("HELLO WORLD".center(50,"$"))

# picnic_dict = {'Apples':4,'Banana':10,'grapes':20,'Kiwi':12}
# def table(dict_items,leftwidth,rightwidth):
#     print("PICNIC ITEMS".center(leftwidth+rightwidth,"-"))
#     for k,v in picnic_dict.items():
#         print(k.ljust(leftwidth,".") + str(v).rjust(rightwidth))
# table(picnic_dict,40,0)
# table(picnic_dict,50,10)

# spam = "........HELLO OTHER WORLD.........."
# spam_1 = "         HELLO WORLD"
# spam_2 = spam_1.lstrip()
# spam_3 = spam.strip(".")
# print(spam_1)
# print(spam_2)
# print(spam)
# print(spam_3)
# spam_4 = 'SpamSpamBaconSpamEggsSpamSpam'
# print(spam_4.strip("Sapm"))
# print(spam_4.strip("Spam"))
# print(spam_4.strip("Smap"))

# print(ord("a"))
# print(ord("b"))
# print(ord("c"))
# print(ord("t"))
# print(ord("0"))
# print(ord("9"))
# print(ord("p"))

# print(chr(90))
# print(chr(88))
# print(chr(9))
# print(chr(55))

# print(chr(ord("b")))
# print(chr(ord("b")+1))

# import pyperclip
# print(pyperclip.paste()) # COMPUTER KE CLIPBOARD ME JO BHI CHIJ COPIED HAIN WO PASTE HO JAEGI
# pyperclip.copy("HELLO THERE")
# print(pyperclip.paste())

# var = ['anurag','pareek']
# var1 = var
# var1.append('KRSNA')
# print(var)
# print(var1)
# print(id(var))
# print(id(var1))
# # BUT
# char = 'hello'
# char1 = char
# char1 = char1+"krsna"
# print(char)
# print(char1)
# print(id(char))
# print(id(char1))
# # BUT WE CAN DO THIS:
# import copy
# var = ['anurag','pareek']
# var1 = copy.copy(var)
# var1.append('KRSNA')
# print(var)
# print(var1)
# print(id(var))
# print(id(var1))

# def func_1(list_1):
#     if list_1:
#         print("THE ITEMS IN YOUR GIVEN LIST ARE : ")
#         for items in list_1[0:len(list_1)-1]:
#             print(f" {items}",end=",")
#         print(f" and {list_1[-1]}.")
#     else:
#         print("YOUR LIST IS EMPTY.\n")
# spam_empty = []
# spam = ['apples', 'bananas', 'tofu', 'cats']
# func_1(spam_empty)
# func_1(spam)

# import random
# def gen_random_number(list_1):
#     head_tail_list = []
#     for turns in range(10000):
#         head_and_tail = random.randint(0,1)
#         if head_and_tail == 0:
#             value = "H"
#         else:
#             value = "T"
#         list_1.append(value)
#     return(list_1)
# def check_streak(list_1):
#     streak = 0
#     number_of_streak = 0
#     for i in range(len(list_1)):
#         if list_1[i]==list_1[i-1]:
#             streak += 1
#         else:
#             streak = 0
#         if streak == 6:
#             number_of_streak += 1
#     print(number_of_streak)
#     percentage_of_streak = (number_of_streak/10000)*100
#     print(f"THE PERCENTAGE OF THE STREAK OF 6 HEADS OR 6 TAILS IN 10000 ATTEMPS ARE : {percentage_of_streak}")
# empty_list = []
# gen_random_number(empty_list)
# check_streak(empty_list)

# type_message = input("TYPE THE ENGLISH MESSAGE TO TRANSLATE IT TO PIG LATIN : ")
# vowels = ('a','e','i','o','u','y')
# pig_latin = [] # A LIST OF WORD IN PIG LATIN
# for word in type_message.split():
#     suffix_non_letters = ''  # PICHHE WALA SUFFIX # REMOVE ANY NON LETTERS FROM THE END OF WORD AND STORE IT THERE SO WE WILL NOT GET ANY ERROR
#     prefix_non_letters = ''  # AAGE WALA PREFIX # REMOVE ANY NON LETTERS FROM THE BEGINNING OF WORD AND STORE IT THERE SO WE WILL NOT GET ANY ERROR
#     while len(word)>0 and not word[0].isalpha():
#         prefix_non_letters += word[0]
#         word = word[1:]
#     if len(word) == 0:
#         pig_latin.append(prefix_non_letters)
#         continue
#     while not word[-1].isalpha():
#         suffix_non_letters += word[-1]
#         word = word[:-1] # IF WORD HAVE ANY NON LETTER AT THE END THEN WE REMOVE IT 
#     word_upper = word.isupper()
#     word_title = word.istitle()
#     # WE MAKE THE WORD LOWERCASE FOR TRANSLATION:
#     word = word.lower()
#     # SEPERATE CONSONANT AT THE START OF THE WORD:
#     prefix_consonant = ''
#     while len(word)>0 and not word[0] in vowels:
#         prefix_consonant += word[0]
#         word = word[1:]
#     # ADD THE PIGLATIN ENDING TO THE WORD:
#     if prefix_consonant != '':
#         word = prefix_consonant + "ay"
#     else:
#         word = word + "yay"
#     # SET THE WORD BACK TO UPPERCASE OR TITLECASE:
#     if word_upper:
#         word = word.upper()
#     if word_title:
#         word = word.title()
#     # ADD THE NON LETTER BACK TO THE START OR END OF THE WORD:
#     pig_latin.append(prefix_non_letters+word+suffix_non_letters)
# # JOIN ALL THE WORDS TOGETHER INTO SINGLE STRING:
# print(" ".join(word))
