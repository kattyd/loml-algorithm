import random

def compare_traits(male, female):
    male = male[:]
    female = female[:]
    
    person1 = male.pop(random.randint(0, len(male) - 1))
    person2 = female.pop(random.randint(0, len(female) - 1))
    
    similar_traits = 0
    for trait_name in person1:
        if person1[trait_name] == person2.get(trait_name):
            similar_traits += 1
    
    total_traits = len(person1) + len(person2)
    percentage_similar = (similar_traits / total_traits) * 100
    
    return (person1["name"], person2["name"], percentage_similar)

male = [{"name": "John", "pets": "birds", "drink": "coke", "habit": "smokes", "religion": "Christian"},
        {"name": "Joshua", "pets": "cats", "drink": "sprite", "habit": "bites nails", "religion": "Agnostic"},
        {"name": "Gerald", "pets": "snakes", "drink": "coke", "habit": "smokes", "religion": "Atheist"},
        {"name": "Ussop", "pets": "dogs", "drink": "ribena", "habit": "drinks", "religion": "Judeaism"},
        {"name": "Lambert", "pets": "none", "drink": "fanta", "habit": "drugs", "religion": "Agnostic"},
        {"name": "Friedmann", "pets": "none", "drink": "tea", "habit": "bites nails", "religion": "Muslim"},
        {"name": "Bazz", "pets": "birds", "drink": "wine", "habit": "drinks", "religion": "Atheist"},
        {"name": "Herbert", "pets": "hamster", "drink": "desperados", "habit": "smokes", "religion": "Agnostic"},
        {"name": "King", "pets": "none", "drink": "water", "habit": "smokes", "religion": "Muslim"},
        {"name": "Hugo", "pets": "snakes", "drink": "sprite", "habit": "drugs", "religion": "Christian"}]

female = [{"name": "Sophie", "pets": "cats", "drink": "coke", "habit": "drugs", "religion": "Atheist"},
        {"name": "Drew", "pets": "birds", "drink": "lemonade", "habit": "smokes", "religion": "Muslim"}, 
        {"name": "Fiona", "pets": "spiders", "drink": "fanta", "habit": "bites nails", "religion": "Hindu"},
        {"name": "Bea", "pets": "dogs", "drink": "wine", "habit": "drinks", "religion": "Christian"}, 
        {"name": "Matilda", "pets": "cats", "drink": "water", "habit": "drugs", "religion": "Agnostic"}, 
        {"name": "Erin", "pets": "goat", "drink": "sprite", "habit": "smokes", "religion": "Judeaism"}, 
        {"name": "Nonnie", "pets": "hamster", "drink": "ribena", "habit": "bites nails", "religion": "Taoism"}, 
        {"name": "Ariel", "pets": "dogs", "drink": "coke", "habit": "drinks", "religion": "Christian"}, 
        {"name": "Kristen", "pets": "snakes", "drink": "tea", "habit": "smokes", "religion": "Muslim"}, 
        {"name": "Vera", "pets": "cats", "drink": "desperados", "habit": "smokes", "religion": "Agnostic"}]

result = compare_traits(male, female)
print("Date:", result[0], "and", result[1])
print("Percentage of similar traits:", result[2])
