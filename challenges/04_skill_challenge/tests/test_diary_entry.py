from lib.diary_entry import *

def test_diary_entry_stored():
    entry = DiaryEntry('Holiday', 'I had a great time')
    assert entry.title == 'Holiday'
    assert entry.contents == 'I had a great time'

def test_clear_diary_entry_format():
    entry = DiaryEntry('Holiday', 'I had a great time')
    assert entry.format() == "Title: Holiday, Content: I had a great time"

def test_correct_word_count_in_contents():
    entry = DiaryEntry('Holiday', 'I had a great time')
    assert entry.count_words() == 5

def test_zero_for_no_words_in_contents():
    entry = DiaryEntry('Holiday', '')
    assert entry.count_words() == 0

def test_correct_reading_minutes_count():
    entry = DiaryEntry('Holiday', 'I had a great time in Scotland and got to explore the highlands.')
    assert entry.reading_time(3) == 4