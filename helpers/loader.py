import re
from helpers.local_paths import ressources_path
from os.path import join


class ChaptersLoader:
    def __init__(self, chapters_file=f'{join(ressources_path, "chapters.txt")}'):
        self.cahpters_file = chapters_file
        self.chapters = []

    def load_chapters(self):
        with open(self.cahpters_file, 'r') as f:
            for line in f:
                hrs, mins, secs, title = self.load_line_elements(line)
                minutes = (hrs * 60) + mins
                seconds = secs + (minutes * 60)
                timestamp = (seconds * 1000)
                chap = {
                    "title": title,
                    "startTime": timestamp,
                    "full_time": f"{hrs}:{mins}:{secs}"
                }
                self.chapters.append(chap)

    def load_line_elements(self, line):
        x = re.match(r"(\d{2}):(\d{2}):(\d{2}) (.*)", line)
        hrs = int(x.group(1))
        mins = int(x.group(2))
        secs = int(x.group(3))
        title = x.group(4)
        return hrs, mins, secs, title
