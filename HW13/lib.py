# створити ієрархію класів (реалізувати наслідування) гаджетів (наприклад, телефон та ноутбук зі спільним абстрактним предком)
# створити фікстури відповідних сутностей та покрити їх тестами
from abc import ABC, abstractmethod


class Gadget(ABC):
    def __init__(self, producer: str, year_of_development: int, gsm_modem: bool = True):
        self.producer = producer.upper()
        self.year_of_development = year_of_development
        self.gsm_modem = gsm_modem

    def __str__(self):
        return f'Device was developed by {self.producer} in {self.year_of_development} with jsm module is built-in : {self.gsm_modem}'

    @abstractmethod
    def get_additional_info(self):
        pass


class Phone(Gadget, ABC):
    def __init__(self, producer: str, year_of_development: int, gsm_modem: bool = True, activated: bool = True):
        super().__init__(producer=producer, year_of_development=year_of_development, gsm_modem=gsm_modem)
        self.type_of_modem = None
        self.activated = activated

    def get_additional_info(self):
        return f'Current status is "Activate": {self.activated}'

    @property
    def define_type_of_modem(self):
        if self.year_of_development >= 2020:
            self.type_of_modem = '5G'
        elif 2016 < self.year_of_development <= 2019:
            self.type_of_modem = '4G'
        else:
            self.type_of_modem = '3G'
        return self.type_of_modem


class Laptop(Gadget, ABC):
    def __init__(self, producer: str, year_of_development: int, gsm_modem: bool = False,
                 battery_is_arranged: bool = True):
        super().__init__(producer=producer, year_of_development=year_of_development, gsm_modem=gsm_modem)
        self.type_of_data_loggers = None
        self.battery_is_arranged = battery_is_arranged

    def get_additional_info(self):
        return f'The battery is arranged: {self.battery_is_arranged}'

    @property
    def define_type_data_loggers(self):
        if self.year_of_development >= 2020:
            self.type_of_data_loggers = 'SSD'
        else:
            self.type_of_data_loggers = 'HDD'
        return self.type_of_data_loggers


samsung_phone = Phone('Samsung', 2021, True, True)
samsung_laptop = Laptop('Samsung', 2022, False, False)
