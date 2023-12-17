import re
from helpers.local_paths import ressources_path
from os.path import join


class Generator:
    def __init__(self, chapters_file=f'{join(ressources_path, "chapters.txt")}',
                 meta_file=f'{join(ressources_path, "FFMETADATAFILE")}'):
        self.cahpters_file = chapters_file
        self.meta_file = meta_file
        self.chapters = list()

    def load_chapters(self):
        with open(self.cahpters_file, 'r') as f:
            for line in f:
                print(line)
                x = re.match(r"(\d{2}):(\d{2}):(\d{2}) (.*)", line)
                hrs = int(x.group(1))
                mins = int(x.group(2))
                secs = int(x.group(3))
                title = x.group(4)

                minutes = (hrs * 60) + mins
                seconds = secs + (minutes * 60)
                timestamp = (seconds * 1000)
                chap = {
                    "title": title,
                    "startTime": timestamp
                }
                self.chapters.append(chap)

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
