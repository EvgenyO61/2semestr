#Составить функцию, которая напечатает сорок любых символов.

import random

def GetRandomString(length):
    Symbols = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+-№;%:?[];',./{}:<>|"
    Output = ""

    for i in range(length):
        Output = Output + Symbols[random.randint(0,len(Symbols)-1)]
    return Output

print(GetRandomString(40))
