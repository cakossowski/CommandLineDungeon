import random

treasure_names = [
    "Goldene Äpfel der Hesperiden",
    "Excalibur, das Schwert des Königs",
    "Der Heilige Gral",
    "Die Bundeslade",
    "Drachenschatz von Fafnir",
    "Mjölnir, Hammer des Thor",
    "Das Goldene Vlies",
    "Die Siebenmeilenstiefel",
    "Der Stein der Weisen",
    "Poseidons Dreizack",
    "Helios' Sonnenwagen",
    "Die Kristallkugel der Seher",
    "Das Auge von Ra",
    "Die Flügel des Hermes",
    "Die Hörner des Einhorns",
    "Das Herz von Tiamat",
    "Das Amulett von Anubis",
    "Der Smaragd der Medusa",
    "Die Träne der Mondgöttin",
    "Die Schattenkrone des Hades"
]


class GameObject:
    def __init__(self, name):
        self.name = name


class Treasure(GameObject):
    def __init__(self, name, worth):
        super().__init__(name)
        self.worth = worth
        self.stackable = None

    def __repr__(self):
        return f"Treasurename: {self.name} | Worth: {self.worth}G | Stackable: {self.stackable}"

    def __str__(self):
        return f"Treasurename: {self.name} | Worth: {self.worth}G | Stackable: {self.stackable}"


def create_treasure(treasure_name_list, treasure_list):
    choose_name = random.choice(treasure_name_list)
    random_worth = random.randint(0, 100)
    new_treasure = Treasure(choose_name, random_worth)
    treasure_list.append(new_treasure)
    return treasure_list