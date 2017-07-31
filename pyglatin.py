pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) == 0:
    print "empty"
elif len (original) > 0 and not original.isalpha():
    print "not a string"
else:
    word = original.lower()
    first = word[0]    
    new_word = word+first+pyg
    new_word = new_word[1:len(new_word)]
    print new_word