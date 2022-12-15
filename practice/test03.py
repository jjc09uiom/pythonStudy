#!/usr/bin/python3
mystatus = 400
print(http_error(mystatus))

def http_error(status) :
    match status:  #python 3.10 support
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"