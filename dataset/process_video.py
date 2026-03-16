from moviepy import VideoFileClip
import numpy as np
import os

def process_video(input_path: str, output_path: str):

    video = VideoFileClip(input_path)

    name = input_path.split("/")[-1].split(".")[-2]

    if not os.path.exists(output_path + "images"):

        os.makedirs(output_path + "images")

    if not os.path.exists(output_path + "sound"):

        os.makedirs(output_path + "sound")

    for clip_start in range(0, int(video.duration) - 10, 10):

        clip = video.subclipped(clip_start, clip_start + 10)

        frame_start = clip.get_frame(0)

        clip_name = name + str(clip_start // 10)

        with open(output_path + "images/" + clip_name + ".npy", "xb") as image_file:

            np.save(image_file, frame_start)

        audio = clip.audio

        with open(output_path + "sound/" + clip_name + ".npy", "xb") as image_file:

            np.save(image_file, audio.to_soundarray())