# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#Define function to censor single phrase from text
def censor_phrase(source_text, censor_phrase):
    censored_text = source_text.replace(censor_phrase, "____")
    censored_text = source_text.replace(censor_phrase.title(), "____")
    censored_text = source_text.replace(censor_phrase.upper(), "____")
    censored_text = source_text.replace(censor_phrase.lower(), "____")
    return censored_text

#Censor phrase "learning algorithms" from email_one
email_one_censored = censor_phrase(email_one, "learning algorithms")
#print(email_one_censored)

#Define function to replace list of phrases from text
def censor_list(source_text, censor_list): #Doesn't censor capitalised words e.g "She"
    censored_text = source_text
    for censor_phrase in censor_list:
        censored_text = censored_text.replace(censor_phrase, "____")
        censored_text = censored_text.replace(censor_phrase.title(), "____")
        censored_text = censored_text.replace(censor_phrase.upper(), "____")
        censored_text = censored_text.replace(censor_phrase.lower(), "____")
    return censored_text

#Censor list proprietary_terms from email_two
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
email_two_censored = censor_list(email_two, proprietary_terms)
#print(email_two_censored)
