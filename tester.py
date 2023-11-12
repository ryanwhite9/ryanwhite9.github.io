x = 10

y = 20

def logans_first_function(x, y):
    if x < y:
        print("True")

    if y > x:
        print( str(y) + " is greater than " + str(x))

    return x + y


i = logans_first_function(x, y)

print(i)