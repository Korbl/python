"""
Silly attempt at a quick and dirty parsing script
"""
from datetime import datetime

fname = "chat.log"
oname = "troll_warrior.csv"

totalAttacks = {}

f = open(fname)
lines = f.readlines()
flag = 0 
style = "Auto"
currentTime = 0

FMT = '%H:%M:%S'

for line in lines:
  splitLine = line.split(" ")
  try:
    if splitLine[2] == "perform":
      style = splitLine[4]
      pastTime = currentTime
      flag = 1
      if splitLine[5] != "perfectly!":
        style += " " + splitLine[5]

      if style not in totalAttacks:
        totalAttacks[style] = {}
        totalAttacks[style]['attacks'] = 1
        totalAttacks[style]['damage'] = 0
        totalAttacks[style]['avgTime'] = 0
      else:
        totalAttacks[style]['attacks'] += 1
    elif flag == 1 and splitLine[2] == "attack":
      if splitLine[2] != "enter" and splitLine[3] != "combat":
        currentTime = splitLine[0].strip('[]')
        timeDiff = datetime.strptime(currentTime, FMT) - datetime.strptime(pastTime, FMT)
        timeLine = str(timeDiff)
        timeLine.split(":")
        finalTime = int(timeLine[-1])
      else:
        finalTime = 0

      damage = splitLine[-2]
      totalAttacks[style]['damage'] += int(damage)
      totalAttacks[style]['avgTime'] = (totalAttacks[style]['avgTime'] + finalTime) / 2
      flag = 0
    elif flag == 0 and splitLine[2] == "attack":
      damage = splitLine[-2]
      if splitLine[4] == "mode":
        finalTime = 0      
      else:
        currentTime = splitLine[0].strip('[]')
        timeDiff = datetime.strptime(currentTime, FMT) - datetime.strptime(pastTime, FMT)
        timeLine = str(timeDiff)
        timeLine.split(":")
        finalTime = int(timeLine[-1])
      
      if 'Auto' not in totalAttacks:
        totalAttacks['Auto'] = {}
        totalAttacks['Auto']['damage'] = 0
        totalAttacks['Auto']['attacks'] = 0
        totalAttacks['Auto']['avgTime'] = 0
      else:
        totalAttacks['Auto']['damage'] += int(damage)
        totalAttacks['Auto']['attacks'] += 1
        print(finalTime)
        totalAttacks['Auto']['avgTime'] = (totalAttacks['Auto']['avgTime'] + finalTime) / 2
    else:
     pass 
  except KeyError:
    print("KeyError, key is {}".format(KeyError))
  except Exception as ex:
    pass

print(totalAttacks)