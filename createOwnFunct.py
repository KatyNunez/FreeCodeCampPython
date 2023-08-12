#functions using parameters
#pasar parametros
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en')

# funciones que devuelven un valor /fruitful
def returnfun():
    return "hello"
print(returnfun(),"katy")

#funciones con multiples parametros
def addtwo( a,b):
    return a+b

print(addtwo(1,3))

# void function do not return value

