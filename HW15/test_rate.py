import HW15.HW15 as HW15


def test_response_code():
    str_rate_response = str(HW15.session_func(url=HW15.url, method='GET'))
    index = str_rate_response.index('[') + 1
    assert str_rate_response[index] == '2'


def test_size_of_response():
    response = HW15.session_func(url=HW15.url, method='GET')
    assert len(response.text) > 0
