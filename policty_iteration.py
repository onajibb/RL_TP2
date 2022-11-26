#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:58:06 2022

"""

import numpy as np

high = 1
low = 0
search, wait, recharge = 0, 1, 2

def mdp(alpha, beta, rs, rw): 
    S = [low, high]
    A = [search, wait, recharge]
    p = np.zeros((len(S), len(S), len(A)))
    p[high, high, search] = 1 - alpha #p(s'|s,a)
    p[high, low, search] = alpha
    p[high, high, wait] = 1
    p[low, low, search] = beta
    p[low, high, search] = 1-beta
    p[low, low, wait] = 1
    p[low, high, recharge] = 1
    
    r = np.zeros((len(s), len(s), len(A)))
    r[high, high, search] = rs
    r[high, low, search] = rs
    r[high, high, wait] = rw
    r[low, low, search] = rs
    r[low, high, search] = -3
    r[low, low, wait] = rw
    r[low, high, recharge] = 0
    
    return S, A, p, r

def distance(v1, v2): 
    return np.max(np.abs(v1 -v2))

def are_equal(pi1, pi2): 
    print("pi1: ", pi1, "pi2: ", pi2)
    for i in range(len(pi1)): 
        if pi1[i] != pi2[i]: 
            return False
    return True

def policy_iteration(MDP, eps, gamma): 
    S, A, p, r = MDP
    pi = np.zeros(len(S))
    k = 0
    stop = False
    while(pi != inter):
        print('k :', k, 'pi: ', pi)
        i = 0
        v = np.zeros(len(S))
        stop2 = False
        while(stop2 == False):  
            v_current = v
            for s in S: 
                for sp in S: 
                    pp = p[int(s), int(sp), int(p[int(s)])]
                    rr = r[int(s), int(sp), int(p[int(s)])]
                    v[s] += pp * rr + gamma * v[sp]
            i += 1
            if(dist(v, v_current) <= epsilon*(1-gamma/2*gamma)): 
                stop2 = True
            
            
