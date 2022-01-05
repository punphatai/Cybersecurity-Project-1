import encyption
import decryption

print("Please input string at least 32 character.")
text = input("Enter string: ")
print('Text before Encrypt: ',text)
print('-'*200)
encrypted_text = encyption.encyptText(text)
print('Encrypted text: ',encrypted_text)
print('-'*200)
decrypted_text = decryption.decryptText(encrypted_text)
print('Decrypted text: ',decrypted_text)
