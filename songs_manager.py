from tinytag import TinyTag
import os
import shutil


#  DISPLAY THE DETAILS OF THE FILE:
def song_details():
#   print('---------------------------------------------------')
    print(f'Title: {song_file.title}')
    print(f'Artist name: {song_file.artist}')
    print(f'the album is: {song_file.album}')
    print(f'Release year: {song_file.year}')
    print(f'Genre: {song_file.genre}')
    print(f'Bitrate: {song_file.bitrate}')
    print(f'Duration in Seconds: {song_file.duration}')
    print('---------------------------------------------------')
# sending the song to the genre folder

def sort_logic():
    if song_file.genre =='R&B/Soul':
        shutil.move(f'{song_path}',r'C:\Users\novas\PycharmProjects\music_tags_alloc\the songs data\point B\soul')
        print('this song is moved to the soul folder')
    elif song_file.genre =='Hip-Hop/Rap':
        shutil.move(f'{song_path}', r'C:\Users\novas\PycharmProjects\music_tags_alloc\the songs data\point B\Rap')
        print('this song is moved to the Rap folder')
    elif song_file.genre =='Pop':
        shutil.move(f'{song_path}', r'C:\Users\novas\PycharmProjects\music_tags_alloc\the songs data\point B\Pop')
        print('this song is moved to the Pop folder')
    elif song_file.genre =='Dance':
        shutil.move(f'{song_path}', r'C:\Users\novas\PycharmProjects\music_tags_alloc\the songs data\point B\dance')
        print('this song is moved to the Dance folder')
    elif song_file.genre =='Alternative':
        shutil.move(f'{song_path}', r'C:\Users\novas\PycharmProjects\music_tags_alloc\the songs data\point B\Alternatives')
    else:
        shutil.move(f'{song_path}', r'C:\Users\novas\PycharmProjects\music_tags_alloc\the songs data\point B\others')
        print("the song is moved to the other's folder ")
print('')
song_path = input('enter the command')
if song_path =='enter':
    for path in song_path:
        song_path = input(r'Enter the path here: ')
        song_file = TinyTag.get(song_path)
        song_details()
        sort_logic()

