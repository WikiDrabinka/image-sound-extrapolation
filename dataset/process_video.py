from moviepy import VideoFileClip
import numpy as np

def process_video(input_path: str, output_path: str):

    video = VideoFileClip(input_path)

    name = input_path.split("/")[-1].split(".")[-2]

    for clip_start in range(0, int(video.duration) - 10, 10):

        clip = video.subclipped(clip_start, clip_start + 10)

        frame_start = clip.get_frame(0)

        with open(output_path + "images/" + name + str(clip_start // 10) + ".npy", "xb") as image_file:

            np.save(image_file, frame_start)