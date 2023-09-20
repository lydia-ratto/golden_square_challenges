MusicTracker Design Recipe
1. Describe the Problem
> As a user
> So that I can keep track of my music listening
> I want to add tracks I've listened to and see a list of them.

2. Design the Class Interface
    class MusicTracker():

    def __init__(self):
        Params: 
            none
    
    def add_track(track):
        Params:
            track as a string

    def show_tracks():
        Params:
            none
        Returns:
            string of tracks, seperated by comma, or message for empty list

    
3. Tests

    Test that the initial list of tracks is empty and shows message

    test_inital_empty_list():
        tracks = MusicTracker()
        tracks.show_tracks ==> 'You haven't listened to any tracks'


    Test a track is added

        tracks = MusicTracker()
        tracks.add_track('Here Comes The Sun')
        tracks.show_tracks ==> 'Here Comes The Sun'


    Test multiple tracks can be added

        tracks = MusicTracker()
        tracks.add_track('Here Comes The Sun')
        tracks.add_track('Twist And Shout')

        tracks.show_tracks ==> 'Here Comes The Sun, Twist And Shout'

    Test lowercase tracks converted to correct format

        tracks = MusicTracker()
        tracks.add_track('here comes the Sun')
        
        tracks.show_tracks ==> 'Here Comes The Sun'

    
    Test uppercase tracks converted to correct format

        tracks = MusicTracker()
        tracks.add_track('HERE comes tHe Sun')
        
        tracks.show_tracks ==> 'Here Comes The Sun'

    
    Test track is a string

        tracks = MusicTracker()
        tracks.add_track(5) ==> 'Track must be a string'