import html
import argparse

from mutagen.mp4 import *


def remove_aART(song_location):
    print("Removing aArt")
    audio = MP4(song_location)

    # audio['aART'] = html.unescape(str(self.keys['singers']))                # Album Artist
    audio.pop('aART')
    audio.save()
    print("aArt Removed Successfully\n")


def get_loc(args: argparse.ArgumentParser.parse_args):
    pass


def start():
    pass

