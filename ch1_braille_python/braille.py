""" Python module for Google's foo bar challenge """

from __future__ import print_function

BRAILLE_TABLE = {
    ' ': '000000',
    'a': '100000',
    'b': '110000',
    'c': '100100',
    'd': '100110',
    'e': '100010',
    'f': '110100',
    'g': '110110',
    'h': '110010',
    'i': '010100',
    'j': '010110',
    'k': '101000',
    'l': '111000',
    'm': '101100',
    'n': '101110',
    'o': '101010',
    'p': '111100',
    'q': '111110',
    'r': '111010',
    's': '011100',
    't': '011110',
    'u': '101001',
    'v': '111001',
    'w': '010111',
    'x': '101101',
    'y': '101111',
    'z': '101011'
}

def solution(plaintext):
    """Provides a function that will convert alpha and space text to braille"""
    result = ''
    #test length is less than 50 characters
    if len(plaintext) >= 50:
        requirements_mismatch()
        return result

    for index_char in plaintext:
        # verify that the character isalpha or isspace
        if index_char.isalpha() or index_char.isspace():
            if index_char.isupper():
                # add capitalization ahead of the next character
                result += '000001'
                index_char = index_char.lower()

            result += BRAILLE_TABLE[index_char]
        else:
            # if we don't meet the input requirements, send an empty result and print the reason
            result = ''
            requirements_mismatch()
            break

    return result

def requirements_mismatch():
    """Tells the user their input does not match requirements"""
    print('input does not match the requirements')
    return
