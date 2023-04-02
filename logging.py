info = {'john': 12345, 'anissa': 00000, 'jacques': 20011, 'umutoni': 20008}
#while True:

#name = input('Enter your name: ')
#client.append(name)
#password = input('Enter your password: ')
#client.append(password)
#info.append(client)
#while True:
def sign_up():
    name = input('Enter your name: ')
    password = int(input('Enter your password and should be 5 digits: '))
    if name not in info or password != info[name]:
        info[name] = password
        print('Sign up successful.')
        
    elif name in info or password == info[name]:
        print('Username or account existed')
    
    print(info)             
def log_in():
    name = input('Enter your name: ')
    password = int(input('Enter your password and should be 5 digits: '))
    
    if name in info and password == info[name]:

        print('Log in successful')
        
    else:
        print('Log in denied.create an account or try again!')
        sign_up()
log_in()                    
 

