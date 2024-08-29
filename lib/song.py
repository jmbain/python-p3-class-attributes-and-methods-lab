class Song:
    count = 0
    artists = [] # generally initialize with empty lists
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Song.count += 1 # can't use just count here or it will be a separate variable from Song.count class attribute, but class method would be better
        Song.increment_song_count() # example of self-documenting code

        Song.add_artist(artist)

        Song.add_genre(genre)
        
        if genre not in Song.genre_count:
            Song.genre_count[genre] = 1
        else:
            Song.genre_count[genre] += 1

        if artist not in Song.artist_count:
            Song.artist_count[artist] = 1
        else:
            Song.artist_count[artist] += 1

    @classmethod
    def increment_song_count(cls):
        cls.count +=1

    @classmethod
    def add_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

        

