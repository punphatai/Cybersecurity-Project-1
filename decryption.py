import string 
import TextGenerate
import sys

def decrypt(chiper_text):
    
    # Remove random insert 
    chiper_text = list(chiper_text)
    mid_old = int((len(chiper_text)/1.5)/2)
    if mid_old + mid_old == 0:
        last_old = 0
    elif mid_old + mid_old > 0:
        last_old = mid_old + mid_old -1
    for i in range(mid_old,last_old+1):
        chiper_text.pop(mid_old)
    chiper_text = ''.join(str(i) for i in chiper_text)

    # Replace text
    text_for_swap = TextGenerate.all_text_for_swap()
    keyboard_text = TextGenerate.all_keyboard_text()
    for i in range(len(keyboard_text)):
        if text_for_swap[i] in chiper_text:
            chiper_text = chiper_text.replace(text_for_swap[i],keyboard_text[i])
    return chiper_text

def decryptText(chipeter_text):
    if not chipeter_text:
        return chipeter_text
    else: 
        return decrypt(chipeter_text)