# Npc-Generator
## What the code does
The code makes 10 completely random non-playable characters (npc's). All of the npc's have random names and ages as well as 3 other different attributes which are 
health, attack power, and exp levels. The code then stores all of the information in separate lists using 'For' loops. Finally the code prints all of the lists out 
to display all of the npc's made. 
## How the code works 
1. The code uses several input statements to get ranges for the random generation of npc attributes
###  
``` ArL = int(input('Enter lowest possible age for NPC: '))```

2. Then the code takes a list of many possible names for a random.choice statement.
###    
``` NpcNames = ['name', 'name', 'name'...] ```

3. The code then uses many lists for name, age, health, attack, and exp level which are randomly generated
###   
``` NpcN = [], for i in range(10): NpcN.append(random.choice(NpcNames) ```

4. After all of this, the code then prints all the lists out
###   
``` for i in range(10): print(lists) ``` 
## Code Highlights
1.  One thing to point out is the amount of names in the list called 'npcN'. This was achieved by using an Ai to get 100 random male names and 100 random female names.
This list can then be used to get a random name for an Npc by running the code ```random.choice(npcN)```.
2. Another thing to highlight is how the lists which stored all the attributes were printed at the end. This was done through running a 'for' loop and printing out all of the lists using an 'f' string to put strings into other expressions. ``` for i in range(10): print(f' Name: {Npcnames[i]}') ``` This 'i' in brackets makes the for loop run for 10 times as it runs for each index 'i'. Then after all of the print statements for the lists are done, one final print statement is used to allow the sets of npcs to be spaced apart instead of close together ``` print('\n'). All of those print statements are also included in the original 'for' loop. 
