import argparse
import os
import re

from mutagen.mp4 import *


def remove_aART(path_to_song):
    print("Removing aArt")
    audio = MP4(path_to_song)

    # audio['aART'] = html.unescape(str(self.keys['singers']))                # Album Artist
    if 'aART' in audio:
        audio.pop('aART')
        audio.save()
        print("aArt Removed Successfully\n")
    else:
        print("No aART tag found")


def getSongList(files: list):
    songs = []
    for x in files:
        x = re.findall(r'(.+\.m4a)', x)
        if len(x) != 0:
            songs.append(x[0])
    sorted(songs)
    return songs


def handleSongs(song_dir, files):
    print('Now in ', song_dir, end='\n\n')

    song_list = getSongList(files)
    for song_name in song_list:
        song_name_with_path = os.path.join(song_dir, song_name)
        print(song_name_with_path)
        # rename.start(song_name_with_path, song_dir, song_name, song_list)
        remove_aART(song_name_with_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Remove aART')
    parser.add_argument('-p', '--path', type=str, help="absolute path to song dir", required=True)

    args = parser.parse_args()
    song_dir = str(args.path).strip()

    print("Walking down ", song_dir, "\b...")
    for curr_dir, sub_dirs, files in os.walk(song_dir, topdown=True):
        os.chdir(curr_dir)
        handleSongs(curr_dir, files)
