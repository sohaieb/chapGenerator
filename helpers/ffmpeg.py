from os import system, path
from helpers.local_paths import ressources_path, output_path
import config


class FFmpeg:
    @staticmethod
    def extract_meta(video_name=f'{path.join(ressources_path, config.input_file_path)}',
                     meta_output=f'{path.join(ressources_path, "FFMETADATAFILE")}'):
        system(f'{config.ffmpeg_exec_path} -i {video_name} -f ffmetadata {meta_output}')

    @staticmethod
    def rebuild_video(video_name_input=f'{path.join(ressources_path, config.input_file_path)}',
                      video_name_output=f'{path.join(output_path, config.output_file_path)}',
                      meta_output=f'{path.join(ressources_path, config.video_metadata_file_name)}'):
        system(
            f'{config.ffmpeg_exec_path} -i {video_name_input} -i {meta_output} -map_metadata 1 -codec copy {video_name_output}')
