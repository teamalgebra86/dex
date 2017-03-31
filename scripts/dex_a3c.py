#!/usr/bin/env python
# By Nick Erickson

# Run with Tensorflow v12 and Keras v2.02

# Done: Target Network https://jaromiru.com/2016/10/21/lets-make-a-dqn-full-dqn/
# TODO: Prioritized Experience Replay
# TODO: Random agent saving memory/loading memory (Mostly done)
    
from __future__ import print_function

#%%

# Experimental
#import threading

# Utilities
from param_const import gym_cart, hex_base
import play_game
import agent_a3c

#%%

def main(args):    
    play_game.run(args, agent_a3c.Agent)
    # TODO: Use finally clause to save model weights

if __name__ == "__main__":
    #args = hex_base
    args = gym_cart
    main(args) 
