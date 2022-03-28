class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator
        duration (int): The duration of the s0ng in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    """Class to represent and album using its tracklist

    Attributes:
        name (str): The name of the album.
        year (int): The year the album was released.
        artist: (Artist)L The artist that create the album, if not specified
            will default to various artists.
        tracks (List[Song]): A list of the songs on the album.

        Methods:
            add_song: Used to add new song to tracklist.
        """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []


    def add_song(self, song, position=None):
        """ Adds a song to track list

        :param song: a song to add
        :param position: if specified the song will be added to this position in the
            track list, otherwise it will be added to the end
        """

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)

class Artist:
    """
    Basic class to store artist details

    Attributes:
        name (str): Name of artist
        albums (List[Album]): List of albums by artist, not exhaustive

    Methods:
          add_album: Use to add a new album to list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """ add a new album to the list
        :arg: album"""

        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []
    album_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            #data row should consist of 4 values (artist, album, year, and song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            if artist_field not in artist_list:
                Artist(artist_field)
                artist_list.append(artist_field)
            if album_field not in album_list:
                Artist.add_album(album_field)
        print(artist_list, Artist.albums)
if __name__ == '__main__':
    load_data()