num_ingredients = int(input("Digite a quantidade de ingredientes necessários para a receita: "))

recipe_ingredients = []
qty_ingredients_Sinmber = []
necessary_ingredients = []

def coxinhaDeJaca():
    i = 0
    while i < num_ingredients:
        qty_ingredients = int(input("Digite a quantidade de cada ingrediente necessário para a receita: "))
        recipe_ingredients.append(qty_ingredients)
        qty_Sinmber = int(input("Digite a quantidade de ingredientes que Sinmber possui: "))
        qty_ingredients_Sinmber.append(qty_Sinmber)

        if recipe_ingredients[i] > qty_ingredients_Sinmber[i]:
            return "Sinmber não conseguirá fazer coxinhas de jaca :("
        else:
            divided_ingredients = qty_ingredients_Sinmber[i]/recipe_ingredients[i]
            necessary_ingredients.append(divided_ingredients)  
            sorted(necessary_ingredients)
        i+=1
    return f"Sinmber conseguirá fazer {necessary_ingredients[i - 1]} receitas de coxinha de jaca ^^"

print(coxinhaDeJaca())
