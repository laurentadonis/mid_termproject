#Project midterm create card game,
#Ask user to play
from game_task import userInput


def yesNo (options):
    question_list = [
     "Are you ready to play (y/n):\n",
     "Do you want to play again (y/n):\n",
     "Type 'y' to get another card: Type 'n' to stop:"
    ]
    while True:
     UserAnswer = input(yesNo(options))
     if UserAnswer ==  "y" or UserAnswer == "n":
       return UserAnswer