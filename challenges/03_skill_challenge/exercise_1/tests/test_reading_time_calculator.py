import pytest
from lib.reading_time_calculator import *

# Given a non-string object it returns an error
def test_error_non_string_param():
    with pytest.raises(Exception) as e:
        reading_time_calculator(3)
    error_message = str(e.value)
    assert error_message == "Parameter must be a string"

# Given a string with 200 words it returns 1
def test_200_words_returns_one_minute():
    assert reading_time_calculator(
        "Auctor malesuada imperdiet. Nec tristique dictum vivamus, natoque inceptos senectus vitae suscipit morbi auctor vulputate accumsan. Semper. Posuere integer habitasse metus dictum. Scelerisque, habitant consectetuer aptent augue platea dapibus lacinia, ultrices Tellus cubilia hymenaeos lobortis bibendum aliquet parturient, amet accumsan potenti consequat torquent nec class fermentum placerat. Sem sem ad tempor ut. Sed senectus convallis cursus elit ad suspendisse vestibulum pulvinar ipsum molestie metus class. Aenean natoque eros nunc amet nascetur vel ligula ornare fames libero cursus felis lacinia lacinia cum euismod dictum metus consectetuer dui natoque convallis magnis fringilla praesent volutpat nibh. Venenatis lobortis arcu. Eu. Arcu felis nostra magna ad duis Facilisi. Cras neque nostra nisl. Adipiscing semper eleifend massa consectetuer gravida venenatis hac aliquet leo montes augue rhoncus phasellus rhoncus laoreet lobortis. Senectus suspendisse malesuada. Ante, orci integer varius erat quam eget Rutrum dictum nostra semper risus nibh litora convallis mollis at curae; metus bibendum. Maecenas curae; semper ligula sociosqu nam rhoncus, curabitur sociosqu posuere, orci vivamus sit sagittis parturient sagittis tristique gravida lorem proin, cubilia ridiculus libero eros. Conubia dictum quis ante, ipsum nulla. Interdum congue integer. Justo dapibus hendrerit ullamcorper, mi habitant. Maecenas in et bibendum. Tortor fusce risus torquent consequat sit suscipit id vehicula."
    ) == "1 minute"

# Given a string with less than 200 words it converts to seconds
def test_under_200_words_returns_seconds():
    short_text = "hello " * 100
    assert reading_time_calculator(short_text) == "30 seconds"

# Given a string with 12,000 words it converts to hours
def test_1200_words_returns_hour():
    large_text = "hello " * 12000
    assert reading_time_calculator(large_text) == "1 hour"

# Given a string with more than 12,000 words it converts to hours and minutes
# reading_time("(Text with 12,600 words)") => '1 hour, 3 minutes"