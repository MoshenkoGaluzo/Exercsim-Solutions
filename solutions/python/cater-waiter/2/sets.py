"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):

    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    
    if len(set(drink_ingredients).intersection(ALCOHOLS)) == 0:
        return drink_name + " Mocktail"
        
    return drink_name + " Cocktail"


def categorize_dish(dish_name, dish_ingredients):
   
    if dish_ingredients.issubset(VEGAN):
        return dish_name + ": VEGAN"
    if dish_ingredients.issubset(VEGETARIAN):
        return dish_name + ": VEGETARIAN"
    if dish_ingredients.issubset(PALEO):
        return dish_name + ": PALEO"
    if dish_ingredients.issubset(KETO):
        return dish_name + ": KETO"
    if dish_ingredients.issubset(OMNIVORE):
        return dish_name + ": OMNIVORE"


def tag_special_ingredients(dish):
    
    return (dish[0], set(dish[1]).intersection(SPECIAL_INGREDIENTS))


def compile_ingredients(dishes):
    
    finalset = set()
    for l in dishes:
        finalset = finalset.union(l)
    return finalset


def separate_appetizers(dishes, appetizers):
    
    return list(set(dishes).difference(set(appetizers)))


def singleton_ingredients(dishes, intersection):
    
    finalset = dishes[0]
    for dish in dishes[1:]:
        finalset = finalset.symmetric_difference(dish)
    finalset = finalset.difference(intersection)
    return finalset
