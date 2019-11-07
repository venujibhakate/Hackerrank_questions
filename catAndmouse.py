def catAndMouse(x, y, z):
    cat_a = (x - z)
    cat_b = (y - z)
    
    if cat_a < cat_b:
        return "Cat A"
    elif cat_a > cat_b:
        return "Cat B"
    else:
        return "Mouse C"
print(catAndMouse(2,5,4))



