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
for c in range(len(decrypt_text)):
    if decrypt_text[c].isupper() and decrypt_text[c-1] != "\n":
        hide_message = hide_message + decrypt_text[c]
print(hide_message)


