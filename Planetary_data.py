class PlanetaryData:
    def __init__(self):
        self.data = list()

    def add(self, planet_name : str, gasses : list, num_moons : int, has_rings : bool):
        self.data.append((planet_name, set(gasses), num_moons, has_rings))

    def count_moons_of_planets_with_rings(self):
        count = 0

        for planet in self.data:
            if planet[3]:
                count += planet[2]

        return count

    def get_most_common_gas(self):
        counts = dict()

        for planet in self.data:
            if planet[1]:
                for gas in planet[1]:
                    counts[gas] = 1 + counts.get(gas, 0)

        res = str()
        curr_max = 0

        for count in counts:
            if counts[count] > curr_max:
                res = count
                curr_max = counts[count]

        return res


planets = PlanetaryData()
planets.add("Mercury", list(), 0, False)
planets.add("Venus", ["Carbon Dioxide", "Nitrogen"], 0, False)
planets.add("Earth", ["Nitrogen", "Oxygen"], 1, False)
planets.add("Jupiter", ["Hydrogen", "Helium"], 79, True)
planets.add("Saturn", ["Hydrogen", "Helium"], 83, True)
planets.add("Uranus", ["Hydrogen", "Helium", "Methane"], 27, True)

print(planets.count_moons_of_planets_with_rings())
print(planets.get_most_common_gas())
