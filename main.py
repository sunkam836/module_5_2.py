class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
            return (f'Название: "{self.name}", '
                    f'кол-во этажей: {self.number_of_floors}')

h1 = House('ЖК Алмаз', 3)
h2 = House('УК Ривьера', 19)

print(h1)
print(h2)

print(len(h1))
print(len(h2))