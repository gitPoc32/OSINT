#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
 
SOURCE_FILE='user-agent.txt'
 
def get():
    f = open(SOURCE_FILE)
    agents = f.readlines()
 
    return random.choice(agents).strip()
 
def getAll():
    f = open(SOURCE_FILE)
    agents = f.readlines()
    return [a.strip() for a in agents]
 
if __name__=='__main__':
    agents = getAll()
    for agent in agents:
        print agent
        
