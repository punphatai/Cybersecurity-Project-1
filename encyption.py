import TextGenerate

def encypt(text):
    # Replace text
    text_for_swap = TextGenerate.all_text_for_swap()
    keyboard_text = TextGenerate.all_keyboard_text()
    for i in range(len(text_for_swap)):
        if keyboard_text[i] in text:
            text = text.replace(keyboard_text[i],text_for_swap[i])
   
    # Insert random
    text = list(text)
    mid = int(len(text)/2)
    last = mid + mid - 1
    if last == -1:
        last = 0
    for i in range(mid,last+1):
        text.insert(i,TextGenerate.random_text_to_insert())
    text = ''.join(str(i) for i in text)
    
    return text

def encyptText(text):
    # check if text = "" or white space
    if not text or text.isspace():
        return text
    else:
        return encypt(text)
