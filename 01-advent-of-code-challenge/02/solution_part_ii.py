# x = LOSE
#rock/1
# y = DRAW
#paper/2
# z = WIN
#scissors/3

#lost = 0
#draw = 3
#win = 6

def GAME(filename):

    with open(filename, "r") as list:
        input = list.read()
        score = 0

    matches = input.splitlines()

    for game in matches:
      #paper
      if(game[0] == "B"):
        if(game[2] == "X"):
          score = score + 1
        elif(game[2] == "Y"):
          score = score + 5
        else:
          score = score + 9
      #rock
      elif(game[0] == "A"):
        if(game[2] == "X"):
          score = score + 3
        elif(game[2] == "Y"):
          score = score + 4
        else:
          score = score + 8
      #scissors
      elif(game[0] == "C"):
        if(game[2] == "X"):
          score = score + 2
        elif(game[2] == "Y"):
          score = score + 6
        else:
          score = score + 7

    

    return score

filename = "01-advent-of-code-challenge/02/sample.in"
print(GAME(filename))