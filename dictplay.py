recipe = {
    "flour" : "1 kg",
    "sugar" : "1 cup",
    "vanilla": "1 spoon",
}

recipe["eggs"] = 2
print(recipe)

recipe.update({"chocolate": "3 squares"})

print(recipe)