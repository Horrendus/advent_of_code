import re


class Moon:
    def __init__(self, id, x, y, z):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.v_x = 0
        self.v_y = 0
        self.v_z = 0

    def update_gravity(self, other_moon):
        self.v_x += 0 if other_moon.x == self.x else 1 if other_moon.x > self.x else -1
        self.v_y += 0 if other_moon.y == self.y else 1 if other_moon.y > self.y else -1
        self.v_z += 0 if other_moon.z == self.z else 1 if other_moon.z > self.z else -1

    def update_gravity_multiple(self, other_moons):
        for other_moon in other_moons:
            # print("Updating grav. Moon ", self.id, " with Moon ", other_moon.id)
            self.update_gravity(other_moon)
            other_moon.update_gravity(self)

    def do_step(self):
        self.x += self.v_x
        self.y += self.v_y
        self.z += self.v_z

    def calculate_energy(self):
        e_pot = abs(self.x) + abs(self.y) + abs(self.z)
        e_kin = abs(self.v_x) + abs(self.v_y) + abs(self.v_z)
        return e_pot * e_kin

    def __str__(self):
        return f"M{self.id}: pos=<x={self.x:3}, y={self.y:3}, z={self.z:3}>, vel=<v_x={self.v_x:3}, v_y={self.v_y:3}, v_z={self.v_z:3}>"


def parse_data(data):
    moons = []
    for i in range(len(data)):
        line = data[i]
        splitted = line.strip().split(",")
        x = int(re.sub("[^0123456789-]", "", splitted[0]))
        y = int(re.sub("[^0123456789-]", "", splitted[1]))
        z = int(re.sub("[^0123456789-]", "", splitted[2]))
        moons.append(Moon(i, x, y, z))
    return moons


def puzzle1(moons):
    for i in range(1000):
        print("Turn ", i)
        for j in range(len(moons)):
            moons[j].update_gravity_multiple(moons[j + 1 :])
            moons[j].do_step()
            # print(moons[j])
    total_energy = 0
    for moon in moons:
        total_energy += moon.calculate_energy()
    print(total_energy)


def puzzle2(data):
    pass


def main():
    with open("input/input_day12.txt") as f:
        data = f.readlines()
    moons = parse_data(data)
    puzzle1(moons)
    puzzle2(data)


if __name__ == "__main__":
    main()
