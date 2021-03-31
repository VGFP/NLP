import re

r = "(hi|hello|hey)[ ]*([a-z]*)"
'''
t1 = re.match(r, 'Hello User', flags=re.IGNORECASE)
t2 = re.match(r, "hi ho, hi ho, it's off to work ...", flags=re.IGNORECASE)
t3 = re.match(r, "hey, what's up", flags=re.IGNORECASE)
print(t1,t2,t3)
'''
# 

r = r"[^a-z]*([y]o|[h']?ello|ok|hey|(good[ ])?(morn[gin']{0,3}|" r"afternoon|even[gin']{0,3}))[\s,;:]{1,3}([a-z]{1,20})"
re_greeting = re.compile(r, flags=re.IGNORECASE)

t1 = re_greeting.match('Hello User')
t2 = re_greeting.match("Good morning User")
# Regular expression can not recognize typos
t3 = re_greeting.match("Good Manning User")
# print(t1,t1.groups(),t2,t2.groups(),t3)

names = set(['user', 'chatty', 'chatbot', 'bot', 'chatterbot'])
curt_names = set(['hal', 'you', 'u'])
greeter_name = 'Filip'
match = re_greeting.match(input(">>> "))

if match:
    at_name = match.groups()[-1]
    if at_name in curt_names:
        print("Good one.")
    elif at_name.lower() in names:
        print("Hi {}, How are you?".format(greeter_name))
    else:
        print("No match :(")
