# # # # # # # # # # # # # # # # # # # CHAPTER_7 # # # # # # # # # # # # # # # #

# def is_american_number(number):
#     if len(number) != 12:
#         return False
#     for i in range(0,3):
#         if not number[i].isdecimal():
#             return False
#     if number[3] != "-":                # WITHOUT USING REGULAR EXPRESSIONS
#         return False
#     for i in range(4,7):
#         if not number[i].isdecimal():
#             return False
#     if number[7] != "-":
#         return False
#     for i in range(8,12):
#         if not number[i].isdecimal():
#             return False
#     return True
# # print(is_american_number("123-456-7890"))
# # print(is_american_number("123-4567890"))
# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     number_1 = message[i:i+12]
#     if is_american_number(number_1):
#         print("NUMBERS IN THE TEXT ARE : ",number_1)

# import re
# is_american_number = re.compile(r"\d{3}-\d{3}-\d{4}")#ALSO:is_american_number = re.compile(r"\d\d\d-\d\d\d\-\d\d\d\d")
# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'                  # BY USING REGULAR EXPRESSIONS
# search = is_american_number.search(message)
# print("YOU NUMBER IS : ",search.group())

# import re
# is_american_number = re.compile(r"(\d{3})-(\d{3}-\d{4})")#ALSO:is_american_number = re.compile(r"\d\d\d-\d\d\d\-\d\d\d\d")
# message = 'Call me at 415-555-1011 tomorrow.'
# search = is_american_number.search(message)
# print("YOU AREA CODE IS : ",search.group(1))
# print("YOU NUMBER IS : ",search.group())

# import re
# is_american_number = re.compile(r"(\d{3})-(\d{3}-\d{4})")#ALSO:is_american_number = re.compile(r"\d\d\d-\d\d\d\-\d\d\d\d")
# message = 'Call me at 415-555-1011 tomorrow.'
# search = is_american_number.search(message)
# # print("YOU AREA CODE IS : ",search.group(1))
# # print("YOU NUMBER IS : ",search.group())
# # print("YOU GROUPS ARE : ",search.groups())
# area_code, rest_numbers = search.groups()
# print(area_code)
# print(rest_numbers)

# import re
# message = 'Call me at (415) 555-1011 tomorrow.'
# is_number = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
# spam = is_number.search(message)
# print("YOUR AREA CODE IS :"+spam.group(1))
# print("YOUR PHONE NUMBER IS :"+spam.group())

# import re
# find_name = re.compile(r"ANURAG|PAREEK")
# message = "ANURAG IS HIS NAME AND HIS SURNAME IS PAREEK"
# spam = find_name.search(message)
# print(spam.group())

# import re
# find_this = re.compile(r"bat(man|mobile|fat|dog)") # ISKA MATLAB SENTENCE ME AGAR BATMAN, BATMOBILE, BATCAT, BATDOG ME SE KUCH BHI HUA TO RETURN HOGA JO HUMNE BOLA HAIN
# message = "batman lost a wheel"
# spam = find_this.search(message)
# print(spam.group())
# print(spam.group(1))

# import re
# bat_regex = re.compile(r"BAT(WO)?MAN")
# message = "HE IS BATMAN"
# message_1 = "SHE IS BATWOMAN"
# print(bat_regex.search(message).group())
# print(bat_regex.search(message_1).group())

# import re
# number_regex = re.compile(r"(\(\d\d\d\))?\d\d\d-\d\d\d\d")
# message = "MY PHONE NUMBER IS (031)655-2234"
# message_1 = "MY PHONE NUMBER IS 895-2233"
# print(number_regex.search(message).group())
# print(number_regex.search(message_1).group())

# import re
# bat_regex = re.compile(r"BAT(WO)*MAN")
# message = "HE IS BATMAN"
# message_1 = "HE IS BATWOMAN"
# message_2 = "HE IS BATWOWOWOWOWOMAN"
# print(bat_regex.search(message).group())
# print(bat_regex.search(message_1).group())
# print(bat_regex.search(message_2).group())

# import re
# bat_regex = re.compile(r"BAT(WO)+MAN")
# # message = "HE IS BATMAN"
# message_1 = "HE IS BATWOMAN"
# message_2 = "HE IS BATWOWOWOWOWOMAN"   # HERE IF WE WANT TO PRINT BATMAN IT WILL NOT
# # print(bat_regex.search(message).group())
# print(bat_regex.search(message_1).group())
# print(bat_regex.search(message_2).group())

