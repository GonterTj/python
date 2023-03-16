# https://www.youtube.com/watch?v=yMk_XtIEzH8&list=PLQVvvaa0QuDezJFIOU5wDdfy4e9vdnx-7&ab_channel=sentdex

import gym

env = gym.make("MountainCar-v0")
env.reset()

done = False

while not done:
    action = 2
    new_state, reward, done, _ = env.step(action)
    print(new_state)
    env.render()

env.close()