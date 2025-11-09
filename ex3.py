def palindrome_detector(word):
    #make everything lowercase
    word = word.lower()
    #initialise palindrome variable so we can create the palindrome inside the for loop
    palindrome = ""
    clean_word = ""
    #use function .isalnum() so program ignores punctuation in phrase
    for ch in word:
        if ch.isalnum():
            clean_word += ch
            

#for loop starts with i =0 and ends with the length of of the word, this is so it can go through every letter and reverse order of letters
    for i in range(len(clean_word)):
        #takes the last letter in the world by taking index and creates a palindrome after each iteration of for loop 
        last = clean_word[len(clean_word)-i-1]
        palindrome = palindrome + last
#test whether the word/phrase entered cleaned up is the same as the created reveresed word (palindrome) if it is a plaindrom it returns true
    return clean_word == palindrome







