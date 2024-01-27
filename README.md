# Base64-Projects
These are my personal projects to learn more about base64 encyption and decryption. 

<b>How Base64 Works</b>

The everyday English that we type in uses a table called ASCII (American Standard Code for Information Interchange). This map helps represent the correlation between characters such as 'A' or 'P' into decimal numbers 65 or 80. Our computer can work with these digits once they are converted into machine code (binary, base2). 

Binary is a system of number representation that can only use 1 and 0. Once these options are fulfilled, it moves over a digit in the pattern of 2^a (where 'a' is the digit place starting at index zero). For the use of Base64, each character will use a 8-bit (1 byte) binary number to correspond to its decimal number. 

Each byte of data is combined and then split every 6 bits. These new binary numbers are converted back into decimal, then mapped to a new character.

Here is an example:

Plaintext: "Secret"

ASCII: 83 101 99 114 101 116

Binary: 01010011 01100101 01100011 01110010 01100101 01110100

Combined Binary: 010100110110010101100011011100100110010101110100

New Binary (after split): 010100 110110 010101 100011 011100 100110 010101 110100

New ASCII: 20 54 21 35 28 38 21 52

Ciphertext: U2VjcmV0
