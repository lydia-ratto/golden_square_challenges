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

def test_reading_chunk_with_4_wpm_and_2_mins():
    entry = DiaryEntry('Holiday', 'I had a great time in Scotland and got to explore the highlands.')
    assert entry.reading_chunk(4, 2) == 'I had a great time in Scotland and'

def test_reading_chunk_with_next_chunk():
    entry = DiaryEntry('Holiday', 'I had a great time in Scotland and got to explore the highlands.')
    entry.reading_chunk(4, 2)
    assert entry.reading_chunk(4, 2) == 'got to explore the highlands.'

def test_restart_reading_chunk_after_end():
    entry = DiaryEntry('Holiday', 'I had a great time in Scotland and got to explore the highlands.')
    entry.reading_chunk(4, 2)
    entry.reading_chunk(4, 2)
    assert entry.reading_chunk(4, 2) == 'I had a great time in Scotland and'