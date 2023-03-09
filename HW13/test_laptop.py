class TestLaptopInfo:
    def test_laptop_get_info(self, laptop):
        assert laptop.get_additional_info() == 'The battery is arranged: True'


class TestYearLaptop:
    def test_default_phone_year(self, laptop):
        assert laptop.year_of_development == 2020

    def test_new_phone_year(self, laptop):
        year = 6
        laptop.year_of_development += year
        assert laptop.year_of_development == 2026


class TestTypeDataLogger:
    def test_type_data_logger_hdd(self, laptop):
        laptop.year_of_development = 2016
        assert laptop.define_type_data_loggers == 'HDD'

    def test_type_data_logger_sdd(self, laptop):
        laptop.year_of_development += 6
        assert laptop.define_type_data_loggers == 'SSD'
