from email.policy import default

a_list = ['a', 'e', 'i', 'o', 'u', 'y']
b_list = ['b', 'c', 'd', 'f', 'g', 'h',
           'j', 'k', 'l', 'm', 'n', 'p',
           'q', 'r', 's', 't', 'v', 'w',
           'x', 'z']

def ask_password(login, password, success, failure):
    if dict.get(password) != None:
        if dict[password] == "":
            return (True, '')
        else:
            return (False, dict[password])
    else:
        a_password = list(map(lambda x: x.lower(), filter(lambda x: x.lower() in a_list, password)))
        b_password = list(map(lambda x: x.lower(), filter(lambda x: x.lower() in b_list, password)))
        b_login = list(map(lambda x: x.lower(), filter(lambda x: x.lower() in b_list, login)))
        if len(a_password) == 3 and (b_password == b_login):
            success(login)
            return (True, '')
        if len(a_password) != 3 and (b_password == b_login):
            failure(login, "Wrong number of vowels")
            return (False, 'Wrong number of vowels')
        if len(a_password) == 3 and (b_password != b_login):
            failure(login, "Wrong consonants")
            return (False, "Wrong consonants")
        if len(a_password) != 3 and (b_password != b_login):
            failure(login, "Everything is wrong")
            return (False, "Everything is wrong")


def success(login):
    return


def failure(login, mes):
    return


def main(login, password):
    e, mes = ask_password(login, password, success, failure)
    if e:
        print('Привет, ' + login.lower() + '!')
    else:
        print('Кто-то пытался притвориться пользователем ' + login.lower() + ', но в пароле '
                                                                             'допустил ошибку: ' + mes.upper() + '.')

import re
dict = {}
string = input()
string = re.split('main\(\"|\", \"|\"\)', string)
login = string[1]
password = string[2]
main(login, password)