# import re
# # ha_regex = re.compile(r"(ha){3}")
# # ha_regex_1 = re.compile(r"(ha){3,}")
# ha_regex_2 = re.compile(r"(ha){3,6}")
# message  = "hahahahahahahaha"
# print(ha_regex_2.search(message).group()) 

# import re
# message = "ha"
# ha_regex = re.compile(r"(ha){3}")
# do = ha_regex.search(message)
# print(do == None)

# print("HELLO","ANURAG","KRSNA")
# print("HELLO","ANURAG","KRSNA",sep=",")
# print("HELLO","ANURAG","KRSNA",end=",")
# print()

# import re
# message = 'Call me at 415-555-1011 tomorrow.You can call me at 555-874-9823 also.'
# number_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# print(number_regex.findall(message))

# import re
# message = 'Call me at 415-555-1011 tomorrow.You can call me at 555-874-9823 also.'
# number_regex = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d\d)")
# print(number_regex.findall(message))

# import re
# message = "I am anurag and the length of word is 6 while lenght of my surname is also 6, maybe 7,8,9"
# message_1 = "I am annurag and the length of word is 7 while lenght of my surname is also 7, maybe 6,8,9."
# message_2 = "I am annurag and the length of word is 8 while lenght of my surname is also 8, maybe 6,7,9."
# message_3 = "I am annurag and the length of word is 9 while lenght of my surname is also 9, maybe 6,7,8."
# # number_regex = re.compile(r'6|7|8|9')
# number_regex_alt = re.compile(r"[6-9]")
# # print(number_regex.search(message).group())
# # print(number_regex.search(message_1).group())
# # print(number_regex.search(message_2).group())
# # print(number_regex.search(message_3).group())
# print(number_regex_alt.search(message).group())
# print(number_regex_alt.search(message_1).group())
# print(number_regex_alt.search(message_2).group())
# print(number_regex_alt.search(message_3).group())

# import re
# message ='12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'
# regex_1 = re.compile(r"\d+\s+\w+")
# print(regex_1.findall(message))

# import re
# message = 'RoboCop eats baby food. BABY FOOD.'
# vowels_regex = re.compile(r"[aeiouAEIOU]")
# consonent_regex = re.compile(r"[^aeiouAEIOU]")
# print(vowels_regex.findall(message))
# print(consonent_regex.findall(message))

# import re
# message_1 = "Hello, there"
# message_2 = "It's Ok"
# message_3 = "1028323232"
# message_4 = "123981 MONEY"
# regex_1 = re.compile(r"^Hello")
# regex_2 = re.compile(r"Ok$")
# regex_3 = re.compile(r"^\d+$")
# regex_4 = re.compile(r"^\d+\s+\w+$")
# print(regex_1.findall(message_1))
# print(regex_2.findall(message_2))
# print(regex_3.findall(message_3))
# print(regex_4.findall(message_4))

# import re
# message = 'The cat in the hat sat on the flat mat.'
# regex = re.compile(r".at")
# print(regex.findall(message))

# import re
# message = 'First Name: Al Last Name: Sweigart'
# regex = re.compile(r"First Name:(.*) Last Name:(.*)")
# # print(regex.findall(message))
# print(regex.search(message).group())
# print(regex.search(message).group(1))
# print(regex.search(message).group(2))

# import re
# message = '<To serve man> for dinner.>'
# spam = re.compile(r"<.*?>")                       # NON GREEDY
# # print(spam.findall(message))      
# print(spam.search(message).group())

# import re
# message = '<To serve man> for dinner.>'
# spam = re.compile(r"<.*>")                        # GREEDY
# # print(spam.findall(message))
# print(spam.search(message).group())

# import re
# message = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
# regex_1 = re.compile(r".*")
# regex_2 = re.compile(r".*",re.DOTALL)
# print(regex_1.search(message).group())
# print(regex_2.search(message).group())

# import re
# message = "Hello how are you. I think you are fine"
# regex_1 = re.compile(r"Hello")
# # regex_2 = re.compile(r"HELLO") # IT WILL GIVE ERROR, REASON: CASE SENSITIVITY
# regex_3 = re.compile(r"HELLO",re.I)  # IT WILL NOT GIVE ERROR (ALSO WE CAN WRITE: re.IGNORECASE)
# print(regex_1.search(message).group()) 
# # print(regex_2.search(message).group()) 
# print(regex_3.search(message).group()) 

# import re
# message = "Agent Alice gave the secret documents to Agent Bob."
# regex_1 = re.compile(r"Agent \w+")
# spam = regex_1.sub("CENSORED",message)
# print(spam)

