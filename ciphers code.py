# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 00:37:42 2024

@author: aoalj
"""
##define a caesar decoding algorithm for a string and a specified offset
def caesar_decode(string, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    msg = ""
    for i in string:
        if i in alphabet and i != " ":
            if (25-alphabet.find(i)) < offset:
                index =offset - 1 - (25-alphabet.find(i))
                msg += alphabet[index]
            else:
                index = alphabet.find(i) + offset
                msg += alphabet[index]
        elif i == " ":
            msg += " "
        else:
            msg += i
    print(msg)

string_de = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
caesar_decode(string_de, 10)

#define a caesar encoding algorithm for a string and a specified offset
def caesar_encode(string, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    msg = ""
    for i in string:
        if i in alphabet and i != " ":
            index = alphabet.find(i) - offset
            msg += alphabet[index]
        elif i == " ":
            msg += " "
        else:
            msg += i
    print(msg)
    
string_en = " hey there Vishal! hope you are doing well. this is a test of my encoding algorithm, tell me how it goes!"
caesar_encode(string_en, 10)

#Vigenère Cipher
# function to map and repeat the key word for a given string
def repeat_word_for_each_word(given_string, word_to_repeat):
    words = given_string.split()
    repeated_string = ""
    friends_index = 0
    for word in words:
        repeated_word = ""
        for character in word:
            if character.isalpha():
                repeated_word += word_to_repeat[friends_index % len(word_to_repeat)]
                friends_index += 1
            else:
                repeated_word += character
        repeated_string += repeated_word + " "
    return repeated_string.rstrip()

# a function to get the indecies of the repeated word (key) in order to have a list of indecies as offset for original string
def get_word_indices_in_alphabet(repeated_string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    x = []
    for i in repeated_string:
        if i in alphabet:
            x.append(alphabet.find(i))
        else:
            x.append(i)
    return x

given_string = "whats up"
word_to_repeat_key = "friends"

repeated_string = repeat_word_for_each_word(given_string, word_to_repeat_key)
print(repeated_string)

x = get_word_indices_in_alphabet(repeated_string)
print(x)

#encoding vig cipher

def vig_encode(string, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    msg = ""
    index_in_offset = 0  # Initialize index for accessing offset values from list x
    for i in string:
        if i in alphabet:
            # Calculate the index to decode the character based on the offset from list x
            if type(offset[index_in_offset]) is int:
                index = alphabet.find(i) - offset[index_in_offset]
                msg += alphabet[index]  # Ensure the index wraps around if it exceeds the alphabet length
            else:
                msg += i
        else:
            msg += i
        index_in_offset = (index_in_offset + 1)  # Move to the next offset in list x

    print(msg)
vig_encode("whats up",x)

# decoding vig cipher
def vig_decode(string, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    msg = ""
    index_in_offset = 0  # Initialize index for accessing offset values from list x
    for i in string:
        if i in alphabet:
            # Calculate the index to decode the character based on the offset from list x
            if type(offset[index_in_offset]) is int:
                if (25 - alphabet.find(i)) < offset[index_in_offset]:
                    index = offset[index_in_offset] - 1 - (25 - alphabet.find(i))
                    msg += alphabet[index]
                else:
                    index = alphabet.find(i) + offset[index_in_offset]
                    msg += alphabet[index]  # Ensure the index wraps around if it exceeds the alphabet length
            else:
                msg += i
        else:
            msg += i
        index_in_offset = (index_in_offset + 1)  # Move to the next offset in list x

    print(msg)

vig_decode("rqspf rx", x)