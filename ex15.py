#get a filename
from sys import argv
script, filename = argv

#creates variable txt and assigns to it opened file object
txt = open(filename)

#message stating the file name
print(f"Here's your file {filename}:")
#display the assigned value of the txt variable, i.e. perform the read function on the contents of the file.
print(txt.read())
txt.close()
#next lines repeat the process, but declaring a new variable
print("Type the filename again:")
#get filename txt_again. So this can be a new filename, one that was not provided in the argv? how come?
file_again = input("< ")
#create variable to hold the opened file contents
txt_again = open(file_again)
#print the open file contents
print(txt_again.read())
txt_again.close()
