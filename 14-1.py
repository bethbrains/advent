import math

def makeMap(fp):
    map = {}
    for line in fp:
        reactions = line.strip('\n').split(" => ")
        raw_inputs = reactions[0].split(",")
        inputs = {}
        for input in raw_inputs:
            input = input.strip().split(" ")
            inputs[input[1]] = int(input[0])
        output = (reactions[1].split(" ")[1], int(reactions[1].split(" ")[0]))
        map[output] = inputs
    return map


def path_node(map, node, path):
    for sat in map:
        if node == 'ORE':
            return path
        elif node in map[sat]:
            path.append(sat)
            return path.append(path_node(map, sat, path))


def find_path(map, node):
    path = [node]
    path.append(path_node(map, node, path))
    return path


def find_recipe(map, ing):
    for recipe in map:
        if recipe[0] == ing:
            return map[recipe]

def find_min_production(map, ing):
    for recipe in map:
        if recipe[0] == ing:
            return recipe[1]


def anti_refine(map, recipe, production):
    for ingredient in [x for x in list(recipe) if x != 'ORE']:
        print('NEXT INGREDIENT')
        needed_quantity = map[root][ingredient]
        print(f"i need {str(needed_quantity)} of {ingredient}")
        # CHECK WHAT WE ALREADY HAVE
        if ingredient in production:
            on_hand = production[ingredient]
        else:
            on_hand = 0
        print(f"i have {on_hand} {ingredient} on hand")
        # UPDATE NEEDED QUANTITY BY USING WHAT WE HAVE ON HAND
        needed_quantity -= on_hand
        sub_recipe = find_recipe(map, ingredient)
        print(f"recipe for {ingredient}: {sub_recipe}")
        min_prod_of_ingredient = find_min_production(map, ingredient)
        print(f"i need to make {needed_quantity} {ingredient} but my min chunk is {min_prod_of_ingredient}")
        recipe_runs = math.ceil(needed_quantity/min_prod_of_ingredient)
        print(f"so let's run the recipe {recipe_runs} times")
        print(sub_recipe)
        for sub_ingredient in list(sub_recipe):
            print(sub_ingredient)
            prod_qty = recipe_runs * sub_recipe[sub_ingredient]

            # ALLOCATE
            if sub_ingredient in recipe:
                recipe[sub_ingredient] += recipe_runs * sub_recipe[sub_ingredient]
            else:
                recipe[sub_ingredient] = recipe_runs * sub_recipe[sub_ingredient]

        extras = (recipe_runs*min_prod_of_ingredient) - needed_quantity
        del recipe[ingredient]
        production[ingredient] = extras
        print(f"final recipe: {recipe}")
        print(f"leftovers: {production}")
        if len(recipe) == 1 and 'ORE' in recipe:
            return recipe['ORE']
        else:
            return anti_refine(map, recipe, production)

with open('14input.txt') as fp:
    map = makeMap(fp)
    print(map)
    root = ('FUEL', 1)
    recipe = map[root]
    production = {}
    print(anti_refine(map, recipe, production))

    #ore_count = count_ore(map, ('FUEL', 1), 0)
    #print(ore_count)