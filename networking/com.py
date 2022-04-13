# Jean Yap s3783869, 12/4/2022
# For RMIT EEET2292
# Centre of Mass Algorithm (COM)
# This has not been fully tested!! Assumptions are that all given inputs are more or less
#   cluster-able, in line with assessments.

import math

# Distance between 2 nodes
#              _______________________
# distance = -/(x1 - x2)² + (y1 - y2)²
def getDistance(node1, node2):
    return math.sqrt(pow(node1['x']-node2['x'],2)+pow(node1['y']-node2['y'],2))

# Return a new cluster node from 2 nodes (i.e. merge them)
#
#               (weight1 * x1) + (weight2 * x2)
# cluster['x'] = ______________________________
#                       weight1 + weight2
#   Same for y', but using y1/y2
def getCluster(node1, node2):
    cluster = {'x': -1, 'y': -1, 'weight': -1}
    cluster['x'] = ((node1['weight'] * node1['x']) + (node2['weight'] * node2['x']))/(node1['weight'] + node2['weight'])
    cluster['y'] = ((node1['weight'] * node1['y']) + (node2['weight'] * node2['y']))/(node1['weight'] + node2['weight'])
    cluster['weight'] = node1['weight'] + node2['weight']
    return cluster

# Given a bunch of nodes, and certain requirements, return the centre
#   of mass for a network.
# nodes is an array of dicts, where a node is in the format: 
#       node = { 'x': 0, 'y': 0, 'weight': 0}
def com(nodes, max_weight, min_weight, max_distance, cluster_amount):
    results = []

    # Base case
    if (len(nodes) == cluster_amount):
        print('Final solution complete')
        print(nodes)
        return nodes
    
# 1. Calculate the distances (costs) between all node pairs.
    # Pair every element (i) with the elements following it (j)
    for i, node1 in enumerate(nodes):
        # We can't pair the last element with anything
        if (i == len(nodes)-1):
            break;
        for j, node2 in enumerate(nodes[i+1:]):
             # i and j are used for indexing the 'nodes' parameter: thus i+j+1
            result = {'node1': i, 'node2': i+j+1, 'distance': -1}
            result['distance'] = getDistance(node1,node2)
            # If distance > max_distance, ignore. We won't be able to cluster it.
            if (result['distance'] > max_distance):
                break;
            results.append(result)
    # If costs are empty, algorithm can't do anything
    if (results == False):
        print('No solution found: all costs are too large')
        return False
        
# 2. Sort results, based on distance in ascending order.
    results = sorted(results, key=lambda a: a['distance'])

# 3. Get the first result we can cluster.
    for r in results:
        node1 = nodes[r['node1']]
        node2 = nodes[r['node2']]
        cluster = getCluster(node1,node2)
        # Again, ignore the pairs we won't be able to cluster
        if (cluster['weight'] < min_weight or cluster['weight'] > max_weight):
            continue
        # node2 HAS to be popped before node 1: because otherwise, an element that doesn't exist might be accessed
        nodes.pop(r['node2'])
        nodes.pop(r['node1'])
        nodes.append(cluster)
        break
# 4. Repeat until finished.
    com(nodes, max_weight, min_weight, max_distance, cluster_amount)