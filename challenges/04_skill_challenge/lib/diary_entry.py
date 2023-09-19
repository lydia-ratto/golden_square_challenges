class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.start_reading_chunk = 0

    def format(self):
        return f"Title: {self.title}, Content: {self.contents}"

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return int(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        n_words = wpm * minutes
        word_list = self.contents.split()
        if self.start_reading_chunk > len(word_list):
            self.start_reading_chunk = 0
        start = self.start_reading_chunk
        end = start + n_words
        text_to_read = word_list[start:end]
        self.start_reading_chunk = end
        return ' '.join(text_to_read)