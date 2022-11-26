# this code was developed with the tutorial : https://www.youtube.com/watch?time_continue=3&v=wc-FxNENg9U&feature=emb_title 
# from source repo https://github.com/philtabor/Deep-Q-Learning-Paper-To-Code 

import gym
from Game import *
from deep_q_learning import Agent
from utils import plot_learning_curve
import numpy as np
import torch as T




if __name__ == '__main__': 
    game = Game(n=4, m=4)
    agent = Agent(gamma=0.99, epsilon=0.1, batch_size=64, n_actions=4, eps_end=0.01, input_dims =[16], lr=0.003)
    scores, eps_history = [], []
    n_games = 500
    n = [16]
    print(*n)    
    for i in range(n_games):
        score = 0
        done = False
        state = game.reset()
        while not done: 
            action = agent.choose_action(state)
            state_, reward, done, info = game.Move(action)
            score +=reward
            agent.store_transition(state, action, reward, state_, done)
            agent.learn()
            state = state_
        scores.append(score)
        eps_history.append(agent.epsilon)
        avg_score = np.mean(scores[-100,:])
        print('episode ', i, 'score %.2f' %score, 
            'average score %.2f' % avg_score, 
            'epsilon %.2f' % agent.epsilon)

    x = [i+1 for i in range(n_games)]
    filename = 'agent_grid_world.png'
    plot_learning_curve(x,scores, eps_history, filename)
