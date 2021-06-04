days_per_month = {'January': 31, 'February': 28, 'March': 31}
print(days_per_month)
for month, days in days_per_month.items():
    print(f'{month} has {days} days')

roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 100}
print(f"dictionary roman_numerals: {roman_numerals}")
print(f"accessing the value associated with a key V: {roman_numerals['V']}")

roman_numerals['X'] = 10
print(f"Updating the Value of an Existing Key–Value Pair: {roman_numerals}")

roman_numerals['L'] = 50
print(f"Adding a New Key–Value Pair: {roman_numerals}")

del roman_numerals['III']
print(f"Removing a Key–Value Pair: {roman_numerals}")

print('V' in roman_numerals)

months = {'January': 1, 'February': 2, 'March': 3}
for month_name in months.keys():
    print(month_name, end=' ')


for month_number in months.values():
    print(month_number, end=' ')

country_capitals1 = {'Belgium': 'Brussels', 'Haiti': 'Port-au-Prince'}
country_capitals2 = {'Nepal': 'Kathmandu', 'Uruguay': 'Montevideo'}
country_capitals3 = {'Haiti': 'Port-au-Prince', 'Belgium': 'Brussels'}


print(country_capitals1 == country_capitals2)

print(country_capitals1 == country_capitals3)
print(country_capitals1 != country_capitals2)

from collections import Counter
text = ('this is sample text with several words ' 'this is more sample text with some different words')
counter = Counter(text.split())
for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')

print('Number of unique keys:', len(counter.keys()))

from collections import Counter
text = ('this is sample text with several words ' 'this is more sample text with some different words' 'this is even more words added')
counter = Counter(text.split())
for word, count in sorted(counter.items()):
    print(f'{word:<12}{count}')

print('Number of unique keys:', len(counter.keys()))


colors = {'red', 'orange', 'yellow', 'green', 'red', 'blue'}
print(f"this is a set: {colors}")
print(f"this is len of above set: {len(colors)}")
print(f"check if red in colors: {'red' in colors}")

for color in colors:
    print(color.upper(), end=' ')

numbers = list(range(10)) + list(range(5))
print(numbers)

print({1, 2, 3} == {3, 2, 4})

print({1, 3, 5} | {2, 3, 4})

print({1, 3, 5}.union([20, 20, 3, 40, 40]))

print({1, 3, 5} & {2, 3, 4})
print({1, 3, 5}.intersection([1, 2, 2, 3, 3, 4, 4]))

print({1, 3, 5} - {2, 3, 4})
print({1, 3, 5, 7}.difference([2, 2, 3, 3, 4, 4]))
 
print({1, 3, 5} ^ {2, 3, 4})
print({1, 3, 5, 7}.symmetric_difference([2, 2, 3, 3, 4, 4]))

print({1, 3, 5}.isdisjoint({2, 4, 6}))
print({1, 3, 5}.isdisjoint({4, 6, 1}))

numbers = {1, 3, 5}
numbers |= {2, 3, 4}
print(numbers)

numbers.update(range(10))
print(numbers)

numbers.add(17)
print(numbers)

numbers.remove(3)
print(numbers)

numbers.clear()
print(numbers)