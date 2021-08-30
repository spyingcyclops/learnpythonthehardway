def cocktail (name, liqor, soda, flavor):
    print(f"One {name} coming up!")
    print(f"The {name} contains {liqor}, with {soda} and flavored with a little {flavor}.")

print("We have several recommended cocktails to choose from.")
drink = "mojito"
alc = "rum"
mix = "soda"
hint = "mint"

cocktail(drink, alc, mix, hint)

print("hello, I'd like to make you a drink.")
alko = input("What kind of alcohol would you like?")
mixer = input("Let's mix that with a soft drink. Please name your choice.")
spice = input("And how about we add some flavor to spice things up?")
name = input("Finally, give your cocktail a sexy name.")

cocktail(name, alko, mixer, spice)
