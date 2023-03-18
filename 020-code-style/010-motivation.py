#!/usr/bin/env python3

import random 
import os

def generate_keys():
    key0 = [] 
    while len(key0) <10: 
        candidate = random.randint(0, 9) 
        if candidate in key0:
            continue   
        key0.append(candidate)

    key1 = [] 
    while len(key1) <10: 
        candidate = random.randint(10,19) 
        if candidate in key1:
               continue
        key1.append(candidate)
    return key0,key1
      
                    
if __name__ == "__main__":
    key0, key1 = generate_keys()
    print('key range 0 = ', key0)
    print("key range 1 = ", key1)
