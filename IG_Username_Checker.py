'''
Instagram: @a7.acc
Telegram : @A7_acc
Tele Channel : https://t.me/A7_courses


WARNING!

This tool is completely FREE and out of charge, it's not allowed to sell in anyway, please consider so.

'''
# Importing modules         // need installing >> only termcolor
import requests, secrets, sys, threading, time, schedule
from random import choice,randint
from termcolor import colored
from os import system
from time import sleep


# Defining the colors
g = lambda x : colored(x,'green')
r = lambda x : colored(x,'red')
b = lambda x : colored(x,'blue')
y = lambda x : colored(x,'yellow')
c = lambda x : colored(x,'cyan')
m = lambda x : colored(x,'magenta')

clear = lambda: system("cls")
clear()
exl = '['+r('!')+']'
ques = '['+m('?')+']'
ha  ='['+g('#')+']'
mult = '['+c('*')+']'
system('title WELCOME TO IG UserChecker !')


#                     Function to send info via Telegram and write it in the file
def send_info(info):
    try:
        if telegram:
            with open('tele.txt','r') as fa:
                tokid = fa.read().split('/')
                requests.post(f'https://api.telegram.org/bot{tokid[0]}/sendMessage?chat_id={tokid[1]}&text={info}')
    except:
        pass
    with open('Available.txt','a') as hackyro:
        hackyro.write(info+'\n')


#                      function that generates random strings
def ra(length,ty):
    if ty == 'a0':#   Small letters only with numbers
        randoms = ''.join('qwertyuiopasdfghjklzxcvbnm1234567890')
    elif ty == 'A0':# Capital letters only with numbers
        randoms = ''.join('QWERTYUIOPASDFGHJKLZXCVBNM1234567890')
    elif ty == 'Az':# Capital and small letters only
        randoms = ''.join('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')
    elif ty == 'All':#Capital and small letters and numbers
        randoms = ''.join('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890')
    elif ty == 'a':#  Small letters only
        randoms = ''.join('qwertyuiopasdfghjklzxcvbnm')
    elif ty == 'n':#  Numbers only
        randoms = ''.join('1234567890')
    random_str = ''
    for _ in range(int(length)):
        random_str += choice(randoms)
    return random_str


#                          function that generates random user agent
def generate_user_agent():
    useragents = [
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2828.31 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2643.44 Safari/537.36'
        'Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
        'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'
        'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Trident/4.0)'
        'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2965.63 Safari/537.36'
        'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2862.69 Safari/537.36'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0'
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2950.18 Safari/537.36'
        'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; WOW64; Trident/6.0)'
        'Mozilla/5.0 (X11; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0'
        'Mozilla/5.0 (Windows NT 5.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
        'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2690.91 Safari/537.36'
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; WOW64; Trident/5.0)'
        'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2777.66 Safari/537.36'
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2898.2 Safari/537.36'
        'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2801.53 Safari/537.36'
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0)'
    ]
    return choice(useragents)



avail = 0
bad = 0
checked = 0

#                      the checking function which will be the threads target
def check_username():
    global usernames,bad,avail,checked
    while True:
        if len(usernames) == 0:
            return
        us = choice(usernames)
        usernames.remove(us)
        available = False
        def even():
            return choice(['0','2','4','6','8'])
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers_login = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': str(randint(200,300)),               #    random content length
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': secrets.token_hex(8)*2,                      #    random cookies
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': generate_user_agent(),                   #    random user agent
            'x-csrftoken': 'missing',
            'x-ig-app-id': '936619743392459',                      #    It tells instagram that we are logging from a PC 
            'x-ig-www-claim': '0',
            'x-instagram-ajax':ra(4,'a0')+ra(6,'a')+even()+even(), #   random instagram ajax
            'x-requested-with': 'XMLHttpRequest'
            }

        data = {
            'username':f'{us}',
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:oerok4okowr',
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }
        
        while True:              # This gonna keep looping till it get a good response
            try:
                rr = requests.post(url,headers=headers_login,data=data,timeout=5,proxies=choice(proxies))
                if 'Please wait a few minutes before you try again' in rr.text:        #  ERROR FROM THE PROXY/IP
                    pass
                elif '"error_type":"ip_block"' in rr.text:                             #  ERROR FROM THE PROXY/IP
                    pass
                elif '"user":false,' in rr.text:                                       # Unavailable username
                    available = True
                    avail += 1
                    checked += 1
                    print(' '+ha+' '+g(us))
                    system(f'title CHECKED:{str(avail+bad)}/{str(len(usernames))}    AVAILABLE:{str(avail)}    BAD:{str(bad)}    THREADS:{str(threading.active_count()-1)}')
                    break             
                elif '"user":true,' in rr.text:                                        # Available username
                    bad += 1
                    checked += 1
                    print(' '+exl+' '+r(us))
                    system(f'title CHECKED:{str(avail+bad)}/{str(len(usernames))}    AVAILABLE:{str(avail)}    BAD:{str(bad)}    THREADS:{str(threading.active_count()-1)}')
                    break
            except:
                pass

        inf = f'''
---- Available Instagram Username ----
Username : {us}
Time     : {time.asctime()}
--------------------------------------
'''
        if available:
            send_info(inf)


