from Game import Game
from main import *
import numpy as np
import random
newGame = Game(n=4, m=4)

genGame = newGame.generate_game()

def choose_action( q, st, eps): 
    random_number = random.random()
    if(random_number > eps):
        action = random.randint(0,3) 
    else: 
        action = np.argmax(q[st, :])
    
    return action

def q_learning( mdp ,gamma,  alpha):
    S = mdp[0]
    A = mdp[1]
    a = len(A)
    s = len(S)
    # initialiser la matrice Q de la bonne façon en respectant les actions possibles à part le passage à l'état finale
    epsilon = np.linspace(0,1, 100)
    Q_estim = np.random.rand(s,a)
    #end = newGame._position_to_id(newGame.end[0], newGame.end[1] )
    #Q_estim[end,:] = np.zeros((1,a))
    etha = np.zeros((s,a))
    p = mdp[2]
    n_victoire = 0
    for i in range(100):
        S0 =  newGame.reset()  # renvoie l'état auquel le jeu commence 
        St = S0
        t = 0
        end = False 
        eps = epsilon[-i]
        action = choose_action(Q_estim,St,eps)
        while not end: 
            # exploration 
            random_number = random.random()
            Stbis, rt, end, _ = newGame.move(action)
            actionbis = choose_action( Q_estim, Stbis, eps)
            Q_estim[St, action] =  Q_estim[St,action] + alpha * (rt + gamma* Q_estim[Stbis, actionbis] - Q_estim[St, action])
            St = Stbis
            action = actionbis
        if(rt == 10 ): 
            n_victoire += 1
            print("epsilon", eps)
        print("WIN") if rt ==10 else print("DEFEAT")    
    print(n_victoire) 
    return Q_estim


mdp1 = mdp(newGame)

Q = q_learning(mdp1, gamma=0.3,alpha=10e-1 )



print(Q)
newGame.print()
    
