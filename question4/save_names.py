# Accept 5 names from the user and save in a file

names = []

for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print("Names have been saved to 'names.txt'.")
