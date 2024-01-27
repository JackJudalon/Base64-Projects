import re

### decrypt(old_text)
### Takes in a String of numbers and characters to decrypt from Base64
### Maps the old String to a Base64 standard index table
### Prints the decrypted String
def decrypt(old_text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    alphabet2 = re.findall(".", alphabet)
    old_text = re.findall(".", old_text)
    for i in range(0,len(old_text)):
        if old_text[i] == "=":
            old_text[i] = ""
            continue
        old_text[i] = alphabet.find(old_text[i])
        old_text[i] = alphabet2[old_text[i]]
        old_text[i] = bin(ord(old_text[i]))
        old_text[i] = old_text[i].replace("b","")
        old_text[i] = old_text[i][2:]
    old_text = ''.join(old_text)
    print(old_text)
    old_text = re.findall(".......", old_text)
    for i in range(0, len(old_text)):
       old_text[i] = int(old_text[i],2)
       old_text[i] = chr(old_text[i])
    old_text = ''.join(old_text)
    print(old_text)

old_text = input("Input your text to decrypt>> ")
decrypt(old_text)

