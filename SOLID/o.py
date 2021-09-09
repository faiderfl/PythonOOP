#Open-Closed Principle: open for extension, but closed for modification.

class Album:
    def __init__(self, name, artist, songs, genre):
        self.name = name
        self.artist = artist
        self.songs = songs
        self.genre = genre
#before
class AlbumBrowser:
    def search_album_by_artist(self, albums, artist):
        return [album for album in albums if album.artist == artist]
    def search_album_by_genre(self, albums, genre):
        return [album for album in albums if album.genre == genre]

#after
class SearchBy:
    def is_matched(self, album):
        pass
    #add __and__:
    def __and__(self, other):
        return AndSearchBy(self, other)

class SearchByGenre(SearchBy):
    def __init__(self, genre):
        self.genre = genre
    def is_matched(self, album):
        return album.genre == self.genre

class SearchByArtist(SearchBy):
    def __init__(self, artist):
        self.artist = artist
    def is_matched(self, album):
        return album.artist == self.artist

class AlbumBrowser:
    def browse(self, albums, searchby):
        return [album for album in albums if searchby.is_matched(album)]


class AndSearchBy(SearchBy):
    def __init__(self, searchby1, searchby2):
        self.searchby1 = searchby1
        self.searchby2 = searchby2
    def is_matched(self, album):
        return self.searchby1.is_matched(album) and self.searchby2.is_matched(album)

LAWoman = Album(
    name="L.A. Woman",
    artist="The Doors",
    songs=["Riders on the Storm"],
    genre="Rock",
)
Trash = Album(
    name="Trash",
    artist="Alice Cooper",
    songs=["Poison"],
    genre="Rock",
)
albums = [LAWoman, Trash]
# this creates the AndSearchBy object
my_search_criteria = SearchByGenre(genre="Rock") & SearchByArtist(
    artist="The Doors"
)
browser = AlbumBrowser()
assert browser.browse(albums=albums, searchby=my_search_criteria) == [LAWoman]
# yay we found our album