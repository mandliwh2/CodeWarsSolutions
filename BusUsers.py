def number(bus_stops):

    il = 0
    out = 0

    for i in bus_stops:

        il += i[0]
        out += i[1]

        users = il - out

    return users
print(number([[5, 2],[6, 4]]))

