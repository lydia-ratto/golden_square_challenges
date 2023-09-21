from unittest.mock import Mock
from lib.music_library import *
from lib.track import *

def test_track_added_to_music_library():
    music_library = MusicLibrary()

    fake_track_with_title_and_artist_1 = Mock()
    music_library.add(fake_track_with_title_and_artist_1)

    fake_track_with_title_and_artist_2 = Mock()
    music_library.add(fake_track_with_title_and_artist_2)

    assert music_library.list == [fake_track_with_title_and_artist_1, fake_track_with_title_and_artist_2]

def test_correct_search_keyword_for_music_library():
    music_library = MusicLibrary()
    track_1 = Track('Title 1', 'Artist 1')
    music_library.add(track_1)
    track_2 = Track('New Title 2', 'New Artist 2')
    music_library.add(track_2)

    assert music_library.search('New') == [track_2]




