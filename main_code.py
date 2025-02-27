import streamlit as st
import os

def cipher1(text, shift):
    result = ""
    shift_amount = int(shift) % 26
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            result += char
    return result

def cipher2(text):
    return "".join(chr(219 - ord(c)) if c.islower() else chr(155 - ord(c)) if c.isupper() else c for c in text)

def cipher3(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return "".join(key[alphabet.index(c.lower())].upper() if c.isupper() else key[alphabet.index(c)] if c.islower() else c for c in text)

def cipher4(text, key):
    key = key.lower()
    key_index = 0
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a')) if char.islower() else chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            result += char
    return result

def cipher5(text):
    morse_dict = {
        'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
        'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
        's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', ' ': '/',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
        '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
        '$': '...-..-', '@': '.--.-.'
    }
    return ' '.join(morse_dict.get(char.lower(), '?') for char in text)

def cipher6(morse_text):
    conversion_dict = {'.': 'b', '-': 'a', '/': 'c', ' ': 'd'}
    return ''.join(conversion_dict.get(char, char) for char in morse_text)

def cipher1_decrypt(text, shift):
    result = ""
    shift_amount = int(shift) % 26
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
        else:
            result += char
    return result

def cipher2_decrypt(text):
    return "".join(chr(219 - ord(c)) if c.islower() else chr(155 - ord(c)) if c.isupper() else c for c in text)

def cipher3_decrypt(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reverse_key = {key[i]: alphabet[i] for i in range(26)}
    return "".join(reverse_key[c.lower()].upper() if c.isupper() else reverse_key[c] if c.islower() else c for c in text)

def cipher4_decrypt(text, key):
    key = key.lower()
    key_index = 0
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            result += chr((ord(char) - ord('a') - shift) % 26 + ord('a')) if char.islower() else chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index += 1
        else:
            result += char
    return result

def cipher5_decrypt(morse_text):
    morse_dict = {
        '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i',
        '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
        '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '/': ' ',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
        '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')',
        '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"',
        '...-..-': '$', '.--.-.': '@'
    }
    words = morse_text.split(' / ')
    decoded_words = []
    for word in words:
        decoded_chars = [morse_dict.get(symbol, '?') for symbol in word.split()]
        decoded_words.append(''.join(decoded_chars))
    return ' '.join(decoded_words)

def cipher6_decrypt(morse_text):
    conversion_dict = {'b': '.', 'a': '-', 'c': '/', 'd': ' '}
    return ''.join(conversion_dict.get(char, char) for char in morse_text)

st.title("AlphaText Encrypter/Decrypter")
st.text("This is the AlphaText Encrypter/Decrypter v3, created by Aakarsh Bajpai. It uses the virtually unbreakable AlphaText cipher (Also made by Aakarsh). Enjoy the security of AlphaText, which not even a Quantum Computer's brute force can break!")
action = st.radio("Choose an action:", ("Encode", "Decode"))
text = st.text_area("Enter text")
shift = os.getenv("CSHIFT", "0")
key1 = os.getenv("SUBS_KEY", "abcdefghijklmnopqrstuvwxyz")
key2 = os.getenv("VIGNKEY", "key")
if st.button("Process"):
    if action == "Encode":
        var1=text
        for i in range(637):
            c1_encoded = cipher1(var1, shift)
            c2_encoded = cipher2(c1_encoded)
            c3_encoded = cipher3(c2_encoded, key1)
            c4_encoded = cipher4(c3_encoded, key2)
            c5_encoded = cipher5(c4_encoded)
            c6_encoded = cipher6(c5_encoded)
            var1=c6_encoded
        st.write("Encoded Text:", var1)
    else:
        var1=text
        for i in range(637):
            c6_decoded = cipher6_decrypt(var1)
            c5_decoded = cipher5_decrypt(c6_decoded)
            c4_decoded = cipher4_decrypt(c5_decoded, key2)
            c3_decoded = cipher3_decrypt(c4_decoded, key1)
            c2_decoded = cipher2_decrypt(c3_decoded)
            c1_decoded = cipher1_decrypt(c2_decoded, shift)
            var1=c1_decoded
        st.write("Decoded Text:", c1_decoded)