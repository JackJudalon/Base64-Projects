import re

def encrypt(old_text): 
    old_text = old_text.replace(" ", "_")
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    alphabet = re.findall(".", alphabet)
    text_to_encrypt = re.findall(".", old_text)
    for i in range(0, len(text_to_encrypt)):
        text_to_encrypt[i] = str(0) + ''.join(format(ord(text_to_encrypt[i]), 'b'))
    text_to_encrypt = ''.join(text_to_encrypt)
    new_text = ""
    text_to_encrypt = [(text_to_encrypt[i:i+24]) for i in range(0, len(text_to_encrypt), 24)]
    for i in range(0,len(text_to_encrypt)):
        if len(text_to_encrypt[i]) < 24:
            for x in range(0, (24-len(text_to_encrypt[i]))):
                text_to_encrypt[i] += "0"
    text_to_encrypt = ''.join(text_to_encrypt)
    text_to_encrypt = [(text_to_encrypt[i:i+6]) for i in range(0, len(text_to_encrypt), 6)]
    for x in range(0, len(text_to_encrypt)):
       if text_to_encrypt[x] == "000000":
           new_text += "="
           continue
       new_text += alphabet[(int(text_to_encrypt[x],2)) % len(alphabet)]
    return "Your code is: " + new_text

old_text = input("Input your text to encode >> ")
print(encrypt(old_text))
