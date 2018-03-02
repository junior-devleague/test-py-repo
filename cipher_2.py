symbol = "abcdefghijklmnopqrstuvwxyz"

MAX_KEY_SIZE = len(symbol)

message = ''

encrypt_message = ''

# this function asks user to encrypt or decrypt

def getMode():
    global mode
    while True:
        mode = input('Hello, would you like to encrypt or decrypt a message? \n').lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Sorry I did not understand your input. Please Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    global message
    message = input("Enter your input: \n").lower()
    if message.isalpha():
        return message
    else:
        print ("Please enter letters only!")
        getMessage()


def getKeyEncrypt():
    global symbol
    global message
    global encrypt_message
    key = int(input("Please enter a key: \n"))
    if (key <= 0 or key > 26):
        print ("Please enter a valid number between 1-26: \n")
        getKeyEncrypt()
        return None

    for char in message:
        position = symbol.find(char)
        new_position = (position + key) % 26
        new_char = symbol[new_position]
        encrypt_message += new_char

    return print('Here is your message: \n', encrypt_message)

def getKeyDecrypt():
    global symbol
    global message
    global encrypt_message
    key = int(input("Please enter a key: \n"))

    for char in message:
        position = symbol.find(char)
        new_position = (position - key) % 26
        new_char = symbol[new_position]
        encrypt_message += new_char

    return print('Here is your message: \n', encrypt_message)

def run_cipher():
    global mode
    global encrypt_message

    #gets the mode to play
    getMode()

    #gets message from the user
    getMessage()

    #either encrypts the message or decrypts the message
    if mode in 'encrypt e'.split():
        print ("Mode", mode)
        getKeyEncrypt()
    if mode in 'decrypt d'.split():
        getKeyDecrypt()

    #resets message variable to blank
    encrypt_message = ""

    #prompts user to play again
    print ("Play again? Type yes/no: \n")
    quitOrNot = getMessage()
    if quitOrNot == 'y':
        run_cipher()
    elif quitOrNot == 'n':
        return "Good Bye!"
    else: 
        return "Please enter 'y' or 'n' "

print(run_cipher())