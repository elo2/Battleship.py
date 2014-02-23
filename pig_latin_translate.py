pyg = 'ay'
original = raw_input('Enter a word:') #asks for input from user
if len(original) > 0 and original.isalpha(): # checks to make sure word has letters
    word = original.lower() #removes any capital letters
    first = original[0] #asks for first letter of word
    if first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u':
        #checks if first letter is a vowl, if so, appends piglatin ending
        new_word = word + pyg
        print new_word
    else:
        #takes consonant and appends to end and then adds pig latin
        new_word = word[1:] + word[0:1] + pyg
        print new_word
else:
    print 'Invalid input'
    