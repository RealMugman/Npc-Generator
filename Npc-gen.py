import random
import time
# imports the random and time libraries for use later
ArL = int(input('Enter lowest possible age for NPC: '))
ArH = int(input('Enter highest possible age for NPC: '))
hL = int(input('Enter minimum health: '))
hH = int(input('Enter maximum health: '))
# Inputs for npc age and health ranges
npcN = ["Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Alexander",
        "Jackson", "Sebastian", "Matthew", "Aiden", "Daniel", "Michael", "Logan", "Owen", "Samuel", "David", 
        "Joseph", "Carter", "Wyatt", "John", "Jack", "Luke", "Isaac", "Ethan", "Gabriel", "Anthony",
        "Dylan", "Grayson", "Levi", "Mateo", "Julian", "Hunter", "Christian", "Isaiah", "Jaxon", "Thomas",
        "Chase", "Zachary", "Asher", "Landon", "Eli", "Mason", "Nolan", "Aaron", "Colton", "Adrian",
        "Parker", "Ryder", "Charles", "Cooper", "Jude", "Silas", "Easton", "Emmett", "Harrison", "Ezekiel",
        "Karter", "Maxwell", "Maddox", "Rhett", "Kaden", "Beckett", "Sawyer", "Graham", "Tucker", "Jesse",
        "Bennett", "Gavin", "Luca", "Emmanuel", "Santiago", "Zane", "Jax", "Caleb", "Jett", "Brayden",
        "River", "Kylan", "Dawson", "Felix", "Malachi", "Kyrie", "Dante", "Zander", "Omar", "Khalil",
        "Quentin", "Reed", "Holden", "Finley", "Javier", "Tristan", "Quincy", "Kobe", "Ramon",
        "Olivia", "Emma", "Ava", "Sophia", "Isabella", "Mia", "Amelia", "Harper", "Evelyn", "Abigail",
        "Ella", "Scarlett", "Grace", "Chloe", "Luna", "Aria", "Sofia", "Zoey", "Mila", "Layla",
        "Nora", "Riley", "Avery", "Hannah", "Lily", "Ellie", "Addison", "Lucy", "Maya", "Natalie",
        "Savannah", "Camila", "Brooklyn", "Bella", "Claire", "Skylar", "Audrey", "Violet", "Stella", "Hazel",
        "Aurora", "Samantha", "Anna", "Sadie", "Delilah", "Quinn", "Serenity", "Caroline", "Kinsley", "Allison",
        "Aaliyah", "Cora", "Julia", "Madelyn", "Gianna", "Autumn", "Piper", "Rylee", "Emery", "Bailey",
        "Eva", "Lydia", "Faith", "Marley", "Summer", "Nina", "Sienna", "Molly", "Daisy", "Sloane",
        "Zara", "Leah", "Sophie", "Gia", "Lola", "Clara", "Reagan", "Mckenna", "Aubrey", "Emilia",
        "Tessa", "Kaylee", "Willa", "Arianna", "Elliana", "Cecilia", "Jasmine", "Sabrina", "Morgan", "Renee",
        "Giselle", "Nadia", "Angelina", "Lana", "Ophelia"]
# List of possible npc names

NPCnames = [random.choice(npcN) for i in range(10)]
NPCage = [random.randint(ArL, ArH) for i in range(10)]
NPChealth = [random.randint(hL, hH) for i in range(10)]
NPCattack = [round(random.uniform(1.0, 10.0), 2) for _ in range(10)]  # Generates random attack powers rounded to two decimal places
NPCex = [random.randint(1, 100) for i in range(10)]  
# Generated npc attributes

for i in range(10):
    print(f"  Name: {NPCnames[i]}")
    print(f"  Age: {NPCage[i]}")
    print(f"  Health: {NPChealth[i]}")
    print(f"  Attack Power: {NPCattack[i]}")
    print(f"  Experience: {NPCex[i]}")
    print('\n')
    time.sleep(1) # displays the Npc's one at a time every second
# displays all of the attributes of the Npc's 
