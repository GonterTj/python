# https://www.youtube.com/watch?v=yMk_XtIEzH8&list=PLQVvvaa0QuDezJFIOU5wDdfy4e9vdnx-7&ab_channel=sentdex

import gym

env = gym.make("MountainCar-v0")
env.reset()

print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space.n)

'''

done = False

while not done:
    action = 2
    n_state, reward, done, state, info = env.step(action)
    print(n_state)
    env.render()

env.close()

'''