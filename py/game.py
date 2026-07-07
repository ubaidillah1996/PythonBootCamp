class character: # template hero dan monster
    def __init__(self, name: str, health: int, attack_damage: int):
        self.name = name
        self.full_health = health
        self.health = health
        self.attack_damage = attack_damage
        

    def attack(self, target: "character"): # template damage pada hero atau monster
        if self.health == 0 :
            print(f"{self.name} Defeated")
            return
        
        print(f"{self.name} attacking {target.name} for {self.attack_damage} is hurt!")
        target.take_damage(self.attack_damage) # nyawa berkurang bila kena serang
    
    def take_damage(self, amount: int): # template kira nyawa diserang dan berapa baki tinggal
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} has {self.health}/{self.health}HP left")

    def heal(self, amount:int): # input validate, nyawa kosong takleh heal
        if self.health == 0:
            print(f"{self.health} is dead and cant heal!")
            return
        
        self.health += amount # nyawa bertambah
        if self.health > self.full_health:
            self.health = self.full_health


            print(f"{self.name} healed {amount} HP.")
            print(f"{self.name} now has {self.health}/{self.full_health}HP. ")

# Buat 2 watak. hero dan monster
hero = character(name="Bobo", health=100, attack_damage=25)
monster = character(name="Bubu", health=90, attack_damage= 20)

print("Fight!")
hero.attack(monster) # hero serang monster # sword = damage
monster.attack(hero) # monster serang hero # casting spell = damage
hero.heal(22) # hero healing

## nota tambahan : polymorphism
# method sama, hasil berbeza.
# okey faham. kalau matematik, kira shape, cara kira sama, hasil berbeza.