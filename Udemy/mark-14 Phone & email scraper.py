import pyperclip
import re

#Todo 1: regex criteria for phone number
phonerg = re.compile(r'''(
(\+\d\d | \d\d | \(\d\d\))? #country code (optional) [+62 | 62 | (62)]
(\s|-)      #separator [spasi or - ]
(\d\d\d)    #operator code (mandatory)
(\s|-)      #separator
(\d\d\d | \d\d\d\d | \d\d\d\d\d\d)  #areal code
(\s|-)      #separator
(\d\d\d) | (\d\d\d\d)    #unique code
)''', re.VERBOSE)


#Todo 2: regex criteria for email
emailrg = re.compile(r'''
[a-zA-Z0-9_.+-]+ #text / name
@                #symbol
[a-zA-Z0-9_.+-]+  #domain
''', re.VERBOSE)

#Todo 3 : Get the data from the copied clipboard
phone_data = pyperclip.paste()  #source: https://bit.ly/3drDEHp
email_data = pyperclip.paste()


#Todo 4: Extract the data from provided data
phone_find = phonerg.findall(phone_data)
email_find = emailrg.findall(email_data)


#Todo 5: Copy & extracted the value into the clipboard
print(phone_find)
#picking the first value and arrange it to arranged result
phone_result = []
for i in phone_find:
    phone_result.append(i[0])
print(f'phone number results are {phone_result}')
print("\n".join(phone_result))

print("\n".join(email_find))