# import re
# message = "Agent Alice gave the secret documents to Agent Bob."
# regex_1 = re.compile(r"Agent (\w)\w*")
# spam = regex_1.sub(r'\1****',message)
# print(spam)

# import re
# message = "Agent Alice gave the secret documents to Agent Bob."
# regex_1 = re.compile(r"Agent (\w)(\w)\w*")
# spam = regex_1.sub(r'\2****',message)
# print(spam)

# import re
# phoneRegex = re.compile(r'''(
#                             (\d{3}|\(\d{3}\))? # area code
#                             (\s|-|\.)? # separator
#                             \d{3} # first 3 digits
#                             (\s|-|\.) # separator
#                             \d{4} # last 4 digits                                   # WE CAN MAKE OUR REGULAR EXPRESSION LIKE THIS TO MAKE IT EASILY READBLE
#                             Pattern Matching with Regular Expressions 179
#                             (\s*(ext|x|ext.)\s*\d{2,5})? # extension
#                             )''', re.VERBOSE)
# phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')   # THIS REGULAR EXPRESSION IS NOT EASILY READABLE

# # # # # # # # # # # # # # # # # # # CHAPTER_8 # # # # # # # # # # # # # # # #

# import sys
# while True:
#     try:
#         your_age = int(input("Enter your age : "))
#     except KeyboardInterrupt:
#         sys.exit()
#     except:
#         print("Please enter an integer type.")
#         continue
#     else:
#         if your_age >= 1:
#             print(f"Your age is {your_age}.")
#             break
#         else:
#             print("Age cannot be in negative value.")
#             continue




# import pyinputplus as pyip
# response1 = pyip.inputNum("Enter a number : ")
# response2 = pyip.inputInt("Enter a number : ")
# response3 = pyip.inputFloat("Enter a number : ")
# print(response1)
# print(response2)
# print(response3)




# import pyinputplus as pyip
# print(type(response))
# response = pyip.inputNum(prompt = "Enter a number : ")
# response = pyip.inputNum("Enter a number : ",max = 10)
# response = pyip.inputNum("Enter a number : ",min = 6)
# response = pyip.inputNum("Enter a number : ",max = 10,min = 6)
# response = pyip.inputNum("Enter a number : ",min = 40,max = 50)
# response = pyip.inputNum("Enter a number : ",greaterThan = 10)
# response = pyip.inputNum("Enter a number : ",lessThan = 6)
# response = pyip.inputNum("Enter a number : ",greaterThan = 10,lessThan = 15)
# response = pyip.inputNum("Enter a integer : ",lessThan = 10,greaterThan = 6)
# response = pyip.inputInt("Enter a number : ",min = 40,max = 50)
# response = pyip.inputFloat("Enter a number : ",min = 40,max = 50)
# help(pyip.inputInt)



# import pyinputplus as pyip
# # input_1 = pyip.inputNum("Enter a number : ",blank = True)
# input_2 = pyip.inputNum("Enter a number : ",limit = 3,timeout = 5)
# # input_3 = pyip.inputNum("Enter a number : ", limit = 3,timeout =5,default = "Arguments condition fails !!!")
# # print(input_3)



# import pyinputplus as pyip
# # input_1 = pyip.inputInt("Enter the number(also in roman number) : ",allowRegexes = [r'(I|V|X|L|C|D|M)+',r'zero',r'(i|v|x|l|c|d|m)+'])
# # print(input_1)
# input_2 = pyip.inputInt("Enter the number(won't accept even number) : ",blockRegexes = [r'[02468]$'])
# print(input_2) 



# import pyinputplus as pyip 
# def add_up_to_ten(numbers):
#     number_list = list(numbers)
#     for i,digit in enumerate(number_list):
#         number_list[i] = int(digit)
#     if sum(number_list) != 10:
#         raise Exception(f"The digit must add up to 10, not {sum(number_list)}")
#     return(int(numbers))
# response = pyip.inputCustom(add_up_to_ten)
# print(f"The {response} is add up to 10 ----> {str(response)[0]}+{str(response)[1]}+{str(response)[2]} = 10")



# import pyinputplus as pyip 
# from AddUptoten import add_up_to_ten
# response = pyip.inputCustom(add_up_to_ten)
# print(f"The {response} is add up to 10 ----> {str(response)[0]}+{str(response)[1]}+{str(response)[2]} = 10")



# # # # # # # # # # # # # # # # # # # CHAPTER_9 # # # # # # # # # # # # # # # #



