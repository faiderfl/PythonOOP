#Single Responsability

class Album:
    def __init__(self, name, artist, songs) -> None:
        self.name = name
        self.artist = artist
        self.songs = songs

    def add_song(self, song):
        self.songs.append(song)
    def remove_song(self, song):
        self.songs.remove(song) 
    def __str__(self) -> str:
        return f"Album {self.name} by {self.artist}\nTracklist:\n{self.songs}"

    # breaks the SRP
    def search_album_by_artist(self):
        """ Searching the database for other albums by same artist """
        pass

    # instead:
    class AlbumBrowser:
        """ Class for browsing the Albums database"""
        def search_album_by_artist(self, albums, artist):
            pass
        
        def search_album_starting_with_letter(self, albums, letter):
            pass