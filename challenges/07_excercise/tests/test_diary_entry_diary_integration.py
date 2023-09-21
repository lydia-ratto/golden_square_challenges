from lib.diary import *
from lib.diary_entry import *

def test_added_diary_entry():
    diary = Diary()
    diary_entry = DiaryEntry('Day 1', 'Started Makers')

    diary.add(diary_entry)

    assert diary.all() == [diary_entry]


def test_correct_number_of_all_entry_words():
    diary = Diary()
    diary_entry_1 = DiaryEntry('Day 1', 'Started Makers')
    diary_entry_2 = DiaryEntry('Day 2', 'Continued Makers today')
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)

    assert diary.count_words() == 5

def test_correct_number_of_total_reading_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry('Day 1', 'Started Makers')
    diary_entry_2 = DiaryEntry('Day 2', 'Continued Makers today')
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)
    

    assert diary.reading_time(1) == 5

def test_closest_entry_to_reading_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry('Day 1', 'Started Makers')
    diary_entry_2 = DiaryEntry('Day 2', 'Continued Makers today')
    diary.add(diary_entry_1)
    diary.add(diary_entry_2)


    assert diary.find_best_entry_for_reading_time(1, 4) == diary_entry_2
