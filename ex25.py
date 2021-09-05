def break_words(stuff): #"stuff" is the required input to the function.
    """This function will break up words for us."""
    words = stuff.split(' ')  #variable words is assigned the value of stuff, after the "split" function (?) has been applied to it.
    return words #words is provided as the output of the function

def sort_words(words): #list of words is the input to the function. Is this taken from the returned value of the break_words function? Or is this a new input list?
    """Sorts the words."""
    return sorted(words) #sorted function is applied on words, and is the output of the function.

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) #pop removes the list item at the position # and assigns the value to the variable word. 0 denotes the first position in the list.
    print(word) #function prints the value of the variable word.

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #as above, but presumably the position -1 denotes the last item in the list.
    print(word) #as above

def sort_sentence(sentence): #? at what point does the variable "sentence" come into existence? Is it when input content is provided, upon calling this function?
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence) #calls the function we defined in line 1, runs it, and assigns the value to the variable "words".
    return sort_words(words) #calls a sort function on the variable. We defined this function in line 6

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence) #calls the function defined in line 1, runs it, and assigns the value to the var "words".
    print_first_word(words) #calls function from line 10
    print_last_word(words) #calls function from line 15

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence) #calls the function defined in line 20, runs it, and assigns the value to var "words".
    print_first_word(words) #calls function from line 10
    print_last_word(words) #calls function from line 15

