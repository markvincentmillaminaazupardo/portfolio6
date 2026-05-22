# Portfolio 6: My Canteen Cravings List

# **Description:**
# A simple program using lists to track and organize the meals I want to eat.

# My starting list of cravings (Using a List Constant)
my_cravings = ['Pinangat', 'Bicol Express', 'Laing']

# I realized I also want some Pancit Bato, so I'll add it to the end of my list
my_cravings.append('Pancit Bato')

# I want to eat them in alphabetical order so I will sort the list
my_cravings.sort()

# Displaying the final organized list using a definite loop
print("My planned canteen meals for the week:")
for meal in my_cravings:
    print("-", meal)

# Checking if a specific food is in my list using the 'in' logical operator
if 'Bicol Express' in my_cravings:
    print("\nAwesome, Bicol Express is on the menu!")
