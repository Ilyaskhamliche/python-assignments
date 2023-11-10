def good():
    return ['Harry', 'Ron', 'Hermione']
good_list = good()
print(good_list)

def get_odds():
    for num in range(10):
        if num % 2 == 1:
            yield num
# Use a for loop to find and print the third odd value returned
count = 0
for odd in get_odds():
    count += 1
    if count == 3:
        print("Third odd value:", odd)
        break
