def obfuscate(text):
    #splits the the inputed textsinto a list of words so that we can manipulate the words@
    words = text.split()
    #for loop that checks every word in the list of words from the text
    for i in range(len(words)):
       #first case that swaps every instance of the word "the" to "and" and "and" to "the"
        if words[i].lower() == "and":
            words[i] = "the"
        
        elif words[i].lower() == "the":
            words[i] = "and"
    #joins the words back into the original place in  the text  
    text = " ".join(words)
       #second case checks every third letter and makes it uppercase
       # for loop that starts at 2 and ends at the length of characters which is 1 repeats every 3 characters

    chars = list(text) # create a kust if chracters based on the inpout so that we make sure every 3rd character is uppercase   
    for i in range(2, len(chars), 3):
        #changes the characters into uppercase  
        chars[i] = chars[i].upper()
    text = "".join(chars)

        #3rd case reverses the letters in every fith word 
    words = text.split() 
    for i in range(4, len(words), 5): #takes the 5th word as we count from 0  abd ebds at the end  goes in increments of 5 so we get every 5 wordsof the word
        words[i] = words[i][::-1]
    text = " ".join(words)
        #4th case caesar shift by 1 on every other word
    words = text.split()
    for i in range(1, len(words), 2): #starts at 1 so its the 2nd word in the li goes in increments of 2 so that its every other wordchecks the whole word to cypher shiftst of words and 
        cipher = ""
        for j in range(len(words[i])):
            char = words[i][j]
            if char.isupper():
                # chr( turns unicode number to letter and ord() turns unicode number to letter allows us to do cypher shift )
                cipher += chr((ord(char) - 64) % 26 + 65) # cypher shift of 1 for uppercase letters
            else:
                cipher += chr((ord(char) - 96) % 26 + 97) # cypher shift of 1 for lowercase letters 
        words[i] = cipher 
    text = " ".join(words)
   
    return text
    



