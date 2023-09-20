class MusicTracker():
    def __init__(self):
        self.tracks = []

    def show_tracks(self):
        if self.tracks == []:
            return "You haven't listened to any tracks"
        return ', '.join(self.tracks)
    
    def formatted_track(self, track):
        track_words = track.split()
        for i in range(len(track_words)):
            track_words[i] = track_words[i].lower().capitalize()
        return ' '.join(track_words)

    def add_track(self, track):
        if type(track) != str:
            return 'Track must be a string'
        self.tracks.append(self.formatted_track(track))
        