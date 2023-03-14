class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

    def __str__(self):
        return f"{self.get_full_name()} is a {self.position} with a total income of {self.get_total_income()}"


worker1 = Position('Nickita', 'Shvetzoff', 'Data Science', 5000, 1000)
print(worker1.get_full_name())
print(worker1.get_total_income())
print(worker1)
