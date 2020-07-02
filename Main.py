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
    "",
    "",
    "",
    "",
    ""
)

onequestions = (
    "",
    "",
    "",
    "",
    ""
)

twoquestions = (
    "",
    "",
    "",
    "",
    ""
)

threequestions = (
    "",
    "",
    "",
    "",
    ""
)

fourquestions = (
    "",
    "",
    "",
    "",
    ""
)

fivequestions = (
    "",
    "",
    "",
    "",
    ""
)

sixquestions = (
    "",
    "",
    "",
    "",
    ""
)

sevenquestions = (
    "",
    "",
    "",
    "",
    ""
)

eightquestions = (
    "",
    "",
    "",
    "",
    ""
)

ninequestions = (
    "",
    "",
    "",
    "",
    ""
)

# --- MAIN
print("Welcome to the NHL Player guesser! Here you will have to guess a certain NHL player based upon the description given")

player = random.randrange(len(Players))
print(player)

if player == 0:
    pass
elif player == 1:
    pass
elif player == 2:
    pass
elif player == 3:
    pass
elif player == 4:
    pass
elif player == 5:
    pass
elif player == 6:
    pass
elif player == 7:
    pass
elif player == 8:
    pass
elif player == 9:
    pass
else:
    print("something went wrong")