def reverse (text):
    l = len(text)
    print l
    st = ""
    for n in range(l - 1, -1, -1):
        st += text[n]
        print st
    return st
    
    

reverse("ravi")