class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
    @property
    def is_alive(self):
        return self.health > 0
    def __repr__(self):
        return "Warrior"

class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = 7
    def __repr__(self):
        return "Knight"

def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        if not unit_2.is_alive: break
        unit_1.health -= unit_2.attack
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

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    print("my_army", my_army)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)
    print("enemy_army", enemy_army)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
