import random

class Artifact:



    def __init__(self) -> None:
        self.artifact_types = {"Flower" : ["HP"], "Plume" : ["ATK"], "Sands" : ["HP%", "ATK%", "DEF%", "EM", "Recharge%"], "Goblet" : ["HP%", "ATK%", "DEF%", "EM", "Cryo Dmg Bonus%", "Pyro Dmg Bonus%", "Electro Dmg Bonus%", "Hydro Dmg Bonus%", "Geo Dmg Bonus%", "Anemo Dmg Bonus%", "Physical Dmg Bonus%"], "Circlet" : ["HP%", "ATK%", "DEF%", "EM", "Crit Rate%", "Crit Dmg%", "Healing Bonus%"]}
        self.artifact_type = random.choice(list(self.artifact_types.keys()))
        self.main_stat = random.choice(self.artifact_types[self.artifact_type])
        
        num_sub_stat = random.choice([3,3,3,3,4])
        self.possible_substats = {
            "HP"        : [209, 239, 269, 299],
            "ATK"       : [14, 16, 18, 19],
            "DEF"       : [16, 19, 21, 23],
            "HP%"       : [4.1, 4.7, 5.3, 5.8],
            "ATK%"      : [4.1, 4.7, 5.3, 5.8],
            "DEF%"      : [5.1, 5.8, 6.6, 7.3],
            "EM"        : [16, 19, 21, 23],
            "Recharge%" : [4.5, 5.2, 5.8, 6.5],
            "Crit Rate%": [2.7, 3.1, 3.5, 3.9],
            "Crit Dmg%" : [5.4, 6.2, 7.0, 7.8]
        }
        self.sub_stats = dict()
        for i in range(num_sub_stat):
            sub_stat = random.choice(list(self.possible_substats.keys()))
            while sub_stat in self.sub_stats or sub_stat == self.main_stat:
                sub_stat = random.choice(list(self.possible_substats.keys()))
            self.sub_stats[sub_stat] = random.choice(self.possible_substats[sub_stat])
    
    def __str__(self):
        to_return =  '''
---------------------------------
Artifact Type: {}
Main Stat: {}

Substats:\n'''.format(self.artifact_type, self.main_stat)
        for key in self.sub_stats:
            to_return += key + "\t" + str(self.sub_stats[key]) + "\n"
        to_return += "---------------------------------\n"
        #print(to_return)
        return to_return
    

    

if __name__ == "__main__":
    a = Artifact()
    print(a)
    