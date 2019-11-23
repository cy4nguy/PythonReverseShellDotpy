#!/usr/bin/python3

from colorama import Fore, Back, Style
from colorama import init



##################################################
# THIS is custome Lib made for beautifying Files #
##################################################


init()

class text(object):
    def __init__(self, string):
        self.string = string
    def Color(strs):
        Word = []

        for L in strs.string :
            
            if (L.isdigit() ) or ( L is "." ) or (L is ":"):
                Word.append(Fore.YELLOW+str(L)+Style.RESET_ALL)
            elif (L is "[") or (L is "]"):
                Word.append(Fore.RED+str(L)+Style.RESET_ALL)
            elif (L is "*") or (L is ">") :
                Word.append(Fore.GREEN+str(L)+Style.RESET_ALL)
            elif(L is "@") :
                Word.append(Fore.BLUE+str(L)+Style.RESET_ALL)
            else: Word.append(L)
                     
        
        return "".join(str(L) for L in Word)

    def Art(strs):
        Word = []

        for L in strs.string:

            if(L is "."):
                Word.append(Style.DIM+Fore.YELLOW+str(L)+Style.RESET_ALL)
            elif(L is "|") or (L is "/") or (L is "\\") or (L is "-") or (L is "_"):
                Word.append(Style.BRIGHT+Fore.GREEN+str(L)+Style.RESET_ALL)
            elif(L is "^") or (L is ")") or (L is "!") or (L is '"') or (L is "("):
                Word.append(Style.BRIGHT+Fore.GREEN+str(L)+Style.RESET_ALL)
            elif(L is ":") or (L is "+"):
                Word.append(Fore.CYAN+str(L)+Style.RESET_ALL)
            else: Word.append(L)

        return "".join(str(L) for L in Word)
