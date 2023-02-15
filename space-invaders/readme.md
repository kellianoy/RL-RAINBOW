# SpaceInvaders

This framework allows training on several games: Breakout, Enduro, MsPacman, Pong, Qbert, Seaquest, and SpaceInvaders. As the time of training is very long, we only provide the trained model for SpaceInvaders. 

Without GPU, the efficient training of SpaceInvaders is too long. We recommend using GPU to train the model.

For 100000 steps per epoch and 100 epochs, it represents about 7h of training on a GPU.

## Pre-requisites

```py
pip install -r requirements.txt
```

## Training

To train the model for SpaceInvaders, run:

```py
python main.py --epoch 10 --step-per-epoch 100000 --resume-path "log/SpaceInvadersNoFrameskip-v4/rainbow/0/policy_save/policy.pth" --save-buffer-name "buffer" --training-num 16
```

## Testing

To test the presaved model for SpaceInvaders:

1. Set `watch` to `True` in `main.py`
2. To watch the trained model with one frame, run:

```py
python main.py --resume-path "log/SpaceInvadersNoFrameskip-v4/rainbow/0/policy_save/policy.pth" --render 0.0125 --test-num 1 --training-num 1 --save-buffer-name "buffer"
```

## Resume training

To resume training, it is possible to specify `--resume-path`:

```py
python main.py --epoch 10 --step-per-epoch 100000 --resume-path "log/SpaceInvadersNoFrameskip-v4/rainbow/0/policy_save/policy.pth"
```
## Tensorboard

To watch metrics pertaining to the training, run tensorboard:

```sh
tensorboard --logdir=log --host localhost --port 8888
```
Go to `localhost:8888` on your web browser.

## Results

The following results are obtained by running the code on a single GPU (NVIDIA GeForce GTX 3070). The [video](./videos/2023_02_13_191552.mp4) was recorded to show the performance of the trained model, after 100 epochs of training.

[![SpaceInvaders](./videos/2023_02_13_191552.gif)](./videos/2023_02_13_191552.mp4)

## References

[1] "Rainbow: Combining Improvements in Deep Reinforcement Learning", Hessel et al., 2017, https://arxiv.org/pdf/1710.02298.pdf  
[2] "Tianshou", https://github.com/thu-ml/tianshou
