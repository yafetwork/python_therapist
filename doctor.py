"""
Program: doctor.py
Author: Yafet
Ch 5 case study

Conducts an interactive session of nondirective psychotherapy
"""

import random
import pyttsx3

hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.")
qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")
replacements = {"I": "you", "me": "you", "my": "your", "we": "you", "us": "you", "mine": "yours", "am": "are", "you": "I", "are": "am"}

# Definition of the speak() function that uses the pyttsx3 module
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def reply(sentence):
    """Builds and returns a reply to the sentence"""
    probability = random.randint(1, 4)
    if probability == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)
    
def changePerson(sentence):
    """Replaces first person pronouns with second person pronouns"""
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacements.get(word, word))
    return " ".join(replyWords)

def main():
    """Handles the interaction between patient and doctor."""
    greeting1 = "Good morning, I hope you are well today."
    greeting2 = "What can I do for you?"

    print(greeting1)
    speak(greeting1)

    print(greeting2)
    speak(greeting2)
    while True:
        sentence = input("\n>> ")
        if sentence.upper().strip() == "QUIT" or sentence == "":
            goodbye = "Have a nice day! Press ENTER to exit"
            # input(goodbye)
            speak(goodbye)
            input(goodbye)
            break
        elif sentence == "":
            warning = "Did you mean to say something? or you can type QUIT to exit."
            print(warning)
            speak(warning)
        else:
            response = reply(sentence)
            print(response)
            speak(response)

if __name__ == '__main__': 
    main()