# A list
MY_LIST = ['Manny', 'Moe', 'Jack']
# A dictionary (dict)
FOOTBALL_TEAM_LOCATIONS = {
        'Broncos': 'Denver',
        'Seahawks': 'Seattle'
        }
# A string
MY_STRING = 'Python is fun'

for item in MY_LIST:
    print item

# For loop with tuple
for (key, value) in FOOTBALL_TEAM_LOCATIONS.items():
    print key, value


# Initialization
value = 'bar'
value_is_foo = False

if value == 'foo':
    value_is_foo = True

print value_is_foo
# Multiple assignment, star means "the rest of the list"
manny, moe, jack = MY_LIST

print manny, moe, jack
