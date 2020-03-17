#Pig Latin
#isalpha
def pigLatin (original):
    #original = raw_input("please input:")
    word = original.lower()
    vowel = "way"
    consonant = "ay"
    first = word[0]
    if len(word) > 0:
        if first.isalpha() == True:
            if first in "aeiou":
                #newWordVowel = str(word) + str(vowel)
                newWordVowel = word + vowel
                print (newWordVowel)
            else:
                #newWordConsonant = str(word[1:]) + str(first) + str(consonant)
                newWordConsonant = word[1:] + first + consonant
                print (newWordConsonant)
        else:
            print ("character only")
    else:
        print ("Empty")

original = input("please input:")
pigLatin (original)
    
    
"""
    
    if len(word) > 0 and first.isalpha() == TRUE:
        if first in "aeiou":
            #newWordVowel = str(word) + str(vowel)
            newWordVowel = word + vowel
            print newWordVowel
        else:
            #newWordConsonant = str(word[1:]) + str(first) + str(consonant)
            newWordConsonant = word[1:] + first + consonant
            print newWordConsonant
            
    elseif len(word) > 0 and first.isalpha() == FALSE:
        print "character only"
        
    else:
        print "Empty"
        
        
"""    
        