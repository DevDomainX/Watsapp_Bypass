#!/usr/bin/env python3
from colorama import Fore, Style, Back
from time import sleep
from random import randint

print(Style.BRIGHT+Fore.YELLOW+"""
Autor: H. Saldias

Lenguaje: python3 

Script: whatsapp bypass code verify          

practica de programacion \n\n
""")
      
print("""
       ##################################   
       ||  BYPASS WHATSAPP CODE VERIFY ||
       ##################################
\n\n""")
password = input("Insert pasword: ")
if password == "User123":
        code = randint(123456, 999999)
        number = input("\n\nInsert number (+569): ")
        if number == number:
            sleep(5)
            print(f"[?] Target: {number}")
            sleep(5)
            print(f"[#] Scanning: {number}")
            sleep(5)
            print(f"[#] Exploiting to: {number}")
            sleep(5)
            print(f"[#] Bypass Verify Whatsapp")
            sleep(5)
            print(Style.BRIGHT+Fore.GREEN+f"[!] Success Bypass")
            sleep(5)
            print(Style.BRIGHT+Fore.YELLOW+f"[#] Get Verify Code")
            sleep(5)
            print(Style.BRIGHT+Fore.GREEN+"Verify Code: "+" " +str(code))
        else:
            print("EL numero es incorrecto, intente nuevamente")
else:
    print("password not found")
    print("Intente contactar al creador\n")
    print("created by: 1LugarParaProgramar")



