#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.

def DepthFirstSearch(G, n, countComponents):
    visited =[False]*(n + 1) 
    l = []
    for i in range (1, n+1):
        if visited[i] == False: 
                val = 0
                nodes  = DFS(i, visited, G, val) 
                countComponents += 1 # It returns from DFS after completing all nodes in a single component. So countComponents is as many DFS calls
                l.append(nodes) #l is the list of num_roads in each component
    print("l: ", l)         
    return l, countComponents
  
def DFS(i, visited, G, val):
    visited[i] = True
    val += 1 #This will count number of cities because for every node in the component this value increments by 1. 
    if (len(G) != 0):
        for v in G[i]: 
                if visited[v] == False: 
                    
                    val = DFS(v, visited,  G, val) 
   
    return val

def create_graph (cities):
    adj = dict()
    for i in range(1,n+1):
            adj[i] = []
    for road in cities:
        #print("i",i)
        if road[0] in adj:
            adj[road[0]].append(road[1])
        else:
            adj[road[0]] = [road[1]]

        if road[1] in adj:
            adj[road[1]].append(road[0])
        else:
            adj[road[1]] = [road[0]]
    return adj

    
def roadsAndLibraries(n, c_lib, c_road, cities):
    print("cities: ", cities)
    countComponents = 0 #In each component there is one library, so countComponents = count_library
    G = create_graph (cities)
    print ("Graph of cities G: ", G)
    
    if c_lib < c_road :
        return c_lib * n
    else:
        l, countComponents = DepthFirstSearch(G, n, countComponents)
        total = 0
        for i in l: #l is the list of num_roads in each component
            print("i: ", i)
            total = total + (c_road*(i-1))
        total = total + countComponents*c_lib
        return (total )
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
