import random
import time
mystr = "This is a sentance about the hobgoblin Jace"
list_of_words = mystr.split() # if we specify nothing, it will split on " "
print(list_of_words)
list_of_words[-1] = "Mykyta"
print(list_of_words)
mystr = " ".joi(list_of_words)
print(mystr)
# simulated csv (comma separated values)
str2 = "name,type,strength,health"
p1 = "zach,orc,50000000,1"
p2 = "isaac,loot goblin,1,50000000"
headers = str2.split(",")
p1_list = p1.split(",")
p2_list = p2.split(",")
# iterate through p1_list with index and value (with enumerate)
for idx, val in enumerate(p1_list):
    print(f"{headers[idx]}: {val}")

for idx, val in enumerate(p2_list):
    print(f"{headers[idx]}: {val}")

playerlists = [p1_list, p2_list]
p1_list.append(0)
p2_list.append(0)
print(f"it's the big battle of {p1_list[0]} the {p1_list[1]} vs {p2_list[0]} the {p2_list[1]}")
input("Enter to continue")
for i in range(5):
    print(f"Round {i+1}")
    choice = random.randint(0,2)
    outcome = []
    if choice < 2:
        attacker = playerlists[choice]
        defender = playerlists[1-choice]
        outcome.append(attacker[0])
        playerlists[choice][-1] += 1
        print(f"{attacker[0]} delivered {attacker[2]} damage to {defender[0]} and defeated him/her")
    else:
        outcome.append("tie")
        print("It was a tie")
    time.sleep(3)

print(f"{p1_list[0]} won {p1_list[-1]} rounds")
print(f"{p2_list[0]} won {p2_list[-1]} rounds")
if p1_list[-1] > p2_list[-1]:
    print(p1_list[0], "won!")
elif p1_list[-1] < p2_list[-1]:
    print(p2_list[0], "won!")
else:
    print("tie")