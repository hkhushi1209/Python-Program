setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)
print(setx.difference(sety))  # Difference of two sets
print (setx.union(sety))
print(setx.symmetric_difference(sety))