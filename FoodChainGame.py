#Food Chain Game Using Python - www.101computing.net/food-chain-game-using-python/
import random
organisms = ["grass" , "insect" , "rabbit", "slug", "frog", "vole", "thrush", "fox", "hawk"]
organismsLength = len(organisms)

#Select organism for player
playerPosition = random.randint(0,organismsLength-1)
playerOrganism = organisms[playerPosition]
print("Player Organism: " + playerOrganism)

#Select organism for computer
computerPosition = random.randint(0,organismsLength-1)
#Ensure that the computer organism will be different from the player organism
while computerPosition==playerPosition:
  computerPosition = random.randint(0,organismsLength-1)

computerOrganism = organisms[computerPosition]
print("Computer Organism: " + computerOrganism)
 
foodWeb = {'grass': [''],
           'insect': ['grass'],
           'rabbit': ['grass'],
           'slug': ['grass'],
           'thrush': ['slug','insect'],
           'vole': ['insect'],
           'frog': ['insect'],
           'hawk': ['frog','vole','thrush'],
           'fox': ['rabbit','frog','vole']}

#Complete code here to find out if the computer organism and the player organism are linked (Direct link or indirect link)
def player_link():
  #enum through values and see if player = CPU
  
  if playerOrganism in foodWeb[computerOrganism]:
    return 1
  elif computerOrganism in foodWeb[playerOrganism]:
    return 2
  else:
    return 0

print ("\n")
print ("Is there a link?:")
if player_link() != 0:
  print("Yes")
else:
  print("No")


#If a link is detected decide who between the computer and the player wins the game
if player_link() == 1:
  print ("Computer Wins!")
elif player_link() == 2:
  print ("Player Wins!")

