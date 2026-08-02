def calculate_area(length, width):
    return length + width


room_length = 8
room_width = 5

area = calculate_area(room_length, room_width)

print(area)

assert 40 == area
