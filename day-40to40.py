import random
import string

# For encoding, this function is created
def encode_language(language):
    splice = language.split(" ")
    #loop contains the enumerate() that uses index and word , index shows index of wod  and word shows word itself
    for index, word in enumerate(splice):
        if len(word) > 3:
            firstchar = word[0]
            newword = word[1:] + firstchar
            
            random_chars_before = ''.join(random.choices(string.ascii_letters, k=3)) #import random 3 characters
            random_chars_after = ''.join(random.choices(string.ascii_letters, k=3))#import random 3 characters
            splice[index] = f"{random_chars_before}{newword}{random_chars_after}"  #modifies the string and the main part of encoding text
        else:
            splice[index] = word[::-1]  #for reversing word

    return ' '.join(splice)

# For decoding, this function is created
def decode_language(encoded_string):
    
    spliceagain = encoded_string.split(" ")
    
    for index, word in enumerate(spliceagain):
        if len(word) > 3:  
            rem_word = word[3:-3]
            
            firstchar = rem_word[-1]
            new_word = firstchar + rem_word[:-1]  
            
            spliceagain[index] = new_word  
        else:
            spliceagain[index] = word[::-1]  

    return ' '.join(spliceagain)
#enter any value that is to be encoded,   function call for encoding
text = input("Enter the Text you want to encode: \n")
x = encode_language(text)
print("Encoded text:", x)
# function call for encoding
y = decode_language(x)
print("Decoded text:", y)
