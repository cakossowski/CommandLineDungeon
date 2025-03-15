import world

rooms = []

world.create_new_room_bundle(rooms)
world.populate_rooms_with_monsters(rooms)

print(rooms)