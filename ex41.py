import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"  # source file
WORDS = []

PHRASES = {  # here we construct our phrases as templates using wildcards, I guess
    "class %%%(%%%)": "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__(self, ***)": "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()": "Set *** to an instance of class %%%.",
    "***.***(@@@)": "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'",
}

# do they want to drill phrases first // WTF is this block for?
if len(sys.argv) == 2 and sys.argv[1] == "english":  # WTF is happening in this line?
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))
    # so from the module we imported at the start
    # we call urlopen (function or method?) and pass our source file to it as an argument
    # we iterate over every word in that file, and append each to our WORDS list.


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    # I guess this function builds the questions/answers using random words?
    # WTF are the arguments passed to random.sample and snippet.count?

    for i in range(0, snippet.count("@@@")):  # WTF are we iterating over?
        param_count = random.randint(1, 3)
        param_names.append(", ".join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:  # WTF are we doing here, and below?
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(
            result
        )  # so the outcome is a sentence? Or are we generating a bunch of sentences up front?

    return results


# keep going until they hit CTRL+D
try:
    while True:
        snippets = list(PHRASES.keys())
        # creates a list of the keys from the Phrases dictionary (without the values). Why is phrases not an argument passed to the keys method? Does keys accept no arguments?
        # doc says keys() returns a "view object" - is that why we need to use "list(...)", so that we can set it as the value of "snippets"?
        random.shuffle(
            snippets
        )  # why shuffle? That does not change the value fo snippets, right?

        for snippet in snippets:  # so, iterate over our list
            phrase = PHRASES[snippet]  # WTF is happening?
            question, answer = convert(
                snippet, phrase
            )  # WTF? How are we setting two vars (question, answer) to a function call? convert returns a single list, no?
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("< ")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
