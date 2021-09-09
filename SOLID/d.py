#Dependency Inversion Principle
#High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g. interfaces).
#Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.

class AlbumStore:
    albums = []
    def add_album(self, name, artist, genre):
        self.albums.append((name, artist, genre))

class ViewRockAlbums:
    def __init__(self, album_store):
        for album in album_store.albums:
            if album[2] == "Rock":
                print(f"We have {album[0]} in store.")

#Instead
class GeneralAlbumStore:
    @abstractmethod
    def filter_by_genre(self, genre):
        pass

class MyAlbumStore(GeneralAlbumStore):
    albums = []
    def add_album(self, name, artist, genre):
        self.albums.append((name, artist, genre))
    def filter_by_genre(self, genre):
        if album[2] == genre:
            yield album[0]

class ViewRockAlbums:
    def __init__(self, album_store):
        for album_name in album_store.filter_by_genre("Rock"):
            print(f"We have {album_name} in store.")