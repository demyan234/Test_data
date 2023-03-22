from pprint import pprint


class House:
    def __init__(self):
        self.entrance = list()

    def get_suitable_entrance(self) -> int:
        self.entrance.sort()

        for i in range(0, len(self.entrance)):
            sub = self.entrance[i:i + 3]

            if len(sub) != 3:
                break

            difference = sub[-1] - sub[0]

            if difference == 3: # 1 2 4
                if sub[1] - sub[0] != 1:
                    return sub[0] + 1

                return sub[1] + 1

            elif difference == 2: # 2 3 4
                if self.entrance[i] - self.entrance[i - 1] != 1:
                    return self.entrance[i] - 1

                if self.entrance[i + 3] - self.entrance[i + 2] != 1:
                    return self.entrance[i + 2] + 1

        return None


with open("26-95.txt") as file:
    string = file.read()


houses = dict()


for elem in string.split('\n'):
    house_id, entrance_id = list(map(int, elem.split(' ')))

    if house_id not in houses.keys():
        houses[house_id] = House()

    houses[house_id].entrance.append(entrance_id)

counter = 0
max_house_id = 0
answer = 0

for house_id, house in houses.items():
    result = house.get_suitable_entrance()

    if result is not None:
        counter += 1

        if house_id > max_house_id:
            answer = result
            max_house_id = house_id

print(counter, answer)

