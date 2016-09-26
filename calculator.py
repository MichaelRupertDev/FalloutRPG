import argparse
from random import randint
skill = 40
distance = 200

hit_percent = min(100, ((skill/2) + max(0, (100-distance*2))) + randint(0, 12))

class Character():
    strength = 5
    perception = 5
    endurance = 5
    charisma = 5
    intelligence = 5
    agility = 5
    luck = 5

    dmg_resist = 0
    HP = 200
    skill_points = 15

    skills = {
        'barter': 15,
        'big_guns': 15,
        'energy_weapons': 15,
        'explosives': 15,
        'lockpick': 15,
        'medicine': 15,
        'melee_weapons': 15,
        'pilot': 15,
        'repair': 15,
        'science': 15,
        'small_guns': 15,
        'sneak': 15,
        'speech': 15,
        'steal': 15,
        'survival': 15,
        'unarmed': 15}

    perks = {
        'small_frame': False}

    rads = 0

    @property
    def carry_weight(self):
        if not self.perks.get('small_frame'):
            return 50 + self.strength * 10
        else:
            return 50 + self.strength * 5

    @property
    def AP(self):
        return 1 + self.agility

    @property
    def crit_chance(self):
        return self.luck

    @property
    def starting_HP(self):
        return (self.endurance + self.strength) * 5

    @property
    def melee_damage(self):
        return 1 + self.stat_from_range('strength')

    def stat_from_range(self, stat):
        level = getattr(self, stat)
        switcher = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 1,
            6: 1,
            7: 1,
            8: 2,
            9: 2,
            10: 3}
        return switcher.get(level)
