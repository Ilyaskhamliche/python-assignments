years_list = [year for year in range(1995, 2000)]
third_birthday_year = years_list[2]
oldest_year = years_list[-1]
things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].capitalize()
things[0] = things[0].upper()
things.remove("salmonella")
surprise = ["Groucho", "Chico", "Harpo"]
surprise[-1] = surprise[-1].lower()[::-1].capitalize()
even = [num for num in range(10) if num % 2 == 0]
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"

for first, second in rhymes:
    # First line
    print(" ".join(word.capitalize() + "!" for word in start1) + " " + first.capitalize() + "!")
    
    # Second line
    print(start2 + " " + second + ".")

# Print results
print("7.1:", years_list)
print("7.2:", third_birthday_year)
print("7.3:", oldest_year)
print("7.4:", things)
print("7.8:", surprise)
print("7.10:", even)
