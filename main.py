import world

rooms = []

world.create_new_room_bundle(rooms)
world.populate_rooms_with_monsters(rooms)
world.fill_rooms_with_treasure(rooms)
print(rooms)