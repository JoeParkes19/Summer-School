'''
Title: Python Document 
Date: 02-07-2020
Name: Joseph Parkes
'''

import random

# My lists to ease the randomization of the players and questions
Players = (
    "McDavid",
    "Kane",
    "Matthews",
    "Pastrnak",
    "Marchand",
    "Draisaitl",
    "Subban",
    "Gaudreau",
    "Pettersson",
    "Lucic"
)

zeroquestions = (
    "He was the 1st overall pick in the 2015 NHL Draft",
    "He plays for the Edmonton Oilers",
    "He is Canadian",
    "He has no previous teams",
    "He was on the cover of NHL 18"
)

onequestions = (
    "He was the 1st overall pick in the 2007 NHL Draft",
    "He plays for the Chicago Blackhawks",
    "He is American",
    "He has no previous teams",
    "He was on the cover of NHL 16"
)

twoquestions = (
    "He was the 1st overall pick in the 2016 NHL Draft",
    "He plays for the Toronto Maple Leafs",
    "He is American",
    "He has no previous teams",
    "He was on the cover of NHL 2020"
)

threequestions = (
    "He was the 25th overall pick in the 2014 NHL Draft",
    "He plays for the Boston Bruins",
    "He is Czech",
    "He has no previous teams",
    "He wears 88 for the Bruins "
)

fourquestions = (
    "He was the 71st overall pick in the 2006 NHL Draft",
    "He plays for the Boston Bruins",
    "He is Canadian",
    "He has no previous teams",
    "He wears 63 for the Bruins"
)

fivequestions = (
    "He was the 3rd overall pick in the 2014 NHL Draft",
    "He plays for the Edmonton Oilers",
    "He is German",
    "He has no previous teams",
    "He had the most points in the 2019-20 season"
)

sixquestions = (
    "He was the  overall pick in the  NHL Draft",
    "He plays for the New Jersey Devils",
    "He is Canadian",
    "He has also played for the Montreal Canadians & Nashville Predators",
    "He was on the cover of NHL 19"
)

sevenquestions = (
    "He was the 104th overall pick in the 2011 NHL Draft",
    "He plays for the Calgary",
    "He is American",
    "He has no previous teams",
    "He can be known as ______ Hockey"
)

eightquestions = (
    "He was the 5th overall pick in the 2017 NHL Draft",
    "He plays for the Vancouver Cannucks",
    "He is Swedish",
    "He has no previous teams",
    "He wears 40 for the Vancouver Cannucks"
)

ninequestions = (
    "He was the 50th overall pick in the 2006 NHL Draft",
    "He plays for the Calgary Flames",
    "He is Canadian",
    "He has also played for the Edmonton Oilers, Boston Bruins & Los Angeles Kings",
    "He was very overpaid by the Edmonton Oilers during the 2016 free agency period"
)

# --- Main Code
print("Welcome to the NHL Player guesser! Here you will have to guess a certain NHL player based upon the description given")

player = 0
print(player)

if player == 0:
    choice0 = random.randrange(len(zeroquestions))
    print(zeroquestions[choice0])
elif player == 1:
    choice1 = choice = random.randrange(len(onequestions))
    print(onequestions[choice1])
elif player == 2:
    choice2 = random.randrange(len(twoquestions))
    print(twoquestions[choice2])
elif player == 3:
    choice3 = random.randrange(len(threequestions))
    print(threequestions[choice3])
elif player == 4:
    choice4 = random.randrange(len(fourquestions))
    print(fourquestions[choice4])
elif player == 5:
    choice5 = random.randrange(len(fivequestions))
    print(fivequestions[choice5])
elif player == 6:
    choice6 = random.randrange(len(sixquestions))
    print(sixquestions[choice6])
elif player == 7:
    choice7 = random.randrange(len(sevenquestions))
    print(sevenquestions[choice7])
elif player == 8:
    choice8 = random.randrange(len(eightquestions))
    print(eightquestions[choice8])
elif player == 9:
    choice9 = random.randrange(len(ninequestions))
    print(ninequestions[choice9])
else:
    print("Something went wrong!")