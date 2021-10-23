
#get filename
from sys import argv

script, filename = argv
#messages
print(f"We're going to erase {filename}")
#escape? caret C?
print("If you don't want that, hit CTRL-C (^C).")
#accept - return is input?
print("If you do want that, hit RETURN.")

input("?")
#message
print("Opening the file...")
#new variable to contain file object
target = open(filename, 'w')
#message, then delete all content in the file. Optional, since we opened in mode w
print("Truncating the file. Goodbye!")
target.truncate()
#message
print("Now I'm going to ask you for three lines.")
#get new inputs
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
#message
print("I'm going to write these to the file.")
#write new inputs to file object using .write
target.write(f"{line1}\n{line2}\n{line3}")

#message and close
print("And finally, we close it.")
target.close()

print("Let's have a look, shall we?")
file = open(filename)
print(file.read())