#                      function that makes random 5l usernames
def make_usernames():
    global usernames
    usernames = set()
    while True:
        try:
            amount = int(input(ques+' How many usernames do you wanna create?? >> '))
            break
        except:
            pass
    letters = [x for x in '1234567890poiuytrewqasdfghjklmnbvcxz_.']
    for _ in range(amount):
        username = ''
        for _ in range(5):
            username += choice(letters)

        if not username.startswith('.') and not username.isdigit() and '..' not in username and not username.endswith('.'):
            if '.' in username or '_' in username:
                for i in username:
                    if username.count(i) >= 2:
                        usernames.add(username)
    with open('usernames.txt', 'w',encoding='utf-8') as us:
        for u in usernames:
            us.write(u+'\n')
    usernames = list(usernames)
    print(mult+' Made '+c(str(len(usernames)))+' usernames and saved them in '+c('usernames.txt'))



#                 THE MAIN FUNC
def main():
    global thredd,telegram, proxies
    print(colored('''
 ▪   ▄▄ •     ▄• ▄▌.▄▄ · ▄▄▄ .▄▄▄   ▄▄·  ▄ .▄▄▄▄ . ▄▄· ▄ •▄ ▄▄▄ .▄▄▄  
 ██ ▐█ ▀ ▪    █▪██▌▐█ ▀. ▀▄.▀·▀▄ █·▐█ ▌▪██▪▐█▀▄.▀·▐█ ▌▪█▌▄▌▪▀▄.▀·▀▄ █·
 ▐█·▄█ ▀█▄    █▌▐█▌▄▀▀▀█▄▐▀▀▪▄▐▀▀▄ ██ ▄▄██▀▐█▐▀▀▪▄██ ▄▄▐▀▀▄·▐▀▀▪▄▐▀▀▄ 
 ▐█▌▐█▄▪▐█    ▐█▄█▌▐█▄▪▐█▐█▄▄▌▐█•█▌▐███▌██▌▐▀▐█▄▄▌▐███▌▐█.█▌▐█▄▄▌▐█•█▌
 ▀▀▀·▀▀▀▀      ▀▀▀  ▀▀▀▀  ▀▀▀ .▀  ▀·▀▀▀ ▀▀▀ · ▀▀▀ ·▀▀▀ ·▀  ▀ ▀▀▀ .▀  ▀
                                        CopyRight: @a7.acc''','green'))
    print(mult+' This tool creates 5 letters usernames with special character like . or _ or repeated letter in it.\n\n')
    
    make_usernames()
    print('\n')
    proxfile = input(ques+' Enter proxies file name >> ')
    if not proxfile.endswith('.txt'):
        proxfile = proxfile+'.txt'
    try:
        proxies = open(proxfile,'r').read().splitlines()
    except Exception as exx:
        print(exl+' Error while openning proxies file >> '+y(str(exx)))
        sleep(4)
        sys.exit()
    prox_type = input(f"Enter the proxies type you want to scrape:\n[{c('1')}] HTTP/S\n[{c('2')}] SOCKS4\n[{c('3')}] SOCKS5\n >> ")
    proxiesy = [x for x in proxies]
    proxies = []
    if prox_type == '1':
        for proxy in proxiesy:
            proxies.append({
                'http':f'https://{proxy}',
                'https':f'http://{proxy}'
            })
    elif prox_type == '2':
        for proxy in proxiesy:
            proxies.append({
                'http':f'socks4://{proxy}',
                'https':f'socks4://{proxy}'
            })
    elif prox_type == '3':
        for proxy in proxiesy:
            proxies.append({
                'http':f'socks5://{proxy}',
                'https':f'socks5://{proxy}'
            })
    thredd = int(input('\n'+ques+' Enter how many threads do you want (recommended 100) >> '))
    print('\n'+mult+f' Enter your telegram bot information in this format {c("token/id")} in {b("tele.txt")} file.')
    print(mult+f' You may NOT recieve the hacked accounts on Telegram.. Anyhow, all the accounts will be in '+c('Hacked.txt '))
    telegram = input(ques+' Do you want to get hacked accounts also on telegram? (Y/n) >> ').lower()
    if telegram == 'y':
        telegram = True
    else:
        telegram = False
    
    print(f'\n[{g("#")}] All availble usernames will be saved in {c("Available.txt")} file or sent via Telegram.')
    print(ha+' Start checking ... ')
    sleep(1)                        

main()


#                  The threads function
def start_threads():
    for _ in range(thredd):
        try:
            thread1 = threading.Thread(target=check_username)
            thread1.start()
        except:
            pass

start_threads()

soppy = True
def CheckThreads():
    global soppy
    if threading.active_count() == 1:
        soppy = False

schedule.every().second.do(CheckThreads)

while soppy:
    schedule.run_pending()
    time.sleep(1)


#
#                If the program done soppy will be False and will execute the code down here 
#
if not soppy:
    if telegram:
        inf = '---------- DONE CHECKING ----------'
        print(f'\n----- Results -----\n CHECKED {c(str(checked)+"/"+str(len(usernames)))} \n AVAILABLE {g(str(avail))} \n BAD {r(str(bad))}\n-------------------')
        with open('tele.txt','r') as fa:
            tokid = fa.read().split('/')
            requests.post(f'https://api.telegram.org/bot{tokid[0]}/sendMessage?chat_id={tokid[1]}&text={inf}')
    else:
        print(f'\n----- Results -----\n CHECKED {c(str(checked)+"/"+str(len(usernames)))} \n AVAILABLE {g(str(avail))} \n BAD {r(str(bad))}\n-------------------')
    input('\n Click Enter To Exit The Program')