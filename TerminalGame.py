# Basic Python Terminal Game
# Sam Armitage
# Started 20/06/23

# Import libs
import random
import time

# Player Class
class Player:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.exp = 0
        self.level = 0
        self.max_health = 10
        self.inventory = []

    def __repr__(self):
        return f"\n{self.name} is level {self.level} and has {self.health}/{self.max_health} health left!"
    
    def use_item(self, item):
        if item in self.inventory:
            if item.level_required <= self.level:
                item_location = self.inventory.index(item)
                self.inventory.pop(item_location)
                item_list.append(item)
                random_num = random.randint(0,100)
                if random_num < item.risk_to_damage * 100:
                    self.health -= item.heal_amount
                    print(f"{item.heal_amount} damaged. {self.health} health left.")
                    if self.health <= 0:
                        print(f"Sorry {self.name}, you have become mulch to feed the trees. Please reload the game to try again...")
                        quit()
                else:
                    self.health += item.heal_amount
                    if self.health > self.max_health:
                        self.health = self.max_health
                    print(f"{item.heal_amount} healed. {self.health} health left.")
            else:
                print("\nYou aren't a high enough level to use this!")
        else:
            print("Item exception, not owned.")
        

    def give_exp(self, exp_to_give):
        self.exp += exp_to_give
        self.level = round(self.exp/10)
        self.max_health = 10 + self.level

    def self_damage(self, damage_amount):
        self.health -= damage_amount
        if self.health <= 0:
            print(f"\nSorry {self.name}, you have become mulch to feed the trees. Please reload the game to try again...")
            quit()

    def give_item(self, item):
        if type(item) == Item:
            self.inventory.append(item)
            item_list.pop(item_list.index(item))
        else:
            print(f"{item} is not a legitimate item. Coding bug.")
    
    def see_inventory(self):
        if len(self.inventory) == 0:
            print("\nYou have no items left...")
        elif len(self.inventory) == 1:
            print(f"\nYou have a singular item in your inventory, this is a {self.inventory[0]}.")
            inv_input = input("\nWould you like to inspect an inventory item in more detial? (y/n)\n").lower()
            if inv_input == 'y':
                print("\nWhat item would you like to inspect?")
                inventory_length = len(player_save.inventory)
                for i in range(1, inventory_length+1):
                    print(f"{i}: {player_save.inventory[i-1]}")
                inventory_choice = int(input())
                if inventory_choice <= inventory_length:
                    player_save.inventory[inventory_choice-1].item_info()
                else:
                    print("\nInvalid choice")
            else:
                pass            
        else:
            print(f"\nYou have {len(self.inventory)} items in your inventory, these are: \n{self.inventory}.")
            inv_input = input("\nWould you like to inspect an inventory item in more detial? (y/n)\n").lower()
            if inv_input == 'y':
                print("\nWhat item would you like to inspect?")
                inventory_length = len(player_save.inventory)
                for i in range(1, inventory_length+1):
                    print(f"{i}: {player_save.inventory[i-1]}")
                inventory_choice = int(input())
                if inventory_choice <= inventory_length:
                    player_save.inventory[inventory_choice-1].item_info()
                else:
                    print("\nInvalid choice")
            else:
                pass               

# Item Class
class Item:
    def __init__(self, name, level_required, heal_amount, description, risk_to_damage = 0):
        self.name = name
        self.heal_amount = heal_amount
        self.level_required = level_required
        self.description = description
        self.risk_to_damage = risk_to_damage
    
    def __repr__(self):
        return self.name
    
    def item_info(self):
        print(f"\n{self.name} is a level {self.level_required} item, which could heal you by {self.heal_amount}. \n\nGeneral Description:\n{self.description}.")

# Item creation & Enemy Names List
stew1 = Item("Suspicious Stew", 0, 5, "An odd smell looms, I am not sure if I should try this",0.6)
stew2 = Item("Suspicious Stew (2)", 0 , 3, "This doesnt smell too bad, maybe give it a go?", 0.1)
stew3 = Item("Suspicious Stew (3)", 2 , 5, "Smells like roses... hmmm...", 0.5)
pie = Item("Pie", 1, 2, "Just like mum used to make!")
apple = Item("Apple", 0 , 1, "Ripe and tasty!")
feast = Item("Delicious Feast", 0 , 5, "I dont think it gets better than this!")
item_list = [stew1,stew2,stew3,pie,pie,pie,pie,apple,apple,apple,apple,feast,feast,feast] # Multiple Instances balances the game (ie not many stew's given)

enemy_names = ["Goblin", "Zombie", "Angry Villager", "Dwarf", "Bear", "Witch", "Wizard"]

# Randomly select which mini-game to play as the 'fight'
def game_type_gen(player):
    if player.level < 1:
        return 1
    elif player.level <= 5:
        return random.randint(1,2)
    elif player.level > 12:
        return 4 # This is going to relate to the 'boss' fight to end the game
    else:
        return random.randint(1,3)
    
# Have a turn function
sleep_timer = 1
def player_move(player):
    print("\nYou continue to wander...")
    time.sleep(sleep_timer)
    print("\n...")
    time.sleep(sleep_timer)

    if random.randint(0,2) < 2:
        enemy_encountered = enemy_names[random.randint(0,len(enemy_names)-1)]
        enemy_game = game_type_gen(player)
        enemy_exp = (player.level+1)*random.randint(1,5)
        print(f"\n{enemy_encountered} attacks you! Game type: {enemy_game}. Exp: {enemy_exp}.")
        player_win = False
        
        if enemy_game == 1: # 3 Guesses for higher or lower
            print(f"{enemy_encountered} gives you 5 chances to guess their magic number between 0 and 50.")
            counter = 0
            computer_number = random.randint(0,50)
            while counter < 5:
                player_game_input = int(input("\nHave a guess...\n"))
                counter += 1
                if player_game_input == computer_number:
                    print("\nYou win!")
                    counter = 10
                    player_win = True
                elif player_game_input < computer_number:
                    print("\nHigher...")
                else:
                    print("\nLower...")
        
        elif enemy_game == 2: # Win one game of rock paper scissors?
            print(f"\n{enemy_encountered} challenges you to a game of rock, paper, scissors,")
            outcome = False
            r_p_s_list = ['r','p','s']
            r_p_s_print_list = ["Rock", "Paper", "Scissors"]
            while outcome == False:
                player_game_input = input("\nRock, Paper or Scissors... (input, 'r', 'p' or 's')\n").lower()
                player_game_number = r_p_s_list.index(player_game_input)
                computer_number = random.randint(0,2)
                if player_game_number == computer_number:
                    print(f"You both chose {r_p_s_print_list[player_game_number]}, its a tie. Try again.")
                elif (player_game_number == 0) and (computer_number == 2):
                    player_win = True
                    outcome = True
                    print("\nYou win!")
                elif (player_game_number == 1) and (computer_number == 0):
                    player_win = True
                    outcome = True
                    print("\nYou win!")
                elif (player_game_number == 2) and (computer_number == 1):
                    player_win = True
                    outcome = True
                    print("\nYou win!")
                else:
                    print("\nYou have been bettered this time!")
                    player_win = False
                    outcome = True

        elif enemy_game == 3: # Single guess the number, the distance off deals that much damage
            pass
        elif enemy_game == 4: # 
            pass
        else:
            print("Error, game not found.")

        if player_win == True:
            player.give_exp(enemy_exp)
        else:
            player.self_damage(enemy_exp) # Used this, as it scales as a player progresses
            print(f"\nYou have taken {enemy_exp} damage! You have {player.health}/{player.max_health} health left!")


    else:
        random_item = item_list[random.randint(0,len(item_list)-1)]
        player.give_item(random_item)
        print(f"\nIt's your lucky day, you found a {random_item}!")

## Main Section
# Get player name and create class instance
print("Hello and welcome to the Terminal choice based game...")
#player_name = input("\nWhat is your name?\n")
player_name = "Sam"
player_save = Player(player_name)
player_save.give_item(apple)
player_save.give_item(apple)

# Start of main game
toggle_play = True
while toggle_play == True:
    print("\nWhat would you like to do?")
    print("1: Make a turn")
    print("2: See a player status")
    print("3: See your inventory")
    print("4: Use an item")
    print("5: Manually end game\n")
    player_inp = int(input())

    if player_inp == 1: # Play Turn
        purpetual_play = True
        
        while purpetual_play == True:
            player_move(player_save)
            keep_playing = input("\nY/N, would you like to go back to the main menu?\n").lower()
            if keep_playing == 'y':
                purpetual_play = False

    elif player_inp == 2: # See player status
        print(player_save)
    
    elif player_inp == 3: # See inventory
        player_save.see_inventory()

    elif player_inp == 4: # Use an item
        if player_save.health != player_save.max_health:
            if len(player_save.inventory) != 0:
                print("\nWhat item would you like to use?")
                inventory_length = len(player_save.inventory)
                for i in range(1, inventory_length+1):
                    print(f"{i}: {player_save.inventory[i-1]}")
                inventory_choice = int(input())
                if inventory_choice <= inventory_length:
                    player_save.use_item(player_save.inventory[inventory_choice-1])
                else:
                    print("\nInvalid choice")
            else:
                print("\nYou have no items to use!")
        else:
            print("\nYou cannot heal, as you already have max health!")

    elif player_inp == 5: # End Game
        toggle_play = False

    else:
        print("\nInvalid input!")
