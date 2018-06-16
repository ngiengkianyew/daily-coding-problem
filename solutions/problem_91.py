# The function prints nine because it uses the variable
# i to determine what to return and i finishes looping
# at 9

functions = []
for i in range(10):
    functions.append(lambda: i)

i = 0
for f in functions:
    print(f())
    i += 1
