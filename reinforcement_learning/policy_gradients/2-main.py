#!/usr/bin/env python3
"""
Main file for training the policy gradient model.
"""

import gym
import matplotlib.pyplot as plt
import numpy as np

from train import train

env = gym.make('CartPole-v1')

scores = train(env, 10000)

plt.plot(np.arange(len(scores)), scores)
plt.xlabel('Episode')
plt.ylabel('Score')
plt.title('Policy Gradient Training Progress')
plt.show()

env.close()

