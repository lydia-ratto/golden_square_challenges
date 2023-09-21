from lib.diary_entry import *

def test_correct_entry_title():
    diary_entry = DiaryEntry('Day 1', 'Started Makers')

    assert diary_entry.title == 'Day 1'

def test_correct_entry_contents():
    diary_entry = DiaryEntry('Day 1', 'Started Makers')

    assert diary_entry.contents == 'Started Makers'

def test_correct_number_of_entry_words():
    diary_entry = DiaryEntry('Day 1', 'Started Makers')

    entry_count = diary_entry.count_words()

    assert entry_count == 2

def test_reading_minutes():
    diary_entry = DiaryEntry('Day 1', 'Started Makers today')
    assert diary_entry.reading_time(1) == 3