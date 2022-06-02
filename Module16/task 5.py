def exist_song(song, playlist):
    for index in playlist:
        if song == index[0]:
            return True
    return False

def song_length(song, playlist):
    for index in playlist:
        if index[0] == song:
            return index[1]

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
count = int(input('Сколько песен выбрать: '))

playlist = []
total = 0

for i in range(count):
    print('Название', i + 1, ' песни: ', end = ' ')
    song = input()
    if exist_song(song,violator_songs):
        playlist.append(song)
        total += song_length(song, violator_songs)

print('Общее время звучания песен: ', total, ' минут')