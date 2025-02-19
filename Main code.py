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

st.title("AlphaText Encrypter/Decrypter")
action = st.radio("Choose an action:", ("Encode", "Decode"))
text = st.text_area("Enter text")
shift = os.getenv("CSHIFT", "0")
key1 = os.getenv("SUBS_KEY", "abcdefghijklmnopqrstuvwxyz")
key2 = os.getenv("VIGNKEY", "key")
if st.button("Process"):
    if action == "Encode":
        c1_encoded = cipher1(text, shift)
        c2_encoded = cipher2(c1_encoded)
        c3_encoded = cipher3(c2_encoded, key1)
        c4_encoded = cipher4(c3_encoded, key2)
        st.write("Encoded Text:", c4_encoded)
    else:
        c4_decoded = cipher4_decrypt(text, key2)
        c3_decoded = cipher3_decrypt(c4_decoded, key1)
        c2_decoded = cipher2_decrypt(c3_decoded)
        c1_decoded = cipher1_decrypt(c2_decoded, shift)
        st.write("Decoded Text:", c1_decoded)
