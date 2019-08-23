class Warrior:
    def __init__(self, health = 50, attack = 5, defence = 0):
        self.health = health
        self.attack = attack
        self.defence = defence
    def hit(self, enemy):
        enemy.loss(self.attack)
    def loss(self, hits):
        self.health -= hits
        return hits
    @property
    def is_alive(self):
        return self.health > 0
    def __repr__(self):
        return "Warrior"

class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self, 50, 7)
    def __repr__(self):
        return "Knight"

class Defender(Warrior):
    def __init__(self):
        Warrior.__init__(self, 60, 3, 2)
    def loss(self, hits):
        if self.defence < hits:
            lost = hits - self.defence
            self.health -= lost
        else:
            lost = 0
        return lost
            
    def __repr__(self):
        return "Defender"

class Vampire(Warrior):
    MAX_HEALTH = 40
    def __init__(self):
        Warrior.__init__(self, 40, 4)
        self.vampirism = 0.5
    def hit(self, enemy):
        hp = enemy.loss(self.attack) * self.vampirism
        self.health += hp
        self.health = min(self.health, Vampire.MAX_HEALTH)
        

def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_1.hit(unit_2)
        if not unit_2.is_alive: break
        unit_2.hit(unit_1)
        
    return unit_1.is_alive

class Army:
    def __init__(self):
        self.units = []
    
    def add_units(self, typ, count):
        for i in range(count):
            self.units.append(typ())

    def is_empty(self):
        return len(self.units) <= 0

    def __repr__(self):
        return str(len(self.units)) + ": " + str(self.units)        


class Battle:
    def fight(self, army1, army2):
        while not army1.is_empty() and not army2.is_empty():
            if fight(army1.units[0], army2.units[0]):
                army2.units.pop(0)
            else:
                army1.units.pop(0)
        return not army1.is_empty()

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")
