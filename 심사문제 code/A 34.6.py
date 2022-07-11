class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        d = self.ability_power * 0.65 + 400
        print('티버: %f' %d)

health, mana, ability_power = map(float, input().split())
x = Annie(health = health, mana = mana, ability_power = ability_power)
x.tibbers()