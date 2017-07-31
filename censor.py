def censor(text, word):
    l = len(word)
    x = str.split(text)
    z = "*" * len(word)
    y = []

    for s in x:
        
        if s == word:
            y.append(z)
            print y
        else:
            y.append(s)
            print y
            
    return " ".join(y)        
     
censor("this hack is wack hack", "hack")