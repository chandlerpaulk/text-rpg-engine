from logic import Logic
import numpy as np

# Initializes Logic for application
engine = Logic(True)

class Avatar():
    def __init__(self, health = 100, name = None, age = None, gender = None, exp = 0, gold = 0, skPoints = 0, inventory = np.array(["Plum", "Water Bottle", "Glow Stick"]), invSize = 15):

        self.health = health
        self.name = name
        self.age = age
        self.gender = gender
        self.exp = exp
        self.gold = gold
        self.skPoints = skPoints
        self.inventory = inventory
        self.invSize = invSize

    # Ask user's name for game engine and store name into Avatar Object
    def askName(self):
        engine.type("What's your name?\n")
        self.name = input("Name: ")
        engine.clear()

    # Ask user's age for game engine and store age into Avatar Object
    def askAge(self):
        engine.type("What's your age?\n")
        self.age = input("Age: ")
        engine.clear()

    # Ask user's gender for game engine and store gender into Avatar Object
    def askGender(self):
        engine.type("What's your gender?\n")
        self.gender = input("Gender: ")
        engine.clear()

    # Displays name of user when called
    def myName(self):
        engine.type("Your name is " + self.name)

    # Displays age of user when called
    def myAge(self):
        engine.type("You are " + self.age + " years old")

    # Displayes gender of user when called
    def myGender(self):
        engine.type("You are a " + self.gender)

    # Experimental health bar idea using emoticons
    def myHealth(self):
        if self.health >= 80:
            engine.type("(^ O ^)")
        elif self.health >= 60:
            engine.type("(' w ')")
        elif self.health >= 40:
            engine.type("(o _ o)")
        elif self.health >= 20:
            engine.type("(~ _ ~)")
        elif self.health > 0:
            engine.type("(- ~ -)")
        elif self.health <= 0:
            engine.type("(X _ X)")

    # Experimentally add item to inventory
    def addItem(self, item):
        if self.inventory.size < self.invSize:
            engine.type("Would you like to add " + item + " to your inventory?")
            res = input("Prompt: ")
            if res == "y":
                engine.next()
                self.inventory.append(item)
                engine.type("Item added to your inventory")
                engine.next()
        else:
            engine.type("Inventory full...")
            engine.next()

    # Experimentally remove item from inventory
    def removeItem(self, item):
        engine.type("Would you like to remove " + item + " from your inventory?")
        res = input("Confirm: ")
        if res == "y":
            engine.next()
            engine.type(item + " is about to be removed from your inventory...")
            res0 = input("Confirm: ")
            if res0 == "y":
                self.inventory.remove(item)
                engine.next()
                engine.type("Item removed")
                engine.next()
            elif res0 == "n":
                engine.next()
                engine.type("Item saved in inventory")
                engine.next()
            else:
                engine.next()
                engine.type("Sorry, I didn't understand that...")
                engine.next()
                self.removeItem(item)
        elif res == "n":
            engine.next()
            engine.type("Item saved in inventory")
            engine.next()
        else:
            engine.next()
            engine.type("Sorry, I didn't understand that...")
            engine.next()
            self.removeItem(item)

    # Experimentally display inventory
    def myInventory(self):
        engine.type(self.inventory)

    # Display character information and stats
    def charStats(self):
        engine.type("Name: ")
        engine.pause(0.5)
        engine.type(self.name)
        engine.pause(0.5)
        engine.type("\n" + "Age: ")
        engine.pause(0.5)
        engine.type(self.age)
        engine.pause(0.5)
        engine.type("\n" + "Gender: ")
        engine.pause(0.5)
        engine.type(self.gender)
        engine.pause(0.5)
        engine.type("\n" + "EXP: ")
        engine.pause(0.5)
        engine.type(str(self.exp))
        engine.pause(0.5)
        engine.type("\n" + "Gold: ")
        engine.pause(0.5)
        engine.type(str(self.gold))
        engine.pause(0.5)
        engine.type("\n\n" + "Does this look correct?\n")
        isCorrect = input("Prompt: ")
        if isCorrect == "y":
            engine.next()
        elif isCorrect == "n":
            engine.next()
            engine.type("Okay, let's update your Avatar...")
            engine.next()
            self.modify()
        else:
            engine.next()
            engine.type("Sorry, I didn't understand that...")
            engine.pause(1.5)
            engine.clear()
            engine.type("Let's try again.")
            engine.next()
            self.charStats()

    # Script for avatar waking up
    def wakeUp(self):

        engine.clear()

        engine.blink(1, 0.04)
        engine.pause(0.8)
        engine.blink(1)

    # Script for creating a new avatar
    def create(self):
        
        self.wakeUp()

        self.askName()
        self.myName()

        engine.next()

        self.askAge()
        self.myAge()

        engine.next()

        self.askGender()
        self.myGender()

        engine.next()

        self.charStats()

        global newAvatar
        newAvatar = Avatar(self.name, self.age, self.gender)

    # Script for modifying an avatar
    def modify(self):

        self.askName()
        self.myName()

        engine.next()

        self.askAge()
        self.myAge()

        engine.next()

        self.askGender()
        self.myGender()

        engine.next()

        self.charStats()