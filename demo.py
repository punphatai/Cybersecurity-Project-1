import encyption
import decryption

text = ""
def input_string():
    global text
    text = input("Enter string: ")
    if len(text) < 32:
        print("Please input string at least 32 character.\n")
        input_string()
    return text

input_string()
print('Text before Encrypt: ',text)
print('-'*200)
encrypted_text = encyption.encyptText(text)
print('Encrypted text: ',encrypted_text)
print('-'*200)
decrypted_text = decryption.decryptText(encrypted_text)
print('Decrypted text: ',decrypted_text)
