# Palindrome is

def is_palindrome(word, index=0):
    center = int((len(word)) / 2)
    if word[index] != word[len(word)-1 - index]:
        return False
    if (index == center):
        return True
    return is_palindrome(word, index + 1)



#Testing function

wordsLit = ["somos o no somos", 'issac no ronca asi', 'Oso',
            'se Verlas al reves amo La PaLoma', 'Anina lava la tina Azul','Dennis and Edna sinned']

for word in wordsLit:
    if is_palindrome(word.lower().replace(' ',"")) :
        print(word + ': Is a palindrome \n')
    else:
        print(word + ': Is not  palindrome \n')