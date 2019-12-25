import pyperclip
import sys
def printingNumbers(num):
    try:
        print(int(num))
    except ValueError:
        print("Can't print text")



pyperclip.copy("Hello world")
print(pyperclip.paste())
print('He', end='')
print('man')
printingNumbers("t")
