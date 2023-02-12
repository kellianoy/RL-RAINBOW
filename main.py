import base64
import glob
import io
import os
import random

import gym
import numpy as np
import torch
from IPython.display import HTML, display

from classes.DQNAgent import DQNAgent


def seed_torch(seed):
    torch.manual_seed(seed)
    if torch.backends.cudnn.enabled:
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True


def show_latest_video(video_folder: str) -> str:
    """Show the most recently recorded video from video folder."""
    list_of_files = glob.glob(os.path.join(video_folder, "*.mp4"))
    latest_file = max(list_of_files, key=os.path.getctime)
    ipython_show_video(latest_file)
    return latest_file


def ipython_show_video(path: str) -> None:
    """Show a video at `path` within IPython Notebook."""
    if not os.path.isfile(path):
        raise NameError("Cannot access: {}".format(path))

    video = io.open(path, "r+b").read()
    encoded = base64.b64encode(video)
    display(HTML(
        data="""
        <video width="320" height="240" alt="test" controls>
        <source src="data:video/mp4;base64,{0}" type="video/mp4"/>
        </video>
        """.format(encoded.decode("ascii"))
    ))


if __name__ == "__main__":

    # environment
    env_id = "CartPole-v0"
    env = gym.make(env_id)
    # seed
    seed = 777
    np.random.seed(seed)
    random.seed(seed)
    seed_torch(seed)
    env.seed(seed)
    # parameters
    num_frames = 20000
    memory_size = 10000
    batch_size = 128
    target_update = 100
    # train
    agent = DQNAgent(env, memory_size, batch_size, target_update)
    agent.train(num_frames)
    # test
    video_folder = "videos/rainbow"
    agent.test(video_folder=video_folder)

    latest_file = show_latest_video(video_folder=video_folder)
    print("Played:", latest_file)
