import re
from helpers.local_paths import ressources_path
from os.path import join
from helpers.loader import ChaptersLoader
from helpers.ffmpeg import FFmpeg


class Generator(ChaptersLoader):
    def __init__(self, chapters_file=f'{join(ressources_path, "chapters.txt")}',
                 meta_file=f'{join(ressources_path, "FFMETADATAFILE")}'):
        super().__init__(chapters_file)
        self.meta_file = meta_file
        FFmpeg.extract_meta()

    def generate(self):
        self.load_chapters()
        text = ""
        for i in range(len(self.chapters) - 1):
            chap = self.chapters[i]
            title = chap['title']
            start = chap['startTime']
            end = self.chapters[i + 1]['startTime'] - 1
            text += f"""
[CHAPTER]
TIMEBASE=1/1000
START={start}
END={end}
title={title}
"""
        with open(self.meta_file, "a") as myfile:
            myfile.write(text)
        FFmpeg.rebuild_video()
