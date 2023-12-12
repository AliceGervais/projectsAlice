# Create a secret santa process
welcome = "SECRET SANTA - Welcome to this Secret Santa creator!"

print(welcome)

# 1. enter the participants
part_from=[]

part_nb = input("Number of participants: ")
part_nb = int(part_nb)

n=1
while n <= part_nb:
    part_from.append(input("Please enter the name of person "+str(n)+": "))
    n+=1
print("These are your participants: ", part_from)

#2. Attribute the presents
import random
part_to =[]
part_temp=part_from.copy()
n=0

while len(part_to) < len(part_from):
    i = random.randint(0,len(part_temp)-1)
    while part_temp[i]==part_from[n]:             #avoiding that someone picks themselves
       i = random.randint(0,len(part_temp)-1)
    name = part_temp[i]
    part_to.append(part_temp.pop(i))
    n=n+1

result= dict(zip(part_from,part_to))

for key, value in result.items():
    print(key, "should give a present to", value)