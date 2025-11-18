from random import randint
import requests
from datetime import datetime, timedelta

class Pokemon:
    pokemons = {}
    # Object initialization (constructor)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp=randint(100,150)
        self.power=randint(15,20)
        self.last_feed_time=datetime.now()

        Pokemon.pokemons[pokemon_trainer] = self

        
    # Method for getting Pokemon image via API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "Pikachu"
        
    # Method for getting Pokemon name via API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Class method for getting information
    def info(self):
        return f"Your Pokemon's name: {self.name}, your Pokemon's strength: {self.power}, your Pokemon's health: {self.hp}"

    # Class method for getting a picture of a Pokemon
    def show_img(self):
        return self.img
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Check that the enemy is of type Wizard (is an instance of the Wizard class)
            chance = randint(1,5)
            if chance == 1:
                return "The Wizard Pokemon used a shield in battle."
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Fighting @{self.pokemon_trainer} with @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Victory @{self.pokemon_trainer} over @{enemy.pokemon_trainer}! "
        
    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Pokemon's health has been increased. Current health: {self.hp}"
        else:
            return f"Next time to feed your Pokemon: {self.last_feed_time+delta_time}"
    
class Wizard(Pokemon):
    def feed(self):
        return super().feed(hp_increase=20)
  
class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        res = super().attack(enemy)
        self.power -= super_power
        return res + f"\nThe fighter used a super attack with force: {super_power} "
    
    def feed(self):
        return super().feed(feed_interval=10)
