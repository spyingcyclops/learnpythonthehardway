from sys import argv

script, input_file = argv
#new function to display contents of variable f.
def print_all(f):
    print(f.read())
# new function to change the position of the file handle (kinda like a cursor). 0 places the handle at the beginning of the file (in terms of bytes, not lines).
def rewind(f):
    f.seek(0)
#new function to print a line based on the line_count, i.e. the line number.
def print_a_line(line_count, f):
    print(line_count, f.readline())
#define variable to hold the opened file object
current_file =  open(input_file)

print("First let's print the whole file:\n")
#call the print_all function defined in line 5
print_all(current_file)

print("now let's rewind, kind of like a tape.")
#call the rewind function, defined in line 8
rewind(current_file)

print("Let's print three lines:")

current_line = 1
#call the print_a_line function defined in line 11.
print_a_line(current_line, current_file)
#value of current_line is incremented each time, new variable value is assigned to same variable.
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
