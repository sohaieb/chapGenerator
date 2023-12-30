from helpers.loader import ChaptersLoader
from os.path import join
from helpers.local_paths import ressources_path
from helpers.ffmpeg import FFmpeg
import re


class Splitter(ChaptersLoader):

    def __init__(self, chapters_file=f'{join(ressources_path, "chapters.txt")}'):
        super().__init__(chapters_file)

    def normalize(self):
        ranges = []
        len_chapters = len(self.chapters) - 1
        for i in range(0, len_chapters):
            ranges.append({
                "title": self.chapters[i]['title'],
                "start": self.chapters[i]['full_time'],
                "stop": self.chapters[i + 1]['full_time']
            })
        return ranges

    def split(self):
        self.load_chapters()
        chap_ranges = self.normalize()
        for index, chapter in enumerate(chap_ranges):
            file_name = re.sub(r'[^A-Za-z]+', '_', f'{chapter["title"].lower()}') + '.mp4'
            FFmpeg.split_video_by(file_name, chapter['start'], chapter['stop'])
