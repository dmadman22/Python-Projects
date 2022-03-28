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
    def get_title(self):
        return self.title
    name = property(get_title)
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

        :param song: title of song to add
        :param position: if specified the song will be added to this position in the
            track list, otherwise it will be added to the end
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)

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

    def add_song(self, name, year, title):
        """ Add new song to collection of albums
        A new album will be created in the collection if non existent

        Args:
            name (str)
            year (int)
            title (str)
        """
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + " not found")
            album_found = Album(name, year, self)
            self.add_album(album_found)
        else:
            print("Found album " + name)

        album_found.add_song(title)

def find_object(field, object_list):
    """Check object_list to see if object with a 'name' attribute equal to 'field' exists, and returns if so"""
    for item in object_list:
        if item.name == field:
            return item
    return None

def load_data():
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            #data row should consist of 4 values (artist, album, year, and song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)

    return artist_list

def create_checkfile(artist_list):
    """ Create a check file from the object data for comparison"""
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                        file=checkfile)
if __name__ == '__main__':
    artists = load_data()
    print(len(artists))

    create_checkfile(artists)