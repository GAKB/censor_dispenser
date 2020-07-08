# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

blank = "____"
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation",
                     "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed",
                  "out of control", "help", "unhappy", "bad", "upset", "awful", "broken",
                  "damage", "damaging", "dismal", "distressed", "distressed", "concerning",
                  "horrible", "horribly", "questionable"]


#Define function to censor single phrase from text
def censor_phrase(source_text, phrase):
    censored_text = source_text
    censored_text = censored_text.replace(phrase, blank)
    censored_text = censored_text.replace(phrase.title(), blank)
    censored_text = censored_text.replace(phrase.upper(), blank)
    return censored_text

#Censor phrase "learning algorithms" from email_one
email_one_censored = censor_phrase(email_one, "learning algorithm")
#print("Email one after censoring 'learning algorithms':\n \n" + email_one_censored)
#print()


#Define function to replace list of phrases from text
def censor_list(source_text, censor_list):
    censored_text = source_text
    for phrase in censor_list:
        censored_text = censor_phrase(censored_text, phrase)
    return censored_text

#Censor list proprietary_terms from email_two
email_two_censored = censor_list(email_two, proprietary_terms)
#print("Email two after censoring items in proprietary_terms:\n \n" + email_two_censored)

