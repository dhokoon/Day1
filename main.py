#1. Create a greeting for your program.
print('''Hi and welome to the Band Name generator.
This program will generate the name of your band.
Please enter in the following information to generate your band name.
            ROCK ON!!!\n''')
#2. Ask the user for the city that they grew up in.
question1 = input(str("What is the name of the city you grew up in? \n"))
answer1 = str(question1.capitalize())
#3. Ask the user for the name of a pet.
question2 = input("\nWhat is the name of your pet? \n")
answer2 = question2.capitalize()
#4. Combine the name of their city and pet and show them their band name.
print(f"\nThe name of your band would be called:\n{answer1} {answer2}")
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end 