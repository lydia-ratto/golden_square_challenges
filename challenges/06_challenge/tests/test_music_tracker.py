from lib.music_tracker import *

def test_inital_empty_list():
    tracks = MusicTracker()

    assert tracks.show_tracks() == "You haven't listened to any tracks"


def test_added_track_to_list():
    tracks = MusicTracker()

    tracks.add_track('Here Comes The Sun')

    assert tracks.show_tracks() == 'Here Comes The Sun'


def test_multiple_tracks_added_to_list():
        tracks = MusicTracker()
        tracks.add_track('Here Comes The Sun')

        tracks.add_track('Twist And Shout')

        assert tracks.show_tracks() == 'Here Comes The Sun, Twist And Shout'


def test_lowercase_tracks_converted_to_correct_format():
        tracks = MusicTracker()

        tracks.add_track('here comes the Sun')
        
        assert tracks.show_tracks() == 'Here Comes The Sun'


def test_uppercase_tracks_converted_to_correct_format():
        tracks = MusicTracker()

        tracks.add_track('HERE comes tHe Sun')
        
        assert tracks.show_tracks() == 'Here Comes The Sun'


def test_track_is_a_string():
    tracks = MusicTracker()

    assert tracks.add_track(5) == 'Track must be a string'