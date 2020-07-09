# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation",
                     "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed",
                  "out of control", "help", "unhappy", "bad", "upset", "awful", "broken",
                  "damage", "damaging", "dismal", "distressed", "distressing", "concerning",
                  "horrible", "horribly", "questionable"]




blank = "____"




#Define function to censor single phrase from text
def censor_phrase(source_text, phrase):
    
    censored_text = source_text
    censored_text = censored_text.replace(phrase, blank)
    censored_text = censored_text.replace(phrase.title(), blank)
    censored_text = censored_text.replace(phrase.upper(), blank)
    
    return censored_text




#Censor phrase "learning algorithms" from email_one
email_one_censored = censor_phrase(email_one, "learning algorithm")
print("------- Email one censored -------\n \n" + email_one_censored)
print()




#Define function to replace list of phrases from text
def censor_list(source_text, censor_list = proprietary_terms):
    
    censored_text = source_text
    sorted_censor_list = sorted(censor_list, key = len, reverse = True)
    
    for phrase in sorted_censor_list:
        censored_text = censor_phrase(censored_text, phrase)
        
    return censored_text




#Censor list proprietary_terms from email_two
email_two_censored = censor_list(email_two)
print("------- Email two censored -------\n \n" + email_two_censored)
print()




#Define function to censor a list of phrases and any occurrence of a negative word after any
#negative words are used twice
def censor_list_and_negative(source_text, proprietary_list = proprietary_terms, negative_list = negative_words):

    censored_text = censor_list(source_text, proprietary_list)
        
    split_text = censored_text.split(" ")
    negative_list_sorted = sorted(negative_list, key = len, reverse = True)
    negative_indicies = []

    #Create a list of all negative words and their index positions within split_text    
    for phrase in negative_list_sorted:
        for i in range(0, len(split_text)):
            if phrase.title() in split_text[i].title():
                negative_indicies.append((i, phrase))
    negative_indicies.sort()
    
    if len(negative_indicies) == 0:
        return censored_text

    #Split the list after the second negative word and assign new strings to each part
    censor_from_index = negative_indicies[1][0] + 1
    split_text_up_to_censor = " ".join(split_text[:censor_from_index])
    split_text_censor = " ".join(split_text[censor_from_index:])

    censored_text = split_text_up_to_censor + " " + censor_list(split_text_censor, negative_list)
    
    return censored_text




#Censor negative terms and proprietary phrases from email three
email_three_censored = censor_list_and_negative(email_three)
print("------- Email three censored -------\n \n" + email_three_censored)
print()




#Define full_censor function to remove all proprietary terms, negative words after 2nd use and words either side of
def full_censor(source, proprietary = proprietary_terms, negative = negative_words):

    censored_text = censor_list_and_negative(source)
    split_text = censored_text.split(" ")
    censored_indicies = []
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for i in range(0, len(split_text)):
        if blank in split_text[i]:
            censored_indicies.append(i)

    for i in censored_indicies:
        for ch in alphabet:
            if i-1 >= 0:
                split_text[i-1] = split_text[i-1].replace(ch, "_")
            if i+1 < len(split_text):
                split_text[i+1] = split_text[i+1].replace(ch, "_")

    fully_censored_text = " ".join(split_text)
    
    return fully_censored_text




#Fully censor email four
email_four_censored = full_censor(email_four)
print("------- Email four censored -------\n\n" + email_four_censored)
