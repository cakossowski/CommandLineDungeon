import random
import entity
import game_objects


room_names = [
    "Die Staubige Stube",
    "Küche des ewigen Hungers",
    "Der Kaffeekessel-Krater",
    "Verwunschene Toilette",
    "Keller des Miefes",
    "Die Krumen-Höhle",
    "Hall of Misplaced Socks",
    "Bibliothek des ewigen Vergessens",
    "Der Raum der verlorenen Schlüssel",
    "Zufallszimmer",
    "Das Plätscherbecken",
    "Die Schimmel-Grotte",
    "Der Raum der stillen Elstern",
    "Der Magen des Drachen",
    "Luftschloss-Salon",
    "Die Schattenhütte",
    "Das Zimmer der wütenden Staubsauger",
    "Ritterliches Wohnzimmer",
    "Das Labyrinth der unaufgeräumten Schreibtische",
    "Die Pfützen-Arena",
    "Vorsicht, Gabel!",
    "Das Sofa der Tauschgeschäfte",
    "Der Ofen des ewigen Missverständnisses",
    "Gruseliges Gäste-WC",
    "Das leere Spinnennetz-Zimmer",
    "Das Chaos-Kabinett",
    "Der Raum der ständig verschobenen Termine"
]

room_content = ["Monster", "Treasure", "Nothing"]


class Dungeon:
    def __init__(self):
        self.rooms = []


class Room:

    def __init__(self, name, content):
        self.name = name
        self.content = content
        self.enemies = []
        self.treasure = []
        self.position = 0

    def __str__(self):
        return f"Name: {self.name}, Content: {self.content}"

    def __repr__(self):
        return (f"_________________________________"
                f"Name: {self.name}, "
                f"Content: {self.content}, "
                f"Enemies: {self.enemies}, "
                f"Treasure: {self.treasure}, "
                f"Position: {self.position}"
                f"_________________________________")


def create_new_room(room_names, possible_content):
    if not room_names:
        raise ValueError("Keine Namen mehr übrig!")

    random_name = random.choice(room_names)
    room_names.remove(random_name)
    random_content = random.choice(possible_content)
    new_room = Room(random_name, random_content)
    return new_room


def create_new_room_bundle(list_of_rooms: list):
    for _ in range(random.randint(3, 10)):
        new_room = create_new_room(room_names, room_content)
        list_of_rooms.append(new_room)


def get_rooms_with_enemies(rooms):
    rooms_to_populate = []
    for room in rooms:
        if room.content == "Monster":
            rooms_to_populate.append(room)
    return rooms_to_populate


def get_rooms_with_treasure(rooms):
    rooms_to_fill = []
    for room in rooms:
        if room.content == "Treasure":
            rooms_to_fill.append(room)
    return rooms_to_fill


def populate_rooms_with_monsters(overall_rooms):
    rooms_to_populate = get_rooms_with_enemies(overall_rooms)
    monster_list = []
    for _ in rooms_to_populate:
        entity.create_monster(entity.monster_names, monster_list)
    for room in rooms_to_populate:
        if monster_list:
            random_monster = random.choice(monster_list)
            room.enemies = random_monster
    return overall_rooms


def fill_rooms_with_treasure(overall_rooms):
    rooms_to_fill = get_rooms_with_treasure(overall_rooms)
    treasure_list = []
    for _ in rooms_to_fill:
        game_objects.create_treasure(game_objects.treasure_names, treasure_list)
    for room in rooms_to_fill:
        if treasure_list:
            random_treasure = random.choice(treasure_list)
            room.treasure = random_treasure
    return overall_rooms