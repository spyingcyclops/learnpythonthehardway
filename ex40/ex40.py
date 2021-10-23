class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there."])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells."])

#happy_bday.sing_me_a_song()

#bulls_on_parade.sing_me_a_song()

class Person: #define a new class
    def __init__(self, name, age, sex): #def the init function. 
        #WHY self? What does that do? 
        #Is it basically a synonym for "within the context of this class"?
        self.name = name #what am I doing here?
        self.age = age
        self.sex = sex

    def greet(self):
        print("Hello, my name is " + self.name)

p1 = Person("John", 42, "Male")
#now I create an instance of Person, with these attributes.
print(f"P1 is {p1.name}, who is {p1.age} and is {p1.sex}.")
#now I access those attributes using the key.value syntax, similar to dict.
p1.greet()