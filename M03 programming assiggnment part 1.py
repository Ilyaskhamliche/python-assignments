years_list = [year for year in range(2003,2009)]
third_birthday_year = years_list[3]
oldest_year = years_list[5]
things = ["mozzarella", "cinderella", "salmonella"]
things[1] = things[1].capitalize()
things[0] = things[0].upper()
things.remove("salmonella")

print("7.1:", years_list)
print("7.2:", third_birthday_year)
print("7.3:", oldest_year)
print("7.4:", things)
