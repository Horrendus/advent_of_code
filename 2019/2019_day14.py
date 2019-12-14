import math

from collections import defaultdict


def produce_one_fuel(reaction_list, leftover_materials):
    materials = defaultdict(int)
    materials["FUEL"] = 1
    # leftover_materials = defaultdict(int)
    while True:
        materials_needed = list(materials.keys())
        for material in materials_needed:
            # print("=" * 80)
            if material == "ORE":
                continue
            amount_needed = materials[material]
            # print("Need ", amount_needed, material)
            # first check already produced materials
            if material in leftover_materials:
                leftover_amount = min(leftover_materials[material], amount_needed)
                amount_needed -= leftover_amount
                leftover_materials[material] -= leftover_amount
                # print("Using ", leftover_amount, material, " from leftover")
            if amount_needed > 0:
                # produce the rest
                reaction = reaction_list[material]
                productions_needed = math.ceil(amount_needed / reaction["amount"])
                """
                print(
                    "Using ",
                    productions_needed,
                    " Productions to produce",
                    amount_needed,
                    material,
                    "via reaction ",
                    reaction,
                )
                """
                for production_material in reaction["input"]:
                    materials[production_material[1]] += (
                        productions_needed * production_material[0]
                    )
                leftover_materials[material] += max(
                    0, productions_needed * reaction["amount"] - amount_needed
                )
            materials.pop(material)
            # print(materials)
            # print(leftover_materials)
        if len(materials) == 1 and "ORE" in materials:
            break
    return materials["ORE"], leftover_materials


def puzzle1(reaction_list):
    ore_needed, _ = produce_one_fuel(reaction_list, defaultdict(int))
    print("Puzzle 1:", ore_needed)


def puzzle2(reaction_list):
    leftover_materials = defaultdict(int)
    fuel_produced = 0
    total_ore = 1000000000000
    while True:
        ore_needed, leftover_materials = produce_one_fuel(
            reaction_list, leftover_materials
        )
        total_ore -= ore_needed
        if total_ore < 0:
            break
        fuel_produced += 1
    print("Puzzle 2:", fuel_produced)


def parse_input(data):
    reaction_list = dict()
    for line in data:
        splitted_line = line.strip().split(" => ")
        reaction_input_list = [
            parse_reaction_part(reaction_input)
            for reaction_input in splitted_line[0].split(",")
        ]
        reaction_output = parse_reaction_part(splitted_line[1])
        reaction_list[reaction_output[1]] = {
            "input": reaction_input_list,
            "amount": reaction_output[0],
        }
    return reaction_list


def parse_reaction_part(reaction_part):
    splitted_reaction_part = reaction_part.strip().split(" ")
    return int(splitted_reaction_part[0]), splitted_reaction_part[1].strip()


def main():
    with open("input/input_day14.txt") as f:
        data = f.readlines()
    reaction_list = parse_input(data)
    puzzle1(reaction_list)
    puzzle2(reaction_list)


if __name__ == "__main__":
    main()
