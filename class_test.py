class Mystaff():
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    
    def apple(self):
        print("I AM CLASSY APPLES!")

class Song(object):
    def __init__(self):
        pass
    def sing_me_a_song(self, lyrics, singer):
        self.lyrics = lyrics
        self.singer = singer

        print("singer of %s\'s song"%self.singer)
        for line in self.lyrics:
            print(line)

song = ["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"]
singer = "taylor"

m = Song( )
m.sing_me_a_song(song,singer)



