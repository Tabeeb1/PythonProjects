import art


def encode(message, shift):
    result = []
    shift = int(shift)
    message = message.lower()
    for item in message:
        if not item.isalpha():
            result.append(item)
        else:
            i = ord(item)
            temp = i
            temp -= shift
            if temp < 97:
                temp = 97 - temp
                i = 122 - (temp - 1)
                item = chr(i)
                result.append(item)
            else:
                item = chr(temp)
                result.append(item)

    for item in result:
        print(item, end='')


def decode(message, shift):
    result = []
    shift = int(shift)
    for item in message:
        if not item.isalpha():
            result.append(item)
        else:
            i = ord(item)
            temp = i
            temp += shift
            if temp > 122:
                temp = temp - 122
                i = 97 + (temp-1)
                item = chr(i)
                result.append(item)
            else:
                item = chr(temp)
                result.append(item)

    for item in result:
        print(item, end='')


logo = art.logo
print(logo)
decision = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
if decision == "encode":
    message = input("Type your message: ")
    shift = input("Type the shift number: ")
    encode(message, shift)
if decision == "decode":
    message = input("Type your message: ")
    shift = input("Type the shift number: ")
    decode(message, shift)

