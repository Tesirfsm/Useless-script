import time

user = 'satan'
password = '666'
#Abfrage der Bedingungen
if user == 'admin' and password == '123safe':
#Ausführung der Befehle
    timer = 'loading'
    while timer != 'loading......':
        time.sleep(0.5)
        print (f'{timer}\r', end="")
        timer = timer+ ('.')
        if timer == 'loading......':
            print('-login in-')
            time.sleep(2.0)
#belangloser innerer Monolog
            print("What am I doing?")
            time.sleep(1.5)
            print("I am not even login in. That's just a String")
elif user == "admin" and password != '123safe':
    timer = 'loading.'
    while timer != 'loading.....':
        time.sleep(0.5)
        print (f'{timer}\r', end="")
        timer = timer+ ('.')
        if timer == 'loading.....':
            time.sleep(1.0)
            print('-acces denied-')
elif user == 'satan' and password == '666':
    highway = ('Entering hell')
    while highway != ('Entering hell......'):
        time.sleep(0.5)
        print (f'{highway}\r', end="")
        highway = highway+ ('.')
        if highway == ('Entering hell......'):
            print ('You drove along the highway to hell\nWelcome, Satan')
