cities = ['davao', 'manila', 'cebu', 'digos', 'midsayap', 'pigawayan']
# mycities = ['calinan','baguio']



        # cities.append(['tacurong','isulan', 'gensan'])
        # print "this will add three fruits", cities

cities_append(cities);

def cities_extend(cities):
        cities.extend(["toril","calinan"])
        print "this will add toril and calinan in the citiest list using extend", cities
        return

cities_extend(cities);

def cities_insert(cities):
        cities.insert(2, "tamayong")
        print "This will insert tamayong in index 2", cities
        return

cities_insert(cities);


def cities_remove(cities):
        cities.remove("tamayong")
        print "this will remove tamayong in the list", cities

cities_remove(cities)

def cities_pop(cities):
        cities.pop()
        print "this will remove calinan in the last same ", cities
        return
cities_pop(cities)

