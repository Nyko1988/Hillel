import HW15.HW15 as HW15


def test_response_code():
    assert str(HW15.session_func(url=HW15.url, method='GET')).find('[2') != '-1'