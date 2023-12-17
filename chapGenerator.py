from helpers.Generator import Generator
from helpers.ffmpeg import FFmpeg

g = Generator()
FFmpeg.extract_meta()
g.generate()
FFmpeg.rebuild_video()
