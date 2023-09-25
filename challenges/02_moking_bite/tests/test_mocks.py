from unittest.mock import Mock
import pytest
from lib.secret_diary import *

# Delete the lines starting with `@pytest.mark.skip` one by one as you work through.

def test_set_up_blank_mock():
    # Uncomment and set up your mocks here
    fake_diary_entry = Mock()

    # Don't edit below
    assert fake_diary_entry is not None

def test_locked_diary():
    # Uncomment and set up your mocks here
    fake_diary_entry = Mock('secret contents')
    fake_diary = SecretDiary(fake_diary_entry)

    with pytest.raises(Exception) as e:
        fake_diary.read()
    error_message = str(e.value)

    assert error_message == "Go away!"

def test_secret_diary_unlocked():
    fake_diary_entry = Mock()
    fake_diary_entry.read.return_value = 'secret contents'
    fake_diary = SecretDiary(fake_diary_entry)

    fake_diary.locked = False
    
    assert fake_diary.read() == 'secret contents'


def test_lock_again_secret_diary():
    fake_diary_entry = Mock()
    fake_diary = SecretDiary(fake_diary_entry)
    fake_diary.locked = False

    fake_diary.lock()
    
    assert fake_diary.locked == True

def test_lock_again_secret_diary():
    fake_diary_entry = Mock()
    fake_diary = SecretDiary(fake_diary_entry)

    fake_diary.unlock()
    
    assert fake_diary.locked == False


