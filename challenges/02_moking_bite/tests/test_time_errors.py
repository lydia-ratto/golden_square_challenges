from lib.time_error import *
from unittest.mock import Mock
import time



def test_call_api_provides_time_error():
    request_mock = Mock()
    response_mock = Mock()
    timer_mock = Mock()
    time_error = TimeError(request_mock,timer_mock)

    request_mock.get.return_value = response_mock
    response_mock.json.return_value = {
        "unixtime": 1668262850
    }
    timer_mock.time.return_value = 1668262850.5

    assert time_error.error() == -0.5



