class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        addition = self.__cpu + self.__memory
        substraction = self.__cpu - self.__memory
        multiplication = self.__cpu * self.__memory
        devision = self.__cpu / self.__memory

        print(f'Addition: {addition}\nSubstraction: {substraction}\nMultiplication: {multiplication}\nDevision: {devision}')

    def __str__(self):
        return f'Computer with cpu {self.__cpu} and memory {self.__memory}'

    def __lt__(self, other):
        return self.memory < other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __ge__(self, other):
        return self.memory >= other.memory



class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number , call_to_number):
        return f'Идет звонок на номер {call_to_number} с сим-карты - {self.sim_cards_list[sim_card_number - 1]}'

    def __str__(self):
        return f'Phone with sim cards: {self.__sim_cards_list}'

class SmartPhone(Phone, Computer):
    def __init__(self, sim_cards_list, cpu, memory):
        Phone.__init__(self, sim_cards_list)
        Computer.__init__(self, cpu, memory)

    def use_gps(self, location):
        return f'Идет поиск координат в {location}'

    def __str__(self):
        return f'Smart phone with sim cards: {self.sim_cards_list}, cpu {self.cpu}, memory {self.memory}'


lst = [Computer(100, 100), Phone(['sim-1 beeline', 'sim-2 o', 'sim-3 megacom']), SmartPhone(['sim-1 o', 'sim-2 beeline', 'sim-3 megacom'], 100, 100), SmartPhone(['sim-1 beeline', 'sim-2 beeline', 'sim-3 beeline'], 10, 100)]
for item in lst:
    print(item)

computer = Computer(100, 100)

print(computer.make_computations())
phone = Phone(['sim-1 beeline', 'sim-2 oshka', 'sim-3 megacom'])
smartphone = SmartPhone(['sim-1 beeline', 'sim-2 oshka', 'sim-3 megacom'], 100, 1000)
print(smartphone.use_gps('Shuha'))
print(phone.call(2, 123456789))
print(smartphone.call(2, 123456789))
print(computer < smartphone)
print(smartphone > computer)
print(smartphone == computer)
