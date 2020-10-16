# importing regex and random libraries
import re
import random

# potential negative responses
negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
# keywords for exiting the conversation
exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
# random starter questions
random_questions = (
    "Why are you here? ",
    "Are there many humans like you? ",
    "What do you consume for sustenance? ",
    "Is there intelligent life on this planet? ",
    "Does Earth have a leader? ",
    "What planets have you visited? ",
    "What technology do you have on this planet?"
)

name = ""

alienbabble = (
    # Your planet...
    {r'.*\s*your planet':
         ("My planet is a utopia of diverse organisms and species. ",
          "I am from Alcustowa, the capital of the Wayward Galaxies. ")
     },
    # why do you...?
    {r'why\sdo\syou\s(.*[^\?]*)\??':
         ("What makes you think I {0}? ",
          "Wear the hat on your head ",
          "think Rocket man is burning out his fuse up here alone ")
     },
    # why...?
    {r'.*why\s+.*':
         ("I came to bring you drama. ",
          "Where did that goat come from? ",
          "It's too hot outside. ")
     },
    # what...?
    {r'.*what\s+.*':
         ("Hi there ",
          "Howdy",
          "I spend all day looking at pictures of dogs. ")
     },
    # it is...
    {r'.*it\s+is':
         ("There is the kiwi. ",
          "There is a semi truck ",
          "It is here, the land of the pancakes. ")
     },
    # I think...
    {r'.*i\s+think\s(.*)[\?\.\!]?':
         ("Therefore I am. ",
          "I will have another taco please. ")
     },
    # Other responses
    {r'.*':
         ("Please tell me more. ",
          "Tell me more! ",
          "Why do you say that? ",
          "I see. Can you elaborate? ",
          "Interesting. Can you tell me more? ",
          "I see. How do you think? ",
          "Why? ",
          "How do you think I feel when you say that? ",
          "Tell me how you really feel",
          "Tell me what you want what you really really want",
          "Do you feel it?")
     }
)


# Define greet() below:
def greet():
    name = input("Hello what is your name? ")
    will_help = input(
        "Hi {}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet? ".format(name))

    if will_help in negative_responses:
        print("Ok, have a nice Earth day!")
        return
    return True


# Define make_exit() here:
def make_exit(reply):
    for exit_command in exit_commands:
        if exit_command in reply:
            print("Bye Bye")
            return True


# Define alienbot() next:
def alienbot():
    if greet():
        reply = input(random.choice(random_questions)).lower()
        while not make_exit(reply):
            reply = converse(reply)


# Define converse() below:
def converse(reply):
    for pair in alienbabble:
        for regex_pattern, alien_answers in pair.items():
            found_match = re.match(regex_pattern, reply)
            if found_match:
                alien_answer = random.choice(alien_answers)
                formatted_alien_answer = alien_answer.format(
                    *[reflect(matching_group) for matching_group in found_match.groups()])
            return reply


# dictionary used to switch pronouns
# and verbs in responses
reflections = {
    "i'm": "you are",
    "you're": "i'm",
    "was": "were",
    "i": "you",
    "are": "am",
    "am": "are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "I",
    "me": "you"
}


def reflect(response):
    words = response.split()
    for index, word in enumerate(words):
        if word in reflections:
            words[index] = reflections[word]
    return ' '.join(words)


alienbot()