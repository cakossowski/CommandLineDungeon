import random

monster_names = [
    "Hassiger Hühnerhaufen",
    "Der Lauernde Lachs",
    "Fledermaus-Monarch",
    "Pustel-Schrecken",
    "Muffiger Mopp",
    "Säufer-Spinne",
    "Der Ungeheuerliche Staubsauger",
    "Zorniger Zuckersirup",
    "Kampf-Krabbler",
    "Der Krabbel-Kobold",
    "Grollender Gummibär",
    "Skelett von Tante Gertrud",
    "Der Grobe Gummistiefel",
    "Mütze der unaufhörlichen Dämmerung",
    "Grummelnde Gurke",
    "Klobrille der Verdammnis",
    "Die Hühnerhorde der Apokalypse",
    "Zombiefischer von Ozean Grau",
    "Die Plüsch-Kreatur",
    "Mächtiger Marshmallow-Monarch",
    "Kriegs-Waschbär",
    "Rumpel-Ratte",
    "Die Blender-Biene",
    "Der Koffein-Dämon",
    "Verschwundene Bananenschale",
    "Das Albtraum-Schaf"
]

class Entity:
    def __init__(self, name):
        self.name = name


class Monster(Entity):
    def __init__(self, name, hp, strength):
        super().__init__(name)
        self.hp = hp
        self.strength = strength

    def __repr__(self):
        return f"Monstername: {self.name},HP: {self.hp}, Stärke: {self.strength}"


def create_monster(monster_names_list, monster_list):
    choose_name = random.choice(monster_names_list)
    random_hp = random.randint(5, 10)
    random_strength = random.randint(1, 10)
    new_monster = Monster(choose_name, random_hp, random_strength)
    monster_list.append(new_monster)
    return monster_list