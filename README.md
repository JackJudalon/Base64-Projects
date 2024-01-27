# Base64-Projects
This projects helped teach me the inner workings of a cryptographic algorithm that is commonly seen in CTF's and insecure security measures. I used Python to create this along with the help of the REGEX library (RE).

I really enjoyed this project because many times during cryptography based challenges in CTF's, people have multiple websites open to decrypt from several different types including ROT-13, Caesar, and Base64. Through this project I got to learn the inner workings of how the function worked along with writing my own script that I can use for future challenges.


# How Base64 Works

The everyday English that we type in uses a table called ASCII (American Standard Code for Information Interchange). This map helps represent the correlation between characters such as 'A' or 'P' into decimal numbers 65 or 80. Our computer can work with these digits once they are converted into machine code (binary, base2). 

Binary is a system of number representation that can only use 1 and 0. Once these options are fulfilled, it moves over a digit in the pattern of 2^a (where 'a' is the digit place starting at index zero). For the use of Base64, each character will use a 8-bit (1 byte) binary number to correspond to its decimal number. 

Each byte of data is combined and then split every 6 bits. These new binary numbers are converted back into decimal, then mapped to a new character.

# Here is an example:

<b>Plaintext</b>: "Secret"

<b>ASCII</b>: 83 101 99 114 101 116

<b>Binary</b>: 01010011 01100101 01100011 01110010 01100101 01110100

<b>Combined Binary</b>: 010100110110010101100011011100100110010101110100

<b>New Binary (after split)</b>: 010100 110110 010101 100011 011100 100110 010101 110100

<b>New ASCII</b>: 20 54 21 35 28 38 21 52

<b>Ciphertext</b>: U2VjcmV0
