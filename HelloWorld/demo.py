albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]
while True:
    print("Please select album: ")
    for index in range(1, 5):
        print(index, ':', albums[index - 1][0])
    album_selection = int(input())
    if album_selection < 1 or album_selection > 4:
        continue
    else:
        album_selection -= 1
        print("Please choose your song: ")
        for songs in range(len(albums[album_selection][3])):
            print(songs + 1, ":", albums[album_selection][3][songs][1])
        song_selection = int(input())
        if song_selection < 1 or song_selection > len(albums[album_selection][3]):
            continue
        else:
            song_selection -= 1
            print("=" * 80)
            print("Now Playing: ", albums[album_selection][0], "-", albums[album_selection][3][song_selection][1],
                  " by ", albums[album_selection][1])
            print("=" * 80)
            input("Press enter to select another song")
print("Invalid selection, Exiting")
