def trans(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": 
            if letter.isupper():
                translation = translation + "T" 
            else:
                translation = translation + "t" 
        else:
            translation = translation + letter 
    return translation
    
print(trans(input("Enter something: ")))
