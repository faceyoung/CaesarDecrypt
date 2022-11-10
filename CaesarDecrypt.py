encrypt_text = {
    "Line1":"Wklv lv Fdhvdu\n",
    "Line2":"Wklv lv Qrw Fdhvdu\n"
}


def decrypt(key, encrypt_text):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    for line in encrypt_text:
        for char in encrypt_text[line]:
            if char.isupper():
                char = char.lower()
                char_index = (alpha.find(char) - key) % 26
                output = output + alpha[char_index].upper()
            elif char in alpha:
                char_index = (alpha.find(char) - key) % 26
                output = output + alpha[char_index]
            else:
                output = output + char
    return output
print(decrypt(3, encrypt_text))


decrypt_text = decrypt(3, encrypt_text)
hide_message = ""
for i in range(len(decrypt_text)):
    if decrypt_text[i].isupper() and decrypt_text[i-1] != "\n":
        hide_message = hide_message + decrypt_text[i]
print(hide_message)



# ---OUTPUT---

# This is Caesar    
# This is Not Caesar

# CNC


