# Author JRI 11/12/21

colors = ["yellow", "black", "green", "red"]
colors.extend(["blue", "orange", "maroon"])

print(colors)
print(colors.count("yellow"))

colors.insert(3, "gray")
print(colors)

clearcolors = colors.clear()
print(clearcolors)

print(colors.count("red"))
