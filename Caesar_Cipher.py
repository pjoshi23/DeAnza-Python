symbols = ('''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()1234567890-_=+[{]}\|;:'"<>?,./''')

maxkeysize = len(symbols)

def getMethod():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        m = input().lower() 
        if m in ['encrypt', 'e', 'decrypt', 'd']:
            return m
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getPhrase():
    print('Enter your message: ') 
    return input()

def getCipherKey():
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (maxkeysize))
        key = int(input())
        if key >= 1 and key <= maxkeysize:
            return key

def getNewMessage(method, message, key):
    if method[0] == 'd':
        key = 0 - key
    translated = ''
    for symbol in message:
        symbolIndex = symbols.find(symbol)
        if symbolIndex == -1: 
            translated += symbol
        else:
            symbolIndex += key
            if symbolIndex >= len(symbols):
                symbolIndex -= len(symbols)
            elif symbolIndex < 0:
                symbolIndex += len(symbols)
            translated += symbols[symbolIndex]
    return translated

method = getMethod()
message = getPhrase()
key = getCipherKey()
print('Your translated text is:')
print(getNewMessage(method, message, key))