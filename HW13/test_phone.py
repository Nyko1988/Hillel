class TestTypeModem:
    def test_type_modem_3g(self, phone):
        phone.year_of_development = 2016
        assert phone.define_type_of_modem == '3G'

    def test_type_modem_4g(self, phone):
        phone.year_of_development += 3
        assert phone.define_type_of_modem == '4G'

    def test_type_modem_5g(self, phone):
        phone.year_of_development += 3
        assert phone.define_type_of_modem == '5G'


class TestYearModem:
    def test_new_phone_yer(self, phone):
        assert phone.year_of_development == 2015

    def test_newer_phone_year(self, phone):
        year = 2
        phone.year_of_development += year
        assert phone.year_of_development == 2017

    def test_newest_phone_year(self, phone):
        year = 5
        phone.year_of_development += year
        assert phone.year_of_development == 2022


class TestProducer:
    def test_def_producer(self, phone):
        assert phone.producer == "SAMSUNG"

    def test_two_producers(self, phone):
        phone.producer += ' and APPLE'
        assert phone.producer == 'SAMSUNG and APPLE'


class TestPhoneInfo:
    def test_phone_get_info(self, phone):
        assert phone.get_additional_info() == 'Current status is "Activate": True'


class TestGsmModem:
    def test_gsm_modem(self, phone):
        assert phone.gsm_modem is